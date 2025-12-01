---
aliases:
checked: false
created: 2023-09-29
draft: false
last_edited: 2023-11-11
name: Find strongly connected components for an undirected graph
tags:
  - programming
type: problem
---
## Statement

> [!tldr] Find [strongly connected components](strongly_connected_components_(directed_graphs).md) in an [directed graph](directed_graph.md)
> Given a [directed graph](directed_graph.md) $G = (V,E)$ how can we find a mapping from it's vertices $V$ to the [strongly connected components](strongly_connected_components_(directed_graphs).md) of $G$.

## Solutions

- [DFS for finding strongly connected components](dfs_for_finding_strongly_connected_components.md)
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$ time.
	- It also outputs the strongly connected components in a reverse [topologically sort](topological_sorting_(dag).md).
