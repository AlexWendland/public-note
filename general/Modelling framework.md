---
aliases:
  - modelling framework
checked: false
created: 2024-01-11
last_edited: 2024-01-11
draft: false
tags:
  - machine-learning
  - statistics
type: definition
---
>[!tldr] Modelling framwork
>Suppose we have some [[Random variable|random variable]] we want to predict $Y$ (over a space $B$) and some set of features or predictors in $A$ to make predictions of $Y$ this are sampled from a [[Random variable|random variable]] $X$. You assume there is some relationship between $Y$ and $X$ given by
>$$Y = f(X) + \epsilon.$$
>Where $\epsilon$ is some [[Irreducible error]] within our system and $f: A \rightarrow B$.
>
>Then you normally pick a modelling paradigm, like [[Linear regression]], which relates to a subset of functions from $A$ to $B$, $M \subset Func(A,B)$ with an [[Objective function|objective function]] $O$. Then pick the best $\hat{f} \in M$ with respect to the [[Objective function|objective function]] $O$. Therefore you are making the [[Prediction|prediction]]
>$$Y \approx \hat{f}(X).$$

# References
- [[Introduction to statistical learning with Applications in Python]]

