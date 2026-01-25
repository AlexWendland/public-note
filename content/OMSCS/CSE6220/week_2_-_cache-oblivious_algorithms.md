---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-01-22'
date_checked: '2026-01-25'
draft: false
last_edited: 2026-01-23
tags:
  - OMSCS
title: Week 2 - Cache-Oblivious Algorithms
type: lecture
week: 2
---

> [!note] Optional reading
> This lecture is optional reading in my course and will not be examinable.

In the example of binary search, we saw we could optimise reads by using a [B-tree](../../notes/b_tree.md) to store the keys.
However, we would need to optimise the tree for the underlying cache size - therefore require specialisation for the hardware.
This may not be possible in cloud systems so it would be good to have an algorithm that was optimised without needing specialisation to the hardware.
This is what is covered in this lecture.

# Managed caches

There are many 'managed' memory systems such as the caches in your CPU.
Therefore, to build a cache-oblivious algorithm we need to have a model for how these work.

## Ideal caches

An ideal cache has two assumptions:

- It is fully associative: This means it can utilise the whole address space.

- It has Optimal replacement: When full, it can look ahead in the code and throw out the currently stored address that is used last in the future.

When working with this model we have:

$$
Q_{OPT}(n, Z, L) = \text{number of misses} + \text{store-evictions}.
$$

This model might seem unrealistic given its look into the future - but this helps us with proving bounds.
Though, it is not as unrealistic as you might fear.

## LRU cache bounds

The LRU (least recently used) cache drops the elements that are least recently used.
This can cause sub-optimal behaviour where we drop something we are going to need next - but it is easy to implement in software.
How far away is the optimal replacement from LRU?

> [!lemma] Lemma
> $Q_{LRU}(n, Z, L) \leq 2 \cdot Q_{OPT}\left (n, \frac{Z}{2}, L \right )$

This is saying that the number of replacements for an LRU cache is at most twice the number of replacements of the optimal policy with half the size of the cache.
This is really saying that asymptotically (what mathematicians really care about) the optimal and LRU designs are similar.

> [!lemma] Corollary "Regularity condition"
> If $Q_{OPT}(n, Z, L) = O(Q_{OPT}(n, 2Z, L))$ then $Q_{LRU}(n,Z,L) = O(Q_{OPT}(n,Z,L))$.

The corollary follows from the lemma fairly simply.

$$
\begin{align*}
Q_{LRU}(n,Z,L) &\leq 2 Q_{OPT} \left ( n, \frac{Z}{2}, L \right ) & \mbox{from the lemma}\\
& \leq O(Q_{OPT}(n,Z,L)) & \mbox{from the assumption}
\end{align*}
$$

As $Q$ is always positive this gives us the required $Q_{LRU}(n,Z,L) = O(Q_{OPT}(n,Z, L))$.

> [!example] Matrix multiply
> Suppose you have an algorithm for matrix multiplication that has the following accesses:
> $$
> Q_{OPT}(n,Z,L) = O\left ( \frac{n^3}{L\sqrt{Z}} \right )
> $$
> On a machine with a line size $L=1$ then we have
> $$
> Q_{OPT}(n,2Z,L=1) = O \left ( \frac{n^3}{\sqrt{2}\sqrt{Z}} \right ) = O(Q_{OPT}(n,Z,L=1)).
> $$
> So this algorithm is regular and the LRU would work as well as the optimal policy asymptotically.

## Tall cache

In the block matrix multiply algorithm, explored in the first lecture, we require block sizes $3 \cdot B^2 \leq Z$ so take $B = O(\sqrt{Z})$.
However, in this case what we really need is at least $3B$ cache lines in $Z$ that can take all the columns/rows of the matrix.
(Reminder: If we have cache lines of size $L$ and a cache of size $Z$ then we have $Z/L$ cache lines.)

> [!definition] Tall cache
> A cache is said to be tall if the number of cache lines is at least the size of the cache lines. I.e. $Z/L \geq  L$.

# Matrix multiply

As discussed previously, the 'block' matrix multiply algorithm relies on picking the parameter $B$ to fit in the fast memory.
Can we rewrite this algorithm to be cache-oblivious?

Let's assume we have $A, B$ $n \times n$ matrices and we want to find $C = A \cdot B$ with $n = 2^k$ (this makes the maths easier but doesn't really matter as we can always embed other matrices into one of this size).
Then let's tackle the problem using divide and conquer by breaking matrices into 4 quarters.
For a matrix $M$ of size $2^j \times 2^j$, let $M_{1,1}$ be the top left, $M_{1,2}$ be the top right, $M_{2,1}$ be the bottom left, and $M_{2,2}$ be the bottom right $2^{j-1} \times 2^{j-1}$ submatrix.
Then our recursive algorithm is as follows:

```
mm(n, A, B, C)
1. if n = 1:
2.   C = A \cdot B
3. else:
4. for i, j, k \in {1,2}:
5.   mm(n/2, A_{i,k}, B_{k,j}, C_{i,j})
```

We can find out the run time $R(n)$ by using the recursive relationship:

$$
R(n) = \begin{cases} 2 & \mbox{if } n = 1\\ 8R(n/2) & \mbox{otherwise} \end{cases}
$$

Solving this gives us $R(n) = 2n^3$ which is the run time.

Next, lets try to calculate cache-misses.
Lets assume we have a tall cache.
Just like the run time, we can define a recurrence relationship for the number of cache misses $Q(n,Z,L)$.
The base case is determined by the size of your cache.
Similarly to the block matrix once we have a $n_L$ such that $3n_L^2 \leq Z$ then we can fit all the rest of the divide and conquer algorithm into memory.
We say that $n_L \leq f \cdot \sqrt{Z}$ where $0 < f < 1$.

> [!warning] I don't understand this
> In the case that $n \leq f \cdot \sqrt{Z}$ the lecturer says the number of cache misses is $O\left ( \frac{n^2}{L} \right )$.
> I think this is saying that any cache miss would be proportional to the number of elements in the matrix, modulo the line size - but I am not 100% sure.

Using this we then define our recurrence relationship:

$$
Q(n,Z,L) = \begin{cases} O\left ( \frac{n^2}{L} \right ) & \mbox{if } n \leq f \sqrt{Z}\\ 8Q(n/2,Z,L) + O(1) & \mbox{otherwise} \end{cases}
$$

Solving this gives us

$$
Q(n,Z,L) = O\left ( \frac{n^3}{L\sqrt{Z}} \right ).
$$

Which is the optimum non-Strassen algorithm.

Note here, there was no fine tuning in this algorithm for the machine we work on.
This means it is Cache-Oblivious.

# Binary Search

Previously we saw that using a [B-tree](../../notes/b_tree.md) to store the keys can give us a cache-aware algorithm.
However, we still needed to finetune the B-tree to the hardware.
Can we make this more cache-oblivious?

The binary search algorithm is already cache-oblivious but we didn't utilise the cache well due to the structure of the data.
Just like with the B-tree, lets structure the data better again!
We can use a binary search tree to assist us in binary search.
Traditionally binary trees are laid out similarly to a heap.
This is where using 0-indexed positions:

- Parent of node at index $i$: $\lfloor (i-1)/2 \rfloor$

- Left child of node at index $i$: $2i+1$

- Right child of node at index $i$: $2i+2$

However, this layout does not help us because children and parents are far away from one another.

> [!definition] Van Emde Boas (tree) layout
> Let $T$ be a complete binary tree of depth $d$.
> Cut the tree in half at layer $\lfloor d/2 \rfloor$, this leaves one full tree at the top and $2^{\lfloor d/2 \rfloor}$ sub-trees in the bottom half.
> Then store the top tree (using the same Van Emde Boas layout) in the first part of the array, and the $2^{\lfloor d/2 \rfloor}$ subtrees one after one another after that.

This layout means that once a sub-tree is of size $\leq L$ it will fit into a single cache line.
Applying this to a search tree means once we have $L$ searches left we will have all the data we need in a single cache line.
Though as this is just a data structure on how we store the tree - it doesn't need to know $L$ before hand to get this advantage, whereas a B-tree does.

Therefore applying binary search to a binary search tree in Van Emde Boas layout is a cache-oblivious search algorithm with:

Operations: $O(\log_2(n))$ (same as binary search).

Cache-misses: $O(\log_2(n) - \log_2(L)) = O \left ( \log \left ( \frac{n}{L}\right ) \right )$ - the optimum for this problem.

