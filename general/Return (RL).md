---
aliases: 
checked: false
created: 2025-05-22
last_edited: 2025-05-22
publish: true
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Return (RL)
>In a [[Markov decision process]] the return $G_t$ at time step $t$ is defined to be the discounted sum of rewards:
> $$
> G_t = \sum_{i=1}^{\infty} \gamma^{i-1} R_{t+i}
> $$
> where $\gamma$ is our [[Discounted rewards|discounted factor]] and the summation goes as high as the length of the run. (Note here $R_{t+i}$ is a random variable as is $G_t$.) Due to the definition of rewards it has a nice recursive property:
> $$
> G_t = R_{t+1} + \gamma G_{t+1}.
> $$

