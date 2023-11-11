---
aliases:
  - Pseudo-polynomial
  - pseudo-polynomial time
checked: false
created: 2023-10-03
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: definition
---
> [!tldr] Pseudo-polynomial time
> An algorithm runs in *pseudo-polynomial time* if its running time is polynomial in the numeric value of the input but not necessarily in the length of the input.

# Intuition

If you are given an integer input $n \in \mathbb{Z}$. If you can solve a problem in $O(n)$ time we think it is [[Polynomial time|polynomial time]] algorithm. However the number $n$ will be represented in [[Binary|binary]] so will have length $l := \log_2(n)$. Therefore the problem running time in the *length* of the input is $O(2^l)$.

# Examples

- [[Ford-Fulkerson Algorithm]]
- [[Knapsack problem (without repetition)]]

