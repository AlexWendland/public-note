---
aliases:
checked: false
course: '[CS7641 Machine Learning](../cs7641_machine_learning.md)'
created: 2024-03-09
draft: false
last_edited: 2024-03-09
name: Week 10 - Feature transformation
tags:
  - OMSCS
type: lecture
week: 10
---
# Week 10 - Feature transformation

[Feature transformation](../../general/dimensionality_reduction.md) is the problem of pre-processing a set of features to create a new (smaller/compact) feature set, while retaining as much information as possible. It is a map $p: \mathbb{F}^N \rightarrow \mathbb{F}^M$ where you usually want $M < N$.

In this course we will focus on [linear  feature reduction](../../general/linear_dimensionality_reduction.md) where $p$ is a [linear map](../../general/linear_map.md).

>[!note]
>Feature selection is a special case of feature transformation

## Problems to overcome

If you think of features in analogy to language there is two problems when using a feature to label data.

[Polysemy](../../general/polysemy.md)

[Synonymy](../../general/synonymy.md)

## Principle component analysis

[Principle component analysis](../../general/principle_component_analysis.md)

## Independent component analysis

[Independent component analysis](../../general/independent_component_analysis.md)

[Cocktail party problem](../../general/cocktail_party_problem.md)

## Comparison of [ICA](../../general/independent_component_analysis.md) and [PCA](../../general/principle_component_analysis.md)

These both do different things. Notice if we have a set of [i.i.d.](../../general/independent_identically_distributed_samples.md) [random variables](../../general/random_variable.md) from the [Central limit theorem](../../general/central_limit_theorem.md) if they set is large enough their sum will look [normally distributed](../../general/normal_distribution.md) which will provide an axis that maximises [variance](../../general/variance.md). Therefore [PCA](../../general/principle_component_analysis.md) might cut a through a line of their addition whereas [ICA](../../general/independent_component_analysis.md) will want to separate them.

Whilst [ICA](../../general/independent_component_analysis.md) solves the [Cocktail party problem](../../general/cocktail_party_problem.md) very well, [PCA](../../general/principle_component_analysis.md) is very poor at it. [PCA](../../general/principle_component_analysis.md)'s goal is to find the most shared features whereas [ICA](../../general/independent_component_analysis.md) finds the features that splits the data apart. For example on faces, [ICA](../../general/independent_component_analysis.md) finds noses, eyes, chins whereas [PCA](../../general/principle_component_analysis.md) find brightness or the average face first.

We can use [ICA](../../general/independent_component_analysis.md) to understand our data on what separates points the best however [ICA](../../general/independent_component_analysis.md) is not the most efficient algorithm. Though the understanding of your data it provides you can then use to implement more efficient algorithms. For example on documents [ICA](../../general/independent_component_analysis.md) picks out topics or on nature pictures [ICA](../../general/independent_component_analysis.md) picks out edges. Both of which there are better algorithms to find.

## Alternatives

[Random component analysis](../../general/random_component_analysis.md)

[Linear discriminant analysis](../../general/linear_discriminant_analysis.md)
