---
aliases:
  - true error
created: 2024-02-16
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: True error
type: definition
---
>[!definition] True error
>Suppose we are in the [modelling framework](modelling_framework.md) with feature space $A$ with some [probability distribution](probability_distribution.md) $\mathbb{D}$ on it, a [hypothesis space](modelling_paradigm.md) $H$ and the true concept $f: A \rightarrow B$. For some candidate hypothesis $h \in H$, the *true error* is:
>$$Error_{\mathbb{D}}(h) = \mathbb{P}_{\mathbb{D}}[h(a) \neq f(a)] = \int_{a \in A} \mathbb{I}[h(a) \neq f(a)] d \mathbb{D}.$$
>This is the [integral](integration.md) of the [indicator function](indicator_function.md) of whether it is correct or not, weighted with respect to $\mathbb{D}$.
