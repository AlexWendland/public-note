---
aliases:
created: 2023-11-12
date_checked:
draft: false
last_edited: 2023-11-12
tags:
  - programming
title: Max-SAT random approximation algorithm
type: algorithm
---

This is a naïve approximate solution to the [Max-SAT](max-satisfiability_problem.md) problem. If the formula has $n$ variables and $m$ clauses this guarantees $m/2$ clauses will be satisfied by the assignment.

# Pseudocode

```pseudocode
Name(f):
	Input: Boolean formula in CNF form f, with variables x_i and clauses c_j.
	Output: An assignment to x_i that satisified m/2 clauses.
1. Let C be the set of clauses and build assignment a : x_i |-> T/F.
2. For each x_i:
	1. Let A be all the clauses in C containing the x_i literal.
	2. Let B be all the clauses in C containing the not x_i literal.
	3. If A is bigger than or equal to B, set a(x_i) = T and remove A from C.
	4. Else set a(x_i) = F and remove B from C.
3. Return assignment a.
```

# Run time

We loop $n$ times having to look through a list of size at most $m$. Therefore this takes $O(nm)$.

# Correctness

We show this by induction on the number of variables.

If we have a single variable, then all clauses are either $x_i$ or $\overline{x_i}$ as we assume each variable only appears in a single literal in each clause. By picking the larger set of either $x_i$ or $\overline{x_i}$ we guarantee our assignment satisfies more than half these clauses.

Assume we have proven that on $k-1$ variables our algorithm satisfies more than $m/2$ clauses.

Suppose we have formula $f$ with $k$ variables. Let $E$ be the set of all clauses that use only $x_k$. Remove all literals from $f$ that involve $x_k$ to make $f'$ with $m - \vert E \vert$ clauses.

Similarly to case $k=1$ there is an assignment $a^{\ast}(x_k)$ that satisfies at least $\vert E \vert / 2$ clauses as they just involve $x_k$.

When we run our algorithm on $f'$ we get an assignment $a'$ that satisfies $y' \geq (m - \vert E \vert) / 2$.

The steps that return this assignment are identical to that of running it on the first $k-1$ variables of $f$. Therefore $a'(x_i) = a(x_i)$ for $1 \leq i \leq k-1$.

In the last step we consider $x_k$, we pick $a(x_k)$ that maximises the number of left over unsatisfied clauses. This includes the clauses in $E$ where $a^{\ast}(a_k)$ satisfies at least $\vert E \vert / 2$, therefore $a(a_k)$ satisfies $z \geq \vert E \vert / 2$ new clauses - as it is maximal.

Therefore the assignment $a$ satisfies
$$
y' + z \geq (m - \vert E \vert)/2 + \vert E \vert / 2 = m / 2
$$
clauses and we have proved the induction case for $k$.
