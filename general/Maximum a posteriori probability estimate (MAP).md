---
aliases:
  - Maximum a posteriori probability estimate
  - Maximum a posteriori probability
  - MAP
  - maximum a posteriori probability
checked: false
created: 2024-02-20
last_edited: 2024-02-20
publish: true
tags:
  - statistics
  - machine-learning
type: definition
---
>[!tldr] Maximum a posteriori probability estimate (MAP)
>Suppose we have a [[Modelling paradigm|hypothesis space]] $H$ and we want to pick the best hypothesis given some data $D$. Further more suppose we have prior belief about the likelihood of each hypothesis represented by a [[Probability distribution|probability distribution]] over $H$. The *maximum a posteriori probability estimate* is
>$$h_{MAP} = \mbox{arg}\max_{h \in H} \ \mathbb{P}[D \ \vert \ h] \ \mathbb{P}[h].$$

