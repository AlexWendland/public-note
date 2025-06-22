---
aliases: 
checked: false
created: 2024-02-24
last_edited: 2024-02-24
draft: false
tags:
  - programming
  - machine-learning
type: algorithm
---
# Naive Bayes classifier

Suppose we have a [[Classification problems|classification problem]] and we are in the [[Modelling framework|modelling framework]]. We are given features $A = \oplus_{i=1}^n A_i$ where each feature $A_i$ has finite values (also split up the [[Random variable|random variable]] $X$ into $X = \oplus_{i=1}^n X_i$ for our input). Let our classification also have finite [[Function domain|domain]] $B$.

We can use our [[Testing data|testing data]] to estimate $\mathbb{P}[Y=b]$ for each $b \in B$ and $\mathbb{P}[X_i = a_i \vert Y = b]$ for each $a_i \in A_i$ and $b \in B$. 

>[!warning] Assumption
>Making the assumption that $Y$ and each of the $X_i$ form a [[Bayesian network]] where $Y$ is the root with one arrow to each of the $X_i$ with the probabilities above. 

Using [[Bayes rule]] then [[Marginalisation (probability)|marginalisation]] and [[Chain rule (probability)|chain rule]] we can calculate
$$
\mathbb{P}[Y = b \vert X = (a_1, a_2, \ldots, a_n)] = \frac{\mathbb{P}[Y=b] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b]}{Z}
$$
with the normalisation term $Z = \sum_{b' \in B} \mathbb{P}[Y=b'] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b']$. Then to compute the [[Maximum a posteriori probability estimate (MAP)|Maximum a posteriori probability]] we don't need to compute $Z$ and we let
$$
f_{MAP}(a_1, a_2, \ldots, a_n) = \mbox{arg}\max_{b \in B} \mathbb{P}[Y=b] \prod_{i=1}^n \mathbb{P}[A_i = a_i \vert Y = b].
$$
This exactly forms our Naive Bayes classifier for this problem.

## Run time

It is [[Eager learner|eager learner]] so requires you to sample the data initially. Though we only ever need to see each data point once - so is fairly fast. The estimating of the parameters is fairly simple. This model also has the minimum number of parameters you need to factor in most 

## Correctness

Whilst this does may a large assumption about the different attributes. Empirically this is considered very successful. It is thought that Google use this a lot in gmail for actual spam!

## Limitations

- It makes a strong assumption that the attributes are not related to one another, which seems ridiculous.
	- It is very venerable to co-dependent variables as its influence will grow exponentially the more variables are related. (i.e. if 3 variables were the same we would cube that term.)
	- Though in practice it turns out not to matter that much!
- If any of the $\mathbb{P}[A_i = a_i \vert Y = b]$ is zero, it zeros out the entire product.
	- We should account for this by always making these values non-zero. This is called "smoothing" of the probabilities.
	- We need a very large amount of data to guarantee our probabilities are accurate. 
