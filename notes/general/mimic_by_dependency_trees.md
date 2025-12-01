---
aliases:
checked: false
created: 2024-02-25
draft: false
last_edited: 2024-02-25
name: MIMIC by dependency trees
tags:
  - programming
type: algorithm
---
# MIMIC by dependency trees

This follows on from [MIMIC (meta)](mimic_(meta).md). Where we are going to use [dependency trees](dependency_trees_(bayesian_network).md) to calculate the distribution. Here we are just implementing a version of the `probability_constructor`.

We assume the [domain](function_domain.md) of our problem breaks up $A = \oplus_{i=1}^n A_i$ into features, we will also break up the random variable $X=\oplus_{i=1}^n X_i$ on this also. To generate the probability distribution we are going to build a [dependency tree](dependency_trees_(bayesian_network).md). To decide the form of this dependency tree - [due to some maths](../OMSCS/CS7641/week_7_-_randomized_optimization.md#estimating-the-probability-distribution-using-dependency-trees) - we will use provide pass or fail samples to calculate [Mutual information](mutual_information.md) for each pair of features.

To do this we need to calculate $\mathbb{P}[X_i = a_i]$ for all $1 \leq i \leq n$, $\mathbb{P}[X_i = a_i, X_j = a_j]$, and $\mathbb{P}[X_i=a_i \vert X_j = a_j]$ for each $1 \leq i < j \leq n$. If we have samples $P, F \subset A$ of pass fails respectively this is simply
$$
\begin{align*}
\mathbb{P}[X_i = a_i] = & \frac{\vert \{x \in P \vert x_i = a_i\} \vert}{\vert P \vert + \vert F \vert}\\
\mathbb{P}[X_i = a_i, X_j = a_j] = & \frac{\vert \{x \in P \vert x_i = a_i, x_j = a_j\} \vert}{\vert P \vert + \vert F \vert}\\
\mathbb{P}[X_i=a_i \vert X_j = a_j] = & \frac{\vert \{x \in P \vert x_i = a_i, x_j = a_j\} \vert}{\vert \{x \in P \cup F \vert x_j = a_j\} \vert}\\
\end{align*}
$$
however there are more advanced technique you can apply here.

Now we apply the formula of [Mutual information](mutual_information.md), [Information entropy](information_entropy.md), and [conditional entropy](conditional_entropy.md) to get $I[X_i, X_j]$.

Then we construct a complete [undirected graph](graph.md) on $\{1,2, \ldots n\}$ then weight the edge $(i,j)$ with $-I[X_i, X_j]$. (Note [Mutual information is symmetric](mutual_information_is_symmetric.md) so we can just use $I[X_i,X_j]$ where $i < j$.)

Then construct a [MST](minimum_spanning_tree_problem_(mst).md) on this graph and pick one node to be the root. This gives us our [dependency tree](dependency_trees_(bayesian_network).md). We can now use the probabilities calculated earlier to find the probabilities associated with this tree.

Once we have this [Bayesian network](bayesian_network.md) we can use it to simulate new samples to evaluate on.

## Run time


## Correctness

