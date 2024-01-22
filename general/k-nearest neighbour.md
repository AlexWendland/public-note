---
aliases:
  - KNN
checked: false
created: 2024-01-22
last_edited: 2024-01-22
publish: true
tags:
  - programming
type: algorithm
---
# k-nearest neighbour

This algorithm is an [[Instance-based learning]] model and uses closest neighbours to determine what values should be.

In the [[Modelling framework|modelling framework]], suppose we are given: 
- [[Training data|training data]] $T \subset (A,B)$,
- a [[Metric|metric]] on $A$ called $d: A \times A \rightarrow \mathbb{R}$,
- $k \in \mathbb{Z}$ to be the number of points to consider, and
- an averaging mechanism $V: \mathcal{P}(B \times \mathbb{R}) \rightarrow B$ that takes a weighted set of values in $B$ and returned another value in $B$ - like the weighted [[Geometric mean|geometric mean]].
Then to model our data when given a new input point $a \in A$ we find the $k$-nearest neighbours in our training data $T$ then take the average of their associated values in $B$.  

This model is very simple - however a lot of the complexity comes in defining $d$ and $V$. 

## Pseudocode

```pseudocode
KNN(T, d, k, V, a):
	Input:
		T our training data which is points in A and B
		d metric on the space of A
		k the number of points to average
		V a way of deciding how to pick out of the neighbours
		a in A
	Output:
		b in B the models prediction
1. Set N = get_k_nearest_neighbours(T, d, k, a)
2. Set b = V({(b',d(a',a)) for (a',b') in N})
3. Return b

get_k_nearest_neighbours(T, d, k, a):
	Input:
		T our training data which is points in A and B
		d metric on the space of A
		k the number of points to average
		V a way of deciding how to pick out of the neighbours
		a in A
	Output:
		N subset A which are the k-nearest neighbours to a in T
1. Let X be a set
2. For each (a',b') in T:
	2.1. Append ((a',b'), d(a',a)) to X
3. Sort X by the second parameter.
4. Let N = {t for the first k elements (t,d') in X}
     # You can also let N include elements of equal distance as the k'th
     # element
5. Return N
```

## Run time



## Correctness

