---
aliases:
  - linear programme
  - linear programming
  - linear programmes
checked: false
created: 2023-11-07
draft: false
last_edited: 2023-11-11
title: Linear programme
tags:
  - programming
type: definition
---
>[!tldr] Linear programme
>A linear programme has $n$ variables $x_j$ for $1 \leq j \leq n$ where we are trying to either
>$$\max_x \sum_{j=1}^n c_jx_j \mbox{ or } \min_x \sum_{j=1}^n c_jx_j$$
>for some constants $c_j \in \mathbb{R}$ for $1 \leq j \leq n$. This is subject to $m$ [linear](linear_function.md) constrains of the form
>$$\sum_{j=1}^n a_{i,j}x_j \leq b_i, \ \sum_{j=1}^n a_{i,j}x_j \geq b_i \mbox{ or } \sum_{j=1}^n a_{i,j}x_j = b_i$$
>for some constants $a_{i,j}, b_i \in \mathbb{R}$ with $1 \leq i \leq m$ and $1 \leq j \leq n$.

