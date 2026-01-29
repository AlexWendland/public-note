---
aliases:
created: 2023-11-03
date_checked: 2026-01-29
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
> For an [undirected graph](graph.md) $G = (V,E)$ and $S \subset V$ we have the following equivalence:
> $S$ is a [clique](clique_(graph).md) in $G$ if and only if $S$ is an [independent set](independent_set_(graph).md) in $G^C$ the [complement graph](complement_graph.md).

# Proof

Suppose $S$ is a [clique](clique_(graph).md) in $G$, then $(s,s') \in E$ for all $s, s' \in S$ with $s \neq s'$. By definition of the complement graph,
$$G^C = (V, \overline{E} := \{(u,v) \in V \times V \mid (u,v) \notin E\})$$
then for all $s, s' \in S$ with $s \neq s'$ we have $(s,s') \notin \overline{E}$, so $S$ is an [independent set](independent_set_(graph).md) in $G^C$.

Similarly, if $S$ is an [independent set](independent_set_(graph).md) in $G^C$, then $(s,s') \notin \overline{E}$ for all $s, s' \in S$ with $s \neq s'$. Therefore, by definition of the complement, $(s,s') \in E$, and we have that $S$ is a [clique](clique_(graph).md).
