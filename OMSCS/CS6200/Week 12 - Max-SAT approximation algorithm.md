---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-11-10
last_edited: 2023-11-11
publish: true
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Max-SAT approximation algorithm

In this lecture we consider the a similar problem to the [[Satisfiability problem (SAT problem)|SAT problem]].

![[Max-Satisfiability Problem#Statement|Max-SAT]]

This is [[NP-hard]].

![[Max-SAT is NP-hard]]

Therefore it is unlikely to find any algorithm that will solve the problem quickly. However we will look at using [[Linear programme|linear programming]] to approximate a solution.

## Approximate algorithms

Let $f$ be a [[Boolean function|boolean function]] in [[Conjunctive normal form (CNF)|CNF]] with $m$ clauses. Let $m^{\ast}$ denote the solution to the [[Max-Satisfiability Problem|max-SAT]] problem for $f$.

We want to construct an algorithm the on an input $f$ outputs $l$ where $l \geq m^{\ast}d$, this will be referred to as a $d$-approximation algorithm.

## Simple half-approximation algorithm

Suppose we have $f$ with variables $x_i$ for $1 \leq i \leq n$ and clauses $c_i$ for $1 \leq i \leq m$.

Make random assignment
$$
x_i = \begin{cases} T & \mbox{with probability } 1/2\\ F & \mbox{with probability } 1/2\end{cases}
$$
lets look at how many clauses this satisfies $w$. We have expectation
$$
\mathbb{E}[w] = \sum_{l=0}^m l \ \mathbb{P}(w = l)
$$
however it will be easier to break it down further. Let
$$
w_j = \begin{cases} 1 & \mbox{if } c_j \mbox{ is satisfied}\\ 0 & \mbox{otherwise}\end{cases}
$$
so we have
$$
w = \sum_{j=1}^m w_j, \mbox{ therefore } \mathbb{E}[w] = \mathbb{E}[\sum_{j=1}^m w_j] = \sum_{j=1}^m \mathbb{E}[w_j].
$$
Suppose $c_j$ has $k_j$ literals that use distinct variables. For any literal, given our assignment, its probability of being true is $1/2$. For $c_j$ to be true we just need one of these literals to be true. We have,
$$
\mathbb{E}[w_j] = 1 \cdot \mathbb{P}[w_j = 1] + 0 \cdot \mathbb{P}[w_j = 0] = \left( 1 - \frac{1}{2^{k_j}}\right) \geq \frac{1}{2}.
$$
In summary we have
$$
\mathbb{E}[w] = \sum_{j=1}^m E[w_j] \geq \frac{m}{2} \geq \frac{m^{\ast}}{2}
$$
though this is in expectation - which means there is an assignment that has more than $m/2$ clauses satisfied.

We can in fact find this pretty easily. 

![[Max-SAT random approximation algorithm#Pseudocode]]

A version of this algorithm works even better on the following problem.

![[Max-k-exact-satisfiability problem#Statement]]

If we calculate this expectation more exactly we can get $m(1-2^{-k})$ clauses are satisfied.

For the case of $k=3$ it has been shown that doing any better than a $7/8$-approximation algorithm is [[NP-hard]].

## Integer programming


