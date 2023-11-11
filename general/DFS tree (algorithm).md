---
aliases:
  - Back edge
  - Cross edge
  - DFS tree
  - Forward edge
  - Tree edge
checked: false
created: 2023-09-27
last_edited: 2023-09-27
publish: true
tags:
  - maths
type: definition
---
> [!tldr] DFS tree
> Given the run a [[Depth-first search (DFS)|DFS]] algorithm $A$ on a [[Directed graph|directed graph]] $G = (V,E)$, the *DFS tree* is a [[Subgraph|sub]]-[[Forest (graph)|forest]] $F = (V,E')$ where $E'$ are the edges used by $A$ to first explore a vertex.

Edges in $G$ can be described in relation to the edges in $T$.

>[!tldr] Edges
>An edge $e \in E$ can be described as one of the following in relation to $F$:
>- Tree edges: edges $e \in E'$
>- Back edges: edges that connect two nodes in the same branch where the origin node is further away from the root node than the terminus.
>- Forward edges: edges that connect two nodes in the same branch where the origin node is closer to the root node than the terminus.
>- Cross edges: edges that connect two branches.

