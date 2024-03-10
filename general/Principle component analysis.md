---
aliases:
  - principle component analysis
checked: false
created: 2024-03-10
last_edited: 2024-03-10
publish: true
tags:
  - machine-learning
  - programming
type: algorithm
---
# Principle component analysis

Principle component analysis is a [[Linear dimensionality reduction|linear dimension reduction]] algorithm. In concept principle component analysis find the axis along which the data has maximal [[Variance|variance]] if it were projected. It does this by finding the [[Eigenvector and Eigenvalue|Eigenvector and Eigenvalues]] of the [[Covariance matrix]]. It uses these [[Eigenvector and Eigenvalue|eigenvectors]] as a new basis of the data's feature space.

It performs dimension reduction by only picking the [[Eigenvector and Eigenvalue|eigenvectors]] which have the highest [[Eigenvector and Eigenvalue|eigenvalue]]. 
