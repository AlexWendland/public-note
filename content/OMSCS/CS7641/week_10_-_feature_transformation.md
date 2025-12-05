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
title: Week 10 - Feature transformation
type: lecture
week: 10
---

[Feature transformation](../../notes/dimensionality_reduction.md) is the problem of pre-processing a set of features to create a new (smaller/compact) feature set, while retaining as much information as possible. It is a map $p: \mathbb{F}^N \rightarrow \mathbb{F}^M$ where you usually want $M < N$.

In this course we will focus on [linear  feature reduction](../../notes/linear_dimensionality_reduction.md) where $p$ is a [linear map](../../notes/linear_map.md).

>[!note]
>Feature selection is a special case of feature transformation

# Problems to overcome

If you think of features in analogy to language there is two problems when using a feature to label data.

[Polysemy](../../notes/polysemy.md)

[Synonymy](../../notes/synonymy.md)

# Principle component analysis

[Principle component analysis](../../notes/principle_component_analysis.md)

# Independent component analysis

[Independent component analysis](../../notes/independent_component_analysis.md)

[Cocktail party problem](../../notes/cocktail_party_problem.md)

# Comparison of [ICA](../../notes/independent_component_analysis.md) and [PCA](../../notes/principle_component_analysis.md)

These both do different things. Notice if we have a set of [i.i.d.](../../notes/independent_identically_distributed_samples.md) [random variables](../../notes/random_variable.md) from the [Central limit theorem](../../notes/central_limit_theorem.md) if they set is large enough their sum will look [normally distributed](../../notes/normal_distribution.md) which will provide an axis that maximises [variance](../../notes/variance.md). Therefore [PCA](../../notes/principle_component_analysis.md) might cut a through a line of their addition whereas [ICA](../../notes/independent_component_analysis.md) will want to separate them.

Whilst [ICA](../../notes/independent_component_analysis.md) solves the [Cocktail party problem](../../notes/cocktail_party_problem.md) very well, [PCA](../../notes/principle_component_analysis.md) is very poor at it. [PCA](../../notes/principle_component_analysis.md)'s goal is to find the most shared features whereas [ICA](../../notes/independent_component_analysis.md) finds the features that splits the data apart. For example on faces, [ICA](../../notes/independent_component_analysis.md) finds noses, eyes, chins whereas [PCA](../../notes/principle_component_analysis.md) find brightness or the average face first.

We can use [ICA](../../notes/independent_component_analysis.md) to understand our data on what separates points the best however [ICA](../../notes/independent_component_analysis.md) is not the most efficient algorithm. Though the understanding of your data it provides you can then use to implement more efficient algorithms. For example on documents [ICA](../../notes/independent_component_analysis.md) picks out topics or on nature pictures [ICA](../../notes/independent_component_analysis.md) picks out edges. Both of which there are better algorithms to find.

# Alternatives

[Random component analysis](../../notes/random_component_analysis.md)

[Linear discriminant analysis](../../notes/linear_discriminant_analysis.md)
