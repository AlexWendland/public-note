---
aliases:
  - KL-divergence
checked: false
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - probability
type: definition
---
>[!tldr] Kullback–Leibler divergence
>Given two [[Probability distribution|probability distributions]] over $A$ called $P$ and $Q$. The *Kullback–Leibler divergence* is the expected value of the log difference between $P$ and $Q$ with the probabilities for each value being given by $P$.
>$$D_{KL}(P \vert \vert Q) = \mathbb{E}_P\left[\log\left (\frac{P}{Q} \right ) \right] = \int_{a \in A} P(a) \log \left( \frac{P(a)}{Q(a)} \right ) da.$$

