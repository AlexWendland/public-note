---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: lemma
---
> [!important] Lemma
> Suppose we have a [[Directed graph|directed graph]] $G = (V,E)$ and $post: V \rightarrow \mathbb{N}$ be the result of running the [[DFS to find connected components in an undirected graph]] algorithm. Then the vertex with the largest post order number lies in a source [[Strongly connected components (directed graphs)|strongly connected component]] in the [[Strongly connected component graph (directed graph)|strongly connected component graph]].

## Proof

Let $S$ be the [[Strongly connected components (directed graphs)|strongly connected component]] with the vertex of highest $post$ value.

Suppose some other [[Strongly connected components (directed graphs)|strongly connected component]] $S'$ were to have an edge connecting to $S$ in the [[Strongly connected component graph (directed graph)|strongly connected component graph]].

From the [[How post order relates to strongly connected components|Lemma]] $S'$ has a vertex with higher post order than all vertices in $S$. This is a contradiction as $S$ contains the vertex with highest post order.


