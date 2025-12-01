---
aliases:
checked: false
created: 2023-11-02
draft: false
last_edited: 2023-11-11
name: The Satisfiability problem is in NP
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> The [Satisfiability problem](satisfiability_problem_(sat_problem).md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

First note that it is in the form of a [search problem](search_problems.md) as it either provides you with a satisfying assignment to the $n$ variables or says one doesn't exist.

All that is left to show is that we can verify an answer in [Polynomial time](polynomial_time.md).

Given an assignment of values to the $n$-variables. To check one clause is satisfied takes $O(n)$ time. There are $m$ clauses, so this in total takes $O(nm)$ time.

This is polynomial so the [Satisfiability problem](satisfiability_problem_(sat_problem).md) is in [NP](nondeterministic_polynomial_time_(np).md).
