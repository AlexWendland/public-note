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
>Note that it also forms a [[Bayesian network]] with $G = (\{A, B\}, \{(A,B)\} )$ or $G = (\{A, B\}, \{(B,A)\} )$ but it would not be minimal.

>[!example] Conditionally independent
>Suppose we have [[Random variable|random variables]] $A$, $B$, and $C$ where $C$ is [[Conditional independence|conditionally independent]] of $A$ given $B$. Then $G = (\{A, B, C\}, \{(A,B), (B,C)\})$ forms as [[Bayesian network]].

The property of being [[Conditional independence|conditionally independent]] is deducible from the [[Bayesian network]] $(G, X)$ by using the [[Chain rule (probability)|chain rule]]. 

![[Chain rule (probability)|chain rule]]

Lets [[Topological sorting (DAG)|topological order]] $V$ so $V = \{1, 2, \ldots, n\}$ where $(i,j) \in E$ we have $i < j$. Then apply the [[Chain rule (probability)|chain rule]] to
$$
\mathbb{P}[X_1, X_2, \ldots, X_n] = \prod_{k=1}^n \mathbb{P}[X_k \vert X_1, X_2, \ldots, X_{k-1}]
$$
and compare this to 
$$\mathbb{P}[X] =\prod_{v \in V} \mathbb{P}[X_v \vert \bigcup_{(u,v) \in E} X_u].$$
So for any $X_i$ and $j < i$ such that $(j,i) \not \in E$ then $X_i$ is [[Conditional independence|conditionally independent]] of $X_j$ given $\bigcup_{(u,v) \in E} X_u$.  

This is in fact a defining property of [[Bayesian network]].

![[Local Markov property]]

![[Bayesian network if and only if it satisfies the local Markov Property]]

## Sampling