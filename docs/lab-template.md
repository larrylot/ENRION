# ENRION Lab Teaching Standard

Every lab follows the same sequence.

## 1. Learn
Introduce only the concepts required for the lab. Keep the system small and show the architecture.

## 2. Threat
Define the asset, untrusted input, agent capability, attacker influence, and vulnerable assumption.

## 3. Predict
Require the learner to predict the outcome **before execution**.

## 4. Break
Run a deliberately vulnerable design with reproducible commands.

## 5. Observe
Show the event sequence without immediately explaining it.

## 6. Explain
Ask:
1. What is the asset?
2. What is untrusted?
3. What authority does the agent hold?
4. Which trust boundary was crossed?
5. What control was missing?
6. What if the model is fully compromised?

Detailed answers belong in LESSON.md.

## 7. Defend
Add the smallest visible control that fixes the architectural failure.

~~~text
request → decision → enforcement
~~~

Do not hide the first implementation inside a large framework.

## 8. Break Again
Repeat the attack and try bypasses.

The success condition is not "the model refused".

The success condition is:

> **The unsafe action is impossible even if the model requests it.**

## 9. Enterprise Mapping
Map toy components to realistic enterprise assets, identities, APIs, platforms, and workflows.

## 10. Challenge
Give the learner an unsolved modification that tests understanding rather than copy/paste skill.

## 11. Key Takeaway
End with one memorable security principle.

## Quality gate

A lab is not complete unless the learner can explain what failed, why it failed, where the control belongs, whether the fix survives a compromised model, the remaining blast radius, and the enterprise equivalent.
