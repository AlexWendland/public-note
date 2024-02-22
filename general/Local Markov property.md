---
aliases: 
checked: false
created: 2024-02-22
last_edited: 2024-02-22
publish: true
tags:
  - probability
type: definition
---
>[!tldr] Local Markov property
>Let $G = (V,E)$ be a [[Directed acyclic graph (DAG)|directed acyclic graph]] and $X = \{X_v\}_{v \in V}$ a set of [[Random variable|random variables]]. We say $(G,X)$ satisfies the *local Markov property* if for all $v \in V$ if for all $w \in V$ such that $(w,v) \not \in E$ and there is no [[Path (graph)|path]] from $v$ to $w$ then $X_v$ is [[Conditional independence|conditionally independent]] of $X_w$ given $\cup_{(u,v) \in E} X_u$.

