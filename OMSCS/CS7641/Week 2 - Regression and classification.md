---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-01-17
last_edited: 2024-01-17
publish: true
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - Regression and classification

# Regression history

![[Regression problems]]

The name comes from [[Regression to the mean|regression to the mean]], this was the technique they used to first talk about it - then the word regression for the technique stuck.

# Linear Regression

Suppose we are in the [[Modelling framework|modelling framework]] then [[Linear regression|linear regression]] is the process of matching a straight line to a set of $(x,y) \in A \times B$ for some continuous $A$ and $B$. Suppose a point in $x = (x_1, \ldots, x_n) \in A$ then we choose the [[Modelling paradigm|modelling paradigm]] of function to be a linear sum of the inputs with a base value:
$$
f(x) = c_0 + \sum_{i=1} c_i x_i
$$
with $c_i$ being constants in an appropriate field. 

Once we have an [[Objective function|objective function]] we can use training data to fit the parameters $c_i$.

## Linear regression using [[Mean squared error (MSE)|MSE]]

![[Mean squared error (MSE)|MSE]]

Suppose $B = \mathbb{R}$ lets use [[Differentiation|differentiation]] to derive the values for $c_i$. 