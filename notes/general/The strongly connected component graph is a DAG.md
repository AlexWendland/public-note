---
aliases:
checked: false
created: 2023-09-27
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: definition
---
> [!important] Lemma
> The [[Strongly connected component graph (directed graph)|strongly connected component graph]] is a [[Directed acyclic graph (DAG)|DAG]].

## Proof

Let $G = (V,E)$ be [[Directed graph|directed graph]].

Suppose two strongly connected components $S$ and $T$ in $G$ had paths $p_1$ connecting $s_1 \in S$ to $t_1 \in T$ and $p_2$ connecting $t_2 \in T$ to $s_2 \in S$.

As $S$ and $T$ are strongly connected components we know there are paths $p_{s_i \rightarrow s_j}$, $p_{t_i \rightarrow t_j}$ connecting $s_1$ to $s_2$ and vice versa as well as $t_1$ to $t_2$.

However, $p_1$ connects $s_1$ to $t_1$ and $p_{t_1,t_2} p_2 p_{s_2,s_1}$ connects $t_1$ to $s_1$ giving $T$ is not maximal. Therefore no such set of paths $p_1$ and $p_2$ exist.

Therefore no cycle can exist in the [[Strongly connected component graph (directed graph)|strongly connected component graph]] either.
