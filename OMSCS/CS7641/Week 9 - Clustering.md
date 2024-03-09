---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
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
- Richness: For any assignment of objects to clusters, there is some distance $d$ such that $P_d$ returns that clustering.
- Scale-invariance: Scaling distances by a positive value does not change the clustering.
- Consistency: Shrinking intra-cluster distances and expanding intercluster distances does not change the clustering.

