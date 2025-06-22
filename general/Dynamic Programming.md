---
aliases:
  - dynamic programming
  - dynamic programs
checked: false
created: 2023-08-26
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: technique
---
# Dynamic programming

This is an algorithmic technique to solve some [[Recursion|recursion]] type problems in an [[Iterative algorithms|iterative]] way. This can speed up this processes dramatically especially when [[Recursion|recursion]] would compute a similar step multiple times.

The basic structure of this technique is to:
1. Break a problem down into smaller sub problems.
2. Use the solutions to previous sub problems to solve subsequent sub-problems.
3. Use the solution to all sub problems to solve the main question.

(If this feels a lot like [[Induction]], that is because this is essentially a programming equivalent.)

> [!example] Longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] (LIS)
> Suppose we are provided with a [[sequence]] of $n$ numbers $a_1, a_2, \ldots, a_n$ and we want to find the length of the longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] in $\{a_i\}_{i=1}^n$.
>
> This can be done using [[Dynamic Programming|dynamic programming]] with the following steps:
>
> Let $L(i)$ be the LIS on $a_1, \ldots, a_i$ that ends with $a_i$.
>
> First note that $L(1) = 1$ as there is only 1 term in $a_1$. Moreover, if $a_i \geq a_j$ for $j<i$ then $L(i) = 1$. Generically though for $i$ we need find the longest increasing subsequence that ended with a number $a_j$ before your current term $a_i$ (so $j < i$) such that the end number is less than your current term (so $a_j < a_i$). Mathematically we would say
> $$L(i) = 1 + \max \{0, \ L(j) \ \vert \ 1 \leq j < i \mbox{ and } a_j < a_i \}.$$
>
> Then the solution to the LIS problem for a given sequence is $\max\{L(i) \vert 1 \leq i \leq n\}$, as a longest increasing subsequence has to end with some term.


This requires that the problem has the following properties.

1. **Overlapping Subproblems**: The problem can be divided into smaller overlapping subproblems that are solved independently.
2. **Optimal Substructure**: The solution to the problem can be constructed from the optimal solutions of its subproblems.

## Advantages

1. **Efficiency**: Dynamic programming can dramatically reduce the time complexity of algorithms that solve problems with overlapping subproblems.
2. **Simplicity**: The core idea is often straightforward to implement, making it easier to write correct and efficient code for complex problems.

## Limitations

1. **Memory**: Storing the results of all subproblems can sometimes require a lot of memory.
2. **Analytical Complexity**: It may be challenging to determine the structure of the subproblems and how to combine them to solve the original problem.

# Links
- [[Week 1 - Dynamic Programming|Lecture notes and worked examples]]
