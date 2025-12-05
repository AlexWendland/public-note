---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2025-12-05
tags:
  - probability
title: If two variables are independent joint entropy is additive
type: lemma
---
# Statement

> [!lemma] Lemma
> Suppose we have two [independent](independent_events.md) [random variables](random_variable.md) $X$ and $Y$ over different [domains](function_domain.md) $A$ and $B$. Then the [Joint Entropy](joint_entropy.md) is additive
> $$H(X, Y) = H(X) + H(Y).$$

# Proof

This follows from the definitions
$$
\begin{align*}
H(X, Y) = & - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a, Y = b] \log(\mathbb{P}[X = a, Y = b])\\
= & - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a]\mathbb{P}[Y = b] \log(\mathbb{P}[X = a]\mathbb{P}[Y = b])\\
= & - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a]\mathbb{P}[Y = b] \log(\mathbb{P}[X = a])\\
& \hspace{0.5 in}- \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a]\mathbb{P}[Y = b] \log(\mathbb{P}[Y = b])\\
= & \sum_{b \in B} \mathbb{P}[Y = b] \left ( - \sum_{a \in A} \mathbb{P}[X = a] \log(\mathbb{P}[X = a]) \right )\\
& \hspace{0.5 in}- \sum_{a \in A} \mathbb{P}[X = a] \left ( - \sum_{b \in B} \mathbb{P}[Y = b] \log(\mathbb{P}[Y = b]) \right )\\
= & \ H(X) + H(Y)
\end{align*}
$$
