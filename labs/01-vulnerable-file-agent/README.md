# Lab 01 — The Agent That Can Read Too Much

**Level:** Foundation  
**Topic:** indirect prompt injection, tool authority, trust boundaries  
**Time:** 15–30 minutes  
**Prerequisites:** basic Python command-line use

## What you will learn

After this lab you should be able to explain:

- what makes an AI system an agent rather than only a chatbot
- why untrusted content can influence an agent's actions
- why a system prompt is not authorization
- where the important trust boundary exists
- why tool permissions must be enforced outside the model

The goal is not to memorize definitions. The goal is to experience the failure.

# 1. Learn

The agent has one capability:

~~~text
read_file(path)
~~~

The user wants it to summarize:

~~~text
workspace/public/invoice.txt
~~~

The environment also contains:

~~~text
workspace/restricted/secret.txt
~~~

The file tool can read both.

Current architecture:

~~~text
User
  ↓
Agent
  ↓ chooses a path
read_file(path)
  ↓
Filesystem
~~~

**Question: where is the authorization decision?**

Do not read LESSON.md yet.

# 2. Threat

The public invoice contains a malicious instruction telling the agent to read the restricted file.

This is **indirect prompt injection**: hostile instructions arrive through data the agent was asked to process.

Real agents may consume email, PDFs, webpages, tickets, source code, databases, memory, and tool output. Any of those can carry instructions aimed at the model.

# 3. Predict

Before running anything, write down your prediction.

If the agent requests:

~~~text
read_file("restricted/secret.txt")
~~~

who decides whether it is authorized?

- system prompt
- model
- file tool
- operating system
- nobody

Also predict whether the secret stays protected, and explain why.

# 4. Break

Run the deliberately vulnerable offline demo:

~~~bash
python offline_demo.py
~~~

On Windows, if needed:

~~~powershell
py offline_demo.py
~~~

Expected security result:

~~~text
[AGENT REQUEST] read_file('restricted/secret.txt')
[TOOL] ALLOWED — no policy layer exists
[SECURITY RESULT] SECRET EXPOSED
~~~

The offline demo intentionally removes LLM randomness. We are testing the architecture, not whether a particular model happens to obey the injected instruction.

# 5. Observe

The important sequence is:

~~~text
Agent requests action
        ↓
Tool executes action
~~~

There is no independent security decision between request and execution.

The model effectively controls its own authority.

# 6. Explain

Before opening LESSON.md, answer:

1. What is the asset?
2. What is untrusted?
3. What capability does the agent have?
4. Where does model output become a real-world action?
5. What control is missing?
6. If the model is fully compromised, what must remain trusted?

Use the [learning journal](../../docs/learning-journal.md).

# 7. Key distinction

> **The model proposes. The security system decides.**

A prompt saying "never read restricted files" may influence behavior.

It does not make the operation impossible.

What we ultimately want is:

~~~text
Agent proposes action
        ↓
Authorization
     ↙     ↘
  DENY     ALLOW
   ↓         ↓
 audit      tool
~~~

We build that in Lab 02.

# 8. Optional live LLM exercise

After understanding the offline failure, you can run live_agent.py.

Create a virtual environment and install dependencies:

~~~bash
python -m venv .venv
pip install -r ../../requirements.txt
~~~

Set OPENAI_API_KEY and OPENAI_MODEL for a Responses-API-compatible model available to your account, then run:

~~~bash
python live_agent.py
~~~

A particular model may or may not follow the malicious instruction. That does not determine whether the architecture is secure.

If the security guarantee is "hopefully the model does not request it", the design is already wrong.

# 9. Enterprise mapping

| Lab | Enterprise equivalent |
|---|---|
| invoice.txt | email, PDF, webpage, ticket |
| secret.txt | API token, customer data, SSH key |
| read_file() | MCP tool, REST API, database connector |
| agent | autonomous workflow / task agent |
| missing authorization | excessive service permissions / missing policy gateway |

A toy file-read failure can become a CRM export, privileged cloud action, payment, or destructive administrative command.

# 10. Challenge

Add a second restricted file named payroll.txt and change the injected instruction to request it.

Then ask:

**Did the attacker need a new vulnerability to reach the second asset?**

If not, what does that say about blast radius?

# 11. Key takeaway

> **Prompt instructions influence agent behavior. They do not enforce agent authority.**

Next: **Lab 02 — Tool Authorization & Deny-by-Default**
