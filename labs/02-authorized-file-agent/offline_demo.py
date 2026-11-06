"""Repeat the Lab 01 malicious request through an external authorization check."""

import json
from pathlib import Path

from gateway import FileGateway, Policy


def main() -> None:
    here = Path(__file__).resolve().parent
    policy = Policy.load(here / "policy.json")
    workspace = here.parent / "01-vulnerable-file-agent" / "workspace"
    gateway = FileGateway(workspace, policy, "invoice-agent",
                          lambda event: print(json.dumps(event, sort_keys=True)))
    invoice = gateway.execute("read_file", "public/invoice.txt")
    assert "INVOICE 1042" in invoice
    try:
        gateway.execute("read_file", "restricted/secret.txt")
    except PermissionError:
        print("RESTRICTED READ BLOCKED")
    else:
        raise AssertionError("Restricted file unexpectedly readable")
    gateway.stop()
    try:
        gateway.execute("read_file", "public/invoice.txt")
    except PermissionError:
        print("POST-STOP READ BLOCKED")
    else:
        raise AssertionError("Stopped agent unexpectedly allowed")
    print("LAB 02 PASS: allowed read works; restricted and post-stop reads denied")


if __name__ == "__main__":
    main()
