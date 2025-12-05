---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-01-22
draft: false
last_edited: 2025-12-05
tags:
  - OMSCS
title: Week 3 - Instance Based Learning
type: lecture
week: 3
---

[Instance-based learning](../../general/instance-based_learning.md)

# k-nearest neighbour

[k-nearest neighbour](../../general/k-nearest_neighbour.md)

# Run times

Quite often [Instance-based learning](../../general/instance-based_learning.md) is called "lazy" learning as you are delaying computation until query time. As you can see in this table below which assumes $A = B = \mathbb{R}$. As well as the input training data is sorted.

| Algorithm                  | Running time   | Space |
| -------------------------- | -------------- | ----- |
| 1-NN learning              | 1              | $n$   |
| 1-NN query                 | $n\log(n)$     | 1     |
| $k$-NN learning            | 1              | $n$   |
| $k$-NN query               | $n\log(n) + k$ | 1     |
| Linear regression learning | $n$            | 1     |
| Linear regression learning | 1              | 1     |

> [!question] Why is linear regression $n$ time to learn?

# The curse of dimensionality

[The curse of dimensionality](../../general/the_curse_of_dimensionality.md)

# Locally weighted regression

You can use [k-nearest neighbour](../../general/k-nearest_neighbour.md) in [regression problems](../../general/regression_problems.md) along with an algorithm like [polynomial regression](../../general/polynomial_regression.md) to replace you voting function $V$. This means at each point $a \in A$ you will construct a local polynomial to map that which you can piece together to fit a larger curve.

This has a nice property that whilst your [modelling paradigm](../../general/modelling_paradigm.md) of your regression might limit you to certain types of functions - your actual output can be a far more complex function.

