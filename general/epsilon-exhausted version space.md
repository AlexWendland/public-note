---
aliases: 
checked: false
created: 2024-02-16
last_edited: 2024-02-16
draft: false
tags:
  - machine-learning
type: definition
---
>[!tldr] epsilon-exhausted version space
>Suppose we are in the [[Modelling framework|modelling framework]] with some [[Training data|training data]] $T \subset A \times B$, a [[Modelling paradigm|hypothesis space]] $H \subset Func(A,B)$ and a [[Probability distribution|probability distribution]] $\mathbb{D}$ on $A$. For some $0 \leq \epsilon \leq 0.5$ the [[Version space|version space]] $VS_H(T)$ is $\epsilon$-exhausted if and only if for all $h \in VS_H(T)$ the [[True error|true error]]
>$$Error_{\mathbb{D}}(h) \leq \epsilon.$$ 
