"""A small application authorization boundary, not an operating system sandbox.

The trusted runner supplies identity, policy and audit sink. Model proposals only
contain an action and a resource. Use disposable local fixtures, never real data.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Callable
from uuid import uuid4


def canonical_resource(value: str) -> str:
    """Accept one portable, unambiguous relative resource name."""
    if not isinstance(value, str) or not value or len(value) > 512:
        raise ValueError("invalid_resource")
    if any(ord(char) < 32 for char in value) or "\\" in value or ":" in value:
        raise ValueError("invalid_resource")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in value.split("/")):
        raise ValueError("invalid_resource")
    return path.as_posix()


@dataclass(frozen=True)
class Policy:
    policy_id: str
    version: str
    owner: str
    purpose: str
    agent_id: str
    autonomy: str
    allowed_resources: frozenset[str]
    risk_id: str

    def __post_init__(self) -> None:
        for name in ("policy_id", "version", "owner", "purpose", "agent_id", "risk_id"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"invalid_policy_{name}")
        if self.autonomy != "read_only_local":
            raise ValueError("unsupported_autonomy")
        if not isinstance(self.allowed_resources, frozenset) or not self.allowed_resources:
            raise ValueError("invalid_policy_resources")
        for resource in self.allowed_resources:
            canonical_resource(resource)

    def as_dict(self) -> dict:
        return {
            "policy_id": self.policy_id,
            "version": self.version,
            "owner": self.owner,
            "purpose": self.purpose,
            "agent_id": self.agent_id,
            "autonomy": self.autonomy,
            "allowed_resources": sorted(self.allowed_resources),
            "risk_id": self.risk_id,
        }

    @property
    def digest(self) -> str:
        encoded = json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()

    @classmethod
    def load(cls, path: Path) -> "Policy":
        data = json.loads(path.read_text(encoding="utf-8"))
        expected = set(cls.__dataclass_fields__)
        if not isinstance(data, dict) or set(data) != expected:
            raise ValueError("invalid_policy_fields")
        resources = data["allowed_resources"]
        if not isinstance(resources, list) or not all(isinstance(x, str) for x in resources):
            raise ValueError("invalid_policy_resources")
        if len(resources) != len(set(resources)):
            raise ValueError("duplicate_policy_resource")
        return cls(**{**data, "allowed_resources": frozenset(resources)})


class FileGateway:
    """Synchronous lab gateway. The agent must not control this Python process.

    The filesystem and policy must not be modified concurrently. Resolving paths
    is not protection against a hostile local process racing a file replacement.
    """

    def __init__(self, workspace: Path, policy: Policy, agent_id: str,
                 audit: Callable[[dict], None]) -> None:
        self._workspace = workspace.resolve(strict=True)
        self._policy = policy
        self._agent_id = agent_id
        self._audit = audit
        self._stopped = False
        self._run_id = str(uuid4())

    def _record(self, decision: str, resource: str, reason: str,
                request_id: str, action: str = "read_file") -> None:
        self._audit({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "run_id": self._run_id,
            "request_id": request_id,
            "agent_id": self._agent_id,
            "policy_id": self._policy.policy_id,
            "policy_version": self._policy.version,
            "policy_sha256": self._policy.digest,
            "risk_id": self._policy.risk_id,
            "action": action,
            "resource": resource,
            "decision": decision,
            "reason": reason,
        })

    def stop(self) -> None:
        """Deny subsequent calls, even if recording the stop event fails."""
        self._stopped = True
        self._record("STOP", "<none>", "operator_stop", str(uuid4()), "stop")

    def execute(self, action: str, resource: str) -> str:
        request_id = str(uuid4())
        safe_action = action if isinstance(action, str) and action in (
            "read_file", "write_file", "delete_file"
        ) else "<unknown>"

        def deny(reason: str, safe_resource: str = "<invalid>") -> None:
            self._record("DENY", safe_resource, reason, request_id, safe_action)
            raise PermissionError(reason)

        if self._stopped:
            deny("agent_stopped")
        if self._agent_id != self._policy.agent_id:
            deny("identity_not_authorized")
        if action != "read_file":
            deny("action_not_authorized")
        try:
            name = canonical_resource(resource)
        except ValueError:
            deny("invalid_resource")
        if name not in self._policy.allowed_resources:
            deny("resource_not_authorized", name)

        # Check the resolved resource as well as the model's lexical path.
        try:
            target = (self._workspace / name).resolve(strict=True)
            resolved_name = target.relative_to(self._workspace).as_posix()
        except (OSError, ValueError, RuntimeError):
            deny("resource_unavailable", name)
        if resolved_name not in self._policy.allowed_resources or not target.is_file():
            deny("resolved_resource_not_authorized", name)

        # A failed audit write prevents the read. No prompt or content is logged.
        self._record("ALLOW", name, "exact_resource_grant", request_id)
        try:
            result = target.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            self._record("ERROR", name, "read_failed", request_id)
            raise
        self._record("RESULT", name, "read_completed", request_id)
        return result
