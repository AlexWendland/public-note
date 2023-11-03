---
aliases: 
type: lemma
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - programming
chatgpt: false
---
# Statement

> [!important] Lemma
> [[k-satisfiability problem (k-SAT problem)|k-SAT]] is [[NP-Complete|NP-complete]] for $k \geq 3$

# Proof

Note that [[k-SAT is in NP]].

Separately we have shown [[3-SAT is NP-complete]]. In this proof we showed a reduction of the [[Satisfiability problem (SAT problem)|SAT problem]] to [[k-satisfiability problem (k-SAT problem)|3-SAT]]. The [[3-SAT is NP-complete#Clause reduction|clause reduction]] in this takes a [[Satisfiability problem (SAT problem)|SAT problem]] and reduces it to a problem in [[k-satisfiability problem (k-SAT problem)|3-SAT]]. The same reduction can we used to reduce the [[Satisfiability problem (SAT problem)|SAT problem]] to [[k-satisfiability problem (k-SAT problem)|k-SAT]] for all $k \geq 3$, as a [[Conjunctive normal form (CNF)|CNF]] with at most $3$ terms has at most $k$ terms for $k \geq 3$.

Therefore [[k-satisfiability problem (k-SAT problem)|k-SAT]] is [[NP-hard]] and in [[Nondeterministic Polynomial time (NP)|NP]] so is [[NP-Complete|NP-complete]].

