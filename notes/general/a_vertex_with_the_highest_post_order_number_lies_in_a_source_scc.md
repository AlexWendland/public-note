---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2023-11-11
title: A vertex with the highest post order number lies in a source SCC
tags:
  - maths
type: lemma
---
> [!important] Lemma
> Suppose we have a [directed graph](directed_graph.md) $G = (V,E)$ and $post: V \rightarrow \mathbb{N}$ be the result of running the [DFS to find connected components in an undirected graph](dfs_to_find_connected_components_in_an_undirected_graph.md) algorithm. Then the vertex with the largest post order number lies in a source [strongly connected component](strongly_connected_components_(directed_graphs).md) in the [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md).

## Proof

Let $S$ be the [strongly connected component](strongly_connected_components_(directed_graphs).md) with the vertex of highest $post$ value.

Suppose some other [strongly connected component](strongly_connected_components_(directed_graphs).md) $S'$ were to have an edge connecting to $S$ in the [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md).

From the [Lemma](how_post_order_relates_to_strongly_connected_components.md) $S'$ has a vertex with higher post order than all vertices in $S$. This is a contradiction as $S$ contains the vertex with highest post order.


