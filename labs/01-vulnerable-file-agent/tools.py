from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent / "workspace"


def read_file(path: str) -> str:
    """
    INTENTIONALLY VULNERABLE.

    This function performs no authorization check. Any file below WORKSPACE can
    be requested by the agent.

    Lab 02 will fix this by separating:
        requested action
        from
        authorization decision
    """
    target = (WORKSPACE / path).resolve()

    # This prevents escaping the demo workspace entirely. It is NOT the policy
    # boundary we care about in this lab.
    if WORKSPACE.resolve() not in target.parents and target != WORKSPACE.resolve():
        raise ValueError("Path escapes the lab workspace.")

    if not target.is_file():
        raise FileNotFoundError(path)

    return target.read_text(encoding="utf-8")
