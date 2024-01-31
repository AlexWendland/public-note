---
aliases: 
checked: false
created: 2024-01-31
last_edited: 2024-01-31
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Margin for a linear separator
>Suppose we have a set of [[Linearly separable|linearly separable]] points $X = X_1 \cup X_2 \subset \mathbb{R}^n$ such that $w \in \mathbb{R}^n$ and $b \in \mathbb{R}$ separate them. We define the *margin* of the [[Hyperplane|hyperplane]] $H = (w, b)$ with respect to $X$ to be
>$$\rho = \min_{x \in X} \left \vert \frac{(x - bw) \cdot w}{\vert \vert w \vert \vert} \right \vert = \min_{x \in X} \left \vert \frac{x \cdot w - \vert \vert w \vert \vert^2 b}{\vert \vert w \vert \vert} \right \vert.$$
>In other words this is the smallest distance from a point in $X$ to the hyperplane $H$.


