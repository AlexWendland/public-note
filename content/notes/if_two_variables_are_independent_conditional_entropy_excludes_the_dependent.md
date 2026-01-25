---
aliases:
created: 2024-02-24
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - probability
title: If two variables are independent conditional entropy excludes the dependent
type: lemma
---
# Statement

> [!lemma] Lemma
> Suppose we have two [independent](independent_events.md) [random variables](random_variable.md) $X$ and $Y$ over different [domains](function_domain.md) $A$ and $B$. Then the [Conditional entropy](conditional_entropy.md) is excludes the dependent
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
