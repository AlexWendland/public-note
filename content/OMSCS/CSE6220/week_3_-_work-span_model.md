---
aliases:
checked: false
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-01-22'
draft: true
last_edited: '2026-01-22'
tags:
  - OMSCS
title: Week 3 - Work-Span model
type: lecture
week: 3
---

In this lecture we explore a method of parallelisation called the work-span model.
This uses [DAGs](../../notes/directed_acyclic_graph_(dag).md) to represent a computation.
Where each node is a computation that needs to be run and arrows between nodes represent dependencies.
We will assume this is connected, and has a start/stop vertex.

![Example DAG](../../../static/images/computational_dag.png)

We will run these on a PRAM machine.
This is a machine with multiple processors attached to some memory.
Here we get 'parallelism' by running multiple operations on different processors.
These can only be run once their dependencies have all been run already.
How to assign the vertices to the processors is called a 'scheduling problem'.

The natural question is for a DAG how long does it take to run?
To answer this we define a cost model with the following assumptions:

- All processors are equally fast.

- A vertex costs 1 operation to run.

- No cost to edges.

- No memory transfer issues (at the moment).

# DAG structure matters

Suppose we need to add $n$ items using $n$ processors.
Using the normal iterative approach with a single sum variable will take $O(n)$ time - not really being able to use the $n$ processors.

![Simple reduction](../../../static/images/reduction_dag_simple.png)

If instead we structure the sum using a binary tree we can do it in $O(\log(n))$ time.

![Binary reduction](../../../static/images/reduction_dag_tree.png)

This now uses more of the processors within the summation.
Giving us that the structure of these DAGs does affect the run time.

# Work-span analysis

Given some DAG $D_n$ that represents a computation of size $n$ we want to define the work and span of it to start providing bounds on the run time of the DAG.

> [!definition] Work
> The work of a DAG is the number of vertices $W(n) = \vert V(D_n) \vert$.

> [!definition] Span
> The span of a DAG is the number of vertices on the longest path between the start and end vertex.
> This uses the notation $D(n)$ as it used to be called depth.

> [!definition] Run time
> We define the run time of DAG $D_n$ on $p$ processors $T_p(n)$.


The ratio of these concepts provides an average of the available parallelism $\frac{W(n)}{D(n)}$ when running this DAG.

There are some immediate things we can say about runtime just using the definitions above.

- $T_1(n) = W(n)$: As each vertex needs to be run, it will take $W(n)$ operations to complete the graph.

- $T_{\infty}(n) = D(n)$: Assuming we have maximum parallelism, we are limited by the longest path between the start and end vertex.

- *Span law*: For any other number of processors $p$ the span still bounds the run time $T_p(n) \leq D(n)$.

- *Work law*: Assuming we have $p$ processors that are working all the time the fastest they can complete the DAG is $T_p(n) \geq \left \lceil \frac{W(n)}{p} \right \rceil$.

- *Work-span law*: Combining the laws above

$$
T_p(n) \geq \max \left \{ D(n), \left \lceil \frac{W(n)}{p} \right \rceil \right \}
$$

This is a lower bound, however it would be good to also achieve an upper bound as well.

# Brent's theorem

> [!lemma] Brent's theorem
> For a DAG $D_n$ we have
> $$
> T_p(n) \leq \frac{W(n) - D(n)}{p} + D(n)
> $$

As the vertices are in a DAG we can label them $l: V(D_n) \rightarrow [1, D(n)]$ by mapping a vertex to the number of vertices on the path of longest distance between the start vertex and itself.
Lets make some observations about this mapping:

- We have $l(start) = 1$ and $l(end) = D(n)$ (moreover these are the only vertices with these values).

- If $l(v) = l(u)$ then $(v,u) \not \in E(D_n)$ as we could form a longer path to $u$ by going through $v$.

Now let $w_k := \vert l^{-1}(k) \vert$ be the number of vertices assigned label $k$.
With this we can get a bound on the execution time of this DAG:
$$
\begin{align*}
T_p(n) & \leq \sum_{k=1}^{D(n)} \left \lceil \frac{w_k}{p} \right \rceil\\
& \leq \sum_{k=1}^{D(n)} \left \lfloor \frac{w_k - 1}{p} \right \rfloor + 1\\
& \leq \sum_{k=1}^{D(n)} \frac{w_k - 1}{p} + 1\\
& \leq \frac{W(n) - D(n)}{p} + D(n)\\
$$
Which gives us our desired bound.

Combining Brent's theorem with the work-span law we get:
$$
\max \left \{ D(n), \left \lceil \frac{W(n)}{p} \right \rceil \right \} \leq T_p(n) \leq \frac{W(n) - D(n)}{p} + D(n)
$$
This is a fairly tight bound when you observe:
$$
\frac{W(n) - D(n)}{p} + D(n) \leq \frac{W(n)}{p} + D(n) \leq \left \lceil \frac{W(n)}{p} \right \rceil + D(n) \leq 2 \max \left \{ D(n), \left \lceil \frac{W(n)}{p} \right \rceil \right \}
$$
Which is pretty good given it applies to any DAG.

# Speedup

We want to work out roughly how much 'extra' we are getting from parallelism.
Therefore we want to compare an optimal linear solution $T_1(n) = W(n)$ with the time it takes on $p$ processors.

> [!definition] Speedup
> The speedup of a DAG is defined to be:
> $$
> S_p(n) = \frac{T_1(n)}{T_p(n)}
> $$

> [!note] DAG changes depending on $p$
> Algorithms may choose to change the underlying DAG as we increase the size of $p$.
> So we will now introduce $W_p(n)$ and $D_p(n)$ to mean the work-span for the DAG using $p$ processors.

The best case speedup is $T_p(n) = \frac{T_1(n)}{p}$ giving us a linear speedup in $p$ i.e. $S_p(n) = p = O(p)$.
Using Brent's theorem we can get a lower bound on speedup.

$$
\begin{align*}
S_p(n) & = \frac{W_1(n)}{T_p(n)}\\
& \geq \frac{W_1(n)}{\frac{W_p(n) - D_p(n)}{p} + D_p(n)}\\
& \geq \frac{p W_1(n)}{W_p(n) + (p-1) D_p(n)}\\
& \geq \frac{p}{\frac{W_p(n)}{W_1(n)} + \frac{p-1}{W_1(n)/D_p(n)}}\\
\end{align*}
$$

So to attain linear speed up ideally we want:

$$
\frac{W_p(n)}{W_1(n)} = O(1) \mbox{ and } \frac{p-1}{W_1(n)/D_p(n)} = O(1)
$$

> [!definition] Work-optimality
> We say a parallelisation achieves work-optimality if $O(W_1(n)) = W_p(n)$.
> This means that the parallelism does not add any extra work for us to do.

> [!definition] Weak-scalability
> We say a parallelisation is weak-scalable if $p = O(\frac{W_1(n)}{D_p(n)})$.
> Intuitively this means that the 'average' parallelism is about $p$.
> Another way to view this is
> $$
> \frac{W_1(n)}{p} = \Omega(D_p(n)).
> $$
> This is saying that the span of a parallel algorithm can only grow at the rate of the original problem divided by $p$.

# Where do DAG's come from?

We write them!
We will use special terminology to write them down with two key words `spawn` and `sync`.
The `spawn` keyword starts a sub-DAG from the process it is handed.
The `sync` keyword waits to gather the results of all previous `spawn`'s.

This then turns into a DAG by starting a process for the main thread and branching at all the `spawn` words and joining at all the `sync` words.
Lets look at an example of reduction.

```
reduce(A[0:n-1])
1. if n >= 2:
2.   a <- spawn reduce(A[0:n/2-1])
3.   b <- spawn reduce(A[n/2:n-1])
4.   sync
5.   return a + b
6. else:
7.   return A[0]
```

This breaks into the following DAG:

![Generated DAG](../../../static/images/dag_generation.png)

To do analysis on this pseudo-code we can apply the usual techniques.
For work we can simply define the recurrence relationship.

$$
W(n) = \begin{cases}
2 \cdot W(n/2) + O(1) & \mbox{if } n \geq 2\\
O(1) & \mbox{otherwise}
\end{cases}
$$

Which gives us $W(n) = O(n)$.

For span on the other hand we have to consider the `spawn`s length and take the max.
i.e. $D(n) = \max\{D(n/2), D(n/2), 1\} + O(1)$.
In our case this is fairly simple as both spawns are of the same size so we get:

$$
D(n) = \begin{cases}
D(n/2) + O(1) & \mbox{if } n \geq 2\\
O(1) & \mbox{otherwise}
\end{cases}
$$

This gives us $D(n) = O(\log(n))$.

# Goals for parallel algorithms

In the past we always tried to build algorithms with the lowest amount of $W(n)$ normally aiming for linear $W(n) = O(n)$.
In parallel algorithms this is the same!
(Though it may not always be possible.)

Though for the Span instead of looking for linear - we want to look for poly-logarithmic growth.
I.e. we want algorithms that grow like $O(D(n)) = \log^k(n)$.

# Parfor

Suppose we have an independent operations $foo(i)$ but we need to run it $n$ times.
In parallel notation we would use:
```
1. par-for i \in [1,n]:
2.   foo(i)
```
This runs in parallel $n$ copies of $foo$.
However, how we turn this into a dag is important - just like the reduce example.
If we just all `spawn` one after another with a `sync` at the end we get the span growing linearly.
So instead we use a tree structure to run the work essentially turning par-for into a process.

```
par-for(foo, a, b)
1. n = b - a + 1
2. if n = 1:
3.   foo(a)
4. else:
5.   let m = a + floor(n/2)
6.   spawn par-for(foo, a, m)
7.   par-for(foo, m, b)
8.   sync
```

This branches giving us a span of $D(n) = O(\log(n) + D(foo))$.

> [!warning] Requires `foo` to be independent!
> If `foo` changes the same data we can't parallelise them quite as easily.
> This will cause a data race on the shared variables.

# Vector notation

Consider matrix-vector multiplication

```
Multiply(A, x) -> Ax:
1. y = 0 vector of length n.
2. for i \in [0,n-1]:
3.   for j \in [0,n-1]:
4.     y[i] = y[i] + A[i,j] * x[j]
5. return y
```

Currently this is fully synchronous so we have $W(n) = O(n^2) = D(n)$.
The first parallelisation we can do it changing the outside loop to a par-for.
However, we can not turn the inner for-loop into a par-for as it relies on the same data, namely $y[i]$.

```
Multiply(A, x) -> Ax:
1. y = 0 vector of length n.
2. par-for i \in [0,n-1]:
3.   for j \in [0,n-1]:
4.     y[i] = y[i] + A[i,j] * x[j]
5. return y
```

This makes some improvement $W(n) = O(n^2)$ but since the inner loop is only $O(n)$ we have $D(n) = O(n)$.
Currently the thing stopping us from parallelising the inner loop is the shared variable $y[i]$ - however just like reduction we are choosing to use a serial way to do this.
Instead lets reduce in a tree-like structure.

```
Multiply(A, x) -> Ax:
1. y = 0 vector of length n.
2. par-for i \in [0,n-1]:
3.   t = 0 vector of length n.
4.   par-for j \in [0,n-1]:
5.     t[j] = A[i,j] * x[j]
6.   y[i] = y[i] + reduce(t)
7. return y
```

By creating $t$ we can use par-for in the inner loop with the reduction at the end.
This still has $W(n) = O(n^2)$ but $D(n) = O(\log(n) + \log(n) + \log(n)) = O(\log(n))$.

To make this kind of operations easier to parse we introduce short notation for it.

```
Vector multiplication
1. par-for j \in [0,n-1]:
2.   t[j] = A[i,j] * x[j]

Vector multiplication
1. t[:] = A[i,:] * x[:] // Implicit par-for loop here
```

We actually reduce this even further using the `reduce` key word.

```
Vector multiplication
1. t = 0 vector of length n.
2. par-for j \in [0,n-1]:
3.   t[j] = A[i,j] * x[j]
4. y[i] = y[i] + reduce(t)
 

Vector multiplication
1. y[i] = y[i] + reduce(A[i,:] * x[:]) // Implicit par-for loop and temporary variable
```
