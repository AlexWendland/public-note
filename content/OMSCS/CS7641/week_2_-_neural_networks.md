---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-01-18
draft: false
last_edited: 2024-01-18
tags:
  - OMSCS
title: Week 2 - Neural networks
type: lecture
week: 2
---

The basis of all neural networks is a simplified model of a neuron in the human body.

[Perceptron (neural network)](../../notes/perceptron_(neural_network).md)

Where we define an [activation function](../../notes/activation_function.md) as.

[Activation function](../../notes/activation_function.md)

First we will just take the function to be [Binary step](../../notes/binary_step.md) which introduces an extra parameter $\theta$.

[Binary step](../../notes/binary_step.md)

# Binary operations with perceptron's

## [Logical and](../../notes/logical_and.md) ($\land$)

Let $n = 2$ and have $x_1, x_2 \in \{0,1\}$ then if we set $w_1 = w_2 = 0.5$ and $\theta = 1$ then $p$ becomes
$$p(x_1, x_2) = \begin{cases} 1 & \mbox{if } x_1 = x_2 = 1\\ 0 & \mbox{otherwise.}\end{cases}$$
## [Logical or](../../notes/logical_or.md) ($\lor$)

Let $n = 2$ and have $x_1, x_2 \in \{0,1\}$ then if we set $w_1 = w_2 = 1$ and $\theta = 1$ then $p$ becomes
$$p(x_1, x_2) = \begin{cases} 1 & \mbox{if } x_1 + x_2 \geq 1\\ 0 & \mbox{otherwise.}\end{cases}$$
## Not

Let $n = 1$ and have $x \in \{0,1\}$ then if we set $w = -1$ and $\theta = 0$ then $p$ becomes

$$p(x) = \begin{cases} 1 & \mbox{if } x = 0\\ 0 & \mbox{otherwise.}\end{cases}$$
## Xor

Define two perceptron's $p_{\land} : \mathbb{R}^2 \rightarrow \{0,1\}$ (from before) and $p : \mathbb{R}^3 \rightarrow \{0,1\}$ with $w_1 = w_2 = 1$, $w_3 = -2$ and $\theta = 0.5$ then
$$p(x) = \begin{cases} 1 & \mbox{if } x \in \{(1,0,0), (0,1,0), (1,1,0)\}\\ 0 & \mbox{otherwise.}\end{cases}$$
Now consider $x_1, x_2 \in \{0,1\}$ and the conjunction
$$p(x_1, x_2, p_{\land}(x_1,x_2)) = \begin{cases} 1 & \mbox{if } (x_1, x_2) \in \{(1,0), (0,1)\} \\ 0 & \mbox{otherwise.} \end{cases}$$
# Perceptron rule

[Perceptron rule](../../notes/perceptron_rule.md)

# Gradient decent

With the [perceptron rule](../../notes/perceptron_rule.md) we applied an activation function that made $p$ [non-differentiable](../../notes/differentiation.md). Lets get rid of this for now and see if we can use [differentiation](../../notes/differentiation.md) to get another training method.

Let our [training data](../../notes/training_data.md) $(x,y) \in T$ have $x = (x_1, x_2, \ldots, x_n) \in \mathbb{R}^n$ and $w = (w_1, w_2, \ldots w_n)$ be our weights for a [perceptron](../../notes/perceptron_(neural_network).md) as before. The define the following [error function](../../notes/error_function_(modelling).md)
$$
E(w) = \frac{1}{2} \sum_{(x,y) \in T} (y - a)^2, \ \ \ \mbox{where} \ \ \ a = \sum_{i=1}^n x_iw_i.
$$
Note $E$ is a function of the weights in this example.

Then we can find a local derivative to decide on the best direction to reduce the weights.

$$
\begin{align*}
\frac{\partial E}{\partial w_i} & = \frac{1}{2} \sum_{(x,y) \in T} -2 (y-a) \frac{\partial a}{\partial w_i}\\
& = - \sum_{(x,y) \in T} (y-a) x_i \end{align*}
$$
This is very similar to the [perceptron rule](../../notes/perceptron_rule.md). Now to completely the training using this we would travel in the opposite of the direction of found by this [derivative](../../notes/differentiation.md). This method is called [Gradient decent](../../notes/gradient_decent.md).

[Gradient decent](../../notes/gradient_decent.md)
# Comparison

Whilst the [perceptron rule](../../notes/perceptron_rule.md) [converges in finite time for linear separable datasets](../../notes/the_perceptron_rule_using_binary_step_converges_in_finite_time_if_the_dataset_is_linearly_separable.md) it is unstable on datasets that are not [linearly separable](../../notes/linearly_separable.md). The advantage of [gradient decent](../../notes/gradient_decent.md) is that it is stable on all datasets but it has the issue of converging only to local minimum.

# Sigmoid function

[Sigmoid function](../../notes/sigmoid_function.md)

Where this function looks similar to the [binary step](../../notes/binary_step.md) function with one big advantage, that it is [differentiable](../../notes/differentiation.md).
$$\frac{d \sigma}{d a} = \sigma(a) (1 - \sigma(a))$$
Which shows the function is relative stable when $\sigma(a)$ is close to either $0$ or $1$ but will have the largest change when it is close to $1/2$.

This allow us to use [gradient decent](../../notes/gradient_decent.md) on a [perceptron](../../notes/perceptron_(neural_network).md) that is using the [Sigmoid function](../../notes/sigmoid_function.md) as its [activation function](../../notes/activation_function.md).

# Neural network

[Neural network](../../notes/neural_network.md)

If we use the [Sigmoid function](../../notes/sigmoid_function.md) for each of the [perceptrons](../../notes/perceptron_(neural_network).md) [activation function](../../notes/activation_function.md) or some other [differentiable](../../notes/differentiation.md) [activation function](../../notes/activation_function.md) - the function this neural network represents is also [differentiable](../../notes/differentiation.md). In this case we can run [gradient decent](../../notes/gradient_decent.md) which in this case is called [Backward propagation of errors (Back propagation)](../../notes/backward_propagation_of_errors_(back_propagation).md).

[Backward propagation of errors (Back propagation)](../../notes/backward_propagation_of_errors_(back_propagation).md)

This will still have the issue with local optimum vs global optimum. Therefore there are some more advanced techniques people use:

- Momentum: Making the learning term very large to skip over local minima,
- Higher order derivatives,
- Random optimization, or
- penalty for complexity.

Complexity in a [neural network](../../notes/neural_network.md) is defined by:

- more nodes,
- more layers, and
- larger numbers as the parameters.

# Bias for [neural networks](../../notes/neural_network.md)

## [Restriction bias](restriction_bias.md)

This is the types of functions [neural networks](../../notes/neural_network.md) can represent.

- Single [perceptron](../../notes/perceptron_(neural_network).md) with [binary step](../../notes/binary_step.md) [activation function](../../notes/activation_function.md): Can only represent half spaces,
- Multi [perceptron](../../notes/perceptron_(neural_network).md) with [binary step](../../notes/binary_step.md) [activation function](../../notes/activation_function.md): Can represent any [Boolean function](../../notes/boolean_function.md).
- Multi [perceptron](../../notes/perceptron_(neural_network).md) with [Sigmoid](../../notes/sigmoid_function.md) [activation function](../../notes/activation_function.md) with one hidden layer: Can represent any [continuous function](../../notes/continuous_function.md).
- Multi [perceptron](../../notes/perceptron_(neural_network).md) with [Sigmoid](../../notes/sigmoid_function.md) [activation function](../../notes/activation_function.md) with two hidden layers: Can represent any function.

Whilst this appears like a multi [perceptron](../../notes/perceptron_(neural_network).md) with [Sigmoid](../../notes/sigmoid_function.md) [activation function](../../notes/activation_function.md) with two hidden layers has no restriction bias - once you have picked your hyper parameters, i.e. the number of layers and nodes, then you have restricted the number of functions you can represent.

>[!warning] Danger of [overfitting](../../notes/overfitting.md)
>It is important to use ideas like [cross validation](../../notes/cross_validation.md) to avoid [overfitting](../../notes/overfitting.md). For [neural networks](../../notes/neural_network.md) it is important to avoid large values also.

## [Preference bias](../../notes/preference_bias.md)

>[!Note] Starting weights
>Normally when you start [back propagation](../../notes/backward_propagation_of_errors_(back_propagation).md) the weights start with small random values. Random values helps us avoid the same local minima each run. Small values has low complexity.

- Training [neural networks](../../notes/neural_network.md) normally have a preference for low complexity networks over high complexity ones.
	- [Occam's razor](../../notes/occam's_razor.md)
- We prefer correct answers to incorrect ones.
