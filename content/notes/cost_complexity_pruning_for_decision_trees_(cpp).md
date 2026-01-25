---
aliases:
  - CPP
created: 2024-02-02
date_checked:
draft: false
last_edited: 2024-02-02
tags:
  - programming
title: Cost complexity pruning for decision trees (CPP)
type: algorithm
---

When making a [decision tree](decision_tree.md) with no pruning it can tend to [overfit](overfitting.md) the [training data](training_data.md). To reduce this we can "prune" the decision tree. We do this by looking at how useful each of the branches are - then removing the ones that don't add enough value. This is controlled by a variable $\alpha$ which increases the cost of having more leaf nodes.

Suppose we are in [modelling framework](modelling_framework.md) where $T$ is our [training data](training_data.md) and let $\hat{f}$ be our decision tree. Assume $R(\hat{f}, T)$ is our function for evaluating how good a fit our tree is (likely this will use [information entropy](information_entropy.md) or the [Gini index](gini_index.md)). Lastly let $L(\hat{f})$ be the number of leaf nodes in our [decision tree](decision_tree.md) $\hat{f}$. Set
$$
R_{\alpha}(\hat{f}, T) = R(\hat{f}, T) + \alpha L(\hat{f})
$$
to be the value we want to minimise on our sub-trees.

Optimally we would iterate over all potential subtrees of $\hat{f}$ and find the sub-tree that optimises $R_{\alpha}$ on $T$. However, computationally this can be expensive. Therefore it is usual to find a heuristic to choose a branch to prune instead.

One method to do this it to calculate the *effective cost complexity* of a non-terminal node. To give you the intuition behind this let $G = (V,E)$ be our decision tree and extend $R$ to be defined at $v \in V$ where $R(v)$ is the evaluation function evaluated on the training data that makes it to $v \in V$ (like when training the [decision tree](decision_tree.md)). Then the effect of a leaf node $v \in L(G)$ on $R_{\alpha}(\hat{f}, T)$ is
 $$
 R(v) + \alpha.
$$
To define the effective cost complexity we will find the $\alpha$ such that the contribution of an internal node to $R_{\alpha}$ would be the same as for $G_v$ the subtree rooted at $v$. This is
$$
\alpha_{eff}(v) = \frac{R(v) - \sum_{x \in L(G_v)} R(x)}{\vert L (G_v) \vert - 1}.
$$
(It can be derived by equating the contribution of $v$ against the contribution of the terminal nodes $G_v$ contains.)

The process then prunes branches with the lowest $\alpha_{eff}$ until that value is greater than $\alpha$.

# Pseudocode

```pseudocode
CPP(decision_tree, alpha, R):
	Input:
		decision_tree with a set of vertices V
		alpha positive constant to determine pruning
		R the evaluation function such as Entropy or Gini, this will have to
			defined on vertices of V (for the training data that gets
			classifed to v)
	Output:
		a pruned decision tree
1. Set best_tree = decision_tree
2. For each non-leaf set alpha_eff(v) = calculate_effective_alpha(decision_tree, v, R)
3. Set min_eff_alpha = min(alpha_eff(v) for v in V non-leaf)
4. While min_eff_alpha < alpha
	4.1. Find v such that alpha_eff(v) = min_eff_alpha
	4.2. Prune best_tree at v
	4.3. Let P be the set of vertices with v downstream of it.
	4.4. For each p in P set alpha_eff(p) = calculate_effective_alpha(best_tree, p, R)
	4.5. Set min_eff_alpha = min(alpha_eff(v) for v in best_tree non-leaf)
	4.6. Break if best_tree only has 1 vertex.
5. return best_tree.

calculate_effective_alpha(tree, v, R):
	Input
		tree is a decision tree
		v is a vertex in V that is not a leaf node
		R the evaluation function such as Entropy or Gini, this will have to
			defined on vertices of V (for the training data that gets
			classifed to v)
	Output
		alpha_eff the effective alpha for that vertex
1. Let L be the set of leaf vertices with v unstream of it in tree.
2. Set total_leaf_weight = sum(R(x) for x in L)
3. Return (R(v) - total_leaf_weight)/(|L| - 1)
```

# Run time

Optimally we would iterate over all potential subtrees of $\hat{f}$ and find the sub-tree that optimises $R_{\alpha}$ on $T$. However, computationally this can be expensive. Instead we can use effective cost complexity which cuts down run time but can still take $O(\vert V \vert^3)$.

# Correctness

This can reduce overfitting, however the parameter $\alpha$ needs to be fine tuned. It is best to use [cross validation](cross_validation.md) for this purpose.
