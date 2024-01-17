---
aliases:
  - mean squared
  - MSE
checked: false
created: 2024-01-13
last_edited: 2024-01-13
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Mean Squared Error (MSE)
>The *mean squared error* is the square of the $l_2$ norm for two points in $B^k$, i.e.
>$$mse(x,y) = \frac{1}{k}\sum_{i=1}^k (x_i - y_i)^2.$$
>This is normally applied in the context of [[Machine Learning|machine learning]] to assess models against some [[Testing data|testing data]] $T$. In the [[Modelling framework|modelling framework]] we would say the
>$$mse(\hat{f}, T) = \frac{1}{\vert T \vert} \sum_{(a, b) \in T} (\hat{f}(a) - b)^2.$$

