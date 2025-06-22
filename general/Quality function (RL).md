---
aliases:
  - quality function
checked: false
created: 2025-05-22
last_edited: 2025-05-22
draft: false
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Quality function (RL)
>Similar to the [[Value function (RL)|value function]] a quality function accounts for both state and action. So functionally $q: S \times A \rightarrow \mathbb{R}$ this is the quality of taking action $a \in A$ when you are in state $s \in S$.
>
>Given a [[Policy (MDP)|policy]] $\pi$ we can calculate the ideal quality function to be
> $$
> q^{\pi}(s,a) = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a].
> $$

