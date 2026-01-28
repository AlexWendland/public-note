---
aliases:
created: 2023-11-03
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
title: k-SAT is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [k-SAT](k-satisfiability_problem_(k-sat_problem).md) is in [NP](nondeterministic_polynomial_time_(np).md)

# Proof

[k-SAT](k-satisfiability_problem_(k-sat_problem).md) is in the correct form for a [search problem](search_problems.md). It either outputs an assignment that satisfies the formula or it says no such assignment exists.

To check an assignment $S$ we have to check each clause, and for each clause we check $k$ of the variables which takes at most $O(nm)$ time—polynomial in the input size.

Therefore [k-SAT](k-satisfiability_problem_(k-sat_problem).md) is in [NP](nondeterministic_polynomial_time_(np).md).
