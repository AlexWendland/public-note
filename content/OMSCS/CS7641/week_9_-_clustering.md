---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-03-09
draft: false
last_edited: 2024-03-09
tags:
  - OMSCS
title: Week 9 - Clustering
type: lecture
week: 9
---
# Unsupervised learning

[Unsupervised learning](../../notes/unsupervised_learning.md)

[Clustering problem](clustering_problem.md)

Two trivial solutions to clustering problems are:
- Set $B = A$ the $f(a) = a$, for all $a \in A$ or
- Set $B = \{1\}$ then $f(a) = 1$ for all $a \in A$.

# Single Linkage Clustering

[Single linkage clustering](../../notes/single_linkage_clustering.md)

# k-means clustering

[k-means clustering](../../notes/k-means_clustering.md)

# Soft clustering

[Expectation Maximisation](../../notes/expectation_maximisation.md)

A concrete example of this comes from using [Normal distribution](../../notes/normal_distribution.md)s for this. Assume our $k$ classes are given by $k$ normal distributions $\mathbb{D}$ where each one has the same standard deviation but a different mean $\mu_j$.

Then we are going to iteratively update
1. the expectation of event $Z_{i,j} = [f(x_i) = j]$ that the $i \in I$ point belongs to the class $j$ given the hypothesis that the clusters use $\mu_j$, and
2. the parameters $\mu_j$ using the distribution of $Z_{i,j}$.

First we will describe step one, given some new means $\mu_j$. We set
$$
\mathbb{E}[z_{i,j}] = \frac{\mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_j]}{\sum_{h=1}^k \mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_h]}
$$
Where the formula for $\mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_j]$ comes from the normal distribution $\mathbb{D}$.

The second step just calculates the best parameters given these probabilities. In this case mean
$$
\mu_j = \frac{\sum_{i \in I} \mathbb{E}[Z_{i,j}]x_i}{\sum_{i \in I} \mathbb{E}[Z_{i,j}]}.
$$
This process is not guaranteed to stop.

# Correctness

- We are monotonically decreasing [Maximum likelihood](../../notes/maximum_likelihood_estimation_(mle).md) error of the groupings.
- Though this is not guaranteed to converge.
- Though it will not diverge either!
- It can get stuck in local optimums.
	- So it is best that we restart this algorithm and take the best outcome.

[Soft clustering](../../notes/soft_clustering.md)
# Clustering properties

There are 3 properties we will want to have from a clustering algorithm.
- [Richness](../../notes/rich_clustering.md): For any assignment of objects to clusters, there is some distance $d$ such that $P_d$ returns that clustering.
- [Scale-invariant clustering](../../notes/scale-invariant_clustering.md): Scaling distances by a positive value does not change the clustering.
- [Consistent clustering](../../notes/consistent_clustering.md): Shrinking intra-cluster distances and expanding inter-cluster distances does not change the clustering.

For example, the [Single linkage clustering](../../notes/single_linkage_clustering.md) as we have defined
- Is not rich, as it can't classify all points as the same.
- Is scale-invariant, as scale preserves the minimum.
- Is consistent, little harder to show but I believe it.

Unfortunately we can't have them all!

[Impossibility Theorem](../../notes/impossibility_theorem.md)

