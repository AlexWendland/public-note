---
aliases:
created: 2023-11-12
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Subset-sum problem is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Subset-sum problem](subset-sum_problem.md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

It conforms to the definition of a [search problem](search_problems.md) as it either returns a result or says no such result exists.

Suppose we are given an instance $a_i$ for $1 \leq i \leq n$ and $t$. To verify a solution $S \subset \{1, \ldots, n\}$ make the check
$$
\sum_{i \in S} a_i = t
$$
This takes $O(n\log(t))$ time. Therefore this takes [polynomial time](polynomial_time.md).
