---
aliases:
  - modelling framework
created: 2024-01-11
date_checked:
draft: false
last_edited: 2024-01-11
tags:
  - machine-learning
  - statistics
title: Modelling framework
type: definition
---
>[!tldr] Modelling framwork
>Suppose we have some [random variable](random_variable.md) we want to predict $Y$ (over a space $B$) and some set of features or predictors in $A$ to make predictions of $Y$ this are sampled from a [random variable](random_variable.md) $X$. You assume there is some relationship between $Y$ and $X$ given by
>$$Y = f(X) + \epsilon.$$
>Where $\epsilon$ is some [Irreducible error](irreducible_error.md) within our system and $f: A \rightarrow B$.
>
>Then you normally pick a modelling paradigm, like [Linear regression](linear_regression.md), which relates to a subset of functions from $A$ to $B$, $M \subset Func(A,B)$ with an [objective function](objective_function.md) $O$. Then pick the best $\hat{f} \in M$ with respect to the [objective function](objective_function.md) $O$. Therefore you are making the [prediction](prediction.md)
>$$Y \approx \hat{f}(X).$$

# References
- [Introduction to statistical learning with Applications in Python](../references/books/introduction_to_statistical_learning_with_applications_in_python.md)

