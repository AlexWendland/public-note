---
aliases:
  - path
  - paths
checked: false
created: 2023-08-28
last_edited: 2023-08-28
publish: true
tags:
  - maths
  - graph-theory
type: definition
---
# Path (graph)

Given a [[Graph|graph]] $G = (V, E)$ a path is a [[Sequence|sequence]] of edges $\{e_i = (x_i, y_i)\}_{i=1}^k$ such that $x_i = y_{i+1}$ for all $1 \leq i < k$. We say the *length* of the path is $k$.

> [!example] Visual representation
> Lets use our simple [[graph]] below
> ![[simple_path]]
> There is a path that goes $(1,3), (3,4)$ from vertex 1 to vertex 4. Note there is an implicit directionality when we say this.

## The path graph

In graph theory we define the Path graph $P_k$ to be a graph as a [[Graph|graph]] with
$$V = \{1,2, \ldots, k\} \ \mbox{ and } \ E = \{(i,i+1)\ \vert \ 1 \leq i < k \}.$$ There is also an infinite analogy, both one sided and two sided.
