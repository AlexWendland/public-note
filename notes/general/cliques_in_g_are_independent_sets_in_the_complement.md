---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
name: Cliques in G are independent sets in the complement
tags:
  - maths
  - graph-theory
type: lemma
---
# Statement

> [!important] Lemma
> For a [undirected graph](graph.md) $G = (V,E)$ and $S \subset V$ we have the following equivalence:
> $S$ is a [clique](clique_(graph).md) in $G$ if and only if $S$ is an [independent set](independent_set_(graph).md) in $G^C$ the [complement graph](complement_graph.md).

# Proof

Suppose $S$ is [clique](clique_(graph).md) in $G$ then $(s,s') \in E$ for all $s, s' \in S$ with $s \not = s'$. As
$$G^C = (V, \overline{E} := \{(u,v) \in V \times V \vert (u,v) \not \in E\})$$
then for all $s, s' \in S$ with $s \not = s'$ we have $(s,s') \not \in \overline{E}$ so $S$ is a [independent set](independent_set_(graph).md) in $G^C$.

Similarly if $S$ is an [independent set](independent_set_(graph).md) in $G^C$ then $(s,s') \not \in E'$ for all $s, s' \in S$ with $s \not = s'$. Therefore by definition $(s,s') \in E$, and we have $S$ is a [clique](clique_(graph).md).
