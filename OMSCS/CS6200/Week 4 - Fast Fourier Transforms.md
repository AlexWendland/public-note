---
aliases: 
type: lecture
publish: true
created: 2023-09-18
last_edited: 2023-09-18
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "4"
chatgpt: false
---
# Week 4 - Fast Fourier Transforms

> [!tldr] Polynomial multiplication problem
> Given polynomials
> $$A(x) = \sum_{i=0}^{n-1} a_i x^i, \mbox{ and } B(x) = \sum_{i=0}^{n-1} b_i x^i.$$
> We want to compute the product 
> $$\sum_{i=0}^{2n-2} c_i x^i = C(x) := A(x) B(x).$$

This can be restated as the following problem.

> [!tldr] Convolution problem
> Given a vector $a = (a_0, a_1, \ldots, a_{n-1})$ and $b = (b_0, b_1, \ldots b_{n-1})$ we want to compute the convolution $c = a \ast b = (c_0, \ldots, c_{2n-2})$. Where
> $$ c_k = \sum_{i=\max\{0,k-n+1\}}^{\min\{n-1,k\}} a_i b_{k-i}.$$

If you where to just do those computations, it would take you $O(n^2)$ time as you 

