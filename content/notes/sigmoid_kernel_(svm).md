---
aliases:
created: 2024-02-02
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Sigmoid kernel (SVM)
type: definition
---
>[!definition] Sigmoid kernel
>The *sigmoid kernel* is a function that can be used in the [Kernel trick](kernel_trick.md) for [SVMs](support_vector_machines_(svm).md). It has two variables $a, b \in \mathbb{R}_{\geq 0}$. It is defined as
>$$K_{a,b}: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}, \mbox{ by } K_{a,b}(x_1, x_2) = \tanh(a \cdot (x \cdot y) + b).$$

