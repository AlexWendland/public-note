---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-01-23'
date_checked: 2026-01-25
draft: false
last_edited: 2026-01-25
tags:
  - OMSCS
title: Week 4 - Comparison-based Sorting
type: lecture
week: 4
---

Comparison-based sorting is done using a 'comparator network' which looks like a circuit with two types of symmetric connections.

> [!definition] Comparison gate
> Positive gates look as below.
> ```
> a --| + | -- min(a,b)
>       |
> b --| + | -- max(a,b)
> ```
> Negative gates look as below.
> ```
> a --| - | -- max(a,b)
>       |
> b --| - | -- min(a,b)
> ```

We can use these comparison gates to build networks.
For example what is below sorts 3 numbers.

> [!example] Sorting 3 numbers
> ```
>            min(a,b)
> a -- | + | ------------------------------ | + | -- min(a,b,c)
>        |                                    |
>        |   max(a,b)       min(c,max(a,b))   |
> b -- | + | -------- | + | --------------- | + | -- median(a,b,c)
>                       |
>                       |   max(a,b,c)
> c ----------------- | + | ------------------------ max(a,b,c)
> ```

This example can be converted into a DAG by making every gate a vertex and wire an edge.

> [!example] Sorting 3 numbers DAG
> ```
> Start --> Sort(a,b) --> Sort(min(a,b),min(c,max(a,b)))
>   |              |          ^          |
>   |              v          |          v
>   + ----------> Sort(max(a,b),c) ---> end
> ```
> You can see here that this DAG has $W = 5$ and $D = 5$.

# Bitonic sequences

If monotonic sequences just increase in 1 direction, we define a bitonic sequence as one that increases in one direction and decreases in the other.

Informally, a bitonic sequence is one that either:
- Increases then decreases (like [1,3,5,4,2])
- Is a rotation of such a sequence (like [4,2,1,3,5])

The formal definition below captures this with modular arithmetic to handle rotations.

> [!definition] Bitonic sequence
> Suppose we have a finite sequence $A = \{a_i\}_{i=0}^{n-1}$, we call $A$ *bitonic* if there exists $k, j \in [0,n-1]$ such that:
>
> - $a_{k+i \pmod{n}} \leq a_{k+i+1 \pmod{n}}$ for all $0 \leq i < j$.
>
> - $a_{k+i \pmod{n}} \geq a_{k+i+1 \pmod{n}}$ for all $j \leq i < n$.
>
> Here the $k$ parameter allows for 'wrap arounds' whereas $j$ is the 'peak' element.

The reasons bitonic sequences are interesting is they are very easy to sort!
To prove this though, we will need a couple of lemmas.
Feel free to skip over the proofs if you want but the results will be used.

> [!lemma] Bitonic sub-sequences are bitonic
> Let $A = \{a_i\}_{i=0}^{n-1}$ be a bitonic sequence.
> Any subsequence $B = \{a_{\phi(x)}\}_{x=1}^{m-1}$ of $A$ is bitonic - for increasing $\phi: [0, \ldots, m-1] \rightarrow [0, \ldots, n-1]$.

As $A$ is bitonic, there exists $k, j \in [0,n-1]$ such that:

- $a_{k+i \pmod{n}} \leq a_{k+i+1 \pmod{n}}$ for all $0 \leq i < j$.

- $a_{k+i \pmod{n}} \geq a_{k+i+1 \pmod{n}}$ for all $j \leq i < n$.

Notice that $k$ and $j$ essentially partition $[0,n-1]$ into:

- An increasing set of indices $I = \{k + i \pmod{n} \vert 0 \leq i < j\}$.

- A decreasing set of indices $D = \{k + i \pmod{n} \vert j \leq i < n\}$.

We define similar sets of indices for $B$ by $I' = \phi^{-1}(I)$ and $D' = \phi^{-1}(D)$.
Therefore $B \vert_{I'}$ is a subsequence of $A \vert_I$ a rotated increasing subsequence.
Similarly $B \vert_{D'}$ is a subsequence of $B \vert_D$ a rotated decreasing subsequence.
This gives us that $B$ is bitonic by definition.

> [!warning] Lazy
> I should really prove these two definitions are equivalent - but it can be a bit fiddly at the boundary.

> [!lemma] Rotations of Bitonic sequences are Bitonic
> Let $A = \{a_i\}_{i=0}^{n-1}$ be a bitonic sequence, and $t \in [0,n-1]$.
> The sequence $B = \{a_{i+t \pmod{n}}\}_{i=0}^{n-1}$ is Bitonic.

As $A$ is bitonic, there exists $k, j \in [0,n-1]$ such that:

- $a_{k+i \pmod{n}} \leq a_{k+i+1 \pmod{n}}$ for all $0 \leq i < j$.

- $a_{k+i \pmod{n}} \geq a_{k+i+1 \pmod{n}}$ for all $j \leq i < n$.

Let $k' = k - t \pmod{n}$ and $j' = j$, and we will show $B$ is Bitonic.

- $b_{k'+i \pmod{n}} = a_{(k - t) + i + k \pmod{n}} \leq a_{(k-t) + i + 1 + k \pmod{n}} = b_{k'+i \pmod{n}}$ for all $0 \leq i < j' = j$.

- $b_{k'+i \pmod{n}} = a_{(k - t) + i + k \pmod{n}} \geq a_{(k-t) + i + 1 + k \pmod{n}} = b_{k'+i \pmod{n}}$ for all $j = j' \leq i < n$.

Thus giving us $B$ is Bitonic.

Combining the two lemmas above you can get the below result.

> [!lemma] Rotated sub-sequences of Bitonic sequences are Bitonic
> Let $A = \{a_i\}_{i=0}^{n-1}$ be a bitonic sequence.
> Suppose we have $\phi: [0, \ldots m-1] \rightarrow [0,n-1]$ which is a rotated increasing sequence.
> Then $B = \{a_{\phi(i)}\}_{i=0}^{m-1}$ is Bitonic.

Let $t = \phi(0)$, then we can rotate $A$ by $-t$ to get $A' = \{a_{i-t \pmod{n}}\}_{i=0}^{n-1}$.
Define $\phi': [0, m-1] \rightarrow [0,n-1]$ by $\phi'(x) = \phi(x) - t \pmod{n}$.
Then $\phi'$ is an increasing sequence - as we have $\phi'(0) = 0$ and $\phi$ was a rotation of an increasing sequence.
As $B$ can be realised as a subsequence of $A'$ using $\phi'$.
Then as $A'$ is Bitonic (rotation of a bitonic sequence is bitonic) and $B$ is a subsequence of $A'$ (subsequence of bitonic sequences are bitonic) this gives $B$ is Bitonic as desired.

# Bitonic split

From now on, we will assume $n = 2^p$ - for sequences that do not satisfy this we can just pad them out.

> [!definition] Bitonic split
> Suppose we have a bitonic sequence $A = \{a_i\}_{i=0}^{2^p-1}$ of length $2^p > 1$.
> We can then pair elements $a_{i}$ and $a_{i+2^{p-1}}$ up and sort them (in place) to make $B$ with $b_i = \min\{a_i, a_{i + 2^{p-1}}\}$ and $b_{i+2^{p-1}} = \max\{a_i, a_{i+2^{p-1}}\}$ for $0 \leq i < 2^{p-1}$.
> We claim that $B$ is two Bitonic sequences $L := \{b_i\}_{i=0}^{2^{p-1} - 1}$ and $U := \{b_{2^{p-1}+i}\}_{i=0}^{2^{p-1}-1}$, such that $l_i \leq u_j$ for all valid $i,j$.
> This is what we call a Bitonic split.

> [!example] Bitonic split
> We apply the Bitonic split on the length 8 sequence below.
> | index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> | ----- | --- | --- | --- | --- | --- | --- | --- |
> | a_i | 0 | 1 | 2 | 3 | 4 | 4 | 2 | 1 |
> | b_i | 0 | 1 | 2 | 1 | 4 | 4 | 2 | 3 |

We see below a pictorial example of the split.

![Bitonic split](../../../static/images/bitonic_split.png)

We need to prove the two facts about the split:

1. $l_i \leq u_j$ for all valid $i,j$.

2. The sequences $L$ and $U$ are bitonic.

> [!lemma] Bitonic splits sort
> Let $A$ be a sequence that has a Bitonic split into $B$ (with $L$ and $U$ as defined above).
> Then $l_i \leq u_j$ for all valid $i,j$.

Suppose this is not the case, and we have $l_x = \min\{a_{x}, a_{x+2^n}\}$ and $u_y = \max\{a_{y}, a_{y+2^n}\}$ where $u_y < l_x$.
Therefore $a_x, a_{x+2^n} < a_y, a_{y + 2^n}$.
Without loss of generality let $x < y$ and let $B$ be the sub-sequence of $A$ defined by $a_x, a_y, a_{x+2^n}, a_{y+2^n}$.
This sequence is not Bitonic as $a_x < a_y$ and $a_y > a_{x+2^n}$.
For $B$ to be bitonic with its peak at $a_y$, we would need the sequence to be decreasing after $a_y$, which would force $a_y > a_{x+2^n} > a_{y+2^n}$ (since $x < y$ means $a_{x+2^n}$ comes after $a_y$ in the sequence but before $a_{y+2^n}$).
However, we know $a_{y+2^n} > a_{x+2^n}$ by our contradiction assumption, so $B$ cannot be bitonic.
Therefore, no such $x$ and $y$ exist and we have the statement holding.

> [!lemma] Bitonic splits sub-sequences are bitonic
> Let $A$ be a sequence that has a Bitonic split into $B$ (with $L$ and $U$ as defined above).
> Then $L$ and $U$ are both bitonic.

The proof structure will show that $L$ and $U$ are just rotated sub-sequences of $A$.
Therefore by the lemmas above we have $L$ and $U$ are bitonic.
Intuitively, you can see this $L \leq U$ therefore we are just taking a pyramid and cutting it in half, the half above the line becomes $U$ and the part below becomes $L$.

Without loss of generality I will show $L$ is a rotated sub-sequence of $A$ (the same proof holds for $U$).
Let $\phi: [0, \ldots, 2^{n-1} - 1] \rightarrow [0, \ldots, 2^n - 1]$ be defined by
$$
\phi(i) = \begin{cases} \argmin_{x \in \{i, i+2^{n-1}\}} a_{x} & \mbox{if } a_x \not = a_{x+2^{n-1}}\\
i & \mbox{if } a_x = a_{x+2^{n-1}} \mbox{ and } \phi(j) = j \forall 0 \leq j < i\\
i + 2^{n-1} & \mbox{otherwise}
\end{cases}
$$
This function maps each index in $L$ to its corresponding index in $A$, choosing the smaller element from each pair (with tie-breaking rules to ensure $\phi$ is increasing).
I am going to assume $\phi(0) = 0$, if not - we can just rotate the whole of $A$ by $2^{n-1}$ (therefore I just need to show $\phi$ is increasing).
Suppose $\phi$ is not increasing, i.e. there exists $0 < x < y < 2^{n-1}$ such that $\phi(x) = x + 2^{n-1}$ and $\phi(y) = y$.

As $\phi(x) \not = x$ we have $a_x > a_{x+2^{n-1}}$ and $a_y < a_{y + 2^{n-1}}$.
Therefore either $a_0, a_y < a_x, a_{y+2^{n-1}}$ or $a_{2^{n-1}}, a_{y+ 2^{n-1}} > a_{x+2^{n-1}}, a_y$ - without loss of generality lets assume the first case is true.
Take the sub-sequence of $A$ defined by $a_0, a_x, a_y, a_{y + 2^{n-1}}$.
Note here that $a_0 < a_x$ and $a_x > a_y$ this implies we need $a_{y + 2^{n-1}} < a_y$ or $a_{y + 2^{n-1}} < a_0$ - however, by construction this is not true.
Therefore $\phi$ is increasing.

As $\phi$ is increasing we have $L$ is a sub-sequence of $A$ and therefore bitonic as required.

# Bitonic splits using gates

We can represent the bitonic split using a circuit with $2^{n-1}$ gates.
If our input sequence $A$ is the $2^{n}$ inputs to a circuit we just need to connect input $i$ to $i+2^{n-1}$ with a plus gate to get a split.

> [!example] Bitonic splits using gates
> Consider the below circuit that performs a bitonic split on 8 inputs.
> ```
> a0 -- | + | ----------------------- b0 = min(a0,a4)
>         |
> a1 ---- | -- | + | ---------------- b1 = min(a1,a5)
>         |      |
> a2 ---- | ---- | -- | + | --------- b2 = min(a2,a6)
>         |      |      |
> a3 ---- | ---- | ---- | -- | + | -- b3 = min(a3, a7)
>         |      |      |      |
> a4 -- | + | -- | ---- | ---- | ---- b4 = max(a0, a4)
>                |      |      |
> a5 --------- | + | -- | ---- | ---- b5 = max(a1, a5)
>                       |      |
> a6 ---------------- | + | -- | ---- b6 = max(a2, a6)
>                              |
> a7 ----------------------- | + | -- b7 = max(a3, a7)
> ```

This could also be represented by the pseudocode:

```
bitonicSplit(A[0,2^n - 1])
1. parfor i in [0,2^{n-1} - 1]
2.   a = A[i]
3.   b = A[i + 2^{n-1}]
4.   A[i] = min(a, b)
5.   A[i + 2^{n-1}] = max(a, b)
```

Whilst both represent the same algorithm the DAG we get from the circuit actually has different properties from the pseudocode.

> [!example] Bitonic splits using gates DAG
> The DAG below represents the bitonic split using gates.
> ```
>  +---- Sort(a0,a4) ----+
>  |                     |
>  | +-- Sort(a1,a5) --+ |
>  | |                 | |
> Start                end
>  | |                 | |
>  | +-- Sort(a2,a6) --+ |
>  |                     |
>  +---- Sort(a3,a7) ----+
> ```

The one from the gates has $D(2^n) = 1$ whereas the pseudocode has $D(2^n) = n$.

# Bitonic merge

In summary, we have a bitonic split $A$ into $B$ which partitions $B$ into two bitonic subsequences $L$ and $U$ where $l_i \leq u_j$ for all valid $i,j$.
The bitonic split thus gives us a divide and conquer algorithm to sort any bitonic sequence by recursively apply the split.

> [!definition] Bitonic merge
> Suppose we have a bitonic sequence $A = \{a_i\}_{i=0}^{2^p-1}$ of length $2^p > 1$.
> A bitonic merge sorts $A$ in place using the below code.
> ```
> BitonicMerge(A[0,2^n - 1])
> 1. if n = 1, return
> 2. BitonicSplit(A) // Changes A inplace
> 3. spawn BitonicMerge(A[0,2^{n-1} - 1])
> 4. BitonicMerge(A[2^{n-1},2^n - 1])
> 5. sync
> ```

Here as we are just iteratively applying bitonic splits, we can also represent the BitonicMerge as a circuit.

# Bitonic sort

BitonicMerge gives us a way to sort a bitonic sequence.
To create a generic sorting algorithm we need to be able to convert any sequence into being bitonic.
Though, we can fall back on our divide and conquer approach from before - we can consider each 2 elements next to one another a bitonic sequence we can call BitonicMerge on.
If we alternate the 'direction' of that Merge we generate a 4 long bitonic sequence.
Specifically, if we sort one pair in ascending order and the adjacent pair in descending order, the concatenated result is bitonic (it goes up then down).
We can recursively apply this pattern: merging two ascending-sorted sequences and two descending-sorted sequences in alternating directions produces a larger bitonic sequence.
This gives us our bitonic sort.

``` pseudocode
BitonicSplit(A[0,2^n - 1], direction)
1. parfor i in [0,2^{n-1} - 1]
2.   a = A[i]
3.   b = A[i + 2^{n-1}]
4.   A[i] = min(a, b) if direction = 1 else max(a,b)
5.   A[i + 2^{n-1}] = max(a, b) if direction = 1 else min(a,b)

BitonicMerge(A[0,2^n - 1], direction)
1. if n = 1, return
2. BitonicSplit(A, direction) // Changes A inplace
3. spawn BitonicMerge(A[0,2^{n-1} - 1], direction)
4. BitonicMerge(A[2^{n-1},2^n - 1], direction)
5. sync

BitonicSort(A[0,2^n - 1], direction = 1)
1. if n > 1:
2.   spawn BitonicSort(A[0,2^{n-1} - 1], direction)
3.   BitonicSort(A[2^{n-1},2^n - 1], -direction)
4. sync
5. BitonicMerge(A, direction)
```

When considering the DAG generated from the circuit, Bitonic sort has interesting properties:

- Work: $W(n) = O(n \log^2(n))$.

- Span: $D(n) = O(\log^2(n))$.

Whilst the above algorithm is not optimal in terms of work (the best sorting algorithms work in $O(n\log(n))$ - its Span is lower than most algorithms at $O(\log^2(n))$ making it easy to parallelise.
