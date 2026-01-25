---
aliases:
created: 2024-02-21
date_checked:
draft: false
last_edited: 2024-02-21
tags:
  - machine-learning
title: Bayeses optimal classifier
type: definition
---
>[!tldr] Bayesian classification
>Suppose we have a [classification problem](classification_problems.md) for some function $f: A \rightarrow B$. We have a [hypothesis space](modelling_paradigm.md) $H$ and [training data](training_data.md) $T$. We want to work out what the best label is for $a \in A$. We can use [maximum a posteriori probability](maximum_a_posteriori_probability_estimate_(map).md) to calculate *Bayeses optimal classifier*
>$$v_{MAP} = \mbox{arg}\max_{v \in V} \sum_{h \in H} \mathbb{P}[v \vert h] \mathbb{P}[h \vert T].$$

