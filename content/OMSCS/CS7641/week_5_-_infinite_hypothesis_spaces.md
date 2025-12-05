---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-02-16
draft: false
last_edited: 2024-02-16
tags:
  - OMSCS
title: Week 5 - Infinite hypothesis spaces
type: lecture
week: 5
---

In [Week 5 - Computational Learning Theory](week_5_-_computational_learning_theory.md) we developed a method to build a [PAC learner](../../notes/probably_approximately_correct_learnable_(pac).md) on a finite dimensional hypothesis space. However this breaks down in infinite dimensions. We need to get around this.

# Lets just cheat

Whilst the [hypothesis space](../../notes/modelling_paradigm.md) might be infinite theoretically, the actual number of distinct hypothesises could be finite. Then we can fall back on the previous work.

>[!example] Discrete problem domain
>Let $A=\{i \in \mathbb{N} \vert i \leq 10\}$ and $B = \{T,F\}$. Then notice that $Fun(A,B) = 2^{10}$ which is finite. If we had $H = \{x \geq \theta \ \vert \ \theta \in \mathbb{R}\}$  then $H$ is infinite as $\theta \in \mathbb{R}$. However, in reality there are at most 11 realised functions here $\{x > n \vert 0 \leq n \leq 10, \ n \in \mathbb{Z}\}$ so we have a finite hypothesis space.

# VC-dimension

In the problem above the hypothesis space was in some way limited. We want to capture the idea of a limited hypothesis space when looking at proper infinite dimensional hypothesis spaces.

[VC dimension](../../notes/vapnik-chervonenkis_dimension.md)

In the example above we have [VC dimension](../../notes/vapnik-chervonenkis_dimension.md) 1. As for any two points $1 \leq l \leq u \leq 10$ if $f(l) = T$ and $f(u) = F$ then no such function $h_{\theta}(x) = [x \geq \theta]$ can set $h_{\theta}(l) = T$ without setting $h_{\theta}(u) = T$.

# VC dimensions roughly follow degrees of freedom

| Separator                               | VC-dimension | parameters |
| --------------------------------------- | ------------ | ---------- |
| 1- demensional hyperplane               | 1            | 1          |
| Interval on $\mathbb{R}$                | 2            | 2          |
| 2-dimensional hyper plane               | 3            | 3          |
| d-dimesional hyperplane                 | d + 1        | -          |
| Convex polygon in $\mathbb{R}^n, n > 1$ | $\infty$     | $\infty$   |

# [PAC learnable](../../notes/probably_approximately_correct_learnable_(pac).md) and [VC dimension](../../notes/vapnik-chervonenkis_dimension.md)

[PAC learnable bound with VC-dimension](../../notes/pac_learnable_bound_with_vc-dimension.md)

This formula is out of no where but there is connection with the finite case where
$$
m \geq \frac{1}{\epsilon}\left ( \ln(\vert H \vert) + \ln\left(\frac{1}{\delta}\right) \right).
$$
For a finite hypothesis space $H$ for $VC(H) = d$ we require $\vert H \vert \geq 2^d$ as we need at last that many hypothesis to split the cases up. Therefore we get a natural upper bound on the [VC dimension](../../notes/vapnik-chervonenkis_dimension.md)
$$
d \leq \log_2(\vert H \vert).
$$
This nicely connects the formulas.

# [PAC learnable](../../notes/probably_approximately_correct_learnable_(pac).md) if and only if finite [VC dimension](../../notes/vapnik-chervonenkis_dimension.md)

[PAC-learnable if and only if finite VC dimension](../../notes/pac-learnable_if_and_only_if_finite_vc_dimension.md)

