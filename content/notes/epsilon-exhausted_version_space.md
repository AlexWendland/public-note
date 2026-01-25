---
aliases:
created: 2024-02-16
date_checked:
draft: false
last_edited: 2024-02-16
tags:
  - machine-learning
title: epsilon-exhausted version space
type: definition
---
>[!tldr] epsilon-exhausted version space
>Suppose we are in the [modelling framework](modelling_framework.md) with some [training data](training_data.md) $T \subset A \times B$, a [hypothesis space](modelling_paradigm.md) $H \subset Func(A,B)$ and a [probability distribution](probability_distribution.md) $\mathbb{D}$ on $A$. For some $0 \leq \epsilon \leq 0.5$ the [version space](version_space.md) $VS_H(T)$ is $\epsilon$-exhausted if and only if for all $h \in VS_H(T)$ the [true error](true_error.md)
>$$Error_{\mathbb{D}}(h) \leq \epsilon.$$
