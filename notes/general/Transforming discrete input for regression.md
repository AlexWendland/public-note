---
aliases:
checked: false
created: 2024-01-17
draft: false
last_edited: 2024-01-17
tags:
  - machine-learning
type: method
---
# Transforming discrete input for regression

Suppose we are in the [[Modelling framework|modelling framework]] and have been given a discrete input variable $d \in A'$ for a [[Regression problems|regression problem]]. If $d$ has $n$ possible values $v_1, v_2, \ldots, v_n$ we introduce $n-1$ dimensional space $\tilde{A} = \mathbb{R}^{n-1}$. Then we define the transformation $t: A' \rightarrow \tilde{A} = \mathbb{R}^{n-1}$
$$t(v_i) = \begin{cases} e_i & \mbox{if } 1 \leq i \leq n-1\\ 0 & \mbox{otherwise}  \end{cases}$$
where $e_1, e_2, \ldots e_{n-1}$ are the basis vectors of $\tilde{A}$.

We would then replace $A'$ by $\tilde{A}$ in the input space $A$.

In the case of [[Boolean variable|boolean]] input variables, this is as simple as saying $0$ is for False and $1$ is for True.

You may wonder why no expand this to an $n$-dimensional space. This would ruin independence of the variables, as we would know that always these values in these $n$ dimensional spaces have to add to 1 - this causes instability in our [[Polynomial regression|polynomial regression]].
