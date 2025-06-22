---
aliases:
  - error function
  - Error function
checked: false
created: 2024-01-20
last_edited: 2024-01-20
draft: false
tags:
  - machine-learning
type: definition
---
>[!tldr] Error function (modelling)
>In the [[Modelling framework|modelling framework]] the *error function* determines how good the current model $\hat{f}$ is at fitting the [[Training data|training data]] $T$. This is a function maps from our parameter space to some evaluation space, usually $\mathbb{R}$ - if we let $o$ be the objective function it normally takes the form
>$$E(w) = \sum_{(x,y) \in T} o(f(x), y).$$
>Though this depends on our learning method.    

