---
aliases:
  - weak learner
checked: false
created: 2024-01-24
draft: false
last_edited: 2024-01-24
tags:
  - machine-learning
type: definition
---
>[!tldr] Weak learner
>Suppose we are in the [[Modelling framework|modelling framework]] a model $\hat{f}$ is called a *weak learner* if for all probability distributions $\mathbb{D}: A \rightarrow [0,1]$ there exists a suffciently small $\epsilon$ such that
>$$\mathbb{P}_{\mathbb{D}}[\hat{f}(x) \neq f(x)] \leq 0.5 - \epsilon.$$
>That is its [[Error rate (modelling)|error rate]] is just bellow chance.


