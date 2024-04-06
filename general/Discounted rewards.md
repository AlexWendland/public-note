---
aliases:
  - discounted rewards
checked: false
created: 2024-04-03
last_edited: 2024-04-03
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Discounted rewards
>*Discounted rewards* is a way to evaluate a [[Markov decision process]] with infinite steps - assuming $R(s)$ is bounded by some constant $R_{max}$. Suppose we have a policy that leads to a sequence of rewards $r_i \in \mathbb{R}$ for $i \in \mathbb{N}$. We pick some $0 \leq \gamma < 1$ then we evaluate this strategy using the following formula
>$$ \sum_{i=0}^{\infty} \gamma^i r_i \leq \frac{R_{max}}{(1 - \gamma)}$$

