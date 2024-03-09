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

Suppose we are in the [[Clustering problem|clustering problem]] set up. Suppose we are provided $k$ the number of clusters. Further assume $A$ is a space with some method of averaging $Avg(S)$ for all $S \subset A$. In the Euclidian example we will have 
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
	1. for t in T:
		1. Set 
```

## Run time



## Correctness

