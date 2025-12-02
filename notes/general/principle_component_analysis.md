---
aliases:
  - principle component analysis
  - PCA
checked: false
created: 2024-03-10
draft: false
last_edited: 2024-03-10
tags:
  - machine-learning
  - programming
title: Principle component analysis
type: algorithm
---

Principle component analysis is a [linear dimension reduction](linear_dimensionality_reduction.md) algorithm. In concept principle component analysis find the axis along which the data has maximal [variance](variance.md) if it were projected. It does this by finding the [Eigenvector and Eigenvalues](eigenvector_and_eigenvalue.md) of the [Covariance matrix](covariance_matrix.md). It uses these [eigenvectors](eigenvector_and_eigenvalue.md) as a new basis of the data's feature space.

It performs dimension reduction by only picking the [eigenvectors](eigenvector_and_eigenvalue.md) which have the highest [eigenvalue](eigenvector_and_eigenvalue.md).
