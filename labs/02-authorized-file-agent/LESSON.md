# Lab 02 lesson notes

The defect in Lab 01 is missing authorization, not simply an insufficient prompt.
Lab 02 keeps the same hostile request and moves the decision into an explicit
gateway. Identity and scope come from the trusted runner, not the proposal.

Only the invoice is granted. A directory called `public` is not a grant for every
file within it. A new task needs a new reviewed scope.

Governance appears in the policy as purpose, ownership, autonomy and risk linkage.
The decision includes its policy version and digest so a reviewer can distinguish
configuration changes even if someone forgets to change the version string.
Neither the digest nor the owner field is a signature or proof of authorization.

The audit sink is called before the read and after completion. This separates an
authorization decision from evidence that the operation returned. It is not an
immutable incident recorder. An independent durable collector is future work.

The stop operation revokes future calls on this gateway instance. It does not
interrupt an in-flight read, terminate another process or revoke cloud credentials.

Most importantly, the model must not have arbitrary code execution inside the
gateway's process. Python object privacy and frozen data classes are programming
constraints, not a boundary against a compromised local process. Runtime isolation,
separate service identity and independent audit are needed before making stronger
claims. Static path checks also leave concurrent filesystem replacement races.

Passing these tests demonstrates the specified lab behavior. It is not proof that
all bypasses have been eliminated or that an agent is safe for production.
