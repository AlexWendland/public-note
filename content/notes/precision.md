---
aliases:
created: 2024-02-02
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Precision
type: definition
---
>[!definition] Precision
> For some [binary](binary.md) [classification problem](classification_problems.md) where we are using $\hat{f}: A \rightarrow \{1, -1\}$ to [predict](prediction.md) $f: A \rightarrow \{1, -1\}$ for some [testing data](testing_data.md) $T$ we define
> $$\mbox{Precision}(\hat{f}, T) = \frac{\vert \{ t \in T \vert f(t) = \hat{f}(t) = 1\} \vert}{\vert \{ t \in T \vert \hat{f}(t) = 1\} \vert}  $$
> in terms [result types](result_types.md) this is
> $$\mbox{Precision}(\hat{f}, T) = \frac{\mbox{True positives}}{\mbox{True positives} + \mbox{False positives}}.$$

