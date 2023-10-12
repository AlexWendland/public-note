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
Using this as there are $n$ bins we can bound the max load
$$\mathbb{P}(\mbox{max load } < \log(n)) \geq 1 - \frac{1}{n}.$$
Infact further analysis can show that [[Happens with high probability|with high probability]] max load = $\Theta(\frac{\log(n)}{\log\log(n)})$.

## Best of 2 approach

```pseudocode
Best of 2(n)
	Input: positive integer n
	Output: allocation of n balls to n bins
1. For i = 1 -> n
	2. Randomly select two bins j & k.
	3. If load(j) < load(k) assign ball to bin j
	4. Otherwise assign ball to bin k
```

In this approach we get the max load is $O(\log \log n)$ [[Happens with high probability|with high probability]]. 

Note if we increase 2 to $d > 2$ then we only get a slight decrease in max load to $O(\frac{\log \log(n)}{\log(d)})$ [[Happens with high probability|with high probability]]. 

## Hashing

>[!example] Unacceptable passwords
>We want to check a user doesn't put in a password that is considered unacceptable.
>We have a huge universe of possible passwords $U$. We want to maintain $S \subset U$ of unacceptable passwords.
>
>For a given password $x \in U$ we want to be able to answer is $x \in S$?

In [[Chain Hashing]]
