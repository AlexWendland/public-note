---
aliases:
created: 2023-11-03
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - maths
  - graph-theory
title: Vertex cover if and only if the complement is an independent set
type: lemma
---
# Statement

> [!lemma]
> Suppose we have an [undirected graph](graph.md) $G = (V,E)$ with $C \subset V$. Then $C$ is a [vertex cover](vertex_cover.md) if and only if $\overline{C} := V \backslash C$ is an [independent set](independent_set_(graph).md).

# Proof

Suppose $C$ is a vertex cover.

For all $(u,v) \in E$ either $u \in C$ or $v \in C$, therefore no edge in $E$ connects two vertices in $\overline{C}$ making $\overline{C}$ an [independent set](independent_set_(graph).md).

Suppose $\overline{C}$ is an independent set.

Let $(u,v) \in E$, as $\overline{C}$ is an [independent set](independent_set_(graph).md) either $u \in C$ or $v \in C$. Therefore $C$ is a [vertex cover](vertex_cover.md) by definition.
