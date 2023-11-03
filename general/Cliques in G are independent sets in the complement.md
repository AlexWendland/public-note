---
aliases: 
type: lemma
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - maths
  - graph-theory
chatgpt: false
---
# Statement

> [!important] Lemma
> For a [[Graph|undirected graph]] $G = (V,E)$ and $S \subset V$ we have the following equivalence: 
> $S$ is a [[Clique (graph)|clique]] in $G$ if and only if $S$ is an [[Independent set (graph)|independent set]] in $G^C$ the [[Complement graph|complement graph]].

# Proof

Suppose $S$ is [[Clique (graph)|clique]] in $G$ then $(s,s') \in E$ for all $s, s' \in S$ with $s \not = s'$. As 
$$G^C = (V, \overline{E} := \{(u,v) \in V \times V \vert (u,v) \not \in E\})$$
then for all $s, s' \in S$ with $s \not = s'$ we have $(s,s') \not \in \overline{E}$ so $S$ is a [[Independent set (graph)|independent set]] in $G^C$.

Similarly if $S$ is an [[Independent set (graph)|independent set]] in $G^C$ then $(s,s') \not \in E'$ for all $s, s' \in S$ with $s \not = s'$. Therefore by definition $(s,s') \in E$, and we have $S$ is a [[Clique (graph)|clique]].
