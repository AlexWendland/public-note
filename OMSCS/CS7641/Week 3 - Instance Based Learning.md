---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-01-22
last_edited: 2024-01-22
publish: true
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

| Algorithm                  | Running time  | Space |
| -------------------------- | ------------- | ----- |
| 1-NN learning              | 1             | $n$   |
| 1-NN query                 | $\log(n)$     | 1     |
| $k$-NN learning            | 1             | $n$   |
| $k$-NN query               | $\log(n) + k$ | 1     |
| Linear regression learning | $n$           | 1     |
| Linear regression learning                           | 1              | 1      |

> [!Question] Why is linear regression $n$ time to learn?

## The curse of dimensionality

![[The curse of dimensionality]]

## Locally weighted regression

