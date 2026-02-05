---
aliases:
  - Maximum a posteriori probability estimate
  - Maximum a posteriori probability
  - MAP
  - maximum a posteriori probability
created: 2024-02-20
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - statistics
  - machine-learning
title: Maximum a posteriori probability estimate (MAP)
type: definition
---
>[!definition] Maximum a posteriori probability estimate (MAP)
>Suppose we have a [hypothesis space](modelling_paradigm.md) $H$ and we want to pick the best hypothesis given some data $D$. Further more suppose we have prior belief about the likelihood of each hypothesis represented by a [probability distribution](probability_distribution.md) over $H$. The *maximum a posteriori probability estimate* is
>$$h_{MAP} = \mbox{arg}\max_{h \in H} \ \mathbb{P}[D \ \vert \ h] \ \mathbb{P}[h].$$

