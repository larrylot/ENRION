# Lab 02: The Model Proposes, the Gateway Decides

Level: foundation. Time: about 20 minutes. Prerequisite: Lab 01 and basic Python.

## Learn

Lab 01 gave the model more authority than its task required. Here, an external
gateway loads a policy that permits only `public/invoice.txt`. The trusted runner
binds `invoice-agent` to that policy. The model can request an action and a path,
but it cannot submit a new identity or policy through the request interface.

## Threat

Assume the invoice successfully manipulates the model into requesting
`restricted/secret.txt`. The asset is the synthetic restricted file. The attacker
controls document contents and tool proposals, not the gateway process or policy.

## Predict

Which of these should work? Write your answer before running the demo.

1. Read the assigned invoice.
2. Read a restricted file.
3. Read a different public file that belongs to another task.
4. Read the invoice after an operator stop.

## Break and observe

From the repository root:

```bash
python -X utf8 labs/01-vulnerable-file-agent/offline_demo.py
python -X utf8 labs/02-authorized-file-agent/offline_demo.py
```

Lab 02 reuses the same synthetic workspace. It makes the malicious request
explicitly; it does not call a model. You should see an allowed read, a denied
restricted read, a stop event and a denied subsequent read. File contents are not
written to the Lab 02 audit events.

## Explain

The boundary is the call to `FileGateway.execute()`. The model's proposed resource
is checked against an exact grant before the file read. The resolved path is also
checked to reject static symlinks that redirect to a different resource.

Policy metadata explains the intended owner, purpose, autonomy and risk. It is
useful evidence, but text fields do not authenticate the owner or create approval.

## Defend and break again

```bash
python -m unittest discover -s tests -v
```

The tests include unrelated public files, unknown identities and actions, path
traversal, static symlinks, malformed policies, audit failure and post-stop calls.
Symlink tests explicitly skip on hosts that cannot create symlinks.

An audit failure before a read prevents the read. If the final result event fails,
the gateway raises and does not return content, but the read has already happened.
That distinction becomes critical for payments or other irreversible operations.

## Enterprise mapping

| Lab element | Enterprise counterpart |
|---|---|
| Trusted runner | Service that binds authenticated identity and task context |
| Policy file | Reviewed capability grant managed outside the model |
| Gateway | Policy enforcement point between agent and real tools |
| JSON event | Input to an independent audit collector |
| Stop flag | Small starting point for capability revocation |

## Challenge

Temporarily grant a second file in the lab policy. What changes in the policy
digest and blast radius? Why is a policy hash not evidence that a change was
authorized? Do not use real data for this exercise.

## Key takeaway

The model may choose a request. A trusted component must decide whether it may
become an action. See [LESSON.md](LESSON.md) after explaining the result yourself.
