---
aliases: Conjunctive normal form, conjunctive normal form, CNF
checked: false
created: 2023-08-28
last_edited: 2023-11-11
publish: true
tags: maths, computer-sciecne, logic
type: definition
---
# Conjunctive normal form (CNF)

A [[Boolean function]] is in *conjunctive normal form* if it is a collection of or statements unified by and operations. The or statements can contain negated variables but no further nesting.

The following are in CNF:
- $A$,
- $(A \lor B)$,
- $(A) \land (B)$,
- $(A \lor B) \land (A)$,
- $\lnot A$ , and
- $(A \lor \lnot B \lor \lnot C) \land (\lnot D \lor E \lor F)$.

The following are not in CNFL:
- $\lnot(B \lor C)$,
- $(A \land B) \lor C$, and
- $A \land (B \lor (C \land E))$.
