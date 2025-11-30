---
aliases: 
checked: false
created: 2024-02-02
last_edited: 2024-02-02
draft: false
tags:
  - machine-learning
type: definition
---
>[!tldr] F1 score
>For some [[Binary|binary]] [[Classification problems|classification problem]] where we are using $\hat{f}: A \rightarrow \{1, -1\}$ to [[Prediction|predict]] $f: A \rightarrow \{1, -1\}$ for some [[Testing data|testing data]] $T$ we define the *F1 score* to be the [[Harmonic mean|harmonic mean]] of [[Precision|precision]] and [[Recall|recall]]. That is
> $$\mbox{F1}(\hat{f}, T) = \frac{2 \cdot \mbox{Precision}(\hat{f}, T) \cdot \mbox{Recall}(\hat{f}, T)}{\mbox{Precision}(\hat{f}, T) + \mbox{Recall}(\hat{f}, T)}.$$

