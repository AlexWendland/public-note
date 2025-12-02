---
aliases:
  - path
  - paths
checked: false
created: 2023-08-28
draft: false
last_edited: 2023-11-11
title: Path (graph)
tags:
  - maths
  - graph-theory
type: definition
---
# Path (graph)

Given a [graph](graph.md) $G = (V, E)$ a path is a [sequence](sequence.md) of edges $\{e_i = (x_i, y_i)\}_{i=1}^k$ such that $x_i = y_{i+1}$ for all $1 \leq i < k$. We say the *length* of the path is $k$.

> [!example] Visual representation
> Lets use our simple [graph](graph.md) below
> ![simple_path](../../images/excalidraw/simple_path.excalidraw.svg)
> There is a path that goes $(1,3), (3,4)$ from vertex 1 to vertex 4. Note there is an implicit directionality when we say this.

## The path graph

In graph theory we define the Path graph $P_k$ to be a graph as a [graph](graph.md) with
$$V = \{1,2, \ldots, k\} \ \mbox{ and } \ E = \{(i,i+1)\ \vert \ 1 \leq i < k \}.$$ There is also an infinite analogy, both one sided and two sided.
