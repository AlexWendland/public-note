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
> Suppose we have an [[Graph|undirected graph]] $G = (V,E)$ with $C \subset V$. Then $C$ is a [[Vertex cover|vertex cover]] if and only if $\overline{C} := V \backslash C$ is an [[Independent set (graph)|independent set]]. 

# Proof

Suppose $C$ is a vertex cover.

For all $(u,v) \in E$ either $u \in C$ or $v \in C$, therefore no edge in $E$ connects two vertices in $\overline{C}$ making $\overline{C}$ an [[Independent set (graph)|independent set]].

Suppose $\overline{C}$ is an independent set.

Let $(u,v) \in E$, as $\overline{C}$ is an [[Independent set (graph)|independent set]] either $u \in C$ or $v \in C$. Therefore $C$ is a [[Vertex cover|vertex cover]] by definition.