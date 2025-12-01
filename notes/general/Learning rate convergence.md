---
aliases:
checked: false
created: 2025-05-20
draft: false
last_edited: 2025-05-20
tags:
  - maths
  - reinforcement-learning
type: lemma
---
# Statement

> [!important] Lemma
> Given a [[Markov decision process]] $M$, let $V_t(s)$ be the value estimate for a state $s$ for the $t$'th state. If we update this using the following update rule:
> $$
> V_t(s) = V_{t-1} + \alpha_t (G_t(s) - V_{t-1}(s))
> $$
> where $G_t(s)$ is a noisy sample of the true value $V^{\pi}(s)$ with noise of mean 0, and $\alpha_t$ is a learning rate. Then the incrementally learned $V_t(s)$ will converge in the limit $\lim_{t \rightarrow \infty} V_t(s) = V^{\pi}(s)$ provided that for every state $s$ is visited infinitely often:
> 1. **The sum of the learning rates diverge**: $\sum_{t=1}^{\infty} \alpha_t \rightarrow \infty$, and
> 2. **The sum of the squared learning rates converges**: $\sum_{t=1}^{\infty} \alpha_t^2 < \infty$.

# Proof
