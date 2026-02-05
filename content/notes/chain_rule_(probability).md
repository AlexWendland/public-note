---
aliases:
  - chain rule
created: 2024-02-22
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - probability
title: Chain rule (probability)
type: definition
---
[!definition] Chain rule (probability)
For [random variables](random_variable.md) $A_k$ for $k \in \{1, 2, \ldots, n\}$ we have
$$\mathbb{P}[A_1, A_2, \ldots, A_n] = \prod_{k=1}^n \mathbb{P}[A_k \vert A_1, A_2, \ldots, A_{k-1}].$$
This follows from the definition of [conditional probability](conditional_probability.md).
