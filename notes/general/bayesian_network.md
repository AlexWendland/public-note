---
aliases:
  - belief network
  - Belief network
checked: false
created: 2024-02-22
draft: false
last_edited: 2024-02-22
title: Bayesian network
tags:
  - probability
type: definition
---
>[!tldr] Bayesian network
>Let $G = (V,E)$ be a [directed acyclic graph](directed_acyclic_graph_(dag).md) and let $X = (X_v)_{v \in V}$ be a set of [random variables](random_variable.md). We say $(G,X)$ forms a *Bayesian network* if the [probability density function](probability_density_function.md) is given by
>$$\mathbb{P}[X] = \prod_{v \in V} \mathbb{P}[X_v \vert \bigcap_{(u,v) \in E} X_u].$$

