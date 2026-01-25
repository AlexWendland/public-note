---
aliases:
created: 2023-11-03
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
  - graph-theory
title: Cliques in G are independent sets in the complement
type: lemma
---
# Statement

> [!lemma] Lemma
> For a [undirected graph](graph.md) $G = (V,E)$ and $S \subset V$ we have the following equivalence:
> $S$ is a [clique](clique_(graph).md) in $G$ if and only if $S$ is an [independent set](independent_set_(graph).md) in $G^C$ the [complement graph](complement_graph.md).

# Proof

Suppose $S$ is [clique](clique_(graph).md) in $G$ then $(s,s') \in E$ for all $s, s' \in S$ with $s \not = s'$. As
$$G^C = (V, \overline{E} := \{(u,v) \in V \times V \vert (u,v) \not \in E\})$$
then for all $s, s' \in S$ with $s \not = s'$ we have $(s,s') \not \in \overline{E}$ so $S$ is a [independent set](independent_set_(graph).md) in $G^C$.

Similarly if $S$ is an [independent set](independent_set_(graph).md) in $G^C$ then $(s,s') \not \in E'$ for all $s, s' \in S$ with $s \not = s'$. Therefore by definition $(s,s') \in E$, and we have $S$ is a [clique](clique_(graph).md).
