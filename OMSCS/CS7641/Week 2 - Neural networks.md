---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2024-01-18
last_edited: 2024-01-18
publish: false
tags:
  - OMSCS
type: lecture
week: null
---
# Week 2 - Neural networks

The basis of all neural networks is a simplified model of a neuron in the human body.

![[Perceptron (neural network)]]

## Binary operations with perceptron's

### [[Logical and]] ($\land$)

Let $n = 2$ and have $x_1, x_2 \in \{0,1\}$ then if we set $w_1 = w_2 = 0.5$ and $\theta = 1$ then $p$ becomes
$$p(x_1, x_2) = \begin{cases} 1 & \mbox{if } x_1 = x_2 = 1\\ 0 & \mbox{otherwise.}\end{cases}$$
### [[Logical or]] ($\lor$)

Let $n = 2$ and have $x_1, x_2 \in \{0,1\}$ then if we set $w_1 = w_2 = 1$ and $\theta = 1$ then $p$ becomes
$$p(x_1, x_2) = \begin{cases} 1 & \mbox{if } x_1 + x_2 \geq 1\\ 0 & \mbox{otherwise.}\end{cases}$$
### Not

Let $n = 1$ and have $x \in \{0,1\}$ then if we set $w = -1$ and $\theta = 0$ then $p$ becomes

$$p(x) = \begin{cases} 1 & \mbox{if } x = 0\\ 0 & \mbox{otherwise.}\end{cases}$$
### Xor

Define two perceptron's $p_{\land} : \mathbb{R}^2 \rightarrow \{0,1\}$ (from before) and $p : \mathbb{R}^3 \rightarrow \{0,1\}$ with $w_1 = w_2 = 1$, $w_3 = -2$ and $\theta = 0.5$ then 
$$p(x) = \begin{cases} 1 & \mbox{if } x \in \{(1,0,0), (0,1,0), (1,1,0)\}\\ 0 & \mbox{otherwise.}\end{cases}$$
Now consider $x_1, x_2 \in \{0,1\}$ and the conjunction 
$$p(x_1, x_2, p_{\land}(x_1,x_2)) = \begin{cases} 1 & \mbox{if } (x_1, x_2) \in \{(1,0), (0,1)\} \\ 0 & \mbox{otherwise.} \end{cases}$$
## Perceptron rule

