---
aliases:
created: 2023-11-16
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: The k-colourings problem is NP-complete
type: lemma
---
# Statement

> [!lemma] Lemma
> The [k-vertex-colouring problem](k-colourings_problem_(graphs).md) is [NP-complete](np-complete.md).

# Proof

We have already show [The k-colourings problem is in NP](the_k-colourings_problem_is_in_np.md). So all that is left to show is that it is [NP-hard](np-hard.md).

We can prove [NP-complete](np-complete.md) using the [SAT problem](satisfiability_problem_(sat_problem).md). (Which we have [SAT is NP-complete](sat_is_np-complete.md).)

Proof outline.

Suppose we have an instance of the $f$ of the [SAT problem](satisfiability_problem_(sat_problem).md) with $n$ variables $x_i$ for $1 \leq i \leq n$ and $m$ clauses $c_j$ for $1 \leq j \leq m$. Note we assume each variable appears in at most one literal per clause so the clauses are of size at most $n$. Then we are going to define a graph $G$ for the $n+1$ colouring problem. (Note: If $n \leq 2$, we solve the problem in polynomial time using the [2-SAT algorithm using SCC](2-sat_algorithm_using_scc.md) - so from now on assume $k \geq 3$.)

The [graph](graph.md) $G$ has the following vertices:
- A $T$ and $F$ vertex for true and false,
- Base vertices $b_k$ for $1 \leq k \leq n - 1$,
- Variable vertices $x_i$ and $\overline{x_i}$ with $1 \leq i \leq n$, and
- Clause vertices $c_j^k$ with $1 \leq j \leq m$ and $1 \leq k \leq n+1$ Suppose clauses are of size at most.

The [graph](graph.md) $G$ has the following edges:
- With $T$, $F$ and $b_k$ for $1  \leq k \leq n-1$ make a [clique](clique_(graph).md) of size $n+1$,
- For each pair variable vertices $x_i$ and $\overline{x_i}$ connect the to one another i.e. $(x_i, \overline{x_i}) \in E$,
- For each variable vertex $x_i$ and $\overline{x_i}$ connect them to all $b_k$ i.e. $(x_i, b_k), (\overline{x_i}, b_k) \in E$,
- For each clause $c_j$ the vertices $c_j^k$ form a [clique](clique_(graph).md) of size $n+1$,
- For each clause $c_j = \bigwedge_{k=1}^{a_j} l^k_j$ for some $1 \leq a_j \leq n$ connect $l^k_j$ to $c_j^k$ i.e. $(l^k_j,c^k_j) \in E$ , and
- For $a_j < k \leq n+1$ connect $c^k_j$ to $F$, i.e. $(c^k_j, F) \in E$.

This graph takes $O(n + m)$ to build the graph as we need to iterate through clauses and variables so can be done in [polynomial time](polynomial_time.md). We provide [graph](graph.md) $G$ to the $n+1$-colouring problem.

If the graph has no $n+1$ colouring, say that $f$ has no assignment. If the graph has an $n+1$ colouring from [Claim 1](the_k-colourings_problem_is_np-complete.md#claim-1) we know each variable vertex $x_i$ and $\overline{x_i}$ as the same colour as either $T$ or $F$. Return the assignment $a(x_i)$ as true if $c(x_i) = c(T)$ or false otherwise. This takes at most $O(n)$ as we have to loop through the variables checking their assignment - so can be done in [polynomial time](polynomial_time.md).

Suppose the constructed colouring problem has a solution. From [Claim 1](the_k-colourings_problem_is_np-complete.md#claim-1) we have a valid assignment and from [Claim 2](the_k-colourings_problem_is_np-complete.md#claim-2) one literal in every clauses is assigned True. Therefore, this assignment satisfies $f$.

Suppose we have an assignment $a$ to $x_i$ (where $a(x)$ is 0 if it is False and 1 if it is True) that is a solution to the [SAT problem](satisfiability_problem_(sat_problem).md) $f$. Then build the following colouring
- Set $c(F) = 1$, $c(T) = 2$, and $c(b_k) = k + 2$,
- Set $c(x_i) = a(x_i) + 1$ and $c(\overline{x_i}) = a(\overline{x_i}) + 1$, and
- Lastly for each clause $c_j$ find literal $l^{k'}_j$ where we have $a(l^{k'}_j)$ is True set the corresponding $c(c_j^{k'}) = 1 = c(F)$ and assign $c(c^{n+1}_j) = 2 = c(T)$ (note as there are at most $n$ literals $k' \not = n+1$) then assign each other $c_j^k$ a different one of the remaining $n-1$ colours.

Lets check the edges to ensure this is a valid colouring:
- As $T$, $F$ and $b_k$ are assigned distinct colours these edges all connect vertices of different colours,
- As $a(x_i) \not = a(\overline{x_i})$ then $c(x_i) \not = c(\overline{x_I})$ and the edge $(x_i, \overline{x_i})$ is respected,
- As $c(x_i), c(\overline{x_i}) \leq 2$ and $c(b_k) \geq 3$ we have these connected edges are respected,
- As each of the clause vertices $c_j^k$ receive a distinct colour the [clique](clique_(graph).md) edges are respected,
- For each clause $c(l^k_j) \leq 2$ as the only $c(c_j^k) \leq 2$ have $k = k'$ or $k = n+1$ and we have $c(l^{k'}_j) = 2$ the rest of the literals $l^k_j$ connect to vertex with $c(c_j^k) \geq 3$ so these edges are respected, and lastly
- As $c(F) = 1$, and $c(l^k_j) \geq 1$ for all $k \not = k'$ where $k' \leq a_j$ we have all the edges $(c_j^k, F)$ are respected.

Therefore this is a valid $n+1$-colouring of our constructed $G$.

So we have this is a [many-one reduction](many-one_reduction_(problem).md) reduction of the [SAT problem](satisfiability_problem_(sat_problem).md) to the [k-colourings problem (graphs)](k-colourings_problem_(graphs).md). Giving it is [NP-complete](np-complete.md).

## Claim 1

>[!important] Claim 1
>If the constructed graph $G$ has a $n+1$-colouring $c$ then the following holds
>- $c(T) \not = c(F)$ moreover $T$, $F$, and $b_k$ all have distinct vertices that use all $n + 1$ colours,
>- $c(x_i) \not = c(\overline{x_i})$ for every $1 \leq i \leq n$, and
>- $\{c(T), c(F)\} = \{c(x_i), c(\overline{x_i})\}$ for every $1 \leq i \leq n$.

## Proof of Claim 1

The first statement holds as $T$, $F$, and $b_k$ are all connected in a [clique](clique_(graph).md) of size $n+1$.

The second statement holds as $x_i$ and $\overline{x_i}$ are connected.

The last statement holds as $x_i$, $\overline{x_i}$, and $b_k$ are all connected in a [clique](clique_(graph).md) of size $n+1$ so have different colours from one another. Therefore the colours each $x_i$ and $\overline{x_i}$ are assignment must be the same as that of $T$ and $F$ up to some order.

## Claim 2

>[!important] Claim 2
>If the constructed graph $G$ has a $n+1$-colouring $c$ then for each clause $c_j = \bigwedge_{k=1}^{a_j} l^k_j$ for some $1 \leq a_j \leq n$ the following holds:
>- The clause vertices $c_j^k$ all have distinct colours that use the $n+1$ colours,
>- The clause vertex with the colouring $c(c_{j}^{k'}) = c(F)$ is connected with a literal vertex of the clause $l_j^{k'}$, i.e. $1 \leq k' \leq a_j$, and
>- The literal vertex $l_j^{k'}$ has $c(l_j^{k'}) = c(T)$

## Proof of Claim 2

The first statement holds as $c_j^k$ form a clique of size $n+1$.

As the vertices $c_j^k$ have every colour there exists a vertex $c_j^{k'}$ where $c(c_j^{k'}) = c(F)$. As vertices $c_j^k$ with $k > a_j$  are connected with vertex $F$ we have $c(c_j^k) \not = c(F)$ for all $k > a_j$. So $k' \leq a_j$ and it is connected to a literal vertex. This shows the second statement.

From [Claim 1](the_k-colourings_problem_is_np-complete.md#claim-1) we have $c(l^{k'}_j) \in \{c(T), c(F)\}$, however as $l^{k'}_j$ is connected to $c_j^{k'}$ with $c(c_j^{k=1}) = c(F)$ by exclusion we have $c(l^{k'}_j) = c(T$). Giving the final statement.


