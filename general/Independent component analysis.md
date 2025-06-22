---
aliases:
  - ICA
  - independent component analysis
checked: false
created: 2024-03-10
last_edited: 2024-03-10
draft: false
tags:
  - probability
  - machine-learning
type: algorithm
---
# Independent component analysis

Independent component analysis is a form of [[Linear dimensionality reduction|linear dimension reduction]]. The goal of independent component analysis is to form a [[Linear map|linear map]] to features which are [[Independent events|independent]] of one another.

Strictly if you previous features were $X_1, X_2, \ldots, X_n$ and you map to $Y_1, Y_2, \ldots, Y_m$ then we want the following statements about [[Mutual information]]:
- $I(Y_i, Y_j) = 0$ for all $i \not = j$, and
- To maximise $I(Y,X)$.

This can be used to solve the [[Cocktail party problem]].