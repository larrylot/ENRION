# Verification record

Date: 6 November 2026. Execution: local Linux, CPython 3.12.14.
Original vulnerable baseline: commit `d8352be66712bebc5076187eb37eb428e3ce9a9c`.
The defended implementation and tests are introduced together with this record.
Use the containing Git commit to identify that source revision.

## Reproduce

```bash
python -X utf8 labs/01-vulnerable-file-agent/offline_demo.py
python -X utf8 labs/02-authorized-file-agent/offline_demo.py
python -m unittest discover -s tests -v
```

Observed locally: Lab 01 exposes the synthetic secret, Lab 02 denies the restricted
request and subsequent calls after stop, and all 33 tests pass with no skips.
No live LLM, external API or production environment was exercised.

## Claim to evidence

| Claim | Regression evidence |
|---|---|
| Vulnerable baseline exposes the fixture | BaselineTests.test_synthetic_restricted_file_is_exposed and test_offline_baseline_reproduces_exposure |
| Allowed operation still works | GatewayTests.test_permitted_read |
| Restricted request denied before read | test_restricted_read_is_denied_before_io |
| Another public file is not implicitly allowed | test_other_public_file_is_not_implicitly_authorized |
| Manipulated invoice does not widen scope | test_injected_instruction_cannot_change_resource_grant |
| Invalid paths and static symlinks deny | test_invalid_paths_are_denied and both symlink tests |
| Missing or malformed policy does not allow | missing policy file, malformed JSON and policy validation tests |
| Identity and action remain constrained | test_unknown_identity_is_denied and test_unknown_action_is_denied |
| Audit failure before read prevents execution | test_audit_failure_prevents_read |
| Events correlate without logging file contents | test_audit_correlates_request_result_and_policy and test_audit_contains_no_file_contents |
| Stop denies future calls even if audit fails | test_stop_denies_subsequent_calls and test_stop_takes_effect_even_if_audit_fails |

The test suite includes explicit skips for symlinks if the host cannot create them.
The local result above had no skips. CI, if run, has its own environment and results.
Inspect the specific commit in [GitHub Actions](https://github.com/larrylot/ENRION/actions).

## What these results do not establish

They do not measure prompt injection success against an actual model, contain a
compromised process, prove log durability, test race resistance, authenticate a
human owner, implement action approvals or establish regulatory compliance.
The offline demo forces the malicious request to isolate authorization behavior.
