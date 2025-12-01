---
aliases:
checked: false
created: 2024-02-02
draft: false
last_edited: 2024-02-02
name: Polynomial kernel (SVMs)
tags:
  - machine-learning
type: definition
---
>[!tldr] Polynomial kernel
>The *polynomial kernel* is a function that can be used in the [Kernel trick](kernel_trick.md) for [SVMs](support_vector_machines_(svm).md). It has two variables the degree $d \in \mathbb{N}$ and constant $c \in \mathbb{R}$. It is defined as
>$$K_{d,c}: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}, \mbox{ by } K_{d,c}(x_1, x_2) = (x \cdot y + c)^d.$$
>If $n = d = 2$ this relates to the embedding
>$$\Phi: \mathbb{R}^2 \rightarrow \mathbb{R}^6, \mbox{ by } (x_1, x_2) \mapsto (x_1^2, x_2^2, \sqrt{2} x_1x_2, \sqrt{2c} x_1, \sqrt{2c} x_2, c)$$
