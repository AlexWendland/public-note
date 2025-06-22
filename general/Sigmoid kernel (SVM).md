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
>[!tldr] Sigmoid kernel
>The *sigmoid kernel* is a function that can be used in the [[Kernel trick]] for [[Support vector machines (SVM)|SVMs]]. It has two variables $a, b \in \mathbb{R}_{\geq 0}$. It is defined as
>$$K_{a,b}: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}, \mbox{ by } K_{a,b}(x_1, x_2) = \tanh(a \cdot (x \cdot y) + b).$$

