---
aliases: null
chatgpt: false
created: 2023-11-02
last_edited: 2023-11-02
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> The [[Satisfiability problem (SAT problem)|Satisfiability problem]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

First note that it is in the form of a [[Search problems|search problem]] as it either provides you with a satisfying assignment to the $n$ variables or says one doesn't exist.

All that is left to show is that we can verify an answer in [[Polynomial time]].

Given an assignment of values to the $n$-variables. To check one clause is satisfied takes $O(n)$ time. There are $m$ clauses, so this in total takes $O(nm)$ time.

This is polynomial so the [[Satisfiability problem (SAT problem)|Satisfiability problem]] is in [[Nondeterministic Polynomial time (NP)|NP]].
