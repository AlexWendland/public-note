---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
tags:
  - probability
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have two [[Independent events|independent]] [[Random variable|random variables]] $X$ and $Y$ over different [[Function domain|domains]] $A$ and $B$. Then the [[Joint Entropy]] is additive
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
