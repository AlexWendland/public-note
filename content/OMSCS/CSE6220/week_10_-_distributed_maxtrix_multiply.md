---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-04-02'
date_checked:
draft: true
last_edited: '2026-04-02'
tags:
  - OMSCS
title: Week 10 - Distributed Maxtrix Multiply
type: lecture
week: 10
---

In this lecture we are looking to optimise the matrix multiply algorithm.
In this lecture this will be, given $A, B, C$ 3 matrices of dimension $m \times k$, $k \times n$ and $m \times n$ calculate $C = C + A \cdot B$.
This means that for a given $i, j$ we need to calculate:

$$
C_{i,j} = C_{i,j} + \sum_{l=1}^k a_{i,l} b_{l,j}
$$

The serial implementation is therefore:

```
for i = 1 to m do:
  for j = 1 to n do:
    for l = 1 to k do:
      C[i,j] = C[i,j] + A[i,l] * B[l,j]
```

Which can be parallelised along i-j and have the final computation be done by a reduce:

```
par-for i = 1 to m do:
  par-for j = 1 to n do:
    temp = array of length k
    par-for l = 1 to k do:
      temp[l] = A[i,l] * B[l,j]
    C[i,j] = C[i,j] + reduce(temp, +)
```

Therefore a have an algorithm with $W(n) = O(mnk)$ and span $D(n) = O(\log(max(m,n,k)))$.
However, this is written for a p-ram system - how can we distribute this?

# Geometric view

You can picture this algorithm like a cube $U$ of size $m \times n \times k$.
This has 3 kinds of sides $m \times k$, $n \times k$ and $m \times n$, which will represent $A$, $B$, $C$ respectively.
Then the point within the cube $U(i, j, l)$ will represent the multiplication $A_{i,l} B_{l,j}$.
Therefore, $C_{i,j} = C_{i,j} + \sum_{l=1}^k U(i,j,l)$ which is the sum of a column through this square. 

![Matrix multiply cube](../../../static/images/matrix_multiply_cube.png)

If you consider now the $1 \times k$, $1 \times k$ and $1 \times 1$ spaces on the outside, you know that their intersection - the $k$ subcubes are the number of multiplications that need to happen between the row and column of $A$ and $B$ that needs to happen to contribute towards $C_{i,j}$.

More generally, if we have two blocks $r \times s$ and $s \times t$ blocks in $A$ and $B$ that both contribute to the $r \times t$ block of $C$ - then we know it relates to $r \dot s \cdot t$ computations.

![Matrix multiply subcube](../../../static/images/matrix_multiply_subcube.png)

This can help us in our analysis of algorithmic run times.
Here we made the assumption that they overlap but more generally there is the below theorem:

> [!lemma] Loomis-Whitney theorem
> Given 3 volumes on the sides of a cube $S_A$, $S_B$, and $S_C$ their intersection within the cube $I$ has volumes:
> $$
> \vert I \vert \leq \sqrt{\vert S_A \vert \cdot \vert S_B \vert \cdot \vert S_C \vert}
> $$

This maximum is achieved on perfect overlap like in the square above

$$
\vert I \vert = \sqrt{(r \cdot s) \cdot (s \cdot t) \cdot (r \cdot t)} = r \cdot s \cdot t. 
$$

# Linear network

Suppose we have $P$ machines and they are connected in a linear fashion.
We would like to do matrix multiply in a network/memory optimal way.

Lets assume $A, B, C$ are $n \times n$ matrices and $P \vert n$.
Our first strategy is to cut all of $A, B, C$ into $n/P \times n$ chunks.
Each machine is then responsible for calculating one chunk of $C$.
To do this it will need access to one chunk of $A$ but all chunks of $B$.
Therefore, we will give each machine their chunk of $A$ and rotate chunks of $B$ between them.

```
// Input: 
//   A, B, C: n x n matrices (not all machines will start with all this data)
//   P: number of machines
//   r: Rank of this machine
// Output:
//   C: n x n matrix (will need to be gathered)
1-d_matrix_multiply(A[1:n][1:n], B[1:n][1:n], C[1:n][1:n], P, r):
  Let A_L[1:n/p][1:n] be A[rn/p: (r+1)n/p - 1][1:n]
  Let B_L[1:n/p][1:n] be B[rn/p: (r+1)n/p - 1][1:n]
  Let C_L[1:n/p][1:n] be C[rn/p: (r+1)n/p - 1][1:n]
  Let A_temp[1:n/p][1:n] be a temporary array of the given size
  Let child = r - 1 mod P
  Let parent = r + 1 mod P
  for L = 0 to P-2:
    // Overlapping communication here with computation below.
    sendAsync(A_L[1:n/p][1:n], child)
    recvAsync(A_temp[1:n/p][1:n], parent)
    // We multiply a n/P x n/P chunk of A by a n/P x n chunk of B
    chunk_index = ((r + L) mod P) * n/P
    for i = 0 to n/P -1:
      for j = 0 to n -1:
        for k = 0 to n/P -1:
          C_L[i][j] = C_L[i][j] + A_L[i][chunk_index+k] * B_L[k][j]
    wait(*)
    Swap(A_L, A_temp)
```

Let $\tau$ be the time it takes to do a floating point operation like add or multiply.
Then the nodes computation time is $T_{comp}(n,P) = 2 \tau n^3 / P$, as it is computing a $n/P \times n$ chunk of a matrix which it needs to multiply and add $n$ elements for each of them.

> [!note] Distributed memory model
> Remember from lecture 8, that on an uncongested network it costs $\alpha + \beta n$ to move $n$ words of data between two machines.

In this case a single node communicates $(n/P)n$ data $P-1$ times so we get it spends $T_{comm} = O(P \alpha + \beta n^2)$ time communicating.

For the total running time of the algorithm, as we are overlapping the communication with the computation we get $T_{1D}(n,P) = \max (2 \tau n^3/P, \alphaP + \beta n^2)$.
This means we have speedup:

$$
S_{1D} = \frac{T_{\ast}(n)}{T_{1D}(n,P)} = \frac{2\tau n^3}{\max (2\tau n^3/P, \alpha P + \beta n^2)} = \frac{P}{\max(1, \frac{\alpha P^2}{2\tau n^3} + \frac{\beta P}{2 \tau n}}.
$$

> [!definition] Parallel Efficiency
> We say an algorithm is parallel efficient if the efficiency (Speedup over P) is a constant.

This algorithm has efficiency:

$$
E_{1D} = \frac{S_{1D}(n,P}}{P} = \frac{1}{\max(1, \frac{\alpha P^2}{2\tau n^3} + \frac{\beta P}{2 \tau n}}.
$$

This is then constant when $n = \Omega(P)$ (by making the $\alpha$ term grow like $1/P$ and the $\beta$ term constant).

> [!definition] Isoefficiency function
> This is the function $n$ has to follow in terms of $P$ to make an algorithm parallel efficient.

This is not great, as we scale the number of processes we put into solving the problem - if the problem doesn't grow we lose our efficient.

Lastly, lets look at the amount of memory this problem uses per node.
We need to store 4 arrays of size $n/P \cdot n$ so we use $M(n,P) = 4 \frac{n^2}{P}$.

# 2-d network (Summa algorithm)

Suppose we have a square $P$ and which has a square grid topology of $\sqrt{P} \times \sqrt{P}$ nodes and $\sqrt{P} \vert n$ (with all the dimensions equal to $n$ again).
Let each node $(a,b)$ be responsible for a block of $C$ $C_{(a,b)} = $\{C_{i,j}\}_{i = an/\sqrt{P}, \ldots, (a+1)n/\sqrt{P} - 1}^{j = bn/\sqrt{P}, \ldots, (b+1)n/\sqrt{P} - 1}$.
Then node $(a,b)$ needs to see $n \times n/\sqrt{P}$ of $A$ and $n/\sqrt{P} \times n$ of $B$ - it will do this in strips of size $s \times n/\sqrt{P}$.

![Summa idea](../../../static/images/summa_idea.png)

Then we delegate out the matrix $A$ and $B$ along the nodes where data is relevant, each node broadcasts the strips one by one and each node makes the local updates required.

```
// Input: 
//   A, B, C: n x n matrices (not all machines will start with all this data)
//   sqrt(P): number of machines in each row/column.
//   a,b: The position of this machine in the grid.
// Output:
//   C: n x n matrix (will need to be gathered)
1-d_matrix_multiply(A[1:n][1:n], B[1:n][1:n], C[1:n][1:n], sqrt(P), a, b):

  // Distribute A and B.
  Let A_L[1:n/sqrt(P)][1:n/sqrt(P)] be A[an/sqrt(p): (a+1)n/sqrt(p) - 1][bn/sqrt(p):(b+1)n/sqrt(p) - 1]
  Let B_L[1:n/sqrt(P)][1:n/sqrt(P)] be B[an/sqrt(p): (a+1)n/sqrt(p) - 1][bn/sqrt(p):(b+1)n/sqrt(p) - 1]
  Let C_L[1:n/sqrt(P)][1:n/sqrt(P)] be C[an/sqrt(p): (a+1)n/sqrt(p) - 1][bn/sqrt(p):(b+1)n/sqrt(p) - 1]

  // Set up arrays to hold the strips.
  Let A_temp[1:n/sqrt(p)][1:s] be a temporary array of the given size
  Let B_temp[1:s][1:n/sqrt(p)] be a temporary array of the given size

  for node = 0 to n/sqrt(P) -1:
    for strip = 0 to n/sqrt(P)s - 1:
      // Get strip of A.
      if (node == a):
        A_temp = A_L[:][s*strip:s*(strip+1) - 1]
        Broadcast(A_temp, (0 to sqrt(P) - 1, b))
      else:
        A_temp = recvAsync(A_temp, (node, b))

      // Get strip of B.
      if (node == b):
        B_temp = B_L[s*strip:s*(strip+1) - 1][:]
        Broadcast(B_temp, (a, 0 to sqrt(P) - 1))
      else:
        B_temp = recvAsync(B_temp, (a, node))

      wait(*)

      // Do update.
      for i = 0 to s - 1:
        for j = 0 to s - 1:
          for k = 0 to n/sqrt(P) - 1:
            left_index = node * n/sqrt(P) + strip * s + i
            right_index = node * n/sqrt(P) + strip * s + j
            C_L[left_index][right_index] += A_temp[i][k] * B_temp[k][j]
```

Lets again look at the 3 important aspects:

- Time spent on compute,
- Time spent on communication, and
- Amount of memory used.

For the compute each node multiplies and adds each $n \times n/sqrt(P)$ block to give a $n/\sqrt(P) \times n/\sqrt(P)$ block which by Loomis-Whitney theorem gives us $T_{comp} = 2 \tau n^3/P$.

For communication - it depends on if we use a tree or bucket algorithm to broadcast the data.
For the tree algorithm we get:
$$
T_{comm} = O(\alpha n/s \log(P) + \beta n^2/\sqrt{P} \log(P))
$$

Whereas for the bucket algorithm we get:
$$
T_{comm} = O(\alpha Pn/s + \beta n^2/\sqrt{P})
$$

This also uses memory $M(n,P) = 3n^2/P + 2sn/\sqrt{P}$ for the 3 blocks of the matrix it holds and the 2 temporary arrays.

Notice in all the above they depend upon $1 \leq s \leq n/\sqrt{P}$ as we increase $s$ we need to use more memory but we are less effected by latency.
If we do the math we get the efficiency of the tree implementation to be:

$$
E_{tree}(n,P) = \frac{S_{tree}(n,P)}{P} = \frac{1}{1 + \frac{\alpha P \log(P)}{2 \tau n^2} + \frac{\beta \sqrt{P} \log(P)}{2 \tau n}}
$$

Giving us an isoefficency of $n = \theta(\sqrt{P}\log(P))$.

However, using the bucketing algorithm we get:

$$
E_{bucket}(n,P} = \frac{1}{1 + \frac{\alpha P^2}{2 \tau n^2} + \frac{\beta \sqrt{P}}{2 \tau n}}
$$

Which apparently leads to an isoefficiency of $n = \Omega(P^{5/6})$ (I don't exactly know why ....).

# Optimal algorithm

Suppose we have some optimal algorithm for matrix multiply.
We want to work out how much communication this algorithm would do.

Suppose we have this algorithm running on a topology with $P$ nodes.
Further, let suppose a node has $M$ words of memory and performs $W$ multiplies.
Let the operation of the node be broken down into $L$ phases where it send and receives exactly $M$ words of data (expect the last phase which may send less).

Then let $S_A$, $S_B$ and $S_C$ be the unique elements of $A$, $B$, and $C$ seen in a phase.
As we start with $M$ memory and can recieve $M$ words we have $\vert S_* \vert \leq 2M$.
Then by the Loomis-Whitney theorem this means in each phase we can perform atmost $2 \sqrt{2} M^{3/2}$ operations.
This gives us that

$$
L \geq \frac{W}{2 \sqrt{2} M^{3/2}} - 1
$$

Now we can use the lower bound on $L$ to give us a lower bound on the number of communications given by this node.

$$
\text{Number of words communicated} \geq \frac{W}{2 \sqrt{2} M^{1/2}} - M
$$

We can bound $W$ by noticing that there is a node that needs to do atleast $n^3/P$ operations as we need to do $n^3$ operations at the very least.
Similarly, within the $P$ nodes we need to store all the $3n^2$ words in the 3 matrices giving $M = \theta(n^2/P)$.
Plugging these in we get:

$$
\text{Number of words communicated} \geq \frac{n^2}{2 \sqrt{P}} - \frac{n^2}{P} = \Omega(\frac{n^2}{\sqrt{P}})
$$

This gives a lower bound on the bandwidth of an algorthm.
In an optimal case we would send the whole of $M$ in one message so this gives us $\theta(\sqrt{P})$ messages.
This together gives us a bound on the time communicating:

$$
T_{comm, optimal} \geq \alpha \sqrt{P} + \beta \frac{n^2}{\sqrt{P}}
$$

If we compare this to the SUMMA algorithm we get the correct bandwidth term but the number of messages is slightly off.
Can we do better than SUMMA?

Yes! There is an algorithm called Cannon's algorithm that achieves the optimal bound on communication but is some what harder to practically implement.

Note the analysis assumed we had $n^3/P$ memory but having more memory can decrease the amount of communication we need!
So this is optimal bound can and has been beaten by a practical algorithm.
