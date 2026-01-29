---
aliases:
created: 2023-09-28
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Find path in a directed graph
type: problem
---
# Statement

> [!definition] Find [path](path_(graph).md) between vertices in a [directed graph](directed_graph.md)
> Given a [directed graph](directed_graph.md) $G = (V,E)$ and two vertices $a,b \in V$, how can we find a [path](path_(graph).md) in $G$ between them? Sometimes we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [DFS to find path in a directed graph](dfs_to_find_path_in_a_directed_graph.md)
	- Runs in $O(\vert V \vert \cdot \vert E \vert)$
	- Unweighted.
