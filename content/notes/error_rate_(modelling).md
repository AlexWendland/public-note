---
aliases:
created: 2024-01-24
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Error rate (modelling)
type: definition
---
>[!definition] Error rate (modelling)
>Suppose we are in the [modelling framework](modelling_framework.md) and have [probability distribution](probability_distribution.md) $\mathbb{D}: A \rightarrow [0,1]$ on our [domain](function_domain.md).  We define the *error rate* to be
>$$\mathbb{P}_{\mathbb{B}}[\hat{f}(x) \neq f(x)] = \int_{a \in A} \mathbb{D}(a) \mathbb{I}[\hat{f}(x) \neq f(x)]$$
> Where $\mathbb{I}$ is the [indicator function](indicator_function.md). If $A$ is discrete, this is simply summing the probability of a value $a \in A$ occurring when our model $\hat{f}$ gets it wrong.

