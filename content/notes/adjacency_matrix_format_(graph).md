---
aliases:
  - Adjacency matrix
created: 2023-10-08
date_checked: 2026-04-07
draft: false
last_edited: 2026-04-07
tags:
  - programming
title: Adjacency matrix format (graph)
type: data structure
---

Given a simple undirected graph $G = (V,E)$ we can define the adjacency matrix $M$ of size $\vert V \vert \times \vert V \vert$ as follows:

$$
M_{i,j} = \begin{cases} 1 & \text{if } (i,j) \in E \text{ or } (j,i) \in E\\ 0 & \text{otherwise} \end{cases}
$$

(This can be extended to directed graphs by removing the check for both directions.)
For undirected graphs this is a symmetric matrix.

> [!example] Undirected graph
> Suppose we have the following graph $(\{1,2,3,4\}, \{(1,2), (1,3), (2,4)\})$, then we will get the following adjacency matrix:
> $$
> \begin{bmatrix}
> 0 & 1 & 1 & 0\\
> 1 & 0 & 0 & 1\\
> 1 & 0 & 0 & 0\\
> 0 & 1 & 0 & 0
> \end{bmatrix}
> $$
