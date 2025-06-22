---
aliases: null
checked: false
created: 2023-11-12
last_edited: 2023-11-12
draft: false
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[Subset-sum problem]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

It is of the format to be a [[Search problems|search problem]] as it either returns a result or it says no such result exists.

Suppose we are given an instance $a_i$ for $1 \leq i \leq n$ and $t$. To verify a solution $S \subset \{1, \ldots, n\}$ make the check
$$
\sum_{i \in S} a_i = t
$$
this takes $O(n\log(t))$ time. Therefore this takes [[Polynomial time|polynomial time]].
