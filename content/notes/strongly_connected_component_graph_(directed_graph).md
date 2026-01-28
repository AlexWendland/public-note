---
aliases:
  - strongly connected component graph
created: 2023-09-27
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: Strongly connected component graph (directed graph)
type: definition
---
> [!definition] Strongly connected component graph
> Let $G = (V,E)$ be a [directed graph](directed_graph.md). Suppose $G$ has strongly connected components $S = \{S_1, \ldots, S_n\}$. We can define the *strongly connected component graph* as a directed graph with vertices $S$ and edges
> $$E' = \{(S_i, S_j) \mid s_i \in S_i, s_j \in S_j \text{ with } (s_i, s_j) \in E\}.$$
