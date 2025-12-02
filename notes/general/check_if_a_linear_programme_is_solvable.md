---
aliases:
checked: false
created: 2023-11-10
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Check if a linear programme is solvable
type: algorithm
---

We are going to use the [feasibility algorithm](checking_if_a_linear_programme_is_feasible.md) for a [linear programme](linear_programme.md) to do this - lets call this $feasibility\_checker$ that takes a [linear programme](linear_programme.md) and outputs a boolean based on if it is feasible or not.

This uses a corollary of the [Weak duality theorem (linear programme)](weak_duality_theorem_(linear_programme).md) which tells us [unbounded linear programmes have infeasible duals](unbounded_linear_programmes_have_infeasible_duals.md). So we will check if the [dual linear programme](dual_linear_programme.md) is feasible. For this let $dual$ be an algorithm to calculate the dual.

 Algorithm

```psuedocode
bounded_checker(A, b, c):
	Input: A linear programme in standard form specified by A, b, c.
	Output: Whether or not that linear programme is feasible and bounded, infeasible or unbounded.
1. Run feasibility_checker(A, b, c)
	1. If it is not feasible return that it is infeasible
2. Calculate the dual linear programme dual(A,b,c) = A^d, b^d, c^d.
3. Check if the dual is feasible feasibility_checker(A^d, b^d, c^d)
	1. If it is return that the original linear programme is solvable.
	2. If it is not return that the original linear programme is unbounded.
```
