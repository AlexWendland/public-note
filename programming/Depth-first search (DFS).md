---
aliases:
  - DFS
  - depth-first search
  - Depth-first search
type: algorithm
publish: false
created: 2023-09-26
last_edited: 2023-09-26
tags:
  - programming
chatgpt: false
---
# Depth-first search (DFS)

This is a way of traversing a [[Graph|graph]] (could be a [[Directed graph|directed graph]] or [[Graph|undirected graph]]). It explores all the way down one branch of the graph before tracing and exploring other branches.

For [[Graph|undirected graphs]] we use the following [[Pseudocode]] to find the [[Connected components (graph)|connected components]] of a graph. However this is indicative of the strategy as a whole. 

```pseudocode
DFS(G)
  input: G = (V,E) in adjacency list representation
  output: Vertices labelled by connected components
    connected_component = 0
    for all v in V, set visited(v) = False
    for all v in V
      if not visited(v) then
        connected_component++
        explore(v)
    return connected_component_number (defined in explore)
```

```pseudocode
Explore(z)
  input: vertex z
  output: side effect, it defines the connected component_number on some vertices and marks them as visited.
    connected_component_number(z) = connected_component
    visited(z) = True
    for all (z, w) in E
      if not visited(w)
        Explore(w)
```

As we run through every vertex once and then every edge twice we have $O(\vert V \vert \cdot \vert E \vert)$. 