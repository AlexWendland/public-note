---
aliases:
  - bagging
  - bootstrapping
  - bootstrap
  - bootstrap aggregation
checked: false
created: 2024-01-24
draft: false
last_edited: 2024-01-24
tags:
  - programming
type: algorithm
---
# Bagging

This is one of the simplest [[Ensemble learning]] methods but out performs classic modelling methods in certain problems.

Suppose we are in the [[Modelling framework|modelling framework]]. The bagging is the following process
1. We choose a set of modelling algorithms $A_i$ for $1 \leq i \leq k$ that could fit the problem - these could all be the same.
2. We take random subsets of the [[Training data|training data]] $T$, $T_i$ for $1 \leq i \leq k$, with replacement - so two samples could contain the same data point.
3. We then train $\hat{f}_i$ using algorithm $A_i$ with [[Training data|training data]] $T_i$ for $1 \leq i \leq k$.
4. Then we have some method of averaging these models over our problem space to produce $\hat{f}$ our final model.

## Example

Suppose we want to use [[Polynomial regression|polynomial regression]] on a simple function $f: \mathbb{R} \rightarrow \mathbb{R}$ with training data $T$.

We could instead of running it once randomly select some $T_i \subset T$ then train $\hat{f}_i$ using [[Polynomial regression|polynomial regression]] on $T_i$.

Then we set our final $\hat{f} = \frac{1}{k} \sum_{i=1}^k \hat{f}_i$.

## Correctness

Bagging tends to lead to less [[Overfitting|overfitting]] so can help algorithms that are particularly prone to this like [[Polynomial regression|polynomial regression]].
