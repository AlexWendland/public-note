---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-05-29'
date_checked: '2026-05-30'
draft: false
last_edited: '2026-05-29'
tags:
  - OMSCS
title: Week 1 - Linear Classifiers and Gradient Descent
type: lecture
week: 1
---

The following quote defines machine learning:

> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

In short, the program's capacity to do the task increases as it experiences more of it.
This is in contradiction to traditional programs as hard-coded algorithms do not improve the more they run on the issues.

There are three main areas of machine learning:

- Supervised Learning: Given labeled data how to find a function that learns an underlying function that explains this data.

- Unsupervised Learning: Given data, learns a feature that is not provided.

- Reinforcement Learning: Given a task, learns a policy that maximizes the reward.

In this course we will mainly be focusing on *Supervised Learning* but deep learning can be used on all of them.

Similarly, we can have parametric or non-parametric models.
The first explicitly relies on and optimises some parameters, and the second does not.
Deep learning and this course focus on parametric models.

In general, our input will be a vector which can be constructed in multiple ways and the output will also be a vector - quite likely a probability distribution over a number of states but we can also model other things.
Therefore, the function we are trying to map is $f_W : \mathbb{R}^n \to \mathbb{R}^m$ where $W \in \mathbb{R}^k$ are some parameters.

# Parametric learning algorithm

A parametric learning algorithm has multiple components:

1. Input/Output or representation of the data.

2. Function form of the model, how we are planning on learning our function - including the set of parameters to optimise.

3. A performance measure of how the model is doing.

4. An optimisation algorithm for tuning parameters.

## 1 & 2 Simple starting point

An example of this is a linear classifier. In the scalar case it operates on functions $f: \mathbb{R} \rightarrow \mathbb{R}$ of the form $f(x, W, b) = Wx + b$ where $W \in \mathbb{R}$ is the weight and $b \in \mathbb{R}$ is the bias.
Here we can tune both $W$ and $b$ to minimise an error such as least squares.
This can also be expanded to multiple dimensions, e.g. $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ by using a matrix $W \in \mathbb{R}^{m \times n}$ (rows = output dimensions, columns = input dimensions) and a vector $b \in \mathbb{R}^m$.

(This in fact can be simplified so $b$ is contained in $W$ by letting $W \in \mathbb{R}^{m \times (n+1)}$ by extending it with $b$ as an extra column and adding a 1 to the input vector.
This allows us to get rid of $b$ from the equation and let the linear model be a simple matrix multiplication.)

This linear classifier is actually incredibly powerful as it is - and a lot of basic models use this once we have done some feature selection on the input vector.
However, it can only make decisions on a linear boundary - if you need split classes along a different boundary you will need a different model.

### Aside: Classifier

The linear classifier above outputs us a vector of 'scores' these are any values in $\mathbb{R}$.
For classifier tasks where each entry in the $\mathbb{R}^n$ refers to a different class we would rather a probability distribution over the classes.
In this case we use the 'softmax' function.
This is a non-linear function $softmax: \mathbb{R}^n \rightarrow \mathbb{R}^n$ given by:

$$
softmax(x) = (\frac{e^{x_1}}{\sum_j e^{x_j}}, \ldots, \frac{e^{x_k}}{\sum_j e^{x_j}}, \ldots, \frac{e^{x_n}}{\sum_j e^{x_j}}) = (\mathbb{P}[Y = 1 \vert X = x], \ldots \mathbb{P}[Y=k \vert X = x], \ldots \mathbb{P}[Y=n \vert X = x])
$$

This gives us a probability distribution as the exponential function is positive and we normalise the classes.

## 3 Performance measures

To now improve the model over the training data we will calculate how well it did on the training data.
This uses some kind of loss function $L: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}$.
This loss function $L(f(x, W), y)$ measures how far the models prediction $f(x, W)$ was from $y$ using parameters $W$.
Then for a batch of data $(x_i, y_i)$ the loss of the model will be the average of this data e.g. $\frac{1}{N} \sum_i L(f(x_i, W), y_i)$.

An example of such a loss function in the classification case is a "Hinge Loss" function.
Suppose we have a score $f(x_i, W)$ which is supposed to predict a class $y_i$.
Then we want to punish the model for each class which has a score higher or close to the score it has for the target class.
To do this we define the loss function:

$$
L_{y_i}(s) = \sum_{j \neq y_i} \max(0, s_j - s_{y_i} + 1).
$$

For classes $j$ that have score $s_j < s_{y_i} - 1$, then it contributes nothing to the loss.
However, for classes that are larger than $s_{y_i} - 1$ we punish the model for that.
The $-1$ is to allow the model to 'clearly' differentiate $s_{y_i}$ from other classes.

The Hinge Loss function works on scores - if instead we used the softmax function and ran it on the probabilities we would need a different Loss function.
In this case the natural, maximum-likelihood-derived loss function is 'cross-entropy', which is:

$$
L_{y_i} = - \log(\mathbb{P}[Y = y_i \vert X = x_i])
$$

### Regularisation

As well as punishing the model for being less accurate we also punish it for being too complex.
For example, having single parameters that are very large or very small.
So we may define loss to include a norm of the parameters to penalise 'over-fitting' — L1 regularisation uses the sum of absolute values $\sum_j |w_j|$, while L2 (weight decay, more common in deep learning) uses the sum of squares $\sum_j w_j^2$.

## 4 Optimisation

The optimisation part of the algorithm really is just looking over all parameters $W$ and picking the best $W$ to minimise the loss function.
There are multiple ways to do this:

- Random search: Just keep picking random parameters and hope you eventually find a good one.

- Genetic algorithms: Keep a pool of potential parameters and keep mixing/mutating them to find better loss values.

- Gradient-based optimisation: Use a form of hill-climbing to take the current parameters and move them in a way to improve the loss.

### Gradient descent

In this course we will be using gradient descent.
This is a simple strategy where you start at a point - work out the steepest way to decrease the loss function and move in that direction.
We will then iterate on this until we hit a local minimum.
This may not be the global minimum but normally it works out quite well.
This follows the below algorithm:

1. Choose a model $f(x,W) = Wx$ (using the bias-absorbed form from above, so $W \in \mathbb{R}^{m \times (n+1)}$).

2. Choose a loss function: $L_i = \vert y - W x_i \vert^2$.

3. Calculate the partial derivatives with respect to each parameter $\frac{\partial L}{\partial w_j}$.

4. Update the parameters $w_j = w_j - \alpha \frac{\partial L}{\partial w_j}$.
(Where $\alpha$ is a learning rate we can vary as the time goes on.)

For gradient descent we keep going between steps 3/4 to update the parameters.
We can do this using either:

- Full batch gradient descent: Here we use the loss function averaged over all the training data.

- Mini-batch gradient descent: Here we use the loss function averaged over a small subset of the training data which changes each step.

The mini-batching makes learning faster when used over large amounts of data.
Gradient descent theoretically does converge; however, this uses some assumptions on the learning rate which are not computable for real-world examples.

In step 3 we calculate the partial derivatives.
There are multiple ways to do this:

- Manual differentiation: Do it by hand.

- Symbolic differentiation: Computational way to do it which provides an exact symbolic solution.

- Numerical differentiation: Numerically compute the gradient by recalculating the function.

- Automatic differentiation: Break down complicated differentiation into simple smaller steps and apply the chain rule.

Functionally only the last is feasible for machine learning.
The first requires too much human intervention, the second experiences expression swell and can be computationally too intensive, and the third at a large scale is too numerically intensive.

Automatic differentiation decomposes any computation into primitive operations with known derivatives and applies the chain rule across the resulting computation graph.
In deep learning, this maps naturally onto the layer structure — each layer is a primitive step — which is why this technique (applied to neural networks specifically) is called backpropagation.

# How deep learning is different

There are three main ways deep learning is different from other forms of machine learning:

- *Hierarchical*: Deep learning involves multiple layers of models these provide multiple different representations of the data.

- *End-to-end learning*: Whilst traditional machine learning involves human alteration of the data through feature extraction and pruning deep learning combines this all into one model.
This means that the model itself is responsible for selecting what data is useful.

- *Distributed representation*: No one bit of the deep learning model is singularly responsible for one part of the output - instead this representation is broken out over the whole model.
This leads to models not being human interpretable.



