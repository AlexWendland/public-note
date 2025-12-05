---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Find path in a directed graph
type: problem
---
# Statement

> [!definition] Find [path](path_(graph).md) between vertices in an [directed graph](directed_graph.md)
> Given an [directed graph](directed_graph.md) $G = (V,E)$ and two vertices $a,b \in V$. How can we find a [path](path_(graph).md) in $G$ between them. Sometime we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [DFS to find path in a directed graph](dfs_to_find_path_in_a_directed_graph.md)
	- Runs in $O(\vert V \vert \cdot \vert E \vert)$
	- Unweighted.
