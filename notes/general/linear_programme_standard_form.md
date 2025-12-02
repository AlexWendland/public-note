---
aliases:
  - linear programme in standard form
  - linear programmes in standard form
checked: false
created: 2023-11-07
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Linear programme standard form
type: definition
---
>[!tldr] Linear programme standard form
>The standard form for a [linear programme](linear_programme.md) with $n$ variables and $m$ constraints is given by [matrices](matrix.md) $x, c \in M_{n,1}(\mathbb{R})$, $A \in M_{m,n}(\mathbb{R})$, and $b \in M_{m,1}(\mathbb{R})$ were we want to
>$$\max_x c^T x \ \mbox{ such that } \ Ax \leq b \mbox{ and } 0 \leq x.$$
>Some variants may use $\min$ instead of $\max$ in the objective function or use $\geq$ instead of $\leq$ in the constraints equation however this can easily be translated using the rules from the [standard form lemma](all_linear_programmes_can_be_represented_in_standard_form.md).

