---
aliases:
checked: false
created: 2024-02-02
draft: false
last_edited: 2024-02-02
name: Gini index
tags:
  - machine-learning
type: definition
---
>[!tldr] Gini index
>Suppose we have a discrete [random variable](random_variable.md) $X$ that can take values in $\{1, 2, \ldots, k\}$. We define the *Gini index* of $X$ to be
>$$Gini(X) = 1 - \sum_{i=1}^k \mathbb{P}(X = i)^2.$$
>The higher the entropy the closer to a uniform the random variable we are. $Gini(X) \in [0,\frac{k-1}{k}]$.

