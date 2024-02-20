---
aliases: 
checked: false
created: 2024-02-20
last_edited: 2024-02-20
publish: true
tags:
  - probability
type: lemma
---
# Statement

> [!important] Lemma
> For two events $A$ and $B$ we have following equality on their [[Conditional probability|conditional probabilities]] 
> $$\mathbb{P}[A \vert B] = \frac{\mathbb{P}[B \vert A] \ \mathbb{P}[A]}{\mathbb{P}[B]}$$

# Proof

This follows from the definition of [[Conditional probability|conditional probability]]
$$
\begin{align*}
\mathbb{P}[A \vert B] = & \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]} & \mbox{from the definition of } \mathbb{P}[A \vert B]\\
= & \frac{\mathbb{P}[B \vert A] \ \mathbb{P}[A]}{\mathbb{P}[B]} & \mbox{as } \mathbb{P}[B \vert A] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[A]}.
\end{align*}
$$