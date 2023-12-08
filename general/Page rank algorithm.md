---
aliases: null
checked: false
created: 2023-12-03
last_edited: 2023-12-03
publish: true
tags:
  - programming
type: algorithm
---
# Page rank algorithm

This algorithm is used to calculate the "importance" of a page on the internet, or the [[Page rank|page rank]]. This a [[Probability distribution]] on the [[Webgraph]], $\pi$.

To approximate this we use a [[Markov chain]] and approximate its [[Stationary distribution (Markov Chains)|stationary distribution]].

## Pseudocode

Build a [[Markov chain]] $P$ on the vertices of the [[Webgraph]] $G = (V, E)$. This will have
$$p_{y,x} = \begin{cases} \frac{\alpha}{\vert Out(y) \vert} + \frac{1 - \alpha}{\vert V \vert} & \mbox{if } (y,x) \in E\\ \frac{1 - \alpha}{\vert V \vert} & \mbox{if } \vert Out(y) \vert > 0\\
\frac{1}{\vert V \vert} & \mbox{otherwise.}\end{cases}$$
for some constant $\alpha \in [0,1]$ with $Out(x) = \{y \in V \vert (x,y) \in E\}$ as in the definition for [[Page rank|page rank]].

We then approximate its [[Stationary distribution (Markov Chains)|stationary distribution]]
$$\mu_0 P^t$$
for some large $t$.

There are some tricks that will help with this computation (note the [[Webgraph]] isn't static)
- if $\alpha$ is sufficiently small, then $t$ doesn't have to be too large,
- if we use an old approximation of $\pi$ for $\mu_0$ it will converge faster, and
- matrix multiplication doesn't need to take $O(N^2)$ instead we can get it on the order of $O(\vert E \vert)$.

