---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-05-30'
date_checked:
draft: false
last_edited: '2026-05-30'
tags:
  - OMSCS
title: Week 2 - Neural Networks
type: lecture
week: 2
---

# Neural Networks

To move beyond the linear classifier from the previous layer we develop a neural network.
A 'neuron' has a single value derived from a linear combination of other neurons that can be modified by a non-linear 'activation function' such as a sigmoid function.
These are normally arranged in 'layers' where between layers there is a complete set of connections.
Each layer will have the same activation function - meaning this can functionally be modeled as $y_{n+1} = A(W y_{n})$.
Here $A$ is the activation function and $W$ is a matrix of weights.
The 'deep' in deep learning refers to the number of layers.
The first layer is the input layer and the last layer is the output layer.
Layers in between are called hidden layers.
We refer to these networks as $n$-layer neural networks - normally we discount the input layer here so a 2 layer neural network will have 1 hidden layer.

Theoretically, a 2 layer neural network can represent any continuous function.
A 3 layer neural network can represent any function at all.
However, in practice we have no bound on the number of neurons needed or how to get the weights to do this!
Practically, you can think of the different layers as learning features or more abstract concepts in the data.
In applications the number of layers can be quite large.

## Activation Functions

TODO: Do this

# Backpropagation

When training a neural network using gradient decent we use the backpropagation algorithm to train the weights.
As we reminder, we know how the following setup:

1. Input data which is pairs $(x, y)$ of inputs with expected outputs.

2. A network $f$ which is a set of layers given by $(M_i, A_i)$ a matrix of weights and an activation function.

3. A loss function $L$ that can evaluate our model $f(x, W)$ with a given set of weights against $y$ the target output.

The goal of gradient decent is to move these weights in the direction that decreases the loss function of these weights in the largest possible amount.
Therefore, we need to calculate $\frac{\partial L}{\partial W}$.

To do this we do the following steps given some weights $W$:

1. On our full/mini-batch do the 'forward' pass to calculate our models evaluation $f(x, W)$.
Using the loss function we can also calculate the loss $L(f(x, W), y)$.

2. Calculate the gradient $\frac{\partial L}{\partial W}$ using the chain rule.

3. Update the weights $W$ using $W = W - \eta \frac{\partial L}{\partial W}$ for some learning rate $\eta$.

The hard step is 2, calculating the gradient but here we know the structure of our model is defined in layers.
Therefore using the chain rule we can break down each calculation into a series of steps.
Suppose we have output $h^l$ and input $h^{l-1}$ in a step with parameters $W_l$ and activation function $A_l$.
Then our recursive algorithm assumes:

1. We are given $\frac{\partial L}{\partial h^{l}}$ from the previous step.

2. We can calculate local gradients $\frac{\partial h^l}{\partial h^{l-1}}$ and $\frac{\partial h^l}{\partial W_l}$.

3. Using step 1 and 2 we can derive

$$
\frac{\partial L}{\partial h^{l-1}} = \frac{\partial L}{\partial h^l} \frac{\partial h^l}{\partial h^{l-1}}
\hspace{1em} \text{and} \hspace{1em}
\frac{\partial L}{\partial W_l} = \frac{\partial L}{\partial h^l} \frac{\partial h^l}{\partial W_l}
$$

for the weights in this layer.

Functionally, step 1 and 3 are easy to do - so the hard step again is step 2, but now we are only looking at a single layers i.e. $h^{l} = A_l(W_l h^{l-1})$.
Therefore calculating $\frac{\partial h^l}{\partial h^{l-1}}$ and $\frac{\partial h^l}{\partial W_l}$ is easy.
This is normally achieved through automatic differentiation - where $A$ is a differentiable function we have pre-computed the derivative for.
With $W_l h^l$ just being a matrix multiplication.

## Example: Back Propagation

A concrete 3-layer network (2 hidden layers + output layer, discounting the input) with 2-dimensional hidden layers.
Biases are omitted for clarity.

**Architecture** — $h^0 \to [W_1, \text{ReLU}] \to h^1 \to [W_2, \sigma] \to h^2 \to [W_3, \text{linear}] \to h^3 = \hat{y}$

**Initial weights:**

$$
W_1 = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}, \quad
W_2 = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}, \quad
W_3 = \begin{bmatrix} 1 & -1 \end{bmatrix}
$$

**Training batch** (2 samples): $\quad L = \tfrac{1}{2}\bigl(L^{(1)} + L^{(2)}\bigr)$

| | Sample 1 | Sample 2 |
|---|---|---|
| Input $x$ | $[1,\ 0]^T$ | $[0,\ 1]^T$ |
| Target $y$ | $1$ | $0$ |

### Forward Pass

Introduce pre-activations $z^l = W_l h^{l-1}$ and post-activations $h^l = A_l(z^l)$, with $h^0 = x$.

**Layer 1 — ReLU:**

$$
z^{1,(1)} = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}
\qquad
h^{1,(1)} = \text{ReLU}(z^{1,(1)}) = \begin{bmatrix} 2 \\ 1 \end{bmatrix}
$$

$$
z^{1,(2)} = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
\qquad
h^{1,(2)} = \text{ReLU}(z^{1,(2)}) = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

For sample 1 both entries are positive and pass through. For sample 2 the first entry is negative — ReLU clamps it to zero, making that neuron **dead** for this sample; no gradient will flow back through it.

**Layer 2 — Sigmoid ($\sigma$):**

$$
z^{2,(1)} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
\qquad
h^{2,(1)} \approx \begin{bmatrix} 0.731 \\ 0.269 \end{bmatrix}
$$

$$
z^{2,(2)} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
\qquad
h^{2,(2)} \approx \begin{bmatrix} 0.269 \\ 0.731 \end{bmatrix}
$$

Note $\sigma(-1) = 1 - \sigma(1) \approx 0.269$ by the antisymmetry of the sigmoid.

**Layer 3 — Linear (identity):**

$$
h^{3,(1)} = \begin{bmatrix} 1 & -1 \end{bmatrix}\begin{bmatrix} 0.731 \\ 0.269 \end{bmatrix} = 0.462
\qquad
L^{(1)} = \tfrac{1}{2}(0.462 - 1)^2 \approx 0.145
$$

$$
h^{3,(2)} = \begin{bmatrix} 1 & -1 \end{bmatrix}\begin{bmatrix} 0.269 \\ 0.731 \end{bmatrix} = -0.462
\qquad
L^{(2)} = \tfrac{1}{2}(-0.462 - 0)^2 \approx 0.107
$$

$$
L = \tfrac{1}{2}(0.145 + 0.107) = 0.126
$$

### Backward Pass

For each layer with pre-activation $z^l = W_l h^{l-1}$ and post-activation $h^l = A_l(z^l)$, three quantities are needed:

$$
\frac{\partial L}{\partial z^l}  = \frac{\partial L}{\partial h^l} \odot \frac{\partial A_l(z^l)}{\partial z^l} = \frac{\partial L}{\partial h^l} \odot A_l'(z^l)
$$
$$
\frac{\partial L}{\partial W_l} = \frac{\partial L}{\partial z^l} \frac{\partial W_l h^{l-1}}{\partial W_l} = \frac{\partial L}{\partial z^l} (h^{l-1})^T
$$
$$
\frac{\partial L}{\partial h^{l-1}} = \frac{\partial L}{\partial z^l} \frac{\partial W_l h^{l-1}}{\partial h^{l-1}} = W_l^T \frac{\partial L}{\partial z^l}
$$

Here $\odot$ denotes element-wise multiplication.
The first equation collapses the activation, the second gives the weight gradient for this layer, and the third passes the gradient upstream.
Run this independently for each sample — we label gradients $\frac{\partial L^{(i)}}{\partial \cdot}$ to keep them separate.

> [!note] Why transpose?
> The Jacobian of $z = Wx$ with respect to $x$ has entry $(i,j)$ equal to
> $\frac{\partial z_i}{\partial x_j} = W_{ij}$, so $J = W$.
> The chain rule for vectors then gives:
> $$
> \frac{\partial L}{\partial x} = J^T \frac{\partial L}{\partial z} = W^T \frac{\partial L}{\partial z}
> $$
> The transpose comes from the chain rule flipping the direction of the map —
> in the forward pass $W$ sends $\mathbb{R}^n \to \mathbb{R}^m$;
> going backwards we need $\mathbb{R}^m \to \mathbb{R}^n$, which is $W^T$.

**Loss gradient at output:**

$$
\frac{\partial L^{(1)}}{\partial h^{3,(1)}} = 0.462 - 1 = -0.538
\qquad
\frac{\partial L^{(2)}}{\partial h^{3,(2)}} = -0.462 - 0 = -0.462
$$

**Layer 3 — Linear ($A_3' = 1$):**

$$
\frac{\partial L^{(1)}}{\partial W_3} = -0.538 \cdot \begin{bmatrix} 0.731 & 0.269 \end{bmatrix} = \begin{bmatrix} -0.393 & -0.145 \end{bmatrix}
$$

$$
\frac{\partial L^{(2)}}{\partial W_3} = -0.462 \cdot \begin{bmatrix} 0.269 & 0.731 \end{bmatrix} = \begin{bmatrix} -0.124 & -0.338 \end{bmatrix}
$$

$$
\frac{\partial L^{(1)}}{\partial h^{2,(1)}} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}(-0.538) = \begin{bmatrix} -0.538 \\ 0.538 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial h^{2,(2)}} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}(-0.462) = \begin{bmatrix} -0.462 \\ 0.462 \end{bmatrix}
$$

**Layer 2 — Sigmoid ($\sigma'(z) = \sigma(z)(1 - \sigma(z))$):**

Both samples have pre-activations $z^{2} = [\pm 1, \mp 1]^T$, so the sigmoid derivative is $[0.197, 0.197]^T$ in both cases (by symmetry):

$$
\frac{\partial L^{(1)}}{\partial z^{2,(1)}} = \begin{bmatrix} -0.538 \\ 0.538 \end{bmatrix} \odot \begin{bmatrix} 0.197 \\ 0.197 \end{bmatrix} = \begin{bmatrix} -0.106 \\ 0.106 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial z^{2,(2)}} = \begin{bmatrix} -0.462 \\ 0.462 \end{bmatrix} \odot \begin{bmatrix} 0.197 \\ 0.197 \end{bmatrix} = \begin{bmatrix} -0.091 \\ 0.091 \end{bmatrix}
$$

$$
\frac{\partial L^{(1)}}{\partial W_2} = \begin{bmatrix} -0.106 \\ 0.106 \end{bmatrix}\begin{bmatrix} 2 & 1 \end{bmatrix} = \begin{bmatrix} -0.212 & -0.106 \\ 0.212 & 0.106 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial W_2} = \begin{bmatrix} -0.091 \\ 0.091 \end{bmatrix}\begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -0.091 \\ 0 & 0.091 \end{bmatrix}
$$

$$
\frac{\partial L^{(1)}}{\partial h^{1,(1)}} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} -0.106 \\ 0.106 \end{bmatrix} = \begin{bmatrix} -0.212 \\ 0.212 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial h^{1,(2)}} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} -0.091 \\ 0.091 \end{bmatrix} = \begin{bmatrix} -0.182 \\ 0.182 \end{bmatrix}
$$

**Layer 1 — ReLU ($A_1'(z) = \mathbf{1}[z > 0]$):**

Sample 1: both $z^{1,(1)}$ entries positive, gradient passes straight through.
Sample 2: first entry of $z^{1,(2)}$ is $-1 < 0$, so $A_1' = [0,\ 1]^T$ — that dead neuron blocks its gradient entirely.

$$
\frac{\partial L^{(1)}}{\partial z^{1,(1)}} = \begin{bmatrix} -0.212 \\ 0.212 \end{bmatrix} \odot \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.212 \\ 0.212 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial z^{1,(2)}} = \begin{bmatrix} -0.182 \\ 0.182 \end{bmatrix} \odot \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0.182 \end{bmatrix}
$$

$$
\frac{\partial L^{(1)}}{\partial W_1} = \begin{bmatrix} -0.212 \\ 0.212 \end{bmatrix}\begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} -0.212 & 0 \\ 0.212 & 0 \end{bmatrix}
\qquad
\frac{\partial L^{(2)}}{\partial W_1} = \begin{bmatrix} 0 \\ 0.182 \end{bmatrix}\begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0.182 \end{bmatrix}
$$

Each sample only updates the weights connected to its non-zero inputs — the two samples cover complementary columns.

### Weight Update

The batch gradient is the average of the two per-sample gradients, $\frac{\partial L}{\partial W_l} = \frac{1}{2}\bigl(\frac{\partial L^{(1)}}{\partial W_l} + \frac{\partial L^{(2)}}{\partial W_l}\bigr)$.
Then apply $W \leftarrow W - \eta \frac{\partial L}{\partial W}$ with $\eta = 0.1$:

$$
\frac{\partial L}{\partial W_3} = \frac{1}{2}\Bigl(\begin{bmatrix} -0.393 & -0.145 \end{bmatrix} + \begin{bmatrix} -0.124 & -0.338 \end{bmatrix}\Bigr) = \begin{bmatrix} -0.259 & -0.242 \end{bmatrix}
$$

$$
W_3 \leftarrow \begin{bmatrix} 1 & -1 \end{bmatrix} - 0.1 \begin{bmatrix} -0.259 & -0.242 \end{bmatrix} = \begin{bmatrix} 1.026 & -0.976 \end{bmatrix}
$$

$$
\frac{\partial L}{\partial W_2} = \frac{1}{2}\left(\begin{bmatrix} -0.212 & -0.106 \\ 0.212 & 0.106 \end{bmatrix} + \begin{bmatrix} 0 & -0.091 \\ 0 & 0.091 \end{bmatrix}\right) = \begin{bmatrix} -0.106 & -0.099 \\ 0.106 & 0.099 \end{bmatrix}
$$

$$
W_2 \leftarrow \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} - 0.1 \begin{bmatrix} -0.106 & -0.099 \\ 0.106 & 0.099 \end{bmatrix} = \begin{bmatrix} 1.011 & -0.990 \\ -1.011 & 0.990 \end{bmatrix}
$$

$$
\frac{\partial L}{\partial W_1} = \frac{1}{2}\left(\begin{bmatrix} -0.212 & 0 \\ 0.212 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 0.182 \end{bmatrix}\right) = \begin{bmatrix} -0.106 & 0 \\ 0.106 & 0.091 \end{bmatrix}
$$

$$
W_1 \leftarrow \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix} - 0.1 \begin{bmatrix} -0.106 & 0 \\ 0.106 & 0.091 \end{bmatrix} = \begin{bmatrix} 2.011 & -1 \\ 0.989 & 0.991 \end{bmatrix}
$$

The second column of $\frac{\partial L}{\partial W_1}$ is now non-zero because sample 2 has $x_2 = 1$ and fills in the signal that sample 1 (with $x_2 = 0$) could not provide.
The batch step is also more conservative than the single-sample update — the two samples pull in somewhat different directions, so the averaged gradient is smaller.

## Computation Graph

Here we specifically applied this to a fully connected neural network.
However, this approach is more general that can apply to [DAGs](../../notes/directed_acyclic_graph_(dag).md) of computation where you put intermediary variables on each edge and sum up incoming edges to get the values for each node.
