---
aliases:
created: 2023-11-07
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: All linear programmes can be represented in standard form
type: lemma
---
# Statement

> [!lemma] Lemma
> All [linear programmes](linear_programme.md) can be represented in [standard form](linear_programme_standard_form.md).

# Proof

Suppose we have a [Linear programme](linear_programme.md) of generic form. We need to turn this into a [standard form](linear_programme_standard_form.md) where:
- We are maximising an objective function,
- All constraints use the same inequality, and
- All variables are greater than zero.

If the objective function is
$$ \min_x \sum_j c_j x_j$$
this can be converted to a maximum by instead looking at
$$ \max_x \sum_j -c_jx_j.$$
Suppose we have an equality constraint
$$ \sum_j a_{i,j} x_j = b_i$$
this can be converted into two inequalities
$$\sum_j a_{i,j} x_j \leq b_i \mbox{ and } \sum_j a_{i,j} x_j \geq b_i.$$
Suppose we have greater than or equal to inequality
$$\sum_j a_{i,j} x_j \geq b_i$$
this can be converted into a less than inequality by multiplying through by negative one
$$\sum_j -a_{i,j} x_j \leq -b_i.$$
Lastly suppose we have a variable $x_j$ that can be negative. We can separate it into its positive and negative components $x_j = x_j^+ - x_j^-$ where $x_j^+, x_j^- \geq 0$. We can then replace all occurrences of $x_j$ with this substitution.

This transformation into standard form may increase the number of variables and number of constraints.
