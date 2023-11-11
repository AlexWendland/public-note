---
aliases: null
chatgpt: false
created: 2023-11-02
last_edited: 2023-11-02
publish: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Knapsack-search (without replacement)|Knapsack-search]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

The problem statement is in the form of a [[Search problems|search problem]].

Given a proposed solution $S' \subset \{1, \ldots, n\}$ to check if it solves the problem we just need to calculate and check the following.
$$
\sum_{i \in S'} w_i \leq B, \mbox{ and } \sum_{i \in S'} v_i \geq g.
$$
This takes $O(n)$ time, so is polynomial.

This makes [[Knapsack-search (without replacement)|Knapsack-search]] run in polynomial time.
