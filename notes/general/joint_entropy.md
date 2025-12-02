---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
title: Joint Entropy
tags:
  - machine-learning
type: definition
---
>[!tldr] Joint Entropy
>Suppose we have two [random variables](random_variable.md) $X$ and $Y$ over different [domains](function_domain.md) $A$ and $B$. The *joint entropy* is defined by
>$$H(X, Y) = - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a, Y = b] \log_2(\mathbb{P}[X = a, Y = b]).$$
>This is [Information entropy](information_entropy.md) of the [joint distribution](joint_distribution.md).

