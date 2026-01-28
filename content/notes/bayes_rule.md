---
aliases:
created: 2024-02-20
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - probability
title: Bayes' rule
type: lemma
---
# Statement

> [!lemma] Bayes' rule
> For two events $A$ and $B$, we have the following equality on their [conditional probabilities](conditional_probability.md):
> $$\mathbb{P}[A \vert B] = \frac{\mathbb{P}[B \vert A] \cdot \mathbb{P}[A]}{\mathbb{P}[B]}$$

# Proof

This follows from the definition of [conditional probability](conditional_probability.md)
$$
\begin{align*}
\mathbb{P}[A \vert B] = & \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]} & \mbox{from the definition of } \mathbb{P}[A \vert B]\\
= & \frac{\mathbb{P}[B \vert A] \cdot \mathbb{P}[A]}{\mathbb{P}[B]} & \mbox{as } \mathbb{P}[B \vert A] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[A]}.
\end{align*}
$$
