---
aliases:
  - marginalisation
checked: false
created: 2024-02-23
last_edited: 2024-02-23
publish: true
tags:
  - probability
type: definition
---
>[!tldr] Marginalisation (probability)
>Suppose we have two [[Random variable|random variables]] $X$ and $Y$ over [[Function domain|domains]] $A$ and $B$ respectively. If we know their join distribution $\mathbb{P}[X, Y]$ then we can calculate either $X$ or $Y$'s (marginal) distribution, i.e.
>$$\mathbb{P}[X = a] = \sum_{b \in B} \mathbb{P}[X=a, Y=b] = \sum_{b \in B} \mathbb{P}[X=a | Y=b] \mathbb{P}[Y=b].$$
>The name comes from if you were to draw a table we would get both $\mathbb{P}[X]$ and $\mathbb{P}[Y]$ in the margins if we summed the rows and columns.

