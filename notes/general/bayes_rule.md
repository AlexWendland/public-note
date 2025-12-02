---
aliases:
checked: false
created: 2024-02-20
draft: false
last_edited: 2024-02-20
title: Bayes rule
tags:
  - probability
type: lemma
---
# Statement

> [!important] Bayes Rule
> For two events $A$ and $B$ we have following equality on their [conditional probabilities](conditional_probability.md)
> $$\mathbb{P}[A \vert B] = \frac{\mathbb{P}[B \vert A] \ \mathbb{P}[A]}{\mathbb{P}[B]}$$

# Proof

This follows from the definition of [conditional probability](conditional_probability.md)
$$
\begin{align*}
\mathbb{P}[A \vert B] = & \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]} & \mbox{from the definition of } \mathbb{P}[A \vert B]\\
= & \frac{\mathbb{P}[B \vert A] \ \mathbb{P}[A]}{\mathbb{P}[B]} & \mbox{as } \mathbb{P}[B \vert A] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[A]}.
\end{align*}
$$
