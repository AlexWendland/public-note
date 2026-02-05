---
aliases:
  - dependency tree
created: 2024-02-24
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Dependency Trees (Bayesian Network)
type: definition
---
> [!definition] Dependency Trees (Bayesian Network)
> A [Bayesian network](bayesian_network.md) $(G, X)$ is a *dependency tree* if $G$ is a directed [tree](tree_(graph).md). That is, every node has at most one parent. Therefore, there is a function $\pi: V \rightarrow V \cup \{\emptyset\}$ which defines every vertex's parent or lack thereof, which gives
> $$\mathbb{P}[X] = \left ( \prod_{v \in V, \pi(v) = \emptyset} \mathbb{P}[X_v] \right ) \prod_{v \in V, \pi(v) \in V} \mathbb{P}[X_v \vert X_{\pi(v)}].$$
