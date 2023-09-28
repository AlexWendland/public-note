---
aliases: 
type: lemma
publish: true
created: 2023-09-28
last_edited: 2023-09-28
tags:
  - maths
chatgpt: false
---
> [!important] Lemma
> Suppose we have a [[Directed graph|directed graph]] $G$ and a [[Strongly connected components (directed graphs)|strongly connected component]] [[Depth-first search (DFS)|DFS]] algorithm $A$ on $G$. Then the vertex with the largest post order number lies in a source [[Strongly connected components (directed graphs)|strongly connected component]].
> 

## Proof

Let $G = (V, E)$ be a [[Directed graph|directed graph]] with $A$ on it. Suppose we have a vert $v \in V$ with the largest post order number. This means it is the root of the [[DFS tree (algorithm)|DFS tree]] and it has a path to all vertices in that tree.

