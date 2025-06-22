---
aliases: 
checked: false
course: "[[CS6215 Introduction to Graduate Algorithms]]"
created: 2023-10-10
last_edited: 2023-11-11
draft: false
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 7 - Homework 5 (unassessed)
# Week 8 - Bloom Filters

This week we will be focusing on [[Hash function|hash functions]]. First we will look at a probability question.

## Balls in bins problem

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

In [[Chain Hashing]], we use a [[Hash table|hash table]] ($A$, $h: U \rightarrow A$) of a given size $n$. Where the entries in $A$ the [[Associative array|associative array]] are [[Linked lists|linked lists]] that handle collisions.

For notation let $\vert U \vert =: N$ and have $\vert S \vert =: m$ then ideally we will have $N >> n >= m$.

In [[Chain Hashing]] the length of the linked lists behave similarly to the balls in the bins problem. Therefore, if $m = n$ [[Happens with high probability|with high probability]] look up time will be $O(\log(n))$ which will be too high if $n$ is sufficiently large. This is where the best of 2 approach can help us.

## Best of 2 hashing

Instead of using a [[Hash table|hash table]] with only one [[Hash function|hash function]] instead lets use two independent hash functions $h_1$ and $h_2$. Then we do the following for operations:

- To add $x \in U$ we:
	- Compute $h_1(x)$ and $h_2(x)$, and
	- add $x$ to the least loaded of $h_1(x)$ and $h_2(x)$.
- To check if $e \in U$ is in $S$
	- Compute $h_1(e)$ and $h_2(e)$, and
	- check for $y$ in $h_1(e)$ and $h_2(e)$.

From the analysis we did above if $n = m$ then this should have run time of $O(\log \log(n))$.

## Bloom filters

[[Bloom filters]] are another way to solve the unacceptable passwords problem.
- Checks take $O(1)$ time,
- It uses less space than [[Chain Hashing]], and
- it is a simpler algorithm.
However, there is a small probability of false positives $x \not \in S$ but we say it is!


