---
aliases:
checked: false
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-01-21'
draft: true
last_edited: '2026-01-21'
tags:
  - OMSCS
title: Week 2 - I/O Avoiding Algorithms
type: lecture
week: 2
---

In this lecture, we will examine different classical algorithms and try to calcalculate their number of transfers in the Von Neumann model introduced in the previous lecture.

# Merge sort

[Merge sort](../../notes/merge_sort.md) divides the array into small chunks.
Then merges each of those chunks into one another to produce a sorted array.
This runs in $O(n \log n)$ time.
So there are two steps to this:

1. Sort the smaller chunks.

2. Merge the sorted chunks together.

Now think about our model which has $L$ sized cache lines, with a $Z$ fast byte cache.
When something is in fast memory we assume accesses take $O(1)$ time so here we can sort effectively.

Lets assume we have a array of length $n$.
As we want to use the fast cache to sort this - lets cut $n$ into $f \cdot Z$ sized chunks with $0 < f < 1$.
I.e. so we can fit a whole chunk into fast memory.

## Step 1: Sorting chunks

Therefore step 1 of merge sort consists of:

1. $n / f \cdot Z$ copies of a chunk into fast memory.

2. In memory sorting of these chunks each taking $O(fZ \log (fZ) )$ operations.

3. $n/ f \cdot Z$ copies of the sorted chunks back into slow memory.

Steps 1 and 2 together essentially copy the entire size $n$ array into fast memory and back - so takes $O(n/L)$ copies.
Step 2 takes $O(fZ \log (fZ))$ operations $n/fZ$ times, so $O(n \log (Z))$ operations in total (we drop $f$ here as it is constant).

In summary, step 1 of merge sort takes:

- Transfers: $O(n/L)$.

- Operations: $O( n \log(Z))$.

## Step 2: Merging chunks - classical merge sort

We now have $n/f \cdot Z$ sorted chunks.
In classical merge sort we take these chunks in sets of two and now do a sorted array merge.
That is we take the two sorted array and use pointers pointing to the top element compare them and place the larger one on the output array.
We keep iterating this on the sets of chunks until we are left with one sorted chunk.
This happens in $\log(n/fZ)$ rounds where the size of the chunks double each time.
(Obviously we are glossing over if $n/fZ$ isn't a power of 2 but this just makes the Maths slightly harder for no intuitive gain.)

Lets think about how we would do this in our model.
We are going to keep 3 $L$ sized arrays in fast memory.
The first two will consist of the two sorted chunks.
The third will be the output array.
If one of the first two chunks depletes we get the next $L$ sized chunk from slow memory to replace it.
If the third chunk fills up, we cache it down to the slow memory.

Therefore for each round we copy the whole $n$ sized data from slow to fast memory in the small chunks and back again in the combined chunks.
This takes $O(n/L)$ transfers.
Therefore we do a total of $O(n/L \log (n/Z) )$ transfers.

For each round and value in the array we do 1 comparison, so we do $O(n)$ operations each round.
Therefore we do a total of $O(n \log (n/Z))$ operations.

In summary, step 2 of merge sort takes:

- Transfers: $O(n/L \log (n/Z))$.

- Operations: $O(n \log (n/Z))$.

Combining this with step 1, classical merge sort takes:

- Transfers: $O(n/L + n/L \log(n/Z)) = O(n/L \log(n/Z) )$.

- Operations: $O(n \log(n/Z) + n \log (Z)) = O(n \log (n))$.

Can we do this in less transfers?

## Step 2: Merging chunks - better memory utilisation

Right now in step 2 we are only using $3 \cdot L$ amount of fast memory.
This presents an opportunity - if we can merge more chunks in one go we reduce the number of rounds.
Right now the number of rounds directly contributes to the number of transfers so this should improve the transfer efficiency.

Lets instead merge $k := \rfloor Z/L - 1 \rfloor$ chunks at a time.
This will give us space for all the chunks in fast memory and space for the output chunk.
This means we will have $O(\log_{Z/L}(n/Z))$ rounds (as there are n/Z root nodes of a Z/L-arry tree).

Then essentially the maths for transfers is all the same as before - each round we will transfer all $n$ of the arrays values into fast memory and back again.
So we do $O(n/L \log_{Z/L}(n/Z)$ transfers.

However, the k-way comparison in fast memory is now slightly more complex.
We could do a linear scan of the current minimum elements on all the $k$ lists - however this is inefficient.
Instead lets use a [Min-heap](../../notes/min-heap.md) this takes $O(k)$ to form and $O(\log_2(k))$ to do each comparison operation.
As dominating term is the $n$ comparison operations this takes us $O(n\log_2(Z/L))$ operations each round.
So we do $O(n \log_{Z/L}(n/Z) \log(Z/L)) = O(n \log(n/Z))$ operations in total.

In summary, step 2 of merge sort takes:

- Transfers: $O(n/L \log_{Z/L} (n/Z))$.

- Operations: $O(n \log (n/Z))$.

Combining this with step 1 this merge sort takes:

- Transfers: $O(n/L + n/L \log_{Z/L}(n/Z)) = O(n/L \left ( \log_{Z/L}(n/Z) + \log_{Z/L}(Z/L) \right ) ) = O(n/L \log_{Z/L} (n/L))$.

- Operations: $O(n \log(n/Z) + n \log (Z)) = O(n \log (n))$.

## Is this the best?

There are some information theoretic ways to actually confirm this is correct - however to be honest I don't really trust them.

# Binary search

In Binary search we are given a sorted array $A$ (of size $n$) and a value $v$.
We want to find the largest $i$ of $A$ such that $A[i] \leq v$.

The classical algorithm looks at the middle element $m := A[n/2]$ and compares that to $v$.
Using this it either looks to the left of this element if $v < m$ or to the right of $v$ if $m \leq v$.
It then recursively searches until it has narrowed it down to a single element.
This takes $O(\log n)$ operations.
We are interested in how many I/O operations this takes.

The simplistic answer would be $O(\log (n))$ operations.
However, when the region we are looking at is smaller that $L$ we can do all the reads on the same block.
This means we do $O(\log(n) - \log(L)) = O(\log(n/L))$ I/O reads.

## Is this the best?

Lets take an information theory approach.
We are trying to find $i$ an index that has $O(\log_2(n))$ bits to it.
Let $x(L)$ be the maximum number of 'bits' of $i$ we can learn for each $L$-sized read.
If we are reading $L$ keys then the most we could learn about the index $i$ would be $\log_2(L)$ bits.
Then in the best case we could solve this problem with $O(\log_2(n) / \log_2(L)) = O(\log_L(n))$ I/O reads.

This can be realised by using a [B-tree](../../notes/b_tree.md) to store the keys.
If we set the key size of the B-tree to be $L$ then we only need exactly the depth of the tree I/O reads which is $O(\log_L(n))$!


