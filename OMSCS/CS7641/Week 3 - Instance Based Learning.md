---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-01-22
last_edited: 2024-01-22
draft: false
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Instance Based Learning

![[Instance-based learning]]

## k-nearest neighbour

![[k-nearest neighbour]]

## Run times

Quite often [[Instance-based learning]] is called "lazy" learning as you are delaying computation until query time. As you can see in this table below which assumes $A = B = \mathbb{R}$. As well as the input training data is sorted.

| Algorithm                  | Running time   | Space |
| -------------------------- | -------------- | ----- |
| 1-NN learning              | 1              | $n$   |
| 1-NN query                 | $n\log(n)$     | 1     |
| $k$-NN learning            | 1              | $n$   |
| $k$-NN query               | $n\log(n) + k$ | 1     |
| Linear regression learning | $n$            | 1     |
| Linear regression learning | 1              | 1     |

> [!Question] Why is linear regression $n$ time to learn?

## The curse of dimensionality

![[The curse of dimensionality]]

## Locally weighted regression

You can use [[k-nearest neighbour]] in [[Regression problems|regression problems]] along with an algorithm like [[Polynomial regression|polynomial regression]] to replace you voting function $V$. This means at each point $a \in A$ you will construct a local polynomial to map that which you can piece together to fit a larger curve.

This has a nice property that whilst your [[Modelling paradigm|modelling paradigm]] of your regression might limit you to certain types of functions - your actual output can be a far more complex function. 

