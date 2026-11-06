# Threat model: local invoice agent

## System and trust boundaries

The user assigns one invoice. Document contents and model tool proposals are
untrusted. The runner supplies a fixed lab identity, a reviewed policy, the local
workspace and an audit sink. The gateway is the boundary between the proposed
action and the file read. It does not parse or follow instructions in the invoice.

The attacker may replace invoice contents and propose arbitrary actions or paths.
The attacker does not control policy loading, the Python gateway process, the audit
sink or concurrent filesystem mutation. Removing any of these assumptions requires
a stronger architecture, not another prompt.

Assets: synthetic restricted data, task scope, policy integrity and decision evidence.
Maximum intended authority: read the exact invoice. No write or network tool is exposed.

## Risks and controls

| Risk | Lab 01 | Lab 02 control and evidence | Residual risk |
|---|---|---|---|
| R-01: injected request reads unrelated data | Exposes restricted fixture | Exact resource grant; denied before file read test | Allowed invoice content still reaches the caller |
| R-02: path traversal or static symlink redirects a read | Workspace check only | Canonical resource and resolved target tests | Filesystem replacement race and hard links not contained |
| R-03: proposal changes identity or action | No policy layer | Fixed runner identity, action allowlist and negative tests | No cryptographic authentication; trusted runner assumed |
| R-04: missing audit hides a read | Console output only | Audit before read; audit failure test | Sink can be tampered with; completion failure after read |
| R-05: stopped agent continues | No stop control | Stop denies subsequent requests, tested | No in-flight cancellation or external credential revocation |
| R-06: policy is broadened without approval | Not modeled | Versioned policy and digest aid review | Digest detects content differences, not authorized changes |
| R-07: model gains execution in gateway process | Out of scope | No model or execution tool in offline lab | Process compromise bypasses the gateway entirely |

Test names and commands are in [evidence.md](evidence.md). Passing a test supports
that narrow claim only. Lab 02 is not safe for production secrets, hostile local
users, arbitrary execution or sensitive external APIs.

## Open questions

Where should authenticated identity and delegated scope be issued? What must be
durably recorded before a consequential action? Which controls survive gateway
process compromise? How quickly can permission revocation take effect? These are
future experiments with explicit acceptance criteria in the [roadmap](roadmap.md).
