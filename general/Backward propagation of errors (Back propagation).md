---
aliases:
  - backward propagation of errors
  - back propagation
checked: false
created: 2024-01-20
last_edited: 2024-01-20
draft: false
tags:
  - programming
type: algorithm
---
# Backward propagation of errors (Back propagation)

This is the specific implementation of [[Gradient decent|gradient decent]] applied to [[Neural network|neural networks]]. There are two stages of this calculation:

- Forward pass through as you evaluate the [[Neural network|neural network]] on [[Testing data|test data]].
- Backward propagation of that error as you use the [[Chain rule (differentiation)|chain rule for differentiation]] on each of the [[Perceptron (neural network)|perceptrons]]. 

For this to work all the [[Perceptron (neural network)|perceptrons]] need to have differentiable [[Activation function|activation function]].