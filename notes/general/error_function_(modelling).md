---
aliases:
  - error function
  - Error function
checked: false
created: 2024-01-20
draft: false
last_edited: 2024-01-20
title: Error function (modelling)
tags:
  - machine-learning
type: definition
---
>[!tldr] Error function (modelling)
>In the [modelling framework](modelling_framework.md) the *error function* determines how good the current model $\hat{f}$ is at fitting the [training data](training_data.md) $T$. This is a function maps from our parameter space to some evaluation space, usually $\mathbb{R}$ - if we let $o$ be the objective function it normally takes the form
>$$E(w) = \sum_{(x,y) \in T} o(f(x), y).$$
>Though this depends on our learning method.

