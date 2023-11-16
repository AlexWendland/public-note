---
aliases: null
checked: false
created: 2023-09-29
last_edited: 2023-11-11
publish: true
tags:
  - maths
type: lemma
---
>[!important] Lemma
>Let $G = (V,E)$ be a [[Directed graph|directed graph]] with two [[Strongly connected components (directed graphs)|strongly connected components]] $S$ and $S'$. Let $post: V \rightarrow \mathbb{N}$ be the result of running the [[DFS to find connected components in an undirected graph]] algorithm $A$. If there exists $v \in S$ and $w \in S'$ such that $(v,w) \in E$ then
>$$\max_{x \in S} post(x) > \max_{y \in S'} post(y).$$

## Proof

As $S$ and $S'$ are separate [[Strongly connected components (directed graphs)|strongly connected components]] with an edge $(S, S')$ in the [[Strongly connected component graph (directed graph)|strongly connected component graph]]. As [[The strongly connected component graph is a DAG|the strongly connected component graph is a DAG]] there is not a path from $S'$ to $S$ in $G$.

During the fun of [[DFS to find connected components in an undirected graph]] $A$ we must visit either a vertex in $S$ or $S'$ first.

Suppose we first visit a vertex $w \in S'$. Here all $S'$ will be visited by `explore` from $w$ and the algorithm will have to leave via $w$ before it can visit a vertex of $S$. Therefore all vertices in $S'$ will have lower post number than any vertex in $S$.

Suppose instead we first visit a vertex $w \in S$. From this vertex we will explore the whole of $S$ and $S'$ before exiting $w$. Therefore all vertices in $S$ and $S'$ will appear in a branch below $w$ in the [[DFS tree (algorithm)|DFS tree]]. This gives that $w$'s post number is larger than that for all vertices $S \cup S' \backslash \{w\}$. So
$$post(w) = \max_{x \in S} post(x) > \max_{y \in S'} post(y)$$
as required.
