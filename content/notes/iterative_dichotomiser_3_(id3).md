---
aliases:
  - Iterative Dichotomiser 3
  - ID3
checked: false
created: 2024-01-11
draft: false
last_edited: 2024-01-11
tags:
  - programming
title: Iterative Dichotomiser 3 (ID3)
type: algorithm
---

This algorithm works on [classification problems](classification_problems.md). It is a greedy algorithm to design a maximal [decision tree](decision_tree.md).  Therefore are looking for the tree to represent some function $f: A \rightarrow B$, where we may only have access to some training data $D \subset f$.

This decision tree will be maximal with regards to the [information entropy](information_entropy.md) of each of the leaf nodes within that [decision tree](decision_tree.md).  For any $A' \subset A$ we can define $Entropy(A')$ by considering drawing a random element in $A'$ out with a probability of them being mapped to some element of $B$.

To make this decision tree assume we have a set of attributes $t \in T$ where $t: A \rightarrow \{1, \ldots, n_t\}$ that split the set $A$ up into subsets of variable length for $n_t \in \mathbb{N}$. Let $\mathcal{P}(A)$ be the subsets of $A$ and define $Gain: \mathcal{P} \times T \rightarrow \mathbb{R}$ where
$$
Gain(A', t) := Entropy(S) - \sum_{j = 1}^{n_i} \frac{\vert A'_j \vert}{\vert A' \vert} Entropy(A'_j), \ \ \ \mbox{with} \ A'_j :=t^{-1}(j) \cap A'.
$$

Lastly we will construct this tree using a [depth-first search](depth-first_search_(dfs).md) algorithm, where at each leaf node we will have a subset of our original training set.

# Pseudocode

```pseudocode
ID3(training_data, attributes):
	Input:
		training_data of the form {(a,f(a)) | a in A'}
		attributes mapping A into some finite set of states
	Output:
		a decision tree for the function f
1. Let A' be the set of points in A of the training data.
2. If Entropy(S) = 0 return a single leaf node with the one element of B all the training data has.
3. For each attribute t calculate Gain(A',t).
	1. If Gain(A',t) = 0 for all t return a signle leaf node with a maximally likely value in the training data.
	2. Otherwise let t' be a maximal element with respect to Gain(A', -)
4. Build rooted tree T with t' being the root node
5. For each j in 1, ..., n_t'
	1. Let A'_j = t'^{-1}(j) intersect A'
	2. Let T_j = ID3({(a,f(a)) | a in A'_j}, attributes without t)
	3. Attach the root of T_j to node t' with outcome j.
6. return decision tree T.
```

# Run time
- $O(\vert A' \vert 2^{\vert T \vert})$

# Correctness

