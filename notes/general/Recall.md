---
aliases:
  - recall
  - sensitivity
checked: false
created: 2024-02-02
last_edited: 2024-02-02
draft: false
tags:
  - machine-learning
  - statistics
type: definition
---
>[!tldr] Recall
> For some [[Binary|binary]] [[Classification problems|classification problem]] where we are using $\hat{f}: A \rightarrow \{1, -1\}$ to [[Prediction|predict]] $f: A \rightarrow \{1, -1\}$ for some [[Testing data|testing data]] $T$ we define
> $$\mbox{Recall}(\hat{f}, T) = \frac{\vert \{ t \in T \vert f(t) = \hat{f}(t) = 1\} \vert}{\vert \{ t \in T \vert f(t) = \hat{f}(t) = 1\} \vert + \vert \{ t \in T \vert \hat{f}(t) = -1, f(t) = 1\} \vert}  $$
> in terms [[Result types|result types]] this is
> $$\mbox{Precision}(\hat{f}, T) = \frac{\mbox{True positives}}{\mbox{True positives} + \mbox{False negatives}}.$$

