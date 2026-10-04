# Lab 01 — Lesson Notes

Read this **after** running the lab and writing your own answers.

## The failure in one sentence

The application allowed a model-generated request to become a real file operation without an independent authorization decision.

## Asset

The asset was the restricted secret file.

In enterprise systems, the asset could instead be customer data, credentials, source code, a privileged API, an email action, a payment, or the ability to modify infrastructure.

Agent security protects both **information and actions**.

## Untrusted input

The invoice was useful business data and still had to be treated as untrusted.

> **Useful data can also contain hostile instructions.**

Email, webpages, documents, tool output, and persistent memory can all become delivery mechanisms for indirect prompt injection.

## Capability and authority

The intended task was:

~~~text
read one public invoice
~~~

The effective tool authority was:

~~~text
read any file in the workspace
~~~

That gap is a least-privilege failure.

## Trust boundary

The important boundary is where model output becomes a consequential action:

~~~text
Model proposal
      ↓
Tool execution
~~~

Before the boundary, the model is proposing.

After the boundary, something real has happened.

## Missing control

Nobody answered:

> Is this agent allowed to perform this action on this resource for this task?

The path check in tools.py prevents escaping the demo workspace. It does not perform task-level authorization.

## Why the prompt is insufficient

System prompts affect behavior probabilistically.

Authorization must be enforced deterministically.

A secure design assumes the model may eventually request an unsafe action due to prompt injection, poisoned memory, malicious tool output, reasoning errors, bugs, or capability improvements.

The system must still reject it.

## Correct architecture

~~~text
User
  ↓
Agent
  ↓ proposes
Authorization / policy
  ├── DENY → audit
  └── ALLOW
        ↓
       Tool
        ↓
     Resource
~~~

The enforcement component might be called a policy enforcement point, reference monitor, authorization gateway, tool broker, or control plane.

The name matters less than the boundary.

## Compromise assumption

If the model is fully compromised, these controls must remain outside its authority:

- identity
- authorization policy
- credentials
- policy enforcement
- runtime isolation
- network controls
- audit logging
- containment

## Blast radius

If there were 10,000 restricted files, the attacker would not need a fundamentally new vulnerability for every file.

One missing authorization boundary creates a broad exposure.

## Mental model

~~~text
MODEL         = untrusted decision maker
CONTROL PLANE = trusted enforcement
TOOL          = capability
RESOURCE      = asset
~~~

> **Prompt alignment is behavioral guidance. Authorization is a security control.**
