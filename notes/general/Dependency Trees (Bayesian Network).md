---
aliases:
  - dependency tree
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
tags:
  - machine-learning
type: definition
---
>[!tldr] Dependency Trees (Bayesian Network)
>A [[Bayesian network]] $(G, X)$ is a *dependency tree* if $G$ is a directed [[Tree (graph)|tree]]. That is every node has at most one parent. Therefore there is a function $\pi: V \rightarrow V \cup \{\emptyset\}$ which defines every vertices parent or lack of it, which gives
>$$\mathbb{P}[X] = \left ( \prod_{v \in V, \pi(v) = \emptyset} \mathbb{P}[X_v] \right ) \prod_{v \in V, \pi(v) \in V} \mathbb{P}[X_v \vert X_{\pi(v)}].$$
>

