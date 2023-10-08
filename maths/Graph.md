---
aliases:
  - graph
  - graphs
  - Graphs
  - undirected graph
  - Undirected graph
  - undirected graphs
type: definition
publish: true
created: 2023-08-28
last_edited: 2023-08-28
tags:
  - maths
  - graph-theory
chatgpt: false
---
> [!tldr] Graph
> A simple undirected graph is tuple $V$ the *vertex set* and $E \subset V \times V$  an *edge set*. This is normally referred to as $G = (V, E)$. As this is undirected an edge $e = (x,y)$ is the same as the edge $e = (y,x)$, so if we define an [[Equivalence relation|equivalence relation]] $(x,y) \sim (y,x)$ for all $x,y \in V$ then it is fairer to say $E \subset V \times V / \sim$.

## Representations

> [!example] Visual representation
> This is normally represented as a series of points and lines like the simple graph below.
> ![[simple_graph]]
> This graph would have formal definition 
> $$V = \{1,2,3,4\} \ \mbox{ and } \ E = \{(1,2), (1,3), (2,3), (3,4)\}.$$

When storing it in a computer we have multiple different formats:
- [[Adjacency list format (graph)|Adjacency list]]
- 