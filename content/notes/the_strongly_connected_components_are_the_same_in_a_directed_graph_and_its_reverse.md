---
aliases:
created: 2023-09-28
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: The strongly connected components are the same in a directed graph and its
  reverse
type: lemma
---
> [!lemma] Lemma
> Let $G = (V,E)$ be a [directed graph](directed_graph.md) and $G^R = (V,E^R)$ be its [reverse](reverse_directed_graph.md). Both $G$ and $G^R$ have the same strongly connected components.

## Proof

For any two vertices $x,y \in V$ who are [strongly connected](strongly_connected_(directed_graphs).md) in $G$ we need a path $p_{x,y}$ connecting $x$ to $y$ and path $p_{y,x}$ connecting $y$ to $x$.

The reverse of the path $p_{x,y}^R$ connected $y$ to $x$ in $G^R$ and $p_{y,x}^R$ connects $x$ to $y$ in $G^R$.

Therefore if two vertices are [strongly connected](strongly_connected_(directed_graphs).md) in $G$ they are strongly connected in $G^R$.

As $G = \left (G^R \right )^R$ this also gives us that if two vertices are [strongly connected](strongly_connected_(directed_graphs).md) in $G^R$ they are strongly connected in $G$.

Thus by the definition of [strongly connected components](strongly_connected_components_(directed_graphs).md) they must be identical in $G$ and $G^R$.
