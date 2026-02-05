---
aliases:
  - rooted tree
created: 2024-01-10
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - graph-theory
  - maths
title: Rooted tree
type: definition
---
>[!definition] Rooted tree
>A *rooted tree* is a [tree](tree_(graph).md) $(V, E)$ with a *root* vertex $r \in V$. This is sometimes represented as $(T = (V,E), r)$.
>In a rooted tree
>- $r \in V$ is not considered a [leaf vertex](leaf_(graph).md),
>- we can assign all vertices $v \in V$ a distance from the root $r$ by the path distance $dist(r,v)$ or the (unique) path length between $r$ and $v$. This is sometimes called its level $l(v) := dist(r,v)$,
>- the vertices $V = P \cup L$ into parents and [leaf vertices](leaf_(graph).md) respectively, and
>- we let $Child(p) = \{(c,p) \in E \vert dist(r,p) < dist(r,c)\} \subset V$ be the set of children of $p \in P$.

