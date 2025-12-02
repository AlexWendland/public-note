---
aliases:
checked: false
created: 2024-02-16
draft: false
last_edited: 2024-02-16
tags:
  - machine-learning
title: Haussler Theorem
type: lemma
---
# Statement

> [!important] Haussler Theorem
> Suppose we are in the [modelling framework](modelling_framework.md) with finite [hypothesis space](modelling_paradigm.md) $H$ and [probability distribution](probability_distribution.md) $\mathbb{D}$ on $A$. Set $0 \leq \epsilon \leq 1$. Let our [training data](training_data.md) $T$ be $m$ [i.i.d.](independent_identically_distributed_samples.md) samples from $\mathbb{D}$ with associated correct answers. For any hypothesis $h \in H$ which is [consistent](consistent_learner.md) with $T$ we have a bound on the [true error](true_error.md)
> $$\mathbb{P}[Error_{\mathbb{D}}(h) > \epsilon] \leq \vert H \vert e^{-m\epsilon}.$$

# Proof

Let $f$ be the target function.

Let $h \in H$ such that $\mathbb{P}_{\mathbb{D}}(h(a) = f(a)) \leq 1 - \epsilon$ (i.e. we have [true error](true_error.md) $Error_{\mathbb{D}}(h) > \epsilon$).

Then let $T$ be $m$ [i.i.d.](independent_identically_distributed_samples.md) samples from $A$ using $\mathbb{D}$. The probability $h$ is [consistent](consistent_learner.md) on $T$ is
$$\mathbb{P}_{\mathbb{D}}[h \mbox{ is consistent on } T] \leq (1 - \epsilon)^m$$
As the samples are [i.i.d.](independent_identically_distributed_samples.md). Moreover as $\ln(1-\epsilon) \leq - \epsilon$ for $0 \leq \epsilon < 1$ this gives us
$$\mathbb{P}_{\mathbb{D}}[h \mbox{ is consistent on } T] \leq (1 - \epsilon)^m \leq e^{-m \epsilon}$$
If all $h \in H$ had $Error_{\mathbb{D}}(h) > \epsilon$ then we have
$$
\mathbb{P}[\mbox{Any } h \in H \mbox{ consistent with }T] \leq \vert H \vert e^{-m\epsilon}
$$
the required result.

