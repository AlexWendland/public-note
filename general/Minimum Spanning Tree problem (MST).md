---
aliases:
  - MST
  - Minimum spanning tree problem
checked: false
created: 2023-10-01
last_edited: 2023-10-01
publish: true
tags:
  - programming
type: problem
---
# Statement

>[!tldr] Minimum Spanning Tree problem
>Given an [[Graph|undirected graph]] $G = (V,E)$ with weights $w: E \rightarrow \mathbb{R}$ can you find a [[Spanning subgraph|spanning]] [[Tree (graph)|tree]] $T = (V, E')$ with minimum weight
>$$w(T) = \sum_{e \in E'} w(e).$$

# Solutions
- [[Kruskal's algorithm]]
	- It takes $O(\vert E \vert \log(\vert V \vert))$.
- [[Prim's algorithm]]
	- It takes $O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.

# Theory
- [[Minimum Spanning Tree problem is in NP]]
-
