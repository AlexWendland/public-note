---
aliases:
checked: false
course: '[[CS7641 Machine Learning]]'
created: 2024-03-09
draft: false
last_edited: 2024-03-09
tags:
  - OMSCS
type: lecture
week: 10
---
# Week 10 - Feature transformation

[[Dimensionality reduction|Feature transformation]] is the problem of pre-processing a set of features to create a new (smaller/compact) feature set, while retaining as much information as possible. It is a map $p: \mathbb{F}^N \rightarrow \mathbb{F}^M$ where you usually want $M < N$.

In this course we will focus on [[Linear dimensionality reduction|linear  feature reduction]] where $p$ is a [[Linear map|linear map]].

>[!note]
>Feature selection is a special case of feature transformation

## Problems to overcome

If you think of features in analogy to language there is two problems when using a feature to label data.

![[Polysemy]]

![[Synonymy]]

## Principle component analysis

![[Principle component analysis]]

## Independent component analysis

![[Independent component analysis]]

![[Cocktail party problem]]

## Comparison of [[Independent component analysis|ICA]] and [[Principle component analysis|PCA]]

These both do different things. Notice if we have a set of [[Independent identically distributed samples|i.i.d.]] [[Random variable|random variables]] from the [[Central limit theorem]] if they set is large enough their sum will look [[Normal distribution|normally distributed]] which will provide an axis that maximises [[Variance|variance]]. Therefore [[Principle component analysis|PCA]] might cut a through a line of their addition whereas [[Independent component analysis|ICA]] will want to separate them.

Whilst [[Independent component analysis|ICA]] solves the [[Cocktail party problem]] very well, [[Principle component analysis|PCA]] is very poor at it. [[Principle component analysis|PCA]]'s goal is to find the most shared features whereas [[Independent component analysis|ICA]] finds the features that splits the data apart. For example on faces, [[Independent component analysis|ICA]] finds noses, eyes, chins whereas [[Principle component analysis|PCA]] find brightness or the average face first.

We can use [[Independent component analysis|ICA]] to understand our data on what separates points the best however [[Independent component analysis|ICA]] is not the most efficient algorithm. Though the understanding of your data it provides you can then use to implement more efficient algorithms. For example on documents [[Independent component analysis|ICA]] picks out topics or on nature pictures [[Independent component analysis|ICA]] picks out edges. Both of which there are better algorithms to find.

## Alternatives

![[Random component analysis]]

![[Linear discriminant analysis]]
