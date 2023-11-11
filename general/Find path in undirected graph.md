---
aliases: null
checked: false
created: 2023-09-28
last_edited: 2023-09-28
publish: true
tags:
  - programming
type: problem
---
# Statement

> [!tldr] Find [[Path (graph)|path]] between vertices in an [[Graph|undirected graph]]
> Given an [[Graph|undirected graph]] $G = (V,E)$ and two vertices $a,b \in V$. How can we find a [[Path (graph)|path]] in $G$ between them. Sometime we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [[DFS to find path in an undirected graph]]
	- This runs in $O(\vert V \vert + \vert E \vert)$.
	- This doesn't use weights.
	- This doesn't get the shortest path.
- [[Bellman-Ford algorithm]]
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$.
	- This works for $\mathbb{R}$ weights finding the shortest path.
	- This find negative cycles.
- [[Floyd-Warshall algorithm]]
	- This runs in $O(\vert V \vert^3)$.
	- This works for $\mathbb{R}$ weights finding the shortest path.
	- This finds paths between all vertices.
	- This find negative cycles.
- [[Dijkstra's algorithm]]
	- This runs in $O((\vert V \vert + \vert E \vert)\log(\vert V \vert))$ (using the [[Min-heap]] data structure).
	- This words for $\mathbb{R}_{>0}$ weights finding the shortest path.
- [[Breath-first search (BFS)|BFS]]
	- This runs in $O(\vert V \vert + \vert E \vert)$.
	- This doesn't use weights.
	- This gets shortest paths from a root vertex.
