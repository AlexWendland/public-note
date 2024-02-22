---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-02-21
last_edited: 2024-02-21
publish: true
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 10 - Bayesian Inference

## Joint distributions

We can use the definition of [[Conditional probability|conditional probability]] to help calculate joint probabilities.
$$\mathbb{P}[A, B] = \mathbb{P}[A \vert B] \mathbb{P}[B].$$
If probabilities are independent this simplifies to
$$\mathbb{P}[A, B] = \mathbb{P}[A] \ \mathbb{P}[B].$$
We say simplifies as to keep track of $\mathbb{P}[A, B]$ if $A$ has domain of size $n$ and $B$ of size $m$ we only need to keep track of $n + m - 2$ values whereas in the first case we need to keep track of $nm - 1$ values.

Therefore independence simplifies the amount of knowledge we need to store to compute the probability of a large state. Therefore is useful to generalise the definition of independence.

![[Conditional independence]]

>[!note] Why is it a generalisation?
>Note if $A$ and $B$ are [[Independent events|independent event]] then
>$$\mathbb{P}[A \vert B] = \frac{\mathbb{P}[A, B]}{\mathbb{P}[B]} = \mathbb{P}[A].$$
>We could say that $A$ is conditionally independent on $B$ given any event.

## Bayesian networks (belief networks)

For a set of [[Random variable|random variables]] $X_v$ for $v \in V$ we would like to [[Graph|graph]] these relationships using a directed graph. We want an edge $(u,v) \in E$ to signify that $X_u$ is dependent on $X_v$. Though there is a lot of choice in this as for any two dependent variables we could choose $(u,v) \in E$ or $(v,u) \in E$ - however we want to make a directional choice.

![[Bayesian network]]

>[!example] Independent variables
>Let $A$ and $B$ be [[Independent events|independent event]]. Then $G = (\{A, B\}, \emptyset )$ forms a [[Bayesian network]] as
>$$\mathbb{P}[A,B] = \mathbb{P}[A]\mathbb{P}[B].$$ 

>[!example] Conditionally independent
>Suppose we have [[Random variable|random variables]] $A$, $B$, and $C$