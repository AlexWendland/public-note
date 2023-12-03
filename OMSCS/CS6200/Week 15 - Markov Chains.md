---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2023-11-11
last_edited: 2023-11-11
publish: true
tags:
  - OMSCS
type: lecture
week: 15
---
# Week 15 - Markov Chains

To talk about [[Markov chain]] it is good to recap what a [[Stochastic matrix|probability matrix]] is:

![[Stochastic matrix]]

Now we can define a [[Markov chain]].

![[Markov chain]]

>[!example] Simple [[Markov chain]]
>Suppose we have 4 states with the following probabilities to go between them. This is commonly represented as a [[Edge weights|edge weighted]] [[Directed graph|directed graph]].
>![[simple_markov_chain]]
>In terms of a [[Stochastic matrix|probability matrix]] it would be represented as
>$$
>P = \left ( \begin{array}
>\ 0.5 & 0.5 & 0 & 0\\
>0.2 & 0 & 0.5 & 0.3\\
>0 & 0.3 & 0.7 & 0\\
>0.7 & 0 & 0 & 0.3\\
>\end{array}\right ) 
>$$
>where $p_{i,j}$ represents the edge weight going from $i$ to $j$ in the graph above.

## Steps through the graph

In a [[Markov chain]] $P$'s term $p_{i,j}$ represents the probability of going from $i$ to $j$ in one step. However $P^k$'s terms represent the probability of going from $i$ to $j$ in $k$ steps, so this is still a [[Stochastic matrix|probability matrix]]. In the example above
$$
P^2 = \left ( \begin{array}
\ 0.35 & 0.25 & 0.25 & 0.15\\
0.31 & 0.25 & 0.35 & 0.09\\
0.06 & 0.21 & 0.64 & 0.09\\
0.56 & 0.35 & 0 & 0.09\\
\end{array}\right ) 
$$
as you can notice there is no path from state $4$ to $3$ in 2 steps.

## Stationary distribution

In the example above as $k$ gets large $P^k$ converges in some sense to a single matrix, this helps us define the [[Stationary distribution (Markov Chains)|stationary distribution]] for $P$.

![[Stationary distribution (Markov Chains)|stationary distribution]]

For very large $k$ we may have

$$
P^k \sim  \left ( \begin{array}
\ \cdots & \pi & \cdots\\
\cdots & \pi & \cdots\\
\vdots & \vdots & \vdots\\
\cdots & \pi & \cdots\\
\end{array}\right )
$$
for some [[Stationary distribution (Markov Chains)|stationary distribution]]. For the example above we have
$$
\pi = \left ( \begin{array} \ 0.244186 & 0.244186 & 0.406977 & 0.104651 \end{array} \right ).
$$
## Algebraic view


