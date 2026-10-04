# Lab 01 — Vulnerable File Agent

## Objective

Learn why an LLM instruction is **not** a security boundary.

The agent has one tool:

`read_file(path)`

The tool is intentionally over-permissioned. It can read both:

- `workspace/public/`
- `workspace/restricted/`

That is the vulnerability.

A public invoice contains an **indirect prompt injection** telling the agent to read
a restricted file. If the agent follows it, the tool happily complies.

## Threat model

### Asset

`workspace/restricted/secret.txt`

### Untrusted input

`workspace/public/invoice.txt`

### Vulnerable trust assumption

The application assumes that because the model was instructed to summarize an invoice,
it will only use the file-reading tool for that purpose.

### Missing control

There is no authorization decision between:

`agent request -> tool execution`

That missing decision point is the trust boundary we will build in Lab 02.

---

# Step 1 — Run the offline demonstration

This requires only Python 3.11+.

From this directory:

```bash
python offline_demo.py
```

The demo simulates the critical security condition: a compromised agent requests
a resource outside its intended scope, and the tool executes the request.

Expected result:

```text
[AGENT REQUEST] read_file('restricted/secret.txt')
[TOOL] ALLOWED (no policy layer exists)
[SECURITY RESULT] SECRET EXPOSED
```

This is intentionally bad.

## Stop and answer these before continuing

1. What is the asset?
2. Which component decided whether the agent was allowed to read it?
3. Is the model prompt enforcing authorization?
4. Where should the real authorization decision happen?
5. If the model becomes fully prompt-injected, what must still remain trustworthy?

Suggested answers are in `LESSON.md`, but write your own answers first.

---

# Step 2 — Optional live LLM version

The live version uses OpenAI function calling.

Install:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then:

```bash
pip install -r ../../requirements.txt
```

Set an API key:

```bash
export OPENAI_API_KEY="..."
```

Set any Responses-API-compatible model available to your API account:

```bash
export OPENAI_MODEL="YOUR_MODEL_NAME"
```

Then:

```bash
python live_agent.py
```

Important: model behavior is probabilistic. The security lesson does **not** depend on
whether a particular model follows the malicious instruction every run.

The vulnerability exists because the application gives the model authority to request
the restricted resource and blindly executes that request.

## Rule for this project

Never use real secrets in these labs.
