---
aliases:
  - ICA
  - independent component analysis
created: 2024-03-10
date_checked:
draft: false
last_edited: 2024-03-10
tags:
  - probability
  - machine-learning
title: Independent component analysis
type: algorithm
---

Independent component analysis is a form of [linear dimension reduction](linear_dimensionality_reduction.md). The goal of independent component analysis is to form a [linear map](linear_map.md) to features which are [independent](independent_events.md) of one another.

Strictly if you previous features were $X_1, X_2, \ldots, X_n$ and you map to $Y_1, Y_2, \ldots, Y_m$ then we want the following statements about [Mutual information](mutual_information.md):
- $I(Y_i, Y_j) = 0$ for all $i \not = j$, and
- To maximise $I(Y,X)$.

This can be used to solve the [Cocktail party problem](cocktail_party_problem.md).
