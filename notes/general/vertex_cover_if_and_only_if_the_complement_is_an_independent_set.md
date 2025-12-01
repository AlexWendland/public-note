---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
name: Vertex cover if and only if the complement is an independent set
tags:
  - maths
  - graph-theory
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have an [undirected graph](graph.md) $G = (V,E)$ with $C \subset V$. Then $C$ is a [vertex cover](vertex_cover.md) if and only if $\overline{C} := V \backslash C$ is an [independent set](independent_set_(graph).md).

# Proof

Suppose $C$ is a vertex cover.

For all $(u,v) \in E$ either $u \in C$ or $v \in C$, therefore no edge in $E$ connects two vertices in $\overline{C}$ making $\overline{C}$ an [independent set](independent_set_(graph).md).

Suppose $\overline{C}$ is an independent set.

Let $(u,v) \in E$, as $\overline{C}$ is an [independent set](independent_set_(graph).md) either $u \in C$ or $v \in C$. Therefore $C$ is a [vertex cover](vertex_cover.md) by definition.
