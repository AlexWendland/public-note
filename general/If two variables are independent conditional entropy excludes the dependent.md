---
aliases: 
checked: false
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - probability
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have two [[Independent events|independent]] [[Random variable|random variables]] $X$ and $Y$ over different [[Function domain|domains]] $A$ and $B$. Then the [[Conditional entropy]] is excludes the dependent
> $$H(Y \vert X) = H(Y).$$

# Proof

This follows from the definitions
$$
\begin{align*}
H(Y \vert X) = & - \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a, Y = b] \log(\mathbb{P}[Y = b \vert X = a])\\
= &- \sum_{a \in A} \sum_{b \in B} \mathbb{P}[X = a] \mathbb{P}[Y = b] \log(\mathbb{P}[Y = b])\\
= &\sum_{a \in A} \mathbb{P}[X = a] \left ( - \sum_{b \in B} \mathbb{P}[Y = b] \log(\mathbb{P}[Y = b]) \right )\\
= &H(Y).
\end{align*}
$$