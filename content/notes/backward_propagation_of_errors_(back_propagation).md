---
aliases:
  - backward propagation of errors
  - back propagation
created: 2024-01-20
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Backward propagation of errors (Back propagation)
type: algorithm
---

This is the specific implementation of [gradient descent](gradient_descent.md) applied to [neural networks](neural_network.md). There are two stages of this calculation:

- Forward pass through the [neural network](neural_network.md) as you evaluate it on [test data](testing_data.md).
- Backward propagation of that error as you use the [chain rule for differentiation](chain_rule_(differentiation).md) on each of the [perceptrons](perceptron_(neural_network).md).

For this to work all the [perceptrons](perceptron_(neural_network).md) need to have differentiable [activation function](activation_function.md).
