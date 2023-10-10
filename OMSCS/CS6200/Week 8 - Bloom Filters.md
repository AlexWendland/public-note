---
aliases: 
type: lecture
publish: true
created: 2023-10-10
last_edited: 2023-10-10
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 8
chatgpt: false
---
# Week 8 - Bloom Filters

This week we will be focusing on [[Hash function|hash functions]]. First we will look at a probability question.

If you randomly throw $n$ identical balls in $n$ identical bins $B_i$ for $1 \leq i \leq n$ where each throw is independent of on another. Define $load(i) =$ number of balls in bin $B_i$. How large is the max load = $\max_i load(i)$?

We are going to show that  ....

So first look at 

$$\mathbb{P}(\geq log(n) \mbox{ balls are ssigned to } B_i) = \binom{n}{log(n)} \left ( \frac{1}{n} \right )^{\log(n)} \leq \left ( \frac{e}{\log(n)} \right )^{\log(n)}$$
by [[Stirling's approximation|Stirling's formula]] and the definition of the [[Binomial coefficient]].

So by letting $n > 2^{11}$ we can further say
$$\mathbb{P}(\geq log(n) \mbox{ balls are ssigned to } B_i) \leq \frac{1}{n^2}.$$
Using this we can bound the max load
$$