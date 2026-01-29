---
aliases:
  - value function
created: 2025-05-14
date_checked: 2026-01-29
draft: false
last_edited: 2025-05-14
tags:
  - reinforcement-learning
title: Value function (RL)
type: definition
---
>[!definition] Value function (RL)
> A value function is a mapping of states to a long term worth for an actor in a [Markov decision process](markov_decision_process.md). This is defined by $V: S \rightarrow \mathbb{R}$.
>
> Given that you are acting along [policy](policy_(mdp).md) $\pi$, we can calculate the ideal value function to be
> $$
> V^{\pi}(s) = \mathbb{E}[G_t \vert S_t = s].
> $$
