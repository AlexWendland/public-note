---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
title: Mutual information is symmetric
tags:
  - probability
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have two [random variables](random_variable.md) $X$ and $Y$ over different [domains](function_domain.md) $A$ and $B$. We have that [Mutual information](mutual_information.md) is symmetric
> $$ I(X, Y) = I(Y, X).$$

# Proof
This follows from [Bayes rule](bayes_rule.md), [rules of logarithms](logarithms.md) and [marginalisation](marginalisation_(probability).md).
$$
\begin{align*}
I(X, Y) & = H(Y) - H(Y \vert X)\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b \vert X=a])\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log\left (\frac{\mathbb{P}[X=a \vert Y=b]\mathbb{P}[Y=b]}{\mathbb{P}[X=a]} \right)\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a \vert Y=b])\\
& \hspace{0.5 in} + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b])\\
& \hspace{0.5 in} - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a])\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a \vert Y=b])\\
& \hspace{0.5 in} + \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) - \sum_{a \in A} \mathbb{P}[X=a]\log(\mathbb{P}[X=a])\\
& = - \sum_{a \in A} \mathbb{P}[X=a]\log(\mathbb{P}[X=a]) - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a \vert Y=b])\\
& = H(X) - H(X \vert Y)\\
& = I(Y,X)
\end{align*}
$$
