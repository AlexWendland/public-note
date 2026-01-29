---
aliases:
created: 2025-05-22
date_checked: 2026-01-29
draft: false
last_edited: 2025-05-22
tags:
  - reinforcement-learning
title: Return (RL)
type: definition
---
>[!definition] Return (RL)
>In a [Markov decision process](markov_decision_process.md) the return $G_t$ at time step $t$ is defined to be the discounted sum of rewards:
> $$
> G_t = \sum_{i=1}^{\infty} \gamma^{i-1} R_{t+i}
> $$
> where $\gamma$ is our [discount factor](discounted_rewards.md) and the summation goes as high as the length of the run. (Note here $R_{t+i}$ is a random variable, as is $G_t$.) As a consequence of the above definition, the return has a nice recursive property:
> $$
> G_t = R_{t+1} + \gamma G_{t+1}.
> $$

