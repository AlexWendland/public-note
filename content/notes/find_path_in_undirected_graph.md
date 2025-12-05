---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Find path in undirected graph
type: problem
---
# Statement

> [!definition] Find [path](path_(graph).md) between vertices in an [undirected graph](graph.md)
> Given an [undirected graph](graph.md) $G = (V,E)$ and two vertices $a,b \in V$. How can we find a [path](path_(graph).md) in $G$ between them. Sometime we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [DFS to find path in an undirected graph](dfs_to_find_path_in_an_undirected_graph.md)
	- This runs in $O(\vert V \vert + \vert E \vert)$.
	- This doesn't use weights.
	- This doesn't get the shortest path.
- [Bellman-Ford algorithm](bellman-ford_algorithm.md)
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$.
	- This works for $\mathbb{R}$ weights finding the shortest path.
	- This find negative cycles.
- [Floyd-Warshall algorithm](floyd-warshall_algorithm.md)
	- This runs in $O(\vert V \vert^3)$.
	- This works for $\mathbb{R}$ weights finding the shortest path.
	- This finds paths between all vertices.
	- This find negative cycles.
- [Dijkstra's algorithm](dijkstra's_algorithm.md)
	- This runs in $O((\vert V \vert + \vert E \vert)\log(\vert V \vert))$ (using the [Min-heap](min-heap.md) data structure).
	- This words for $\mathbb{R}_{>0}$ weights finding the shortest path.
- [BFS](breath-first_search_(bfs).md)
	- This runs in $O(\vert V \vert + \vert E \vert)$.
	- This doesn't use weights.
	- This gets shortest paths from a root vertex.
