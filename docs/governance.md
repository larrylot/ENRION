# AI governance in ENRION

## Scope

ENRION studies how an agent's purpose, authority and accountability can be turned
into testable controls. It is not a compliance pack or a certification claim.

Project maintainer: Lars Örtegren. Lab 02's example policy names Lars as the owner
of a synthetic invoice exercise. This is a local lab configuration, not an approved
enterprise risk acceptance or a delegation of real authority.

## Current mandate

The example agent may read one synthetic invoice. It may not write files, contact
external systems, spend money, change policy or approve its own actions through
the gateway. No real credentials are involved. The optional Lab 01 live model
exercise is separate and does use an external API.

| Governance concern | Present implementation | Remaining work |
|---|---|---|
| Purpose and owner | Required fields in policy.json | Independent approval and accountable review |
| Autonomy and scope | Only local reads and exact resource grants | Per-task delegation and expiry |
| Risk linkage | R-01 referenced in policy and events | Reviewed risk acceptance and evidence history |
| Policy versioning | Git history, version and configuration digest | Signed decisions and authorized release process |
| Human oversight | Operator can stop future gateway calls | Approvals bound to exact actions; no replay |
| Changes | Regression tests can be rerun | Reviewed model/tool/policy changes and retained reports |
| Exceptions | No exception or override request API | Explicit owner, rationale and expiry if introduced |
| Incident evidence | Correlated decisions and results | Independent durable collector and recovery drill |

## Change review procedure

For a change to policy, model or tool, record the intended behavior, affected risk,
reason, reviewer and test evidence in a pull request. Rerun the baseline and defended
cases. Do not describe an unreviewed change as approved. A change to the policy
content changes its digest; reviewers still need to inspect what changed.

The repository has a regression workflow configuration. Whether a specific commit
passed CI is shown in GitHub Actions, not inferred from the presence of that file.

## Incident procedure for this lab

Stop the gateway, preserve the synthetic event stream, identify its run and policy
digest, and compare requested versus completed actions. Check for data returned
before the stop. Restart with a new instance only after reviewing scope and tests.
This is a learning procedure, not a verified enterprise incident response process.

## Future governance experiments

Bind a human approval to agent identity, action, resource, policy digest, expiry and
single use. Deny altered or replayed approvals. Then test what happens if the audit
collector fails, credentials expire or the operator stops the agent during a call.

Policy change monitoring could later turn a provider terms change into a review
task. It should never silently widen agent permissions or be described as a legal
assessment. Agent Incident Black Box is an evidence experiment, not a deployed product.
