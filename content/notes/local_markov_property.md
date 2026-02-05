---
aliases:
created: 2024-02-22
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - probability
title: Local Markov property
type: definition
---
>[!definition] Local Markov property
>Let $G = (V,E)$ be a [directed acyclic graph](directed_acyclic_graph_(dag).md) and $X = \{X_v\}_{v \in V}$ a set of [random variables](random_variable.md). We say $(G,X)$ satisfies the *local Markov property* if for all $v \in V$ and $w \in V$ such that $(w,v) \not \in E$ where there is no [path](path_(graph).md) from $v$ to $w$ then $X_v$ is [conditionally independent](conditional_independence.md) of $X_w$ given $\cup_{(u,v) \in E} X_u$.

