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
> Suppose we have two [[Random variable|random variables]] $X$ and $Y$ over different [[Function domain|domains]] $A$ and $B$. We have that [[Mutual information]] is symmetric
> $$ I(X, Y) = I(Y, X).$$

# Proof
This follows from [[Bayes rule]], [[Logarithms|rules of logarithms]] and [[Marginalisation (probability)|marginalisation]].
$$
\begin{align*}
I(X, Y) & = H(Y) - H(X \vert Y)\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a \vert Y=b])\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log\left (\frac{\mathbb{P}[Y=b \vert X=a]\mathbb{P}[X=a]}{\mathbb{P}[Y=b]} \right)\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b \vert X=a])\\
& \hspace{0.5 in} + \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b])\\
& \hspace{0.5 in} - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[X=a])\\
& = - \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b \vert X=a])\\
& \hspace{0.5 in} + \sum_{b \in B} \mathbb{P}[Y=b]\log(\mathbb{P}[Y=b]) - \sum_{a \in A} \mathbb{P}[X=a]\log(\mathbb{P}[X=a])\\
& = - \sum_{a \in A} \mathbb{P}[X=a]\log(\mathbb{P}[X=a]) - \sum_{a \in A}\sum_{b \in B} \mathbb{P}[X=a, Y=b]\log(\mathbb{P}[Y=b \vert X=a])\\
& = H(X) - 
\end{align*}
$$