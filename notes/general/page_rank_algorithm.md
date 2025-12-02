---
aliases:
checked: false
created: 2023-12-03
draft: false
last_edited: 2023-12-03
title: Page rank algorithm
tags:
  - programming
type: algorithm
---
# Page rank algorithm

This algorithm is used to calculate the "importance" of a page on the internet, or the [page rank](page_rank.md). This a [Probability distribution](probability_distribution.md) on the [Webgraph](webgraph.md), $\pi$.

To approximate this we use a [Markov chain](markov_chain.md) and approximate its [stationary distribution](stationary_distribution_(markov_chains).md).

## Pseudocode

Build a [Markov chain](markov_chain.md) $P$ on the vertices of the [Webgraph](webgraph.md) $G = (V, E)$. This will have
$$p_{y,x} = \begin{cases} \frac{\alpha}{\vert Out(y) \vert} + \frac{1 - \alpha}{\vert V \vert} & \mbox{if } (y,x) \in E\\ \frac{1 - \alpha}{\vert V \vert} & \mbox{if } \vert Out(y) \vert > 0\\
\frac{1}{\vert V \vert} & \mbox{otherwise.}\end{cases}$$
for some constant $\alpha \in [0,1]$ with $Out(x) = \{y \in V \vert (x,y) \in E\}$ as in the definition for [page rank](page_rank.md).

We then approximate its [stationary distribution](stationary_distribution_(markov_chains).md)
$$\mu_0 P^t$$
for some large $t$.

There are some tricks that will help with this computation (note the [Webgraph](webgraph.md) isn't static)
- if $\alpha$ is sufficiently small, then $t$ doesn't have to be too large,
- if we use an old approximation of $\pi$ for $\mu_0$ it will converge faster, and
- matrix multiplication doesn't need to take $O(N^2)$ instead we can get it on the order of $O(\vert E \vert)$.

