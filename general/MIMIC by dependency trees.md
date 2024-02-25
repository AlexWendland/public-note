---
aliases: 
checked: false
created: 2024-02-25
last_edited: 2024-02-25
publish: true
tags:
  - programming
type: algorithm
---
# MIMIC by dependency trees

This follows on from [[MIMIC (meta)]]. Where we are going to use [[Dependency Trees (Bayesian Network)|dependency trees]] to calculate the distribution. Here we are just implementing a version of the `probability_constructor`.

We assume the [[Function domain|domain]] of our problem breaks up $A = \oplus_{i=1}^n A_i$ into features, we will also break up the random variable $X=\oplus_{i=1}^n X_i$ on this also. To generate the probability distribution we are going to build a [[Dependency Trees (Bayesian Network)|dependency tree]]. To decide the form of this dependency tree - [[Week 7 - Randomized Optimization#Estimating the probability distribution using dependency trees|due to some maths]] - we will use provide pass or fail samples to calculate [[Mutual information]] for each pair of features.

To do this we need to calculate $\mathbb{P}[X_i = a_i]$ for all $1 \leq i \leq n$, $\mathbb{P}[X_i = a_i, X_j = a_j]$, and $\mathbb{P}[X_i=a_i \vert X_j = a_j]$ for each $1 \leq i < j \leq n$. If we have samples $P, F \subset A$ of pass fails respectively this is simply 
$$
\begin{align*}
\mathbb{P}[X_i = a_i] = & \frac{\vert \{x \in P \vert x_i = a_i\} \vert}{\vert P \vert + \vert F \vert}\\
\mathbb{P}[X_i = a_i, X_j = a_j] = & \frac{\vert \{x \in P \vert x_i = a_i, x_j = a_j\} \vert}{\vert P \vert + \vert F \vert}\\
\mathbb{P}[X_i=a_i \vert X_j = a_j] = & \frac{\vert \{x \in P \vert x_i = a_i, x_j = a_j\} \vert}{\vert \{x \in P \cup F \vert x_j = a_j\} \vert}\\
\end{align*}
$$
however there are more advanced technique you can apply here. 

Now we apply the formula of [[Mutual information]], [[Information entropy]], and [[Conditional entropy|conditional entropy]] to get $I[X_i, X_j]$.

Then we construct a complete [[Graph|undirected graph]] on $\{1,2, \ldots n\}$ then weight the edge $(i,j)$ with $-I[X_i, X_j]$. (Note [[Mutual information is symmetric]] so we can just use $I[X_i,X_j]$ where $i < j$.)

Then construct a [[Minimum Spanning Tree problem (MST)|MST]] on this graph and pick one node to be the root. This gives us our [[Dependency Trees (Bayesian Network)|dependency tree]]. We can now use the probabilities calculated earlier to find the probabilities associated with this tree. 

Once we have this [[Bayesian network]] we can use it to simulate new samples to evaluate on.

## Run time


## Correctness

