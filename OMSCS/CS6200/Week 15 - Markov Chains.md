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

In the example above as $k$ gets large $P^k$ converges in some sense to a single matrix. For very large $k$ we may have

$$
\lim_{k \rightarrow \infty} P^k =  \left ( \begin{array}
\ \cdots & \pi & \cdots\\
\cdots & \pi & \cdots\\
\vdots & \vdots & \vdots\\
\cdots & \pi & \cdots\\
\end{array}\right )
$$
for some [[Stationary distribution (Markov Chains)|stationary distribution]] $\pi$. For the example above we have
$$
\pi = \left ( \begin{array} \ 0.244186 & 0.244186 & 0.406977 & 0.104651 \end{array} \right ).
$$
Formalising what we mean her we have.

![[Stationary distribution (Markov Chains)|stationary distribution]]

The connection follows as to calculate $P \cdot P^k$ for each row we calculate something similar to $\pi P$.

## Algebraic view

For some [[Markov chain]] given by $P \in M_{N, N}(\mathbb{R})$ if you start at state $i$ with $1 \leq i \leq N$ then the [[Probability distribution|probability distribution]] of where you are is given by the $i$'th row of $P$. 

Equivalently, if $\mu_0 \in M_{1,N}(\mathbb{R})$ is the vector with $0$'s in all entries other than $1$ in the $i$'th column then its [[Probability distribution|probability distribution]] is given by
$$
\mu_0 P =: \mu_1
$$
with the [[Probability distribution|probability distribution]] of it after $k$ steps being
$$
\mu_0P^k = \mu_{k-1}P =: \mu_k.
$$
However, we can pick any [[Probability distribution|probability distribution]] over the $N$ states for $\mu_0$. Therefore a [[Stationary distribution (Markov Chains)|stationary distribution]] is just one in which this doesn't change over time.

From the definition any [[Stationary distribution (Markov Chains)|stationary distribution]] is simply an [[Eigenvector and Eigenvalue|eigenvector]] for $P$ with [[Eigenvector and Eigenvalue|eigenvalue]] 1. 

## When does a [[Markov chain]] not have a [[Stationary distribution (Markov Chains)|stationary distribution]]?

If the state [[Directed graph|directed graph]] is a [[Bipartite graph|bipartite graph]] then notice if we start on one side at every even step we are on that side - however for every odd step we are on the other side. This is a classic example of when no [[Stationary distribution (Markov Chains)|stationary distribution]] will exist. This can be summarised by the following definitions.

![[Periodic state (markov chain)|periodic state]]

![[Periodic Markov chain]]

We can show [[Periodic Markov chain|periodic Markov chains]] have no [[Stationary distribution (Markov Chains)|stationary distribution]].

## When does a [[Markov chain]] not have a unique [[Stationary distribution (Markov Chains)|stationary distribution]]?

Suppose we have a [[Markov chain]] with multiple [[Strongly connected components (directed graphs)|strongly connected component]] sinks in the [[Strongly connected component graph (directed graph)|strongly connected component graph]]. Then for each of these we will get a [[Stationary distribution (Markov Chains)|stationary distribution]] on the vertices involved. Then any weighted sum of these [[Stationary distribution (Markov Chains)|stationary distribution]] such that they sum to a [[Probability distribution|probability distribution]] would be a [[Stationary distribution (Markov Chains)|stationary distribution]] on the whole [[Markov chain]] and it wouldn't be unique. 

![[Irreducible Markov chain]]


## [[Markov chain]] with a unique [[Stationary distribution (Markov Chains)|stationary distribution]]

Now we know what to avoid we define the following. 

![[Ergodic Markov chain]]

These [[Markov chain|Markov chains]] have the desired property.

![[Ergodic Markov chains have a unique stationary distribution#Statement]]

They also have the observed limiting form.

![[Ergodic Markov chain limiting distrubution#Statement]]

## What is the [[Stationary distribution (Markov Chains)|stationary distribution]]?

There is one class of [[Markov chain]] that has an easy [[Stationary distribution (Markov Chains)|stationary distribution]] to compute.

![[Symmetric Markov chain]]

![[Symmetric Markov chains have a uniform stationary distribution#Statement]]

There is another form [[Markov chain]] that has an explicit form.

![[Reversible Markov chain]]

Though in general it does not have anything explicit.

## Page Rank algorithm

There is an algorithm invented in 1998 that was used to rate the importance of webpages.

The way it determines importance has nice applications for [[Markov chain|Markov chains]]. It was used in search engines at the beginning of the popularisation of the internet. 

For this lets start by defining the object we are working with.

![[Webgraph]]

We think of this graph in an extended [[Adjacency list format (graph)|Adjacency list]] form,

- $Out(x) = \{y \in V \vert (x,y) \in E\}$, and
- $In(x) = \{y \in V \vert (y,x) \in E\}$. 

The problem is to define $\pi(x)$ to be the "rank" of a page - which will be a measure of importance.