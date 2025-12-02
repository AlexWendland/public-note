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
title: Week 10 - Feature selection
type: lecture
week: 10
---

Feature selection is the process of deciding what features of the data are worth training on. Then picking the subset of them that are the most important. The reason to do this is:
- Knowledge discovery, interpretability, and insight.
	- When you get the results back you are going to have to be able to explain them.
- [The curse of dimensionality](../../general/the_curse_of_dimensionality.md)
	- If you put too many dimensions in - it will decrease the accuracy of your models!

# How hard is this problem?

Assume we want to know the best $m \leq n$ subset of columns. The only way to verify it is the best is to check them all so it is $\binom{n}{m}$. If you don't know $m$ then it is $2^n$.

This problem is know to be [NP-hard](../../general/np-hard.md).

# Techniques

There are 2 main families of techniques to solve this problem
- [Filtering](../../general/filtering_(feature_selection).md), a process of deciding which features to keep before passing it to the learning algorithm, and
- [Wrapping](../../general/wrapping_(feature_selection).md), using the learning algorithm to decide which features to keep.

[Filtering](../../general/filtering_(feature_selection).md) has the following pay offs
- It is faster normally as it doesn't need to retrain models,
- It is invariant of the learning problem making it more generic but also receiving no feedback from it, and
- The speed can come from looking at features in isolation that may not provide the full picture.

[Wrapping](../../general/wrapping_(feature_selection).md) has the following pay offs
- It takes into account the models bias and can account for it, and
- It can be very slow depending on the algorithm.

We have already come across methods of doing filtering
- [Information entropy](../../general/information_entropy.md),
- [Decision tree](../../general/decision_tree.md) does feature selection already, and
- [Neural network](../../general/neural_network.md) internally does features selection.

We have already come across some ways to do wrapping too
- [Hill climbing](../../general/hill_climbing.md),
- [Random optimisation](week_7_-_randomized_optimization.md) more generally,
- [Gradient decent](../../general/gradient_decent.md),
- Forward search where we keep adding features until we don't get any better, and
- Backward search where we keep removing features until the score starts to drop.

# Relevance

[Strongly relevant feature](../../general/strongly_relevant_feature.md)

[Weakly relevant feature](../../general/weakly_relevant_feature.md)

[Irrelevant feature](../../general/irrelevant_feature.md)

Whilst relevance is very abstract, you can have irrelevant features that help a particular algorithm. These features are useful.

[Useful feature](../../general/useful_feature.md)
