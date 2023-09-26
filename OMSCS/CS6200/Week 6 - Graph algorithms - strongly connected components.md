---
aliases: 
type: lecture
publish: false
created: 2023-09-26
last_edited: 2023-09-26
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "6"
chatgpt: false
---
# Week 6 - Graph algorithms - strongly connected components

## DFS - not the sofa seller!

Recall the definition of [[Depth-first search (DFS)]] in the note. We used it there to find the [[Connected components (graph)|connected components]] of a graph. We will show another application where we find the paths in a graph.

## Finding paths in an [[Graph|undirected graph]] via [[Depth-first search (DFS)|DFS]]

First for [[Graph|undirected graphs]] we just keep track of the previous vertex and find a [[Spanning subgraph|spanning]] [[Subgraph|sub]]-[[Forest (graph)|forest]] for the [[Graph|graph]]. We can use this to find [[Path (graph)|paths]] between vertices by going back to the root vertices of the [[Tree (graph)|trees]]. 

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

## Finding paths in a [[Directed graph|directed graph]] via [[Depth-first search (DFS)|DFS]]

To do this we are going to use a [[Depth-first search (DFS)|DFS]] algorithm like above but we are going to track pre/postorder numbers. 

```pseudocode
DFS(G)
  input: G = (V,E) in adjacency list representation
  output: Vertices labelled by connected components
    clock = 1
    for all v in V, set visited(v) = False
    for all v in V
      if not visited(v) then
        explore(v)
  return post (defined in Explore)
```

```pseudocode
Explore(z)
  input: vertex z
    pre(z) = clock, clock ++
    visited(z) = True
    for all (z, w) in E
      if not visited(w)
        Explore(w)
	post(z) = clock, clock++
```

