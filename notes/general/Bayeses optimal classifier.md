---
aliases:
checked: false
created: 2024-02-21
draft: false
last_edited: 2024-02-21
tags:
  - machine-learning
type: definition
---
>[!tldr] Bayesian classification
>Suppose we have a [[Classification problems|classification problem]] for some function $f: A \rightarrow B$. We have a [[Modelling paradigm|hypothesis space]] $H$ and [[Training data|training data]] $T$. We want to work out what the best label is for $a \in A$. We can use [[Maximum a posteriori probability estimate (MAP)|maximum a posteriori probability]] to calculate *Bayeses optimal classifier*
>$$v_{MAP} = \mbox{arg}\max_{v \in V} \sum_{h \in H} \mathbb{P}[v \vert h] \mathbb{P}[h \vert T].$$

