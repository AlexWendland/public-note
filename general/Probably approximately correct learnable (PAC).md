---
aliases:
  - PAC learner
  - PAC learnable
checked: false
created: 2024-02-16
last_edited: 2024-02-16
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Probably approximately correct learnable (PAC)
>A [[Concept class|concept class]] $C$ is *probably approximately correct learnable* by learner $L$ using [[Modelling paradigm|hypothesis space]] $H$ with error $0 \leq \epsilon \leq 0.5$ and probability $0 \leq 1 - \delta \leq 1$  if and only if learner $L$ with probability $1-\delta$ outputs hypothesis $h \in H$ such that the [[True error|true error]]
>$$Error_{\mathbb{D}}(h) \leq \epsilon$$
>in time and samples [[Polynomial time|polynomial]] in $\frac{1}{\epsilon}, \frac{1}{\delta}$ and $\vert H \vert$. 

