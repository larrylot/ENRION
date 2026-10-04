"""
ENRION Lab 01 — Offline security demonstration.

No LLM is required.

We simulate the important part of the failure:
a compromised agent asks the tool for a restricted resource.

The purpose is to isolate the architecture problem from model behavior.
"""

from tools import read_file


def main() -> None:
    print("ENRION / Lab 01")
    print("=" * 60)

    print("\n1. The user asks the agent to summarize public/invoice.txt")
    invoice = read_file("public/invoice.txt")
    print("\n[UNTRUSTED DOCUMENT]")
    print(invoice)

    print("\n2. The document contains an instruction aimed at the agent.")
    print("   Assume the model is successfully prompt-injected.")

    requested_path = "restricted/secret.txt"

    print(f"\n[AGENT REQUEST] read_file({requested_path!r})")
    print("[TOOL] ALLOWED — no policy layer exists")

    secret = read_file(requested_path)

    print("\n[TOOL OUTPUT]")
    print(secret)

    print("\n[SECURITY RESULT] SECRET EXPOSED")
    print("\nWhy? The model's requested action and authorization were treated")
    print("as the same thing. Lab 02 will separate them.")


if __name__ == "__main__":
    main()
