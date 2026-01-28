---
aliases:
created: 2025-05-20
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
  - reinforcement-learning
title: Learning rate convergence
type: lemma
---
# Statement

> [!lemma] Lemma
> Given a [Markov decision process](markov_decision_process.md) $M$, let $V_t(s)$ be the value estimate for a state $s$ at the $t$-th iteration. If we update this using the following update rule:
> $$
> V_t(s) = V_{t-1} + \alpha_t (G_t(s) - V_{t-1}(s))
> $$
> where $G_t(s)$ is a noisy sample of the true value $V^{\pi}(s)$ with noise of mean 0, and $\alpha_t$ is a learning rate. Then the incrementally learned $V_t(s)$ will converge in the limit $\lim_{t \rightarrow \infty} V_t(s) = V^{\pi}(s)$ provided that every state $s$ is visited infinitely often:
> 1. **The sum of the learning rates diverge**: $\sum_{t=1}^{\infty} \alpha_t \rightarrow \infty$, and
> 2. **The sum of the squared learning rates converges**: $\sum_{t=1}^{\infty} \alpha_t^2 < \infty$.

# Proof
