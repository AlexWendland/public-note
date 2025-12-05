---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-09-26
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 6 - Graph algorithms - strongly connected components
type: lecture
week: '6'
---
# DFS - not the sofa seller!

Recall the definition of [Depth-first search (DFS)](../../notes/depth-first_search_(dfs).md) in the note. We used it there to find the [connected components](../../notes/connected_components_(graph).md) of a graph.

[DFS to find connected components in an undirected graph](../../notes/dfs_to_find_connected_components_in_an_undirected_graph.md)

# [Find paths in undirected graph](../../notes/find_path_in_undirected_graph.md) via [DFS](../../notes/depth-first_search_(dfs).md)

First for [undirected graphs](../../notes/graph.md) we just keep track of the previous vertex and find a [spanning](../../notes/spanning_subgraph.md) [sub](../../notes/subgraph.md)-[forest](../../notes/forest_(graph).md) for the [graph](../../notes/graph.md). We can use this to find [paths](../../notes/path_(graph).md) between vertices by going back to the root vertices of the [trees](../../notes/tree_(graph).md).

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

# [Find paths in undirected graph](../../notes/find_path_in_undirected_graph.md) via [DFS](../../notes/depth-first_search_(dfs).md)

To do this we are going to use a [DFS](../../notes/depth-first_search_(dfs).md) algorithm like above but we are going to track pre/postorder numbers.

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

## Example

Suppose we have the following graph and let $B$ be the root node. Suppose we explore edges alphabetically and lets run the algorithm above on it.

![Dfs Example](../../../static/images/dfs_example.png)

As we are using [DFS](../../notes/depth-first_search_(dfs).md) we explore far first and then slowly come back. Which gives us the following [DFS tree](../../notes/dfs_tree_(algorithm).md) with the pre/post numbers.

![Pre Post Calculation Example](../../../static/images/pre_post_calculation_example.png)

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

- [Tree edges](../../notes/dfs_tree_(algorithm).md)
	- First explored edges (black) that form a [spanning](../../notes/spanning_subgraph.md) [subgraph](../../notes/subgraph.md).
	- Examples: $B \rightarrow A$, $A \rightarrow D$
	- $post(z) > post(w)$
- [Back edges](../../notes/dfs_tree_(algorithm).md)
	- Edges going from a node further out from the root (in the black edges) to a node closer to it but still in the same branch.
	- Examples $E \rightarrow A$, $F \rightarrow B$
	- $post(z) < post(w)$
- [Forward edges](../../notes/dfs_tree_(algorithm).md)
	- Edges that go further down the tree.
	- Examples: $B \rightarrow E$, $D \rightarrow G$
	- $post(z) > post(w)$
- [Cross edges](../../notes/dfs_tree_(algorithm).md)
	- Edges that go from one branch to another.
	- Examples: $F \rightarrow H$, $H \rightarrow G$
	- $post(z) > post(w)$

Note here there the only type of edges to have $post(z) < post(w)$ are back edges.

[Cycles in a graph via the DFS tree](../../notes/cycles_in_a_graph_via_the_dfs_tree.md)

# Topological sorting

[Topological sorting (DAG)](../../notes/topological_sorting_(dag).md)

Suppose we have a [DAG](../../notes/directed_acyclic_graph_(dag).md) $D$ from [the lemma above](../../notes/cycles_in_a_graph_via_the_dfs_tree.md) we can run a [DFS](../../notes/depth-first_search_(dfs).md) algorithm starting at the root of $D$ and the post ordering will provide a [topological sorting](../../notes/topological_sorting_(dag).md) of the vertices of $D$.

# Vertices in a [DAG](dag.md)

We can classify special vertices in a [DAG](../../notes/directed_acyclic_graph_(dag).md)

- Source vertices: These have no incoming edges
- Sink vertices: no outgoing edges

Given a linear ordering we know the minimal vertex is a source and the maximal vertex is a sink. This gives us another algorithm to find a [topologically sorting](../../notes/topological_sorting_(dag).md):

1. Find a sink vertex, label it and then delete it.
2. Repeat (1) until the graph is empty

# Strongly connected components

Recall the definitions

[strongly connected](../../notes/strongly_connected_(directed_graphs).md)

[strongly connected components](../../notes/strongly_connected_components_(directed_graphs).md)

Then we can define the [strongly connected component graph](../../notes/strongly_connected_component_graph_(directed_graph).md)

[strongly connected component graph](../../notes/strongly_connected_component_graph_(directed_graph).md)

Which we can show is a [DAG](dag.md).

[The strongly connected component graph is a DAG](../../notes/the_strongly_connected_component_graph_is_a_dag.md)

# Strongly connected component algorithm

The idea of the algorithm is the following:

- Find a sink [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md),
- Remove it,
- Repeat!

We use sinks as if we start a [DFS](../../notes/depth-first_search_(dfs).md) algorithm in a sink [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md) we only discover vertices in that [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md).

This is not true for source [strongly connected components](../../notes/strongly_connected_components_(directed_graphs).md), here we discover everything.

# Finding a vertex in a sink SCC

We have the following two statements in a [DAG](../../notes/directed_acyclic_graph_(dag).md):
- The vertex with the lowest postorder number is a sink.
- Then vertex with the highest postorder number is a source.

We would hope for the analogous statements in a general [directed graph](../../notes/directed_graph.md):
- The vertex with the lowest post order number is in a sink [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md)
- The vertex with the highest post order number is in a source [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md)

The first statement is false consider the following counter example.

![sink_counter_example](../../../static/images/excalidraw/sink_counter_example.excalidraw.svg)

If we run a [DFS](../../notes/depth-first_search_(dfs).md) algorithm starting at $A$ using an alphabetical ordering on the vertices then $B$ has the lowest post order number but is in the source [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md).

[A vertex with the highest post order number lies in a source SCC](../../notes/a_vertex_with_the_highest_post_order_number_lies_in_a_source_scc.md)

Suppose we a directed graph $G$ define the [reverse directed graph](../../notes/reverse_directed_graph.md) $G^R$. Now observe

[The strongly connected components are the same in a directed graph and its reverse](../../notes/the_strongly_connected_components_are_the_same_in_a_directed_graph_and_its_reverse.md)

Moverover we have.

[Taking the reverse respects going to the strongly connected component graph](../../notes/taking_the_reverse_respects_going_to_the_strongly_connected_component_graph.md)

Therefore if we can find a source vertex in $S_{G^R}$ then we have found a sink vertex in $S_G$. This is exactly what our algorithm will depend on.

# Algorithm for finding the strongly connected components

```pseudocode
SCC(G):
	Input: directed graph G = (V,E) in adjacency list
	Output: labeling of V by strongly connected component
		1. Construct G^R
		2. Run DFS on G^R
		3. Order V by decreasing post order number.
		4. Run directed DFS on G using the vertex ordering from before and
		   label the connected components we reach.
```

>[!note] Additional property
>In addition to labelling the connected components the order we have labelled them is in reverse topological ordering. This is because we always start at the next sink vertex after we have labelled a component.

This takes $O(\vert V \vert + \vert E \vert)$ as we do two runs of a [DFS](../../notes/depth-first_search_(dfs).md) algorithm.

## Example

Suppose we want to find the strongly connected components of the graph $G$ below.

![Strongly Connected Component Graph](../../../static/images/strongly_connected_component_graph.png)

First we look at $G^R$ and run the [DFS to find path in an undirected graph](../../notes/dfs_to_find_path_in_an_undirected_graph.md) algorithm.

![Reverse Strongly Connected Compoent Graph](../../../static/images/reverse_strongly_connected_compoent_graph.png)

This gives us $post : V \rightarrow \mathbb{N}$ - in this example we started at $C$ and did a fairly random vertex ordering.

![Scc Tree Example](../../../static/images/scc_tree_example.png)

| Letter | Pre | Post |
| ------ | --- | ---- |
| A      | 7   | 8    |
| B      | 6   | 11   |
| C      | 1   | 12   |
| D      | 12  | 13   |
| E      | 9   | 10   |
| F      | 3   | 4    |
| G      | 2   | 5    |
| H      | 17  | 18   |
| I      | 19  | 20   |
| J      | 16  | 21   |
| K      | 15  | 22   |
| L      | 14  | 23     |

Then we order the vertices by reverse post order.

| Letter | L   | K   | J   | I   | H   | D   | C   | B   | E   | A   | G   | F   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Post   | 23  | 22  | 21  | 20  | 18  | 13  | 12  | 11  | 10  | 8   | 5   | 4   |

Now run a connected components [DFS](dfs.md) using the vertex ordering above.

| Letter | L   | K   | J   | I   | H   | D   | C   | B   | E   | A   | G   | F   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Post   | 23  | 22  | 21  | 20  | 18  | 13  | 12  | 11  | 10  | 8   | 5   | 4   |
| CC     | 1   | 1   | 1   | 1   | 1   | 2   | 3   | 4   | 4   | 5   | 3   | 3    |

Notice also that the [strongly connected component graph](../../notes/strongly_connected_component_graph_(directed_graph).md) is the following.

![Scc Graph Example Reverse Topological Sorting](../../../static/images/SCC_graph_example_reverse_topological_sorting.png)

Giving that our ordering is exactly a reverse [topological sorting](../../notes/topological_sorting_(dag).md).
