---
aliases:
created: 2023-09-29
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: DFS for finding strongly connected components
type: algorithm
---

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

This takes $O(\vert V \vert + \vert E \vert)$ as we do two runs of a [DFS](depth-first_search_(dfs).md) algorithm.

# Correctness Proof

Find this in [Week 6 - Graph algorithms - strongly connected components](../OMSCS/CS6215/week_6_-_graph_algorithms_-_strongly_connected_components.md).

## Example

Suppose we want to find the strongly connected components of the graph $G$ below.

![Strongly Connected Component Graph](../../static/images/strongly_connected_component_graph.png)

First we look at $G^R$ and run the [DFS to find path in an undirected graph](dfs_to_find_path_in_an_undirected_graph.md) algorithm.

![Reverse Strongly Connected Compoent Graph](../../static/images/reverse_strongly_connected_compoent_graph.png)

This gives us $post : V \rightarrow \mathbb{N}$ - in this example we started at $C$ and did a fairly random vertex ordering.

![Scc Tree Example](../../static/images/scc_tree_example.png)

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

Notice also that the [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md) is the following.

![Scc Graph Example Reverse Topological Sorting](../../static/images/SCC_graph_example_reverse_topological_sorting.png)

Giving that our ordering is exactly a reverse [topological sorting](topological_sorting_(dag).md).
