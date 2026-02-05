---
aliases:
  - conditional entropy
created: 2024-02-24
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - probability
title: Conditional entropy
type: definition
---
>[!definition] Conditional entropy
>Suppose we have two [random variables](random_variable.md) $X$ and $Y$ over different [domains](function_domain.md) $A$ and $B$. The *conditional entropy* is defined by
>$$H(Y \vert X) = - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a, Y = b] \log_2(\mathbb{P}[Y = b \vert X = a]).$$

