---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-03-09
last_edited: 2024-03-09
publish: true
tags:
  - OMSCS
type: lecture
week: 9
---
# Week 9 - Clustering

## Unsupervised learning

![[Unsupervised learning]]

![[Clustering problem]]

Two trivial solutions to clustering problems are:
- Set $B = A$ the $f(a) = a$, for all $a \in A$ or
- Set $B = \{1\}$ then $f(a) = 1$ for all $a \in A$.

## Single Linkage Clustering

![[Single linkage clustering]]

## k-means clustering

![[k-means clustering]]

## Soft clustering

![[Soft clustering]]

![[Expectation Maximisation]]

## Clustering properties

There are 3 properties we will want to have from a clustering algorithm.
- [[Rich clustering|Richness]]: For any assignment of objects to clusters, there is some distance $d$ such that $P_d$ returns that clustering.
- [[Scale-invariant clustering]]: Scaling distances by a positive value does not change the clustering.
- [[Consistent clustering]]: Shrinking intra-cluster distances and expanding inter-cluster distances does not change the clustering.

For example, the [[Single linkage clustering]] as we have defined
- Is not rich, as it can't classify all points as the same.
- Is scale-invariant, as scale preserves the minimum.
- Is consistent, little harder to show but I believe it. 

Unfortunately we can't have them all! 

![[Impossibility Theorem]]

