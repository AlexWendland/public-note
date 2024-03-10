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
week: 10
---
# Week 10 - Feature transformation

Feature transformation is the problem of pre-processing a set of features to create a new (smaller/compact) feature set, while retaining as much information as possible. It is a map $p: \mathbb{F}^N \rightarrow \mathbb{F}^M$ where you usually want $M < N$.

In this course we will focus on linear feature transformation where $p$ is a [[Linear map|linear map]].

>[!note]
>Feature selection is a special case of feature transformation

## Problems to overcome

If you think of features in analogy to language there is two problems when using a feature to label data.

![[Polysemy]]

![[Synonymy]]

