---
aliases: null
checked: false
created: 2023-11-09
last_edited: 2023-11-09
publish: true
tags:
  - programming
type: algorithm
---
# Checking if a linear programme is feasible

Suppose we are given a [[Linear programme standard form|linear programme in standard form]] specified by $x, c \in M_{n,1}(\mathbb{R})$, $A \in M_{m,n}(\mathbb{R})$, and $b \in M_{m,1}(\mathbb{R})$ and we have a standard form linear programme solver $linear\_programme\_solver$.

Note we will include in the algorithm some transformation to guarantee the inputted linear programme is in standard form by breaking up the added variable into it's positive and negative components. See [[Linear programme standard form|getting a linear programme in standard form]]

```pseudocode
feasibility_check(A, b):
	Input: The constraints to a linear programme in standard form.
	Output: If the linear programme is feasible.
1. Extend A with a column of 1's and another column of -1's at the end, making A' size m x (n+2).
2. Set objective function c = (0, 0, ..., 0, 1, -1) of length n+2.
3. Run linear_programme_solver(A', b, c).
4. If the value of the objective function is positive output it is feasible.
5. Otherwise say it is not.
```

