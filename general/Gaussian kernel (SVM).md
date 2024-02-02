---
aliases: 
checked: false
created: 2024-02-02
last_edited: 2024-02-02
publish: false
tags:
  - machine-learning
type: definition
---
>[!tldr] Gaussian kernel
>The *gaussian kernel* is a function that can be used in the [[Kernel trick]] for [[Support vector machines (SVM)|SVMs]]. It has one variable $\sigma \in \mathbb{R}$ with $\sigma \not = 0$. It is defined as
>$$K_{\sigma}: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}, \mbox{ by } K_{\sigma}(x_1, x_2) = \exp \left ( - \frac{\vert \vert x - y \vert \vert^2}{2 \sigma^2} \right ).$$


