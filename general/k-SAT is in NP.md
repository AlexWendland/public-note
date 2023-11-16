---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[k-satisfiability problem (k-SAT problem)|k-SAT]] is in [[Nondeterministic Polynomial time (NP)|NP]]

# Proof

[[k-satisfiability problem (k-SAT problem)|k-SAT]] is in the correct form for a [[Search problems|search problem]]. It either outputs an assignment that satisfies the formula or it says no such assignment exists.

To check an assignment $S$ we have to check each clause, with each clause we check $k$ of the variables which takes at most $O(nm)$ time - polynomial in the input size.

Therefore [[k-satisfiability problem (k-SAT problem)|k-SAT]] is in [[Nondeterministic Polynomial time (NP)|NP]].
