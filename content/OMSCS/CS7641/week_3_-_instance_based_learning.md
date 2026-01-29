---
course_code: CS7641
course_name: Machine Learning
created: 2024-01-22
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - OMSCS
title: Week 3 - Instance Based Learning
type: lecture
week: 3
---

[Instance-based learning](../../notes/instance-based_learning.md)

# K-nearest neighbour

[k-nearest neighbour](../../notes/k-nearest_neighbour.md)

# Run times

[Instance-based learning](../../notes/instance-based_learning.md) is often called "lazy" learning because you delay computation until query time. As you can see in the table below, we assume $A = B = \mathbb{R}$ and that the input training data is sorted.

| Algorithm                  | Running time   | Space |
| -------------------------- | -------------- | ----- |
| 1-NN learning              | 1              | $n$   |
| 1-NN query                 | $n\log(n)$     | 1     |
| $k$-NN learning            | 1              | $n$   |
| $k$-NN query               | $n\log(n) + k$ | 1     |
| Linear regression learning | $n$            | 1     |
| Linear regression query    | 1              | 1     |

> [!question] Why is linear regression $n$ time to learn?

# The curse of dimensionality

[The curse of dimensionality](../../notes/the_curse_of_dimensionality.md)

# Locally weighted regression

You can use [k-nearest neighbour](../../notes/k-nearest_neighbour.md) in [regression problems](../../notes/regression_problems.md) along with an algorithm like [polynomial regression](../../notes/polynomial_regression.md) to replace your voting function $V$. This means at each point $a \in A$ you construct a local polynomial to map that, which you can piece together to fit a larger curve.

This has a nice property that whilst your [modelling paradigm](../../notes/modelling_paradigm.md) of your regression might limit you to certain types of functions - your actual output can be a far more complex function.

