---
aliases:
  - PAC learner
  - PAC learnable
checked: false
created: 2024-02-16
draft: false
last_edited: 2024-02-16
name: Probably approximately correct learnable (PAC)
tags:
  - machine-learning
type: definition
---
>[!tldr] Probably approximately correct learnable (PAC)
>A [concept class](concept_class.md) $C$ is *probably approximately correct learnable* by learner $L$ using [hypothesis space](modelling_paradigm.md) $H$ with error $0 \leq \epsilon \leq 0.5$ and probability $0 \leq 1 - \delta \leq 1$  if and only if learner $L$ when ran on concept $c \in C$ with probability $1-\delta$ outputs hypothesis $h \in H$ such that the [true error](true_error.md)
>$$Error_{\mathbb{D}}(h) \leq \epsilon$$
>in time and samples [polynomial](polynomial_time.md) in $\frac{1}{\epsilon}, \frac{1}{\delta}$ and $\vert H \vert$.

