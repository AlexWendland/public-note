---
aliases: 
checked: false
created: 2024-03-09
last_edited: 2024-03-09
draft: false
tags:
  - programming
  - machine-learning
type: algorithm
---
# Single linkage clustering

Suppose we are in the [[Clustering problem|clustering problem]] set up. Here we are given the number of desired clusters $k$, and the sense of distance $d$.

The idea will be to make every element in our [[Training data|training data]] $T$ its own cluster. Then we take the union of two clusters which are considered the closest. For this linkage clustering we use the minimum distance of points in the cluster. i.e.
$$
d_C: 2^T \times 2^T \rightarrow \mathbb{R}, \ d_C(C_1, C_2) = \min_{a \in C_1, b \in C_2} d(a,b)
$$
where $2^T$ is the [[Power set|power set]] of $T$. We keep iterating this until we are left with $k$ clusters.

## Pseudocode

```pseudocode
Name(k, d, T):
	Input:
		k - the number of clusters
		d - the a symetric distance on T
		T - training data
	Output:
		A function from f splitting T into k groups
1. Set f to be the identity function.
2. While the codain of f has size larger than k:
	1. Set C_a, C_b, min_distance to be empty 
	2. For add X, Y in f^{-1}(T):
		1. Caluclate dist = min_{x in X, y in Y} d(x,y)
		2. if dist < min_distance:
			1. Set C_a = X, C_b = Y
	3. Update f(C_b) = f(C_a)
3. Return f
```

## Run time

If you implement this in the worst case it is $O(n^3)$ but realistically you could get it to be $O(n^2)$.

## Correctness

Whilst it solves the problem it can lead to counter intuitive answers as chains for very closely grouped points will cluster together even when by eye you might split them differently.
