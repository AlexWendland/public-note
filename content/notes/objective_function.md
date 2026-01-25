---
aliases:
  - objective function
created: 2024-01-13
date_checked:
draft: false
last_edited: 2024-01-13
tags:
  - machine-learning
title: Objective function
type: definition
---
>[!tldr] Objective function
>An objective function $o: S \rightarrow E$ is simply a method to assess how "well" some function is doing. The evaluation space $E$ should ideally be [totally ordered](total_ordering.md).
>
>For example in the [modelling framework](modelling_framework.md) given some [testing data](testing_data.md) $T \subset A \times B$ the objective function could be [Mean squared error (MSE)](mean_squared_error_(mse).md) where $o: B^{T} \rightarrow \mathbb{R}_{\geq 0}$. Then $o((\hat{f}(a))_{(a, b) \in T})$ will be some score of candidate $\hat{f} \in M$. However, they can be much more generic or even less deterministic than this.

