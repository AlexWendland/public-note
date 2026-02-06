---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-02-06'
date_checked:
draft: true
last_edited: '2026-02-06'
tags:
  - OMSCS
title: Week 5 - Scans and list ranking
type: lecture
week: 5
---

In this lecture we will look at how to parallelise algorithms that use linked lists.
They are notoriously hard to parallelise as we just have a single linked list with the head pointer.

# Scan

Given a operation like sum, product, max a scan takes a sequence and returns a new one where that operation is performed on the entries up to that value.

> [!definition] Scan
> Given a sequence $A = \{a_i\}_{i=0}^{n-1}$ and an operation $\bigoplus$ we define the scan to be $S = \{s_i\}_{i=0}^{n-1}$ as $s_i = \bigoplus_{j=0}^i a_j$.

For example using add the 'add-scan' of $A = \{1,2,3,4\}$ is $S = \{1,3,6,10\}$.
This can be computed sequentially as you would expect.

``` pseudocode
seq_scan(A[0,n-1], op):
  B = copy(A)
  for i in [1,n-1]:
    B[i] = op(B[i-1], B[i])
  return B
```

This has $W(n) = O(n)$ work and $D(n) = O(n)$ span.
We cannot replace for by par-for here as $B[i]$ depends on $B[i-1]$ being computed.

Lets assume our operation is associative, then we can divide and conquer the task by first applying it to pairs of elements.
Then if we scan the sub-problem of half the size we get the even solutions.
With the odd solutions now just being the even solutions plus the odd elements of our original list.

``` pseudocode
par_scan(A[0,n-1], op):
  if n = 1 then return A
  B = copy(A)
  let I_o[1:n/2] be the odd indices of A
  let I_e[1:n/2] be the even indices of A
  B[I_e] <- Op(B[I_e], B[I_o])
  B[I_e] <- par_scan(B[I_e], op)
  B[I_o] <- Op(B[I_e[2:]], B[I_o[2:]])
  return B
```

> [!note] Implicit par-for
> Vector notation here like `B[I_e] <- Op(B[I_e], B[I_o])` is an implicit par-for on a list of size n/2.
> Par-for loops have $W(n) = n$ but span $D(n) = \log(n)$.

To analyse the work lets set up our recurrence relationship:

$$
W(n) = \begin{cases} 0 & \text{if } n = 1\\
(n/2 + n/2 - 1) + W(n/2) & \text{otherwise} \end{cases}
$$

By case 3 of [Masters' theorem](../../notes/masters_theorem.md) gives us $W(n) = O(n)$.
Though notice here that if you pull it all through $W(n) = n-1 + n/2-1 + \ldots \approx 2n$ which means we are actually doing twice as much work here in comparison to the serial algorithm.

Lets look at the span next:

$$
B(n) = \begin{cases} 1 & \text{if } n = 1\\
B(n/2) + \log(n/2) & \text{otherwise} \end{cases}
$$

Which if we apply case 2 of [Masters' theorem](../../notes/masters_theorem.md) gives us $B(n) = n^{\log_2(1)} \log^2(n) = \log^2(n)$.

# Parallelising quicksort

[Quicksort](../../notes/quick_sort.md) uses a pivot to sort elements, where we partition the elements into a set that are less than or great than the pivot then apply recursion.
This can naturally be parallelised by branching out the recursion.

```
quicksort(A[0,n-1]):
  if n = 1 then return A
  pivot = random(A)
  A_L <- A[A <= pivot]
  A_R <- A[A > pivot]
  A_L <- spawn quicksort(A_L)
  A_R <- quicksort(A_R)
  sync
  return append(A_L, A_R)
```

Though right now the creation of $A_L$ and $A_R$ aren't parallelised.
We can compute the boolean array $A <= pivot$ or $A > pivot$ in parallel but we can't write the new arrays $A_L$ and $A_R$ in parallel as we need to allocate the correct amount of space and increment the index as we write the new elements.

Once we have the boolean array we can do an add-scan in parallel to get an array whos last element is the size of the output array.
For elements that need to be moved the add-scan array's value at that index is the position on the output array for that element.

> [!example] Quicksort step
> Suppose we have the array:
> ```
> A                = [3,1,4,1,5,9,2,6,5,3,5,9]
> A <= 3           = [1,1,0,1,0,0,1,0,0,1,0,0]
> add-scan(A <= 3) = [1,2,2,3,3,3,4,4,4,5,5,5]
>
> Output array:    = [3,1,1,2,3]
> ```
> Here if we assume 1 indexing, then if `A[i]` needs to be moved into the output its position is `add-scan(A <= 3)[i]`. 

This means we can parallelise the allocation step.

```
get_comparison(A[0,n-1], pivot, comp):
  F[0,n-1] <- comp(A[:], pivot)  # Can be done in parallel
  K[:] <- scan(F[:], +)
  define O[1:K[n-1]]
  par-for i \in [0,n-1]:
    if F[i] == 1 then O[K[i]] = A[i]
  return L
```

In fact this idea is commonly used so we introduce a new function for it.

```
gather_if(A[0,n-1], F[0,n-1]):
  K <- scan(F[:], +)
  define O[1:K[n-1]]
  par-for i \in [0,n-1]:
    if F[i] == 1 then O[K[i]] = A[i]
  return O
```

Which is sometimes abbreviated to $A[F[:]]$ or in the case of quicksort something like $A[A <= pivot]$.
This has $W(n) = O(n)$ but span of $D(n) = O(\log^2(n))$ (coming from the scan operation which dominates the parfor).

# Segmented scans

Suppose instead of running a full scan over the whole list, we instead only wanted to run it on sublists.
Here we are provided $A[0,n-1]$ and $F[0,n-1]$ a boolean array that indicates the start indexes of all the sublists.
If we did this serially we might write something like:

``` pseudocode
segmented_scan(A[0,n-1], F[0,n-1], op):
  B = copy(A)
  for i in [1,n-1]:
    if not F[i] then
      B[i] = op(B[i-1], B[i])
  return B
```

This is close to being a scan but we skip each step which the boolean flag.
However, we can actually solve this by using a scan with a novel new operation $op^{\ast}$.
Let $X = A \times F$ be the array with 2 components.
Then define

```
op^{\ast}((a_l,f_l), (a_r,f_r)):
  if not f_r then
    return (op(a_l, a_r), f_l or f_r)
  return (a_r, f_r)
```

We can show this operation is associative by considering what happens if each position has a negative flag.
Therefore we can now use this new operation to solve segmented scan deferring back to the old scan implementation.

``` pseudocode
segmented_scan(A[0,n-1], F[0,n-1], op):
  X = A \times F
  X <- scan(X, op^{\ast})
  return left(X)
```

# List ranking

> [!definition] List ranking
> Given a single linked list, for each node calculate the distance that node is from the head.

> [!example] List ranking
> See the below worked example.
> ```
> A       = [1,6,1,8,0,3,3,9,8,8,7 ,5 ]
> rank(A) = [0,1,2,3,4,5,6,7,8,9,10,11]
> ```

**Connection to scans**: List ranking is equivalent to computing an add-scan over the sequence `[0,1,1,1,...,1]` along the linked list. If we had random access (arrays), this would be trivially parallelizable using our parallel scan algorithm.

Serially we can do the dumb thing of walking the list and indexing the elements as we went along.
We can also use a scan to solve this issue by creating an auxiliary list with 0 in the first element and 1 in the rest and doing a add-scan on that.
However, the real issue with parallelising this problem is the data structure itself as we have no random access.
So can we introduce another one that will make it easier?

## Array pool

Suppose we have a linked list of size $n$ and we randomly allocate indices to each element.
Then an array pool consists of two arrays of size $m > n$:

- Values: An array containing the value of the linked list given this index.

- Next: An array containing the index of the next element from this index.

> [!note] Creating the array pool
> Building an array pool from a linked list requires at least one O(n) sequential traversal to walk the list and populate the arrays.
> This upfront sequential cost is worthwhile when:
> 1. **Multiple operations**: The conversion cost is amortized across many parallel operations on the same structure
> 2. **Pointer jumping**: We can parallelize even the conversion itself using pointer jumping (the technique shown below), though this trades work efficiency (O(n log n) work) for parallelism (O(log² n) span)
> 3. **Data structure choice**: In practice, if you need parallelism, start with array-based structures. The real lesson here is understanding *why* linked lists are fundamentally problematic for parallel algorithms.

> [!example] Array pool
> Suppose we have the random index assignment below:
> ```
> A     = [1 ,6,1,8,0 ,3,3,9,8,8,7,5]
> index = [11,4,9,7,12,8,0,1,2,5,6,3]
> ```
> Then we would get the array pool as below:
> ```
> index  = [0,1,2,3,4,5,6,7 ,8,9,10,11,12,13]
> values = [3,9,8,5,6,8,7,8 ,3,1,  ,1 ,0 ,  ]
> next   = [1,2,5, ,9,6,3,12,0,7,  ,4 ,8 ,  ]
> ```
> Where the starting index is 12.

## Jump

Now we have the array pool we can use these indices more liberally.

Now to parallelise the algorithm we need a way to split the problem into two.
To do this we introduce a new operation 'jump' intuitively this double the index shift of next where $jump[i] = next[next[i]]$.

> [!example] Jump
> Using the example above we get:
> ```
> index  = [0,1,2,3,4,5,6,7 ,8,9 ,10,11,12,13]
> values = [3,9,8,5,6,8,7,8 ,3,1 ,  ,1 ,0 ,  ]
> next   = [1,2,5, ,9,6,3,12,0,7 ,  ,4 ,8 ,  ]
> jump   = [2,5,6, ,7,3, ,8 ,1,12,  ,9 ,0 ,  ]
> ```
> Where we now have two starting indexes 12 and 5.

The creation of the jump list can be parallelised as to define it for $i$ we only need the values of $next$.

```
jump(N_{in}[0:n-1], N_{out}[0:n-1]):
  par-for i \in [0,n-1]:
    N_{out}[i] = N_{in}[N_{in}[i]] if N_{in}[i] != null else null
```

## Parallelising list ranking

Now we know the solution of the list rank is the same as performing a scan on the list $0, 1, 1, \ldots$.
If we use the `jump` operator from before we can cut the scan down to smaller lists.
However, if we do this we need to 'push' values along from the base as we jump.
As the gap gets longer we need to reflect that in the values we are scanning along.

> [!example] Parallelising list ranking
> Using the example above we get:
> ```
> index  = [0,1,2,3 ,4,5,6 ,7 ,8,9,10,11,12,13]
> values = [3,9,8,5 ,6,8,7 ,8 ,3,1,  ,1 ,0 ,  ]
> next   = [1,2,5,  ,9,6,3 ,12,0,7,  ,4 ,8 ,  ]
> rank_1 = [1,1,1,1 ,1,1,1 ,1 ,1,1,  ,0 ,1 ,  ]
> ---
> jump_2 = [2,5,6,  ,7,3,  ,8 ,1,1,  ,9 ,0 ,  ]
> rank_2 = [2,2,2,2 ,1,2,2 ,2 ,2,2,  ,0 ,2 ,  ]
> ---
> jump_4 = [6,3, ,  ,8, ,  ,1 ,5,0,  ,12,2 ,  ]
> rank_4 = [4,4,4,4 ,1,4,4 ,3 ,4,2,  ,0 ,4 ,  ]
> ---
> jump_8 = [ , , ,  ,5, ,  ,3 , ,6,  ,0 ,  ,  ]
> rank_8 = [6,7,8,8 ,1,8,8 ,3 ,5,2,  ,0 ,4 ,  ]
> ---
> jump_16 = [ , , ,  , , ,  ,  , , ,  ,  ,  ,  ]
> rank_16 = [6,7,8,11,1,9,10,3 ,5,2,  ,0 ,4 ,  ]
> ```

Which can be done in parallel similarly to the jump operation.

``` pseudocode
update_rank(rank_{in}[0,n-1], rank_{out}[0,n-1], jump[0:n-1]):
  par-for i \in [0,n-1]:
    if jump[i] != null then
      rank_{out}[jump[i]] = rank_in[i] + rank_in[jump[i]]
```

This now gives us our whole algorithm for computing the list ranking.

``` pseudocode
list_rank_parallel(value[0,n-1], next[0,n-1], head):
  let rank_in[0:n-1] = 1, rank_out[0:n-1] = 1
  let jump_in[0:n-1] = copy(next), jump_out[0:n-1] = copy(next)
  let rank_in[head] = rank_out[head] = 0
  for _ in [0,log_2(n)]:
    update_rank(rank_in, rank_out, jump_in)
    jump(jump_in, jump_out)
    swap(rank_in, rank_out), swap(jump_in, jump_out)
  return rank_in
```

Then to compute the work/span we do $log_2(n)$ operations involving jump/update_rank which also takes $n$ operations and has span $\log_2(n)$ giving us $W(n) = n \log_2(n)$ and $D(n) = \log_2^2(n)$.
This means that we are not work optimal with the naive algorithm only having $W(n) = n$ but for this we gain parallelism.

> [!note] Work-span trade-off
> The parallel list ranking algorithm demonstrates a fundamental trade-off in parallel computing:
> - **Sequential**: O(n) work, O(n) span (no parallelism)
> - **Parallel (array pool + pointer jumping)**: O(n log n) work, O(log² n) span
>
> We sacrifice work efficiency (doing more total operations) to achieve parallelism. This trade-off is worthwhile when:
> 1. You have sufficient processors to exploit the parallelism
> 2. The time savings from reduced span outweigh the extra work
> 3. The linked list structure is unavoidable (otherwise, just use arrays from the start!)
>
> In practice, this teaches us that **linked lists and parallelism don't mix well** - if you control the data structure, choose arrays for parallel algorithms.
