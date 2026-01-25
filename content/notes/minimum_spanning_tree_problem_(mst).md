---
aliases:
  - MST
  - Minimum spanning tree problem
created: 2023-10-01
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Minimum Spanning Tree problem (MST)
type: problem
---
# Statement

>[!tldr] Minimum Spanning Tree problem
>Given an [undirected graph](graph.md) $G = (V,E)$ with weights $w: E \rightarrow \mathbb{R}$ can you find a [spanning](spanning_subgraph.md) [tree](tree_(graph).md) $T = (V, E')$ with minimum weight
>$$w(T) = \sum_{e \in E'} w(e).$$

# Solutions
- [Kruskal's algorithm](kruskal's_algorithm.md)
	- It takes $O(\vert E \vert \log(\vert V \vert))$.
- [Prim's algorithm](prim's_algorithm.md)
	- It takes $O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.

# Theory
- [Minimum Spanning Tree problem is in NP](minimum_spanning_tree_problem_is_in_np.md)
-
