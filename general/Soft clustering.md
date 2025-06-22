---
aliases: 
checked: false
created: 2024-03-09
last_edited: 2024-03-09
draft: false
tags:
  - programming
  - machine-learning
type: algorithm
---
# Soft clustering

Suppose we are in the [[Clustering problem|clustering problem]] set up. Soft clustering will use [[Expectation Maximisation]] with the [[Normal distribution|Gaussian distribution]]. Here we fix a $\sigma^2$ and then we have
$$
\mathbb{P}[X=x_i \vert \mu = \mu_j] = \exp\left[- \frac{1}{2} \sigma^2 (x_i - \mu_j)^2 \right].
$$
We will use a mean to optimise $\mu_j$ at each step.

## Correctness

- It will have all the downsides of [[Expectation Maximisation]] but we can use restarts to over come them.
