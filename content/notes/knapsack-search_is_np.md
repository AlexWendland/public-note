---
aliases:
created: 2023-11-02
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: Knapsack-search is NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Knapsack-search](knapsack-search_(without_replacement).md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

The problem statement is in the form of a [search problem](search_problems.md).

Given a proposed solution $S' \subset \{1, \ldots, n\}$ to check if it solves the problem we just need to calculate and check the following.
$$
\sum_{i \in S'} w_i \leq B, \mbox{ and } \sum_{i \in S'} v_i \geq g.
$$
This takes $O(n)$ time, so is polynomial.

Since the verification of a proposed solution can be done in polynomial time, [Knapsack-search](knapsack-search_(without_replacement).md) is in NP.
