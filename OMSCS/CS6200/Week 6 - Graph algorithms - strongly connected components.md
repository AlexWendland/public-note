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

### Example

Suppose we have the following graph and let $B$ be the root node. Suppose we explore edges alphabetically and lets run the algorithm above on it. 

![[dfs_example.png]]

As we are using [[Depth-first search (DFS)|DFS]] we explore far first and then slowly come back. Which gives us the following [[DFS tree (algorithm)|DFS tree]] with the pre/post numbers.

![[pre_post_calculation_example.png]]

| Letter | Pre | Post |
| ------ | --- | ---- |
| A      | 2   | 11   |
| B      | 1   | 16   |
| C      | 12  | 15   |
| D      | 3   | 10   |
| E      | 4   | 7    |
| F      | 13  | 15   |
| G      | 5   | 6    |
| H      | 8   | 9    |

Lets try and classify the edges $(z,w)$ in this graph

- [[DFS tree (algorithm)|Tree edges]]
	- First explored edges (black) that form a [[Spanning subgraph|spanning]] [[Subgraph|subgraph]].
	- Examples: $B \rightarrow A$, $A \rightarrow D$
	- $post(z) > post(w)$
- [[DFS tree (algorithm)|Back edges]]
	- Edges going from a node further out from the root (in the black edges) to a node closer to it but still in the same branch.
	- Examples $E \rightarrow A$, $F \rightarrow B$
	- $post(z) < post(w)$
- [[DFS tree (algorithm)|Forward edges]]
	- Edges that go further down the tree.
	- Examples: $B \rightarrow E$, $D \rightarrow G$
	- $post(z) > post(w)$
- [[DFS tree (algorithm)|Cross edges]]
	- Edges that go from one branch to another.
	- Examples: $F \rightarrow H$, $H \rightarrow G$
	- $post(z) > post(w)$

Note here there the only type of edges to have $post(z) < post(w)$ are back edges.

![[Cycles in a graph via the DFS tree]]

## Topological sorting

![[Topological sorting (DAG)]]

Suppose we have a [[Directed acyclic graph (DAG)|DAG]] $D$ from [[Cycles in a graph via the DFS tree|the lemma above]] we can run a [[Depth-first search (DFS)|DFS]] algorithm starting at the root of $D$ and the post ordering will provide a [[Topological sorting (DAG)|topological sorting]] of the vertices of $D$.

## Vertices in a [[DAG]]

We can classify special vertices in a [[Directed acyclic graph (DAG)|DAG]]

- Source vertices: These have no incoming edges
- Sink vertices: no outgoing edges

Given a linear ordering we know the minimal vertex is a source and the maximal vertex is a sink. This gives us another algorithm to find a [[Topological sorting (DAG)|topologically sorting]]:

1. Find a sink vertex, label it and then delete it.
2. Repeat (1) until the graph is empty

