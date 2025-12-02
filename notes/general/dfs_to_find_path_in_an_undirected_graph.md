---
aliases:
checked: false
created: 2023-09-29
draft: false
last_edited: 2023-11-11
title: DFS to find path in an undirected graph
tags:
  - programming
type: algorithm
---
# [DFS](depth-first_search_(dfs).md) to find path in an undirected graph

For [undirected graphs](graph.md) we just keep track of the previous vertex and find a [spanning](spanning_subgraph.md) [sub](subgraph.md)-[forest](forest_(graph).md) for the [graph](graph.md). We can use this to find [paths](path_(graph).md) between vertices by going back to the root vertices of the [trees](tree_(graph).md).

```pseudocode
DFS(G)
  input: G = (V,E) in adjacency list representation
  output: Vertices labelled by connected components
    connected_component = 0
    for all v in V, set visited(v) = False, previous(v) = Null
    for all v in V
      if not visited(v) then
        connected_component++
        explore(v)
    return previous
```

```pseudocode
Explore(z)
  input: vertex z
    connected_component_number(z) = connected_component
    visited(z) = True
    for all (z, w) in E
      if not visited(w)
        previous(w) = z
        Explore(w)
```

# Correctness

# Runtime

$O(\vert V \vert + \vert E \vert)$
