---
aliases:
  - BFS
  - Breath-first search
  - breath-first search
type: algorithm
publish: true
created: 2023-09-29
last_edited: 2023-09-29
tags:
  - programming
chatgpt: false
---
# Breath-first search (BFS)

This is a method for exploring a tree. Lets say you have a vertex $v \in E$ and you either want to run some procedure on vertices or extract some information form them (here we return the parents). Here we use a [[Queue|queue]] data structure.

```pseudocode
 BFS(G, root):
	Input: Graph G = (V,E) and root in V
	Output: Shortest paths to the root.
	let Q be a queue
	label root as explored
	Q.enqueue(root)
	while Q is not empty
		v = Q.dequeue()
		for all edges from v to w in G.adjacentEdges(v)
			if w is not labeled as explored:
				label w as explored
					w.parent := v
					Q.enqueue(w)
	return parent
```

This runs in $O(\vert V \vert + \vert E \vert)$ as we run over each edge once (or twice if undirected) and visit each vertex once.