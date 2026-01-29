---
aliases:
created: 2023-09-27
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: The strongly connected component graph is a DAG
type: definition
---
> [!lemma] Lemma
> The [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md) is a [DAG](directed_acyclic_graph_(dag).md).

## Proof

Let $G = (V,E)$ be a [directed graph](directed_graph.md).

Suppose two strongly connected components $S$ and $T$ in $G$ had paths $p_1$ connecting $s_1 \in S$ to $t_1 \in T$ and $p_2$ connecting $t_2 \in T$ to $s_2 \in S$.

As $S$ and $T$ are strongly connected components, we know there are paths $p_{s_1 \rightarrow s_2}$ and $p_{t_1 \rightarrow t_2}$ connecting $s_1$ to $s_2$ and $t_1$ to $t_2$, respectively.

However, $p_1$ connects $s_1$ to $t_1$ and $p_{t_1 \rightarrow t_2} \circ p_2 \circ p_{s_2 \rightarrow s_1}$ connects $t_1$ to $s_1$, which contradicts the maximality of $T$. Therefore no such set of paths $p_1$ and $p_2$ exist.

Therefore no cycle can exist in the [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md) either.
