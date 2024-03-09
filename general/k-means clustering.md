---
aliases: 
checked: false
created: 2024-03-09
last_edited: 2024-03-09
publish: true
tags:
  - programming
  - machine-learning
type: algorithm
---
# k-means clustering

Suppose we are in the [[Clustering problem|clustering problem]] set up. Suppose we are provided $k$ the number of clusters. Further assume $A$ is a space with some method of averaging $Avg:2^A \rightarrow A$ which satisfies 
$$
\sum_{x \in X} d(x, Avg(X)) = \min_{a \in A} \sum_{x \in X} d(x,a), \mbox{ for all } X \subset A.
$$
In the Euclidian example we will have 
$$
Avg(X) = \frac{1}{\vert X \vert} \sum_{x \in X} x.
$$
To start the algorithm we pick $k$ random points in our [[Training data|training data]] $T$. We set these to be the current centres $center^0_i$ for $1 \leq i \leq k$. For iteration $t \in \mathbb{N}$ assume we have centres $center_i^{t-1} \in A$ (they don't need to be points in $T$). Now we group the training data
$$
C^t_i = \left \{t \in T \Bigg \vert \left ( \mbox{ arg}\min_{1 \leq j \leq k} d(t, center_j^{t-1}) \right ) = i \right \}
$$
Then we update our centres $center_i^t = Avg(C_i^t)$. We keep iterating until $C_i^t = C_i^{t+1}$ for all $1 \leq i \leq k$. 

## Pseudocode

```pseudocode
Name(k, T, d, Avg):
	Input:
		k - the number of clusers
		T - the training data
		d - the symetric distance function on A
		Avg - a method of averaging points
	Output:
		A function f mapping T to k groups.
1. Pick k random points in T and set this to be center_i
2. Set f_last, f_current to be empty
3. While f_last empty or f_last != f_current:
	1. Set f_last = f_current
	3. Set center_i = Avg(f_last^{-1}(i)) for all 1 <= i <= k
	4. Set f_current(t) = argmin_j d(t, center_j) for all t in T
4. Return f_current
```

## Run time

We will go on to "hand wave" that this algorithm can never return to the same state without stopping. Let $n = \vert T \vert$ then the number of possible iterations is $O(k^n)$ (lazy estimations on the number of partitions). Each iteration takes $O(k(n+O(Avg(n)))$ as we need to calculate the distance between each of the centres for each point and then calculate overages of each of the centres.  

This gives the run time to be $O(k^{n+1}(n + O(Avg(n))))$.

In practice this algorithm is much faster than the run time lets on.

## Correctness

Correctness in this situation will mean that it will terminate eventually. To "handwave" this we will phrase this problem as a [[Hill climbing]] problem.

Let the configurations be the [[Partition (set)|partition]] with the centres $(C_i, center_i)_{1 \leq i \leq k}$. Then we can score each configuration as
$$
E(C_i, center_i) = \sum_{i=1}^k \sum_{x \in C_i} d(c, center_i).
$$
To define a configurations $(C_i, center_i)_{1 \leq i \leq k}$ neighbourhood let $center_i' = Avg(C_i)$ and $$
C_i' = \left \{t \in T \Bigg \vert \left ( \mbox{ arg}\min_{1 \leq j \leq k} d(t, center_j) \right ) = i \right \}
$$
Then point $(C_i, center_i)_{1 \leq i \leq k}$ has up to two neighbours $(C_i, center_i')$ and $(C_i', center_i)$ (we only include them if they are distinct from $(C_i, center_i)_{1 \leq i \leq k}$). This has the interesting property the
$$E(C_i,center_i) \geq E(C_i, center_i'), \mbox{ and } E(C_i,center_i) \geq E(C_i', center_i).
$$
The first inequality follows from the property of average we have required. The second one follows as we picked $C'_i$ to minimise distance between the points and the centres.

Then our algorithm is identical to the [[Hill climbing]] algorithm in this set up. 

>[!note] Double hop
> This argument only works when you think of one iteration of our algorithm being 2 steps in the [[Hill climbing]]. First you update the centres, one hop, then you update the partition, two hop.
> The state we visit after the first state will only have at most 1 neighbour as the previous step we will have picked either the center or partitions to be optimal. 

Therefore we don't revisit a state?

>[!warning] Might only be true in Euclidian spaces

Given this is the same as [[Hill climbing]] we can get stuck in a local optimum which is not a global optimum. There are two ways to get around this:
- Do it with random restarts, or
- Pick the starting states well.