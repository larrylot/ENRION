# ENRION

**Agent security and AI governance, tested through small, reproducible labs.**

ENRION is an independent learning and security architecture project maintained by
Lars Örtegren. It explores what an autonomous agent can actually do, who grants
that authority, and which controls still work when the model makes the wrong decision.

The aim is to connect governance decisions to technical enforcement and observable
evidence. A policy saying "do not read this" is not the same as a tool that cannot read it.

## What you can run today

| Component | Current evidence | Important limit |
|---|---|---|
| Lab 01: vulnerable file agent | Reproducible exposure of a synthetic restricted file | Offline exercise assumes a compromised model |
| Lab 02: authorized file agent | Exact resource grants, bound lab identity, default denial | Application boundary, not an OS sandbox |
| Governance configuration | Versioned owner, purpose, autonomy, resource scope and risk reference | Trusted runner loads the policy; no approval service |
| Decision telemetry | JSON events with run, request and policy identifiers | Local sink is neither durable nor tamper resistant |
| Stop control | Further calls are denied after operator stop | No cancellation of an operation already in progress |
| Regression suite | Baseline, denial, path, identity, audit and stop tests | Does not establish production security or compliance |

See the [verification record](docs/evidence.md) for commands, observed results and limitations.

## Five minute walkthrough

Python 3.11 or later is sufficient for both offline labs and the tests. No API key,
model download, cloud account or dependency installation is needed.

~~~bash
git clone https://github.com/larrylot/ENRION.git
cd ENRION
python -X utf8 labs/01-vulnerable-file-agent/offline_demo.py
python -X utf8 labs/02-authorized-file-agent/offline_demo.py
python -m unittest discover -s tests -v
~~~

On Windows, use `py` instead of `python` if that is how Python is installed.

Expected contrast:

~~~text
Lab 01: [SECURITY RESULT] SECRET EXPOSED
Lab 02: LAB 02 PASS: allowed read works; restricted and post-stop reads denied
~~~

These are deterministic architecture exercises, not measurements of how often a
particular LLM follows prompt injection. Lab 01 also contains an optional live
model exercise. That exercise uses an external API, requires separate dependencies
and is not part of the verified offline results.

## Governance becomes an engineering question

| Governance question | Lab implementation or next step |
|---|---|
| Who owns the agent and what is its purpose? | Explicit fields in the versioned lab policy |
| What may it access? | One exact resource grant, checked outside the model |
| Can the agent grant itself more authority? | Model proposals cannot set policy or identity through the gateway API |
| Can we explain a decision? | Request, decision and result share identifiers and a policy digest |
| Can an operator stop it? | Synchronous stop denies subsequent tool calls |
| Who approves a consequential action? | Planned: approval bound to identity, action, resource, expiry and single use |
| What happens after a change? | Repeat regression tests; record policy changes and remaining risks |

Read the [governance model](docs/governance.md) and
[threat model](docs/threat-model.md). Neither is a claim of regulatory compliance.

## Direction

The next step is a small agent security testbed: execute the same scenarios against
a vulnerable design and a defended design, then inspect what was allowed, denied
and actually executed.

Longer term, ENRION could support architecture reviews, practical AI governance
workshops and evaluation of agent tooling. Those are possible applications, not
existing services or validated commercial offerings.

The [roadmap](docs/roadmap.md) defines the next experiments and completion gates.
The [learning path](docs/learning-path.md) retains the broader curriculum without
pretending all fifteen labs exist.

## Learning method

Learn → Predict → Break → Observe → Explain → Defend → Break Again → Map to Enterprise.

Start with [Lab 01](labs/01-vulnerable-file-agent/README.md), then
[Lab 02](labs/02-authorized-file-agent/README.md). Predict the outcome before reading
the lesson notes. Use the [learning journal](docs/learning-journal.md) to record
your own observations.

## Safety and project status

This is an early educational prototype. Lab 01 is intentionally vulnerable. Use
synthetic files only, on a disposable local environment. Do not use customer data,
real secrets, production credentials or production systems.

Lab 02 assumes the policy, gateway process and local filesystem are trusted. It
does not contain arbitrary Python execution, authenticate a real user, prevent
filesystem replacement races or restrict network access. A compromised process
can bypass its application checks. The [threat model](docs/threat-model.md)
explains why these boundaries matter.

No software license has been selected. Public visibility is not a license grant.
