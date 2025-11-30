---
aliases: null
checked: false
created: 2023-11-10
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
---
# Check if a linear programme is solvable

We are going to use the [[Checking if a linear programme is feasible|feasibility algorithm]] for a [[Linear programme|linear programme]] to do this - lets call this $feasibility\_checker$ that takes a [[Linear programme|linear programme]] and outputs a boolean based on if it is feasible or not.

This uses a corollary of the [[Weak duality theorem (linear programme)]] which tells us [[Unbounded linear programmes have infeasible duals|unbounded linear programmes have infeasible duals]]. So we will check if the [[Dual linear programme|dual linear programme]] is feasible. For this let $dual$ be an algorithm to calculate the dual.

# Algorithm

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
