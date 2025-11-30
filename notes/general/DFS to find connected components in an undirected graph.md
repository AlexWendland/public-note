---
aliases: null
checked: false
created: 2023-09-28
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
---
# DFS to find connected components in an undirected graph

To solve the following problem.
![[Find connected components in a undirected graph#Statement]]

We can use the following [[Depth-first search (DFS)|DFS]] algorithm.

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

As we run through every vertex once and then every edge twice we have $O(\vert V \vert + \vert E \vert)$.
