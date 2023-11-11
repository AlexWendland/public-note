---
aliases: null
checked: false
created: 2023-11-07
last_edited: 2023-11-07
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> All [[Linear programme|linear programmes]] can be represented in [[Linear programme standard form|standard form]].

# Proof

Suppose we have a [[Linear programme]] of generic form. We need to turn this into a [[Linear programme standard form|standard form]] where:
- We are maximising an objective function,
- All constraints use the same inequality, and
- All variables are greater than zero.

If the objective function is
$$ \min_x \sum_j c_j x_j$$
this can be converted to a maximum by instead looking at
$$ \max_x \sum_j -c_jx_j.$$
Suppose we have an equality constraint
$$ \sum_j a_{i,j} x_j = b_j$$
this can be converted into two inequalities
$$\sum_j a_{i,j} x_j \leq b_j \mbox{ and } \sum_j a_{i,j} x_j \geq b_j.$$
Suppose we have greater than or equal to inequality
$$\sum_j a_{i,j} x_j \geq b_j$$
this can be converted into a less than inequality by multiplying through by negative one
$$\sum_j -a_{i,j} x_j \leq -b_j.$$
Lastly suppose we have a variable $x_j$ that can be negative. We can separated it into its positive and negative components $x_i = x_i^+ - x_i^-$ where $x_i^+, x_i^- \geq 0$. We can then replace the use of $x_i$ by using the before substitution.

This transformation into a general form may increase the number of variables and number on constraints.
