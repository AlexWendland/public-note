---
aliases:
  - mean squared
  - MSE
created: 2024-01-13
date_checked:
draft: false
last_edited: 2024-01-13
tags:
  - machine-learning
title: Mean squared error (MSE)
type: definition
---
>[!tldr] Mean Squared Error (MSE)
>The *mean squared error* is the square of the $l_2$ norm for two points in $B^k$, i.e.
>$$mse(x,y) = \frac{1}{k}\sum_{i=1}^k (x_i - y_i)^2.$$
>This is normally applied in the context of [machine learning](machine_learning.md) to assess models against some [testing data](testing_data.md) $T$. In the [modelling framework](modelling_framework.md) we would say the
>$$mse(\hat{f}, T) = \frac{1}{\vert T \vert} \sum_{(a, b) \in T} (\hat{f}(a) - b)^2.$$

