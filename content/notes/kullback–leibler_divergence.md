---
aliases:
  - KL-divergence
created: 2024-02-24
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - probability
title: "Kullback\u2013Leibler divergence"
type: definition
---
>[!definition] Kullback–Leibler divergence
>Given two [probability distributions](probability_distribution.md) over $A$ called $P$ and $Q$. The *Kullback–Leibler divergence* is the expected value of the log difference between $P$ and $Q$ with the probabilities for each value being given by $P$.
>$$D_{KL}(P \vert \vert Q) = \mathbb{E}_P\left[\log\left (\frac{P}{Q} \right ) \right] = \int_{a \in A} P(a) \log \left( \frac{P(a)}{Q(a)} \right ) da.$$

