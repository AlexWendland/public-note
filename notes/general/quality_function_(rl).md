---
aliases:
  - quality function
checked: false
created: 2025-05-22
draft: false
last_edited: 2025-05-22
tags:
  - reinforcement-learning
title: Quality function (RL)
type: definition
---
>[!tldr] Quality function (RL)
>Similar to the [value function](value_function_(rl).md) a quality function accounts for both state and action. So functionally $q: S \times A \rightarrow \mathbb{R}$ this is the quality of taking action $a \in A$ when you are in state $s \in S$.
>
>Given a [policy](policy_(mdp).md) $\pi$ we can calculate the ideal quality function to be
> $$
> q^{\pi}(s,a) = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a].
> $$

