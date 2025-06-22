---
aliases:
  - discounted rewards
checked: false
created: 2024-04-03
last_edited: 2024-04-03
draft: false
tags:
  - machine-learning
type: definition
---
>[!tldr] Discounted rewards
>*Discounted rewards* is a way to evaluate a [[Markov decision process]] with infinite steps. Let $r_i$ for $i \in \mathbb{N}$ be a sequence of rewards for this decision process. Let $\gamma \in [0,1)$ be some constant. Then we set the value of these choices as
>$$
> V(r) = \sum_{i \in \mathbb{N}} \gamma^i r_i.
> $$
> If all $r_i$ are bounded by some constant $R_{max}$ then we have
>$$ \sum_{i=0}^{\infty} \gamma^i r_i \leq \frac{R_{max}}{(1 - \gamma)}$$
>and this is finite.
