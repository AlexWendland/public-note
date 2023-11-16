---
aliases: null
checked: false
created: 2023-09-17
last_edited: 2023-11-11
publish: true
tags:
  - lecture
type: study-group
---
# Introduction to Statistical Learning in Python

Book: statlearning
Github: https://github.com/bomtall/islp

>[!todo] Set up environment
> Sort out python

## Difference between Prediction and Inference

Given a setting where $Y = f(X) + \epsilon$ then there.

[[Prediction]] - Is building a blackbox $\hat{f}$  such that $\hat{f}(x)$ is close to $f(x)$ on a subdomain $\hat{X} \subset X$. For notation we have $\hat{Y} = \hat{f}(X)$.

[[Inference]] - This is the process of understanding the true form of $f$.

## Accuracy

Reducible error - The difference between $\hat{f}(x) - f(x)$.

Irreducible error - The $\epsilon$ coming from measurement, innate randomness, ....

## Why is irreducible error larger than zero?

$$\mathbb{E}[(Y - \hat{Y})^2] = E(f(X) + \epsilon - \hat{f}(X)^2) = [f(X) - \hat{f}(X)] + Var(\epsilon)$$
With the following assumptions.

- $Y = f(X) + \epsilon$
- $\hat{Y} = \hat{f}(X)$
- $\mathbb{E}(\hat{Y} - Y)$
- $\mathbb{E}[\epsilon] = 0$

Definition of mean squared error here:

$$MSE(y, \hat{f}(x)) = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{f}(x_i))^2.$$
## What is bias?

How good can your model be given it is of a certain form.


-
