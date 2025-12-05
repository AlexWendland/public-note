---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-11-11
draft: false
last_edited: 2023-12-03
tags:
  - OMSCS
title: Week 15 - Markov Chains
type: lecture
week: 15
---

To talk about [Markov chain](../../notes/markov_chain.md) it is good to recap what a [probability matrix](../../notes/stochastic_matrix.md) is:

[Stochastic matrix](../../notes/stochastic_matrix.md)

Now we can define a [Markov chain](../../notes/markov_chain.md).

[Markov chain](../../notes/markov_chain.md)

>[!example] Simple [Markov chain](../../notes/markov_chain.md)
>Suppose we have 4 states with the following probabilities to go between them. This is commonly represented as a [edge weighted](../../notes/edge_weights.md) [directed graph](../../notes/directed_graph.md).
>![simple_markov_chain](../../../static/images/excalidraw/simple_markov_chain.excalidraw.svg)
>In terms of a [probability matrix](../../notes/stochastic_matrix.md) it would be represented as
>$$
>P = \left ( \begin{array}
>\ 0.5 & 0.5 & 0 & 0\\
>0.2 & 0 & 0.5 & 0.3\\
>0 & 0.3 & 0.7 & 0\\
>0.7 & 0 & 0 & 0.3\\
>\end{array}\right )
>$$
>where $p_{i,j}$ represents the edge weight going from $i$ to $j$ in the graph above.

# Steps through the graph

In a [Markov chain](../../notes/markov_chain.md) $P$'s term $p_{i,j}$ represents the probability of going from $i$ to $j$ in one step. However $P^k$'s terms represent the probability of going from $i$ to $j$ in $k$ steps, so this is still a [probability matrix](../../notes/stochastic_matrix.md). In the example above
$$
P^2 = \left ( \begin{array}
\ 0.35 & 0.25 & 0.25 & 0.15\\
0.31 & 0.25 & 0.35 & 0.09\\
0.06 & 0.21 & 0.64 & 0.09\\
0.56 & 0.35 & 0 & 0.09\\
\end{array}\right )
$$
as you can notice there is no path from state $4$ to $3$ in 2 steps.

# Stationary distribution

In the example above as $k$ gets large $P^k$ converges in some sense to a single matrix. For very large $k$ we may have

$$
\lim_{k \rightarrow \infty} P^k =  \left ( \begin{array}
\ \cdots & \pi & \cdots\\
\cdots & \pi & \cdots\\
\vdots & \vdots & \vdots\\
\cdots & \pi & \cdots\\
\end{array}\right )
$$
for some [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) $\pi$. For the example above we have
$$
\pi = \left ( \begin{array} \ 0.244186 & 0.244186 & 0.406977 & 0.104651 \end{array} \right ).
$$
Formalising what we mean her we have.

[stationary distribution](../../notes/stationary_distribution_(markov_chains).md)

The connection follows as to calculate $P \cdot P^k$ for each row we calculate something similar to $\pi P$.

# Algebraic view

For some [Markov chain](../../notes/markov_chain.md) given by $P \in M_{N, N}(\mathbb{R})$ if you start at state $i$ with $1 \leq i \leq N$ then the [probability distribution](../../notes/probability_distribution.md) of where you are is given by the $i$'th row of $P$.

Equivalently, if $\mu_0 \in M_{1,N}(\mathbb{R})$ is the vector with $0$'s in all entries other than $1$ in the $i$'th column then its [probability distribution](../../notes/probability_distribution.md) is given by
$$
\mu_0 P =: \mu_1
$$
with the [probability distribution](../../notes/probability_distribution.md) of it after $k$ steps being
$$
\mu_0P^k = \mu_{k-1}P =: \mu_k.
$$
However, we can pick any [probability distribution](../../notes/probability_distribution.md) over the $N$ states for $\mu_0$. Therefore a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) is just one in which this doesn't change over time.

From the definition any [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) is simply an [eigenvector](../../notes/eigenvector_and_eigenvalue.md) for $P$ with [eigenvalue](../../notes/eigenvector_and_eigenvalue.md) 1.

# When does a [Markov chain](../../notes/markov_chain.md) not have a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md)?

If the state [directed graph](../../notes/directed_graph.md) is a [bipartite graph](../../notes/bipartite_graph.md) then notice if we start on one side at every even step we are on that side - however for every odd step we are on the other side. This is a classic example of when no [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) will exist. This can be summarised by the following definitions.

[periodic state](../../notes/periodic_state_(markov_chain).md)

[Periodic Markov chain](../../notes/periodic_markov_chain.md)

We can show [periodic Markov chains](../../notes/periodic_markov_chain.md) have no [stationary distribution](../../notes/stationary_distribution_(markov_chains).md).

# When does a [Markov chain](../../notes/markov_chain.md) not have a unique [stationary distribution](../../notes/stationary_distribution_(markov_chains).md)?

Suppose we have a [Markov chain](../../notes/markov_chain.md) with multiple [strongly connected component](../../notes/strongly_connected_components_(directed_graphs).md) sinks in the [strongly connected component graph](../../notes/strongly_connected_component_graph_(directed_graph).md). Then for each of these we will get a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) on the vertices involved. Then any weighted sum of these [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) such that they sum to a [probability distribution](../../notes/probability_distribution.md) would be a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) on the whole [Markov chain](../../notes/markov_chain.md) and it wouldn't be unique.

[Irreducible Markov chain](../../notes/irreducible_markov_chain.md)


# [Markov chain](../../notes/markov_chain.md) with a unique [stationary distribution](../../notes/stationary_distribution_(markov_chains).md)

Now we know what to avoid we define the following.

[Ergodic Markov chain](../../notes/ergodic_markov_chain.md)

These [Markov chains](../../notes/markov_chain.md) have the desired property.

[Statement](../../notes/ergodic_markov_chains_have_a_unique_stationary_distribution.md#statement)

They also have the observed limiting form.

[Statement](../../notes/ergodic_markov_chain_limiting_distrubution.md#statement)

# What is the [stationary distribution](../../notes/stationary_distribution_(markov_chains).md)?

There is one class of [Markov chain](../../notes/markov_chain.md) that has an easy [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) to compute.

[Symmetric Markov chain](../../notes/symmetric_markov_chain.md)

[Statement](../../notes/symmetric_markov_chains_have_a_uniform_stationary_distribution.md#statement)

There is another form [Markov chain](../../notes/markov_chain.md) that has an explicit form.

[Reversible Markov chain](../../notes/reversible_markov_chain.md)

Though in general it does not have anything explicit.

# Page Rank algorithm

There is an algorithm invented in 1998 that was used to rate the importance of webpages.

The way it determines importance has nice applications for [Markov chains](../../notes/markov_chain.md). It was used in search engines at the beginning of the popularisation of the internet.

For this lets start by defining the object we are working with.

[Webgraph](../../notes/webgraph.md)

We think of this graph in an extended [Adjacency list](../../notes/adjacency_list_format_(graph).md) form,

- $Out(x) = \{y \in V \vert (x,y) \in E\}$, and
- $In(x) = \{y \in V \vert (y,x) \in E\}$.

The problem is to define $\pi(x)$ to be the "rank" of a page - which will be a measure of importance.

# How to construct the page rank

We want the page rank that obays some simple ideas.

- the value of a page should be linked to the pages linking to it,
- the value of a link should be inversely proportional to how many outbound links it has, and
- the value of a link should be proportional to the value of the page.

The simplest formula obeying these rules would be
$$\pi(x) = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
This is recursive however, so we don't know if there will be a solution for $\pi$. We define this as the [page rank](../../notes/page_rank.md).

Though the suggestive notation of $\pi$ and the idea of a limit should give you an idea that we will construct this via a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md) of a [Markov chain](../../notes/markov_chain.md). In this world we already know when [stationary distributions](../../notes/stationary_distribution_(markov_chains).md) exist.

# Random walk

Suppose we play a game on the [Webgraph](../../notes/webgraph.md) where we start at one page, then uniformly at random we hit one of the outbound hyperlinks on that webpage. This defines us a [Markov chain](../../notes/markov_chain.md) on the [Webgraph](../../notes/webgraph.md) where
$$p_{y,x} = \begin{cases} \frac{1}{\vert Out(y) \vert} & \mbox{if } (y,x) \in E\\ 0 & \mbox{otherwise} \end{cases}.$$
Then consider its stationary distribution from the perspective of
$$\pi = \pi P$$
then for a particular position $x$ on the righthand side we have
$$\pi(x) = \sum_{y \in In(x)} \pi(y)p_{y,x} = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
Giving us the page rank we defined above.

# Technical tweaks

The web we might be on might have horrible irregularities within it so we get [periodic states](../../notes/periodic_state_(markov_chain).md) or [strongly connected components](../../notes/strongly_connected_components_(directed_graphs).md). Therefore we add the possibility to randomly jump from the page you are on to one picked uniformly at random from all the pages on the web. We will do this with probability $1 - \alpha$ for some $\alpha \in (0,1] \subset \mathbb{R}$.

Therefore we get the following [Markov chain](../../notes/markov_chain.md)
$$p_{y,x} = \begin{cases} \frac{\alpha}{\vert Out(y) \vert} + \frac{1 - \alpha}{\vert V \vert} & \mbox{if } (y,x) \in E\\ \frac{1 - \alpha}{\vert V \vert} & \mbox{otherwise} \end{cases}.$$
There is one last problem with this definition. What do we do when a page has no outgoing links? There are a couple approaches taken:
1. Self-loop with all its weight,
2. Remove such nodes (recursively), and
3. Set $\alpha = 0$ for these nodes.
The first solution makes these pages have a much higher page rank. The second solution leaves us with pages with no page rank. The third solution is practically what happens within the Page Rank algorithm.

This [Markov chain](../../notes/markov_chain.md) is [strongly connected](../../notes/strongly_connected_(directed_graphs).md) as every vertex connects to every other - so it is [irreducible](../../notes/irreducible_markov_chain.md). Every vertex has a self-loop so it is an [aperiodic state](../../notes/periodic_state_(markov_chain).md) - making the [Markov chain](../../notes/markov_chain.md) [aperiodic](../../notes/periodic_markov_chain.md).

This tweaked [Markov chain](../../notes/markov_chain.md) is an [Ergodic Markov chain](../../notes/ergodic_markov_chain.md) so has a unique [stationary distribution](../../notes/stationary_distribution_(markov_chains).md). We use this to find the page rank.

# How to compute $\pi$

This is the [Page rank algorithm](../../notes/page_rank_algorithm.md).

Computing $\pi$ is hard as $N$ therefore $P$ is huge. You will need to compute
$$\mu_0 P^t$$
for some large $t$. There are some tricks that will help
- if $\alpha$ is sufficiently small, then $t$ doesn't have to be too large,
- if we use an old approximation of $\pi$ for $\mu_0$ it will mix faster, and
- matrix multiplication doesn't need to take $O(N^2)$ instead we can get it on the order of $O(\vert E \vert)$.

# What value to set $\alpha$

If $\alpha = 0$ then we have a [Symmetric Markov chain](../../notes/symmetric_markov_chain.md) with just the uniform [stationary distribution](../../notes/stationary_distribution_(markov_chains).md). So $\alpha$ in some sense is reflecting how much the tweaked [Markov chain](../../notes/markov_chain.md) is reflecting the original idea of the page rank.

The trade off for increasing $\alpha$ is that it is slower to converge to a [stationary distribution](../../notes/stationary_distribution_(markov_chains).md). Google are believed to use $\alpha = 0.85$.

