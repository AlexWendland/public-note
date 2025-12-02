---
aliases:
  - gradient decent
checked: false
created: 2024-01-20
draft: false
last_edited: 2024-01-20
title: Gradient decent
tags:
  - programming
  - machine-learning
type: algorithm
---
# Gradient decent

This algorithm uses [differentiation](differentiation.md) to minimise error terms for models. Suppose we have a model with some parameters $w \in \mathbb{R}^k$. Further suppose the [error function](error_function_(modelling).md) $E(w)$ is [differentiable](differentiation.md) with respect to $w$. Then we set some learning rate $\eta$ and we perturb the weights $w$ by $w \leftarrow w - \eta \frac{\partial E}{\partial w}$ until $w$ settles in some local minimum.

Note the convergence to a local minimum - rather than a global minimum. There are techniques to get around this but it is a hard problem to know you are in some global minimum.

## Run time

Run time can be effected by the complexity of the model. Also there are different techniques to change the learning rate $\eta$ over time.


