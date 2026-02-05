---
aliases:
created: 2024-01-31
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Margin for a linear separator
type: definition
---
>[!definition] Margin for a linear separator
>Suppose we have a set of [linearly separable](linearly_separable.md) points $X = X_1 \cup X_2 \subset \mathbb{R}^n$ such that $w \in \mathbb{R}^n$ and $b \in \mathbb{R}$ separate them. We define the *margin* of the [hyperplane](hyperplane.md) $H = (w, b)$ with respect to $X$ to be
>$$\rho = \min_{x \in X} \left \vert \frac{(x - bw) \cdot w}{\vert \vert w \vert \vert} \right \vert = \min_{x \in X} \left \vert \frac{x \cdot w - \vert \vert w \vert \vert^2 b}{\vert \vert w \vert \vert} \right \vert.$$
>In other words this is the smallest distance from a point in $X$ to the hyperplane $H$.


