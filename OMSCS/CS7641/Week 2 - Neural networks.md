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

Where we define an [[Activation function|activation function]] as.

![[Activation function]]

First we will just take the function to be [[Binary step]] which introduces an extra parameter $\theta$.

![[Binary step]]

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

![[Perceptron rule]]

## Gradient decent

With the [[Perceptron rule|perceptron rule]] we applied an activation function that made $p$ [[Differentiation|non-differentiable]]. Lets get rid of this for now and see if we can use [[Differentiation|differentiation]] to get another training method. 

Let our [[Training data|training data]] $(x,y) \in T$ have $x = (x_1, x_2, \ldots, x_n) \in \mathbb{R}^n$ and $w = (w_1, w_2, \ldots w_n)$ be our weights for a [[Perceptron (neural network)|perceptron]] as before. The define the following [[Error function (modelling)|error function]]
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
This is very similar to the [[Perceptron rule|perceptron rule]]. Now to completely the training using this we would travel in the opposite of the direction of found by this [[Differentiation|derivative]]. This method is called [[Gradient decent]].

![[Gradient decent]]
## Comparison

Whilst the [[Perceptron rule|perceptron rule]] [[The perceptron rule using binary step converges in finite time if the dataset is linearly separable|converges in finite time for linear separable datasets]] it is unstable on datasets that are not [[Linearly separable|linearly separable]]. The advantage of [[Gradient decent|gradient decent]] is that it is stable on all datasets but it has the issue of converging only to local minimum.

## Sigmoid function

![[Sigmoid function]]

Where this function looks similar to the [[Binary step|binary step]] function with one big advantage, that it is [[Differentiation|differentiable]]. 
$$\frac{d \sigma}{d a} = \sigma(a) (1 - \sigma(a))$$
Which shows the function is relative stable when $\sigma(a)$ is close to either $0$ or $1$ but will have the largest change when it is close to $1/2$. 

This allow us to use [[Gradient decent|gradient decent]] on a [[Perceptron (neural network)|perceptron]] that is using the [[Sigmoid function]] as its [[Activation function|activation function]].

## Neural network

![[Neural network]]

If we use the [[Sigmoid function]] for each of the [[Perceptron (neural network)|perceptrons]] [[Activation function|activation function]] or some other [[Differentiation|differentiable]] [[Activation function|activation function]] - the function this neural network represents is also [[Differentiation|differentiable]]. In this case we can run [[Gradient decent|gradient decent]] which in this case is called [[Backward propagation of errors (Back propagation)]].

![[Backward propagation of errors (Back propagation)]]

This will still have the issue with local optimum vs global optimum. Therefore there are some more advanced techniques people use: 

- Momentum: Making the learning term very large to skip over local minima,
- Higher order derivatives,
- Random optimization, or
- penalty for complexity.

Complexity in a [[Neural network|neural network]] is defined by:

- more nodes,
- more layers, and
- larger numbers as the parameters. 

## Bias for [[Neural network|neural networks]]

### [[Restriction bias]]

This is the types of functions [[Neural network|neural networks]] can represent.

- Single [[Perceptron (neural network)|perceptron]] with [[Binary step|binary step]] [[Activation function|activation function]]: Can only represent half spaces,
- Multi [[Perceptron (neural network)|perceptron]] with [[Binary step|binary step]] [[Activation function|activation function]]: Can represent any [[Boolean function]].
- Multi [[Perceptron (neural network)|perceptron]] with [[Sigmoid function|Sigmoid]] [[Activation function|activation function]] with one hidden layer: Can represent any [[Continuous function|continuous function]].
- Multi [[Perceptron (neural network)|perceptron]] with [[Sigmoid function|Sigmoid]] [[Activation function|activation function]] with two hidden layers: Can represent any function.

Whilst this appears like a multi [[Perceptron (neural network)|perceptron]] with [[Sigmoid function|Sigmoid]] [[Activation function|activation function]] with two hidden layers has no restriction bias - once you have picked your hyper parameters, i.e. the number of layers and nodes, then you have restricted the number of functions you can represent. 

>[!warning] Danger of [[Overfitting|overfitting]]
>It is important to use ideas like [[Cross validation|cross validation]] to avoid [[Overfitting|overfitting]]. For [[Neural network|neural networks]] it is important to avoid large values also.

### [[Preference bias]]

>[!Note] Starting weights
>Normally when you start [[Backward propagation of errors (Back propagation)|back propagation]] the weights start with small random values. Random values helps us avoid the same local minima each run. Small values has low complexity.

- Training [[Neural network|neural networks]] normally have a preference for low complexity networks over high complexity ones.
	- [[Occam's razor]]
- We prefer correct answers to incorrect ones.