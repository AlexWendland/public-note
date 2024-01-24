---
aliases: 
checked: false
created: 2024-01-24
last_edited: 2024-01-24
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Error rate (modelling)
>Suppose we are in the [[Modelling framework|modelling framework]] and have [[Probability distribution|probability distribution]] $\mathbb{D}: A \rightarrow [0,1]$ on our [[Function domain|domain]]. The we define the *error rate* to be
>$$\mathbb{P}_{\mathbb{B}}[\hat{f}(x) \neq f(x)] = \int_{a \in A} \mathbb{D}(a) \mathbb{I}[\hat{f}(x) \neq f(x)]$$
> Where $\mathbb{I}$ is the [[Indicator function|indicator function]]. If $A$ is discrete is simply adding the probability of a value $a \in A$ occurring if our model $\hat{f}$ got it right. 

