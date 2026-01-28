---
aliases:
created: 2023-09-29
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
title: Find strongly connected components for a directed graph
type: problem
---
## Statement

> [!definition] Find [strongly connected components](strongly_connected_components_(directed_graphs).md) in a [directed graph](directed_graph.md)
> Given a [directed graph](directed_graph.md) $G = (V,E)$ how can we find a mapping from its vertices $V$ to the [strongly connected components](strongly_connected_components_(directed_graphs).md) of $G$.

## Solutions

- [DFS for finding strongly connected components](dfs_for_finding_strongly_connected_components.md)
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$ time.
	- It also outputs the strongly connected components in reverse [topological sort](topological_sorting_(dag).md).
