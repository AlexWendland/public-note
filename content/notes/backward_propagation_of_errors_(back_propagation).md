---
aliases:
  - backward propagation of errors
  - back propagation
checked: false
created: 2024-01-20
draft: false
last_edited: 2024-01-20
tags:
  - programming
title: Backward propagation of errors (Back propagation)
type: algorithm
---

This is the specific implementation of [gradient decent](gradient_decent.md) applied to [neural networks](neural_network.md). There are two stages of this calculation:

- Forward pass through as you evaluate the [neural network](neural_network.md) on [test data](testing_data.md).
- Backward propagation of that error as you use the [chain rule for differentiation](chain_rule_(differentiation).md) on each of the [perceptrons](perceptron_(neural_network).md).

For this to work all the [perceptrons](perceptron_(neural_network).md) need to have differentiable [activation function](activation_function.md).
