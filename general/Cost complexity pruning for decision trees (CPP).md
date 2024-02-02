---
aliases:
  - CPP
checked: false
created: 2024-02-02
last_edited: 2024-02-02
publish: true
tags:
  - programming
type: algorithm
---
# Cost complexity pruning for decision trees (CPP)

When making a [[Decision tree|decision tree]] with no pruning it can tend to [[Overfitting|overfit]] the [[Training data|training data]]. To reduce this we can "prune" the decision tree. We do this by looking at how useful each of the branches are - then removing the ones that don't add enough value. This is controlled by a variable $\alpha$ which increases the cost of having more leaf nodes. 

Suppose we are in [[Modelling framework|modelling framework]] where $T$ is our [[Training data|training data]] and let $\hat{f}$ be our decision tree. Assume $R(\hat{f}, T)$ is our function for evaluating how good a fit our tree is (likely this will use [[Information entropy|information entropy]] or the [[Gini index]]). Lastly let $L(\hat{f})$ be the number of leaf nodes in our [[Decision tree|decision tree]] $\hat{f}$. Set
$$
R_{\alpha}(\hat{f}, T) = R(\hat{f}, T) + \alpha L(\hat{f})
$$
to be the value we want to minimise on our sub-trees.

Optimally we would iterate over all potential subtrees of $\hat{f}$ and find the sub-tree that optimises $R_{\alpha}$ on $T$. However, computationally this can be expensive. Therefore it is usual to find a heuristic to choose a branch to prune instead.

One method to do this it to calculate the *effective cost complexity* of a non-terminal node. To define this let the $G = (V,E)$ be our decision tree and for $v \in V$ let $G_v$ be the subtree rooted at $v$. 

## Pseudocode

## Run time

Optimally we would iterate over all potential subtrees of $\hat{f}$ and find the sub-tree that optimises $R_{\alpha}$ on $T$. However, computationally this can be expensive. 

## Correctness

This can reduce overfitting, however the parameter $\alpha$ needs to be fine tuned. It is best to use [[Cross validation|cross validation]] for this purpose. 