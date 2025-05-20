---
aliases: 
checked: false
created: 2025-05-20
last_edited: 2025-05-20
publish: true
tags:
  - maths
  - reinforcement-learning
type: lemma
---
# Statement

> [!important] Lemma
> Given a [[Markov decision process]] $M$ and infinite uniform random runs of $M$ where for some discount factor $0 < \gamma < 1$ we have $R_t(s)$ to be the discounted rewards for state $s$ in run $t$. The incrementally learnt value functions $V_t$
> $$
> V_t(s) = V_{t-1} + \alpha_t (R_t(s) - V_{t-1}(s))
> $$
> will converge in the limit $\lim_{t \rightarrow \infty} V_t(s) = V(s)$ to $M$'s real value function if the learning rate $\alpha_t$ has the following properties:
> 1. $\sum_{t=1}^{\infty} \alpha_t \rightarrow \infty$, and
> 2. $\sum_{t=1}^{\infty} \alpha_t^2 < \infty$.

# Proof
