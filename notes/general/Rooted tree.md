---
aliases:
  - rooted tree
checked: false
created: 2024-01-10
draft: false
last_edited: 2024-01-10
tags:
  - graph-theory
  - maths
type: definition
---
>[!tldr] Rooted tree
>A *rooted tree* is a [[Tree (graph)|tree]] $(V, E)$ with a *root* vertex $r \in V$. This is sometimes represented as $(T = (V,E), r)$.
>In a rooted tree
>- $r \in V$ is not considered a [[Leaf (graph)|leaf vertex]],
>- we can assign all vertices $v \in V$ a distance from the root $r$ by the path distance $dist(r,v)$ or the (unique) path length between $r$ and $v$. This is sometimes called its level $l(v) := dist(r,v)$,
>- the vertices $V = P \cup L$ into parents and [[Leaf (graph)|leaf vertices]] respectively, and
>- we let $Child(p) = \{(c,p) \in E \vert dist(r,p) < dist(r,c)\} \subset V$ be the set of children of $p \in P$.

