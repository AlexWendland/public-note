---
aliases: 
checked: false
created: 2024-02-16
last_edited: 2024-02-16
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] True error
>Suppose we are in the [[Modelling framework|modelling framework]] with feature space $A$ with some [[Probability distribution|probability distribution]] $\mathbb{D}$ on it, a [[Modelling paradigm|hypothesis space]] $H$ and the true concept $f: A \rightarrow B$. For some candidate hypothesis $h \in H$ the *true error*
>$$Error_{\mathbb{D}}(h) = \mathbb{P}_{\mathbb{D}}[h(a) = f(a)] = \int_{a \in A} \mathbb{I}[h(a) = f(a)]it is  d \mathbb{D}.$$
>This is the [[Integration|integral]] of the [[Indicator function|indicator function]] on whether it is correct or not weighted with respect to $\mathbb{D}$.

