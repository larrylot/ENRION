# ENRION

**Learn agent security by breaking and defending agents.**

ENRION is an open, hands-on learning path for understanding how autonomous agents fail and how to design controls that still hold when the model behaves incorrectly.

You do not need to be an AI researcher. The project is designed for security engineers, architects, developers, platform engineers, AI-governance practitioners, and curious technologists.

## The ENRION method

Every lab follows the same cycle:

**Learn → Predict → Break → Observe → Explain → Defend → Break Again → Map to Enterprise**

We deliberately experience the failure before introducing the control.

> **A model may be compromised. The security boundary must still hold.**

Prompts guide behavior. They must not be the final authority for access, execution, identity, secrets, networking, or other consequential actions.

## Learning path

### Foundation

| Lab | Topic | Status |
|---|---|---|
| 01 | Indirect prompt injection & missing authorization | **Ready** |
| 02 | Tool authorization & deny-by-default | Next |
| 03 | Identity, delegation & audit | Planned |
| 04 | Secrets & least privilege | Planned |

### Defense

| Lab | Topic | Status |
|---|---|---|
| 05 | Runtime sandboxing | Planned |
| 06 | Network egress control | Planned |
| 07 | Human approval & consequential actions | Planned |
| 08 | Detection, telemetry & containment | Planned |

### Advanced

| Lab | Topic | Status |
|---|---|---|
| 09 | MCP tool poisoning | Planned |
| 10 | Memory poisoning | Planned |
| 11 | Cross-agent communication & isolation | Planned |
| 12 | Privilege escalation & control-plane attacks | Planned |
| 13 | Automated adversarial evaluation | Planned |
| 14 | Kill switches & fail-safe design | Planned |
| 15 | Enterprise threat model & governance mapping | Planned |

See [the learning path](docs/learning-path.md) for the intended progression.

## Start here

1. Clone the repository.
2. Open [Lab 01](labs/01-vulnerable-file-agent/README.md).
3. **Do not read the lesson notes first.**
4. Predict what will happen.
5. Run the demo.
6. Explain the failure in your own words.
7. Compare your reasoning with the lesson notes.

Lab 01 needs only Python 3.11/3.12 and Git. No API key is required for the offline exercise.

## The questions every lab must answer

1. What is the protected asset?
2. What is untrusted?
3. What authority does the agent have?
4. Where does model output become a real action?
5. Which control should decide whether that action is allowed?
6. Does the control still work if the model is fully compromised?
7. What is the blast radius?
8. What telemetry proves what happened?

If you cannot answer those questions, running the code is not enough.

## Repository structure

~~~text
ENRION/
├── labs/                 # hands-on attack and defense labs
├── docs/
│   ├── learning-path.md  # curriculum
│   ├── lab-template.md   # teaching standard
│   └── learning-journal.md
├── requirements.txt
└── README.md
~~~

## Safety

The labs use fake credentials, local files, and deliberately constrained examples.

**Never use real secrets, production credentials, customer data, or production systems in an ENRION lab.**
