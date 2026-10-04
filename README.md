# ENRION

**Agent Security Research Lab**

ENRION is a learning-first project for understanding how autonomous agents fail,
how those failures cross trust boundaries, and how technical controls can contain them.

The project deliberately starts insecure.

We will:
1. Build a vulnerable agent.
2. Make the failure observable.
3. Threat-model the failure.
4. Add deterministic controls outside the model.
5. Replace home-grown controls with production-grade open-source components where useful.

## Core principle

> A model may be compromised. The security boundary must still hold.

## Labs

| Lab | Topic | Status |
|---|---|---|
| 01 | Vulnerable file agent / indirect prompt injection | Ready |
| 02 | Tool authorization / deny-by-default | Next |
| 03 | Identity + audit | Planned |
| 04 | Governance toolkit integration | Planned |
| 05 | Runtime sandbox / egress control | Planned |
| 06 | Automated attack/eval suite | Planned |
| 07 | Detection + containment / kill switch | Planned |

## Start here

Open:

`labs/01-vulnerable-file-agent/README.md`

Do the offline demo first. Do not skip directly to the live LLM version.
