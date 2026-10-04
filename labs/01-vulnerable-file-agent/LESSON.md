# Lab 01 — Lesson Notes

Do not read this until you have answered the questions in the lab README.

## 1. Asset

The protected asset is:

`workspace/restricted/secret.txt`

In a real system this could instead be:

- an API token
- customer data
- an SSH key
- an internal database
- an administrative API
- a payment action

## 2. Who enforced authorization?

Nobody.

The file tool accepts a path and executes the read.

The LLM is effectively deciding its own access by choosing which path to request.

That is the architectural mistake.

## 3. Why isn't the system prompt enough?

A system prompt influences model behavior.

It does not provide deterministic authorization.

Untrusted content, reasoning errors, malicious instructions, model bugs, or future
capabilities may all cause the model to request an unsafe action.

Security must assume that this happens.

## 4. Where should authorization live?

Outside the model, immediately before the consequential action.

The desired flow is:

```text
Agent proposes action
        |
        v
Policy / authorization
        |
   ALLOW or DENY
        |
        v
Tool execution
```

The model proposes.

The control plane decides.

## 5. What must remain trustworthy?

Even if the model is completely compromised:

- policy enforcement
- identity
- credentials
- runtime isolation
- audit logging
- containment

must remain outside the model's authority.

## Key concept

**Prompt alignment is behavioral guidance. Authorization is a security control.**

Do not confuse them.
