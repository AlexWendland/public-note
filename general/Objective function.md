---
aliases:
  - objective function
checked: false
created: 2024-01-13
last_edited: 2024-01-13
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Objective function
>An objective function $o: S \rightarrow E$ is simply a method to assess how "well" some function is doing. The evaluation space $E$ should ideally be [[Total ordering|totally ordered]].
>
>For example in the [[Modelling framework|modelling framework]] given some [[Testing data|testing data]] $T \subset A \times B$ the objective function could be [[Mean squared error (MSE)]] where $o: B^{T} \rightarrow \mathbb{R}_{\geq 0}$. Then $o((\hat{f}(a))_{(a, b) \in T})$ will be some score of candidate $\hat{f} \in M$. However, they can be much more generic or even less deterministic than this.

