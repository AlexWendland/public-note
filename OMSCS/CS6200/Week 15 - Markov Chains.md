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

## How to construct the page rank

We want the page rank that obays some simple ideas.

- the value of a page should be linked to the pages linking to it,
- the value of a link should be inversely proportional to how many outbound links it has, and
- the value of a link should be proportional to the value of the page.

The simplest formula obeying these rules would be
$$\pi(x) = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
This is recursive however, so we don't know if there will be a solution for $\pi$.

Though the suggestive notation of $\pi$ and the idea of a limit should give you an idea that we will construct this via a [[Stationary distribution (Markov Chains)|stationary distribution]] of a [[Markov chain]]. In this world we already know when [[Stationary distribution (Markov Chains)|stationary distributions]] exist.

## Random walk

Suppose we play a game on the [[Webgraph]] where we start at one page, then uniformly at random we hit one of the outbound hyperlinks on that webpage. This defines us a [[Markov chain]] on the [[Webgraph]] where
$$p_{y,x} = \begin{cases} \frac{1}{\vert Out(y) \vert} & \mbox{if } (y,x) \in E\\ 0 & \mbox{otherwise} \end{cases}.$$
Then consider its stationary distribution from the perspective of
$$\pi = \pi P$$
then for a particular position $x$ on the righthand side we have
$$\pi(x) = \sum_{y \in In(x)} \pi(y)p_{y,x} = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
Giving us the page rank we defined above.

## Technical tweaks

The web we might be on might have horrible irregularities within it so we get [[Periodic state (markov chain)|periodic states]] or [[Strongly connected components (directed graphs)|strongly connected components]]. Therefore we add the possibility to randomly jump from the page you are on to one picked uniformly at random from all the pages on the web. We will do this with probability $1 - \alpha$ for some $\alpha \in (0,1] \subset \mathbb{R}$.

Therefore we get the following [[Markov chain]]
$$p_{y,x} = \begin{cases} \frac{\alpha}{\vert Out(y) \vert} + \frac{1 - \alpha}{\vert V \vert} & \mbox{if } (y,x) \in E\\ \frac{1 - \alpha}{\vert V \vert} & \mbox{otherwise} \end{cases}.$$
There is one last problem with this definition. What do we do when a page has no outgoing links? There are a couple approaches taken:
1. Self-loop with all its weight,
2. Remove such nodes (recursively), and
3. Set $\alpha = 0$ for these nodes.
The first solution makes these pages have a much higher page rank. The second solution leaves us with pages with no page rank. The third solution is practically what happens within the Page Rank algorithm.

This [[Markov chain]] is [[Strongly connected (directed graphs)|strongly connected]] as every vertex connects to every other - so it is [[Irreducible Markov chain|irreducible]]. Every vertex has a self-loop so it is an [[Periodic state (markov chain)|aperiodic state]] - making the [[Markov chain]] [[Periodic Markov chain|aperiodic]].

This tweaked [[Markov chain]] is an [[Ergodic Markov chain]] so has a unique [[Stationary distribution (Markov Chains)|stationary distribution]]. We use this to find the page rank.

## How to compute $\pi$

Computing $\pi$ is hard as $N$ therefore $P$ is huge. You will need to compute
$$\mu_0 P^t$$
for some large $t$. There are some tricks that will help
- if $\alpha$ is sufficiently small, then $t$ doesn't have to be too large,
- if we use an old approximation of $\pi$ for $\mu_0$ it will mix faster, and
- matrix multiplication doesn't need to take $O(N^2)$ instead we can get it on the order of $O(\vert E \vert)$.

## What value to set $\alpha$ 

If $\alpha = 0$ then we have a [[Symmetric Markov chain]] with just the uniform [[Stationary distribution (Markov Chains)|stationary distribution]]. So $\alpha$ in some sense is reflecting how much the tweaked [[Markov chain]] is reflecting the original idea of the page rank. 

The trade off for increasing $\alpha$ is that it is slower to converge to a [[Stationary distribution (Markov Chains)|stationary distribution]]. Google are believed to use $\alpha = 0.85$.

