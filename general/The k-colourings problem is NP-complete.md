---
aliases: null
checked: false
created: 2023-11-16
last_edited: 2023-11-16
publish: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> The [[k-colourings problem (graphs)|k-vertex-colouring problem]] is [[NP-Complete|NP-complete]].

# Proof

We have already show [[The k-colourings problem is in NP]]. So all that is left to show is that it is [[NP-hard]].

We can prove [[NP-Complete|NP-complete]] using the [[Satisfiability problem (SAT problem)|SAT problem]]. (Which we have [[SAT is NP-complete]].) 

Proof outline.

Suppose we have an instance of the $f$ of the [[Satisfiability problem (SAT problem)|SAT problem]] with $n$ variables $x_i$ for $1 \leq i \leq n$ and $m$ clauses $c_j$ for $1 \leq j \leq m$. Note we assume each variable appears in at most one literal per clause so the clauses are of size at most $n$. Then we are going to define a graph $G$ for the $n+1$ colouring problem. (Note: If $n \leq 2$, we solve the problem in polynomial time using the [[2-SAT algorithm using SCC]] - so from now on assume $k \geq 3$.) 

$G$ has the following vertices:
- A $T$ and $F$ vertex for true and false,
- Base vertices $b_i$ for $1 \leq i \leq n - 1$,
- Variable vertices $x_i$ and $\overline{x_i}$ with $1 \leq i \leq n$,
- Clause vertices $c_j^i$ with $1 \leq j \leq m$ and $1 \leq i \leq k-1$ 

- 