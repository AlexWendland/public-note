---
aliases: 
checked: false
created: 2024-01-24
last_edited: 2024-01-24
draft: false
tags:
  - programming
type: algorithm
---
# Boosting

Boosting is an [[Ensemble learning]] method that uses multiple instances of another model to average them out to make a classifier that is better than any one individual one.

Suppose we are in the [[Modelling framework|modelling framework]] where $B = \{-1,1\}$ and we have a training set $T$ where $(a_t, b_t) = t \in T$. Boosting iteratively train classifiers $h_i: A \rightarrow \mathbb{R}$ based on how the past classifiers have performed. To do this before training $h_i$ we define a distribution $\mathbb{D}_i$ on $A_T = \{a_t \vert t \in T\}$. 

We set  
$$\mathbb{D}_1(a) = \frac{1}{\vert T \vert}.$$
To define the other terms lets introduce some notation.

Let $\epsilon_i$ be the [[Error rate (modelling)|error rate]] of $h_i$ with respect to $\mathbb{D}_i$ 

Set our learning rate
$$
\alpha_i = \frac{1}{2} \ln \left ( \frac{1 - \epsilon_i}{\epsilon_i} \right ).
$$
Other choices of $\alpha_i$ can be made. 

Now define $\mathbb{D}_{i+1}$ iteratively by setting
$$
C_{i,t} = \mathbb{D}_i(a_t) \cdot e^{- \alpha_i \ b_t \ h_i(a_t)}, \ \mbox{ with } \ Z_i = \sum_{t \in T} C_{i,t}$$
to give
$$\mathbb{D}_{i+1}(a_t) = \frac{C_{i,t}}{Z_i}.
$$
Note that if $b_t$ and $h_i(a_t)$ share the same sign then the power of $e$ is negative and we decrease the weight of $a_t$ whereas if they don't we increase the weight of $a_t$ (generally there are some cases where this isn't true!).

Once we have trained for some large number times $N$ we aggregate this all by defining our output 
$$\hat{f}(a) = \mbox{sgn}\left ( \sum_{i = 1}^N \alpha_t h_t(a) \right )$$ with $\mbox{sgn}$ being the [[Sign function]].

## Pseudocode

```pseudocode
Name(classifier, N, T):
	Input:
		classifier - some way to train a classifier given some training data and a distrubution.
		N - the number of itterations we want to do.
		T - pairs of points (a_t, b_t) to train on.
	Output:
		a moddel f on the space A to {-1, 1}.
1. Set D: T -> [0,1] to be D(t) = 1/|T|
2. For i = 1, ... , number_of_itterations do
	2.1. let h_i = classifier(T, D)
	2.2. Set alpha_i = calculate_learning_rate(h_i, T, D)
	2.2. Set D = Update_distrubution(h_i, T, D, alpha_i)
3. Return sgn(sum(alpha_t h_t(x) for t in T))

calculate_learning_rate(h, T, D):
	Input:
		h - A classifier mapping points in A to a real number 
		T - pairs of points (a_t, b_t) to train on.
		D - A distrubution over T
	Output:
		a learning rate for this itteration
1. Set e = 0
2. For each t in T
	2.1. If b_t != sgn(h(a_t)) then
		2.1.1 Set e = e + D(t)
3. Return ln((1-e)/e)/2

Update_distrubution(h, T, D, alpha)
	Input:
		h - A classifier mapping points in A to a real number 
		T - pairs of points (a_t, b_t) to train on.
		D - A distrubution over T
		alhpa - a learning rate
	Output:
		a new distrubution over T
1. For each t in T
	2.1. Set C_t = D(t) exp(- alpha b_t h(a_t))
2. Set Z = sum(C_t for t in T)
3. Intialise new distrubution over T D'
4. For each t in T
	4.1. Set D'(t) = C_t/Z
5. Return D'
```

## Correctness

