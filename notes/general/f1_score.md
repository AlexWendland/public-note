---
aliases:
checked: false
created: 2024-02-02
draft: false
last_edited: 2024-02-02
title: F1 score
tags:
  - machine-learning
type: definition
---
>[!tldr] F1 score
>For some [binary](binary.md) [classification problem](classification_problems.md) where we are using $\hat{f}: A \rightarrow \{1, -1\}$ to [predict](prediction.md) $f: A \rightarrow \{1, -1\}$ for some [testing data](testing_data.md) $T$ we define the *F1 score* to be the [harmonic mean](harmonic_mean.md) of [precision](precision.md) and [recall](recall.md). That is
> $$\mbox{F1}(\hat{f}, T) = \frac{2 \cdot \mbox{Precision}(\hat{f}, T) \cdot \mbox{Recall}(\hat{f}, T)}{\mbox{Precision}(\hat{f}, T) + \mbox{Recall}(\hat{f}, T)}.$$

