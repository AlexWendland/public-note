---
aliases:
  - value function
checked: false
created: 2025-05-14
draft: false
last_edited: 2025-05-14
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Value function (RL)
> A value function is a mapping of states to a long term worth for a actor in a [[Markov decision process]]. This is defined by $V: S \rightarrow \mathbb{R}$.
>
> Given you are acting along [[Policy (MDP)|policy]] $\pi$ we can calculate the ideal value function to be
> $$
> V^{\pi}(s) = \mathbb{E}[G_t \vert S_t = s].
> $$
