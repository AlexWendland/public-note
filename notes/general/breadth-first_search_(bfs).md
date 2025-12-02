---
aliases:
  - BFS
  - Breadth-first search
  - breadth-first search
checked: false
created: 2023-09-29
draft: false
last_edited: 2023-11-11
title: Breadth-first search (BFS)
tags:
  - programming
type: algorithm
---
# Breadth-first search (BFS)

This is a method for exploring a tree. Lets say you have a vertex $v \in E$ and you either want to run some procedure on vertices or extract some information form them (here we return the parents). Here we use a [queue](queue.md) data structure.

```pseudocode
 BFS(G, root):
	Input: Graph G = (V,E) and root in V
	Output: Shortest paths to the root in a tree.
1. let Q be a queue
2. label root as explored
3. Queue the root node on Q.
4. while Q is not empty
	4.1. v = Q.dequeue()
	4.2. for all edges (v,w) in E
		4.2.1. if w is not labeled as explored:
			4.2.1.1. label w as explored
			4.2.1.2. set v to be the parent of w.
			4.2.1.3. Queue w on Q.
5. return parent array
```

This runs in $O(\vert V \vert + \vert E \vert)$ as we run over each edge once (or twice if undirected) and visit each vertex once.
