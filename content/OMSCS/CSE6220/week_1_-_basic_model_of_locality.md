---
aliases:
checked: false
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-01-15'
draft: true
last_edited: '2026-01-15'
tags:
  - OMSCS
title: Week 1 - Basic Model of Locality
type: lecture
week: 1
---

This lecture is based on the paper:

> [The Input/Output Complexity of Sorting and Related Problems](https://static.us.edusercontent.com/files/0wf5yhXPyB0fWmGiW0NefTc9)

> [!note] High performance computing
> This is a bad name, all computing should be high performance.
> This course is really about supercomputers, where you need to extract every last ounce of compute you have to solve the problem faster.

# Memory models

When talking about high performance computing - it is not only about optimising the run time of the algorithm but also about how long it takes to move the memory around to complete the algorithm.
Most algorithm classes work in a simple 'fast memory' model, where you have instant access to an infinitely large memory.
This is a fairly unreasonable model - whilst some OS try to automatically handle memory for you, this is still inefficient in comparison to adapting your algorithm for the computer it is running on.

The most basic memory model which is not the above is called the 'von Neumann model'.
This has a processor with a limited fast memory cache next to it (of size $Z$ words), and an infinite slow main memory slightly further away.
In this model, we want to limit the number of data transfers between slow and fast memory.
This model follows some rules:

1. Local data rule: The processor may only compute on data in fast memory.

2. Block transfer rule: Slow-fast transfers in blocks of size $L$ words.

> [!definition] Words
> We use a generic unit 'word' this will vary based on what computation or computer you are on.
> For example, it could be a 32/64 bits depending on the architecture.

As we load in blocks of $L$ words, you may have to consider 'data alignment'.
This means if you are loading an array of $n$ elements, if $n$ is not divisible by $L$ then you may have to do extra transfers.
Or if your data is sitting within a larger block of data, your start address might not align with $L$-sized block boundaries - so you might require extra transfers even if $n$ is divisible by $L$.
When $n$ is sufficiently large - we don't really care about this.

So there are two main costs we now will care about:

- *Work*: $W(n)$ is the number of computations needed to complete the algorithm.

- *Transfers* (I/O complexity): $Q(n,Z,L)$ is the number of $L$-sized slow-fast transfers.

> [!example] Summing an array
> Let's say we have an array of $n$ integers that all take 1 word.
> The work is $W(n) = n$.
> The transfers are $Q(n,Z,L) = \lceil n/L \rceil$.
> As we just break the array into L chunks and read it from slow memory.

> [!example] Matrix multiplication
> Suppose we have 2 $n \times n$ matrices and we want to multiply them.
> A simple algorithm to do this would take $W(n) = O(n^3)$.
> To read this all into memory we would need $Q(n,Z,L) = O(n^2/L)$.

Our goals then become two fold:

1. *Work optimality*: We want to minimize $W(n)$ (achieve work-optimality).

2. *High computational intensity*: We want to maximise intensity:

$$
I(n,Z,L) = \frac{W(n)}{L \cdot Q(n,Z,L)} \mbox{ ops / word }
$$

To know how to balance these we need to know more about the system we are working on.
Suppose one operation takes $\tau$ time/op - so the compute time for our algorithm is $T_{comp} := \tau W(n)$.
Next suppose we take $\alpha$ time/word transfer time - so the transfer time for our algorithm is $T_{mem} := \alpha L Q(n,Z,L)$.
If we can perfectly overlap these the overall run time would be $T \geq \max(T_{comp}, T_{mem})$.
We can reformulate this in terms of the idealised run time $T_{comp}$:

$$
\begin{align*}
T & \geq \max(T_{comp}, T_{mem}) \\
& \geq \tau W(n) \cdot \max \left ( 1, \frac{ \alpha / \tau }{W / (L Q(n,Z,L))} \right ) \\
& \geq \tau W(n) \cdot \max \left ( 1, \frac{ B / I(n, Z, L) } \right )\\
\end{align*}
$$

In this we defined a new term $B := \alpha / \tau$ ops/word, what we will call the 'machine balance'.
It is measured in the number of operations the CPU can do per word transferred from the slow to fast memory.
This balance then effects how much we want to prioritise the intensity, as we will see later.

There is a second measure of performance called the 'normalised performance' of the algorithm.
Let $W_{\ast}$ be the best possible work time in the 'pure model' where we don't have any memory considerations.
Then the normalised performance is:

$$
R := \frac{\tau W_{\ast}}{T} \in (0,1]
$$

This is really saying, how bad is the memory model algorithm in comparison to what is best if memory wasn't an issue - ratios close to 1 are good.
Using what we have above we can get a bound for this:

$$
R := \frac{\tau W_{\ast}}{\max(T_{comp}, T_{mem})} \leq \frac{W_{\ast}(n)}{W(n)} \cdot \min \left ( 1, \frac{I(n,Z,L)}{B} \right )
$$

Notice here that the intensity only effects the ratio when $I(n,Z,L) < B$.
This gives us our tradeoff between improving $W(n)$ and $I(n,Z,L)$.
For example, if $I(n,Z,L) > B$ there is no point increasing it at the expense of $W(n)$ because it will not improve our normalised performance.

> [!example] Conventional matrix multiplication
> Suppose we use the following pseudocode for matrix multiplication:
> ```
> for i = 0 to n-1:
>   // read A[i,:]
>   for j = 0 to n-1:
>     // read C[i,j], B[:,j]
>     for k=0 to n-1:
>       C[i,j] += A[i,k] * B[k,j]
>     // store C[i,j]
> ```
> Also assume $L = 1$ and $Z = 2n + o(1)$.
> Here we have $W(n) = O(n^3)$.
> The transfer complexity is $Q(n) = O(n^2) + O(n^3) = O(n^3)$ with the first component coming from reading $A$ and the second from reading $B$ and $C$.
> Therefore we get intensity $I(n) = O(n^3) / O(n^3) = O(1)$.

Though this is a bit sad, as we are having to transfer $O(n^3)$ words when there is only really $O(n^2)$ data.
Can we do better?

Let's say we have some $b \vert n$ then we can rewrite
$$
c_{i,j} = \sum_{k=0}^{n-1} a_{i,k} b_{k,j} = \sum_{l=0}^{n/b - 1} \sum_{k=0}^{b-1} a_{i, lb + k} b_{lb + k, j}.
$$
This means we can compute matrix multiplication in blocks.
Let $M_{i,j}$ be the $b \times b$ sub-block of $M$ with the top-left corner being $i,j$.
Then using the above we can write:
$$
C_{i,j} = \sum_{l=0}^{n/b - 1} A_{i,lb} B_{lb,j}
$$

> [!example] Block matrix multiplication
> Suppose we have $b \vert n$ like above with $L=1$, $n \vert Z$ with $Z = 3b^2 + O(1)$.
> Let's use the following pseudocode for matrix multiplication:
> ```
> for i = 0 to n-1 by b:
>   for j = 0 to n-1 by b:
>     // let C_{i,j} be the b x b block.
>     for k=0 to n-1 by b:
>       // read A_{i,k}, B_{k,j}
>       C_{i,j} += A_{i,k} * B_{k,j}
>     // store C_{i,j}
> ```
> This has the same computational complexity $W(n) = \Theta(n^3)$.
> The transfer complexity however is $Q(n,Z) = \Theta(b^2 \cdot n^3/b^3) = \Theta(n^3/b)$.
> We read $b^2$ blocks $(n/b)^3$ times for each of A and B.
> This provides intensity $I(n,Z) = \Theta(n^3) / \Theta(n^3/b) = \Theta(b) = \Theta(\sqrt{Z})$.

Here notice that $b$ really depends on the size of the $Z$ ($b = \sqrt{Z/3}$) - we can pick it to be optimal for this particular architecture.
Therefore we can optimize our algorithms for the architecture we are running on.

> [!question] Doubling machine balance
> Suppose $B$ the machine balance doubles, if we are using the block matrix multiplication - how much should $Z$ change to keep the same performance?
> The machine balance doubling means that we need to do twice the number of operations for each word transferred to be optimal.
> This can be solved by looking at:
> $$
> R \leq \frac{W_{\ast}(n)}{W(n)} \cdot \min \left ( 1, \frac{I(n,Z,L)}{B} \right )
> $$
> For $R$ to stay the same we need $\frac{I(n,Z,L)}{B}$ to stay the same i.e.
> $$
> \frac{\sqrt{Z}}{B} = \frac{\sqrt{Z'}}{2B}
> $$
> This gives us we need $Z' = 4Z$, i.e. the size of the fast memory to increase by a factor of 4!

# Summary

Whilst this memory model is over-simplified in comparison to real hardware, it sets out the concepts that will be used elsewhere.
