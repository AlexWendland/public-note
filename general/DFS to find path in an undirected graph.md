---
aliases: null
checked: false
created: 2023-09-29
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
---
# [[Depth-first search (DFS)|DFS]] to find path in an undirected graph

For [[Graph|undirected graphs]] we just keep track of the previous vertex and find a [[Spanning subgraph|spanning]] [[Subgraph|sub]]-[[Forest (graph)|forest]] for the [[Graph|graph]]. We can use this to find [[Path (graph)|paths]] between vertices by going back to the root vertices of the [[Tree (graph)|trees]].

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
