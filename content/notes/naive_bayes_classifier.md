---
aliases:
created: 2024-02-24
date_checked:
draft: false
last_edited: 2024-02-24
tags:
  - programming
  - machine-learning
title: Naive Bayes classifier
type: algorithm
---

Suppose we have a [classification problem](classification_problems.md) and we are in the [modelling framework](modelling_framework.md). We are given features $A = \oplus_{i=1}^n A_i$ where each feature $A_i$ has finite values (also split up the [random variable](random_variable.md) $X$ into $X = \oplus_{i=1}^n X_i$ for our input). Let our classification also have finite [domain](function_domain.md) $B$.

We can use our [testing data](testing_data.md) to estimate $\mathbb{P}[Y=b]$ for each $b \in B$ and $\mathbb{P}[X_i = a_i \vert Y = b]$ for each $a_i \in A_i$ and $b \in B$.

>[!warning] Assumption
>Making the assumption that $Y$ and each of the $X_i$ form a [Bayesian network](bayesian_network.md) where $Y$ is the root with one arrow to each of the $X_i$ with the probabilities above.

Using [Bayes rule](bayes_rule.md) then [marginalisation](marginalisation_(probability).md) and [chain rule](chain_rule_(probability).md) we can calculate
$$
\mathbb{P}[Y = b \vert X = (a_1, a_2, \ldots, a_n)] = \frac{\mathbb{P}[Y=b] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b]}{Z}
$$
with the normalisation term $Z = \sum_{b' \in B} \mathbb{P}[Y=b'] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b']$. Then to compute the [Maximum a posteriori probability](maximum_a_posteriori_probability_estimate_(map).md) we don't need to compute $Z$ and we let
$$
f_{MAP}(a_1, a_2, \ldots, a_n) = \mbox{arg}\max_{b \in B} \mathbb{P}[Y=b] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b].
$$
This exactly forms our Naive Bayes classifier for this problem.

# Run time

It is [eager learner](eager_learner.md) so requires you to sample the data initially. Though we only ever need to see each data point once - so is fairly fast. The estimating of the parameters is fairly simple. This model also has the minimum number of parameters you need to factor in most

# Correctness

Whilst this does may a large assumption about the different attributes. Empirically this is considered very successful. It is thought that Google use this a lot in gmail for actual spam!

# Limitations

- It makes a strong assumption that the attributes are not related to one another, which seems ridiculous.
	- It is very venerable to co-dependent variables as its influence will grow exponentially the more variables are related. (i.e. if 3 variables were the same we would cube that term.)
	- Though in practice it turns out not to matter that much!
- If any of the $\mathbb{P}[A_i = a_i \vert Y = b]$ is zero, it zeros out the entire product.
	- We should account for this by always making these values non-zero. This is called "smoothing" of the probabilities.
	- We need a very large amount of data to guarantee our probabilities are accurate.
