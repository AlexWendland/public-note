---
aliases:
  - belief network
  - Belief network
checked: false
created: 2024-02-22
draft: false
last_edited: 2024-02-22
tags:
  - probability
type: definition
---
>[!tldr] Bayesian network
>Let $G = (V,E)$ be a [[Directed acyclic graph (DAG)|directed acyclic graph]] and let $X = (X_v)_{v \in V}$ be a set of [[Random variable|random variables]]. We say $(G,X)$ forms a *Bayesian network* if the [[Probability density function|probability density function]] is given by
>$$\mathbb{P}[X] = \prod_{v \in V} \mathbb{P}[X_v \vert \bigcap_{(u,v) \in E} X_u].$$

