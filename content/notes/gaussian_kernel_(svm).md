---
aliases:
created: 2024-02-02
date_checked:
draft: false
last_edited: 2024-02-02
tags:
  - machine-learning
title: Gaussian kernel (SVM)
type: definition
---
>[!tldr] Gaussian kernel
>The *gaussian kernel* is a function that can be used in the [Kernel trick](kernel_trick.md) for [SVMs](support_vector_machines_(svm).md). It has one variable $\sigma \in \mathbb{R}$ with $\sigma \not = 0$. It is defined as
>$$K_{\sigma}: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}, \mbox{ by } K_{\sigma}(x_1, x_2) = \exp \left ( - \frac{\vert \vert x - y \vert \vert^2}{2 \sigma^2} \right ).$$


