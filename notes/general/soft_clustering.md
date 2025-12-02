---
aliases:
checked: false
created: 2024-03-09
draft: false
last_edited: 2024-03-09
tags:
  - programming
  - machine-learning
title: Soft clustering
type: algorithm
---

Suppose we are in the [clustering problem](clustering_problem.md) set up. Soft clustering will use [Expectation Maximisation](expectation_maximisation.md) with the [Gaussian distribution](normal_distribution.md). Here we fix a $\sigma^2$ and then we have
$$
\mathbb{P}[X=x_i \vert \mu = \mu_j] = \exp\left[- \frac{1}{2} \sigma^2 (x_i - \mu_j)^2 \right].
$$
We will use a mean to optimise $\mu_j$ at each step.

# Correctness

- It will have all the downsides of [Expectation Maximisation](expectation_maximisation.md) but we can use restarts to over come them.
