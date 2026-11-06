# ENRION roadmap

Updated 6 November 2026. This is direction, not a delivery commitment.

## Now: a small, defensible foundation

Implemented: vulnerable Lab 01, defended Lab 02, synthetic fixtures, versioned lab
policy, structured decision events, synchronous stop, regression tests, threat
model and governance mapping. See [evidence](evidence.md) for what was actually run.

## Next: prove three harder boundaries

| Priority | Experiment and hypothesis | Completion gate |
|---|---|---|
| 1 | Per-task identity and delegation: a grant cannot be reused for another agent or task | Positive control works; wrong identity, wrong task, expired and revoked grants deny before execution |
| 2 | Human approval: approval authorizes exactly one consequential action | Altered parameters, changed policy, expired approval and replay deny; one valid action succeeds once |
| 3 | Agent Incident Black Box: a reviewer can reconstruct an incident from independent evidence | Every request has a terminal result or explicit uncertainty; reconstruct identity, policy, decision and effect; test collector failure and stop |

Each experiment must include an attack, an allowed control, an attempted bypass,
a reproducible command and a written limitation. An expected result alone is not
completion. Keep model behavior measurements separate from gateway tests.

## Later: contain more than a file tool

* Run the agent and gateway in separate processes with separate privileges.
* Add a disposable runtime and default denial of network egress; verify blocked
  connections rather than inferring safety from configuration.
* Integrate one real agent or MCP tool using synthetic resources and an explicit
  local authority boundary.
* Replay prompt injection, poisoned tool output, memory poisoning and delegated
  agent attacks against vulnerable and defended configurations.
* Test model, policy and tool changes against the same evidence set.

These features are not implemented by the present file gateway.

## What ENRION could become

1. A practical learning path for security engineers and architects.
2. An agent security testbed with repeatable attack and defense comparisons.
3. A reference architecture linking governance decisions to tool permissions,
   telemetry, human oversight and incident handling.
4. A basis for workshops and architecture reviews, if the labs prove useful to others.

There are no production deployments, customer outcomes, market validation or
certifications claimed here. A dashboard or service would be a later packaging
choice, not the next security milestone. Choose a software license before inviting
reuse or accepting external contributions.
