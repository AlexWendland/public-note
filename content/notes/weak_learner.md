---
aliases:
  - weak learner
created: 2024-01-24
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Weak learner
type: definition
---
>[!definition] Weak learner
>Suppose we are in the [modelling framework](modelling_framework.md) a model $\hat{f}$ is called a *weak learner* if for all probability distributions $\mathbb{D}: A \rightarrow [0,1]$ there exists a sufficiently small $\epsilon$ such that
>$$\mathbb{P}_{\mathbb{D}}[\hat{f}(x) \neq f(x)] \leq 0.5 - \epsilon.$$
>That is the [error rate](error_rate_(modelling).md) is just below chance.


