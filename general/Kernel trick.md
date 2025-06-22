---
aliases:
  - kernel trick
  - kernel method
  - Kernel methods
checked: false
created: 2024-02-02
last_edited: 2024-02-02
draft: false
tags:
  - machine-learning
  - maths
type: definition
---
>[!tldr] Kernel trick
>Suppose we are in the [[Modelling framework|modelling framework]] with training data $T \subset A \times B$. When using [[Support vector machines (SVM)|SVMs]] we want to find a [[Hyperplane|hyperplane]] that [[Linearly separable|linearly separates]] the data - though this might not be possible for the current embedding of $T$ in $A$. Though it might be possible for a map
>$$\Phi: A \rightarrow A'.$$
>The *kernel trick* is to define a kernel of similarity
>$$K: A \times A \rightarrow \mathbb{R}, \mbox{ by } K(x_1,x_2) = \Phi(x_1) \cdot \Phi(x_2).$$
>Whilst the form of $K$ may look complicated it usually is simpler than the embedding $\Phi$. Normally you do not find the function $\Phi$ instead you define $K$ and check the [[Mercer’s condition]] which guarantees the existence of $\Phi$. 

