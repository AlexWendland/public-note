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
# Expectation Maximisation

In the [[Clustering problem|clustering problem]] setting with a given number of classes $k$ and training data $T = \{x_i \vert i \in I\}$. Suppose we have assumed our data is clustered according to some distribution $\mathbb{D}$ each cluster depends on a parameter $\mu_j$ (for this example we will use the mean).  

Then we are going to iteratively update 
1. the expectation of event $Z_{i,j} = [f(x_i) = j]$ that the $i \in I$ point belongs to the class $j$ given the hypothesis that the clusters use $\mu_j$, and
2. the parameters $\mu_j$ using the distribution of $Z_{i,j}$.

First we will describe step one, given some new parameters $\mu_j$. We set
$$
\mathbb{E}[z_{i,j}] = \frac{\mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_j]}{\sum_{h=1}^k \mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_h]}
$$
Where the formula for $\mathbb{P}_{\mathbb{D}}[x=x_i \vert \mu = \mu_j]$ comes from the distribution $\mathbb{D}$.

The second step just calculates the best parameters given these probabilities. In this case mean
$$
\mu_j = \frac{\sum_{i \in I} \mathbb{E}[Z_{i,j}]x_i}{\sum_{i \in I} \mathbb{E}[Z_{i,j}]}.
$$
This process is not guaranteed to stop. 

## Correctness

- We are monotonically decreasing [[Maximum likelihood estimation (MLE)|Maximum likelihood]] error of the groupings.
- Though this is not guaranteed to converge.
- Though it will not diverge either! 
- It can get stuck in local optimums.
	- So it is best that we restart this algorithm and take the best outcome.