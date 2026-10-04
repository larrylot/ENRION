# ENRION Learning Path

ENRION teaches agent security as an engineering discipline.

~~~text
Understand capability
        ↓
Experience failure
        ↓
Identify trust boundary
        ↓
Add external control
        ↓
Attack the control
        ↓
Reduce blast radius
        ↓
Map to enterprise
~~~

## Stage 1 — Foundation

**Lab 01 — Indirect Prompt Injection & Missing Authorization**  
Agents, tools as capabilities, indirect prompt injection, trust boundaries, and why prompts are not authorization.

**Lab 02 — Tool Authorization & Deny-by-Default**  
Policy enforcement points, resource scope, ALLOW/DENY, fail-closed design, reference-monitor thinking.

**Lab 03 — Identity, Delegation & Audit**  
Who is acting, on whose behalf, delegated authority, session identity, immutable audit events.

**Lab 04 — Secrets & Least Privilege**  
Scoped and short-lived credentials, service identity, secret exposure, capability minimization.

## Stage 2 — Defense

**Lab 05 — Runtime Sandboxing**  
Process/filesystem isolation, disposable execution, and defense beyond application policy.

**Lab 06 — Network Egress**  
Default-deny networking, allowlists, DNS egress, proxies, exfiltration boundaries.

**Lab 07 — Consequential Actions & Human Approval**  
Risk-tiered actions, approval gates, separation of duties, transaction boundaries.

**Lab 08 — Detection & Containment**  
Telemetry, behavioral signals, automatic containment, revocation, machine-speed response.

## Stage 3 — Advanced

Labs 09–15 cover MCP tool poisoning, memory poisoning, multi-agent isolation, privilege escalation, adversarial evaluations, kill switches, fail-safe design, and enterprise governance mapping.

## Graduation outcome

A learner completing ENRION should be able to:

1. Draw an agentic system and identify trust boundaries.
2. Separate behavioral guardrails from deterministic security controls.
3. Scope agent authority using least privilege.
4. Design authorization between model decisions and real-world actions.
5. Design runtime and network containment.
6. Threat-model prompt injection, tool poisoning, memory poisoning, and multi-agent risks.
7. Define useful telemetry and containment triggers.
8. Evaluate blast radius if the model is compromised.
9. Map governance requirements to technical controls.
10. Explain the architecture to engineers, security teams, architects, and leadership.
