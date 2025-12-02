---
aliases:
  - Back edge
  - Cross edge
  - DFS tree
  - Forward edge
  - Tree edge
checked: false
created: 2023-09-27
draft: false
last_edited: 2023-11-11
title: DFS tree (algorithm)
tags:
  - maths
type: definition
---
> [!tldr] DFS tree
> Given the run a [DFS](depth-first_search_(dfs).md) algorithm $A$ on a [directed graph](directed_graph.md) $G = (V,E)$, the *DFS tree* is a [sub](subgraph.md)-[forest](forest_(graph).md) $F = (V,E')$ where $E'$ are the edges used by $A$ to first explore a vertex.

Edges in $G$ can be described in relation to the edges in $T$.

>[!tldr] Edges
>An edge $e \in E$ can be described as one of the following in relation to $F$:
>- Tree edges: edges $e \in E'$
>- Back edges: edges that connect two nodes in the same branch where the origin node is further away from the root node than the terminus.
>- Forward edges: edges that connect two nodes in the same branch where the origin node is closer to the root node than the terminus.
>- Cross edges: edges that connect two branches.

