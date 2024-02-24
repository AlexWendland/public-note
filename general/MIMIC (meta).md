---
aliases: 
checked: false
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - programming
type: algorithm
---
# MIMIC (meta)

Suppose we have some [[Optimisation problem]] with input space $A$ and fitness function $f: A \rightarrow \mathbb{R}$. Then for any $\theta \in \mathbb{R}$ define
$$
P^{\theta}(a) = \begin{cases} \frac{1}{Z_{\theta}} & \mbox{if } f(a) \geq \theta\\ 0 & \mbox{otherwise.} \end{cases}$$
(Where $Z_{\theta}$ is some normalisation coefficient to make this a [[Probability distribution|probability distribution]].) Then let $\theta_{min} = \min_{a \in A} f(a)$ and $\theta_{max} = \max_{a \in A} f(a)$ then $P^{\theta_{min}}$ is the uniform distribution over $A$ whereas $P^{\theta_{max}}$ is the uniform distribution over the optimum.

The goal if MIMIC is to simulate $P^{\theta}$ whilst slowing increasing $\theta$ to find the maximum.

Functionally how we do that is similar to [[Genetic algorithm (meta)|genetic algorithm]]. We will suppose we currently have our [[Probability distribution|probability distribution]] $P^{\theta_t} : A \rightarrow [0,1] \subset \mathbb{R}$ we will obtain samples $S$ from $A$ using $P^{\theta_t}$. Let $\theta_{t+1}$ to be some predefined quartile of $f(S)$ for example the median. Then we have some positive sample $S' = \{s \in S \vert f(s) \geq \theta_{t+1}\}$ and negative samples $S \backslash S'$ to try and estimate the distribution $P^{\theta_{t+1}}$. 

The method to estimate $P^{\theta_{t+1}}$ from $S'$ encodes some domain knowledge about the system - this can very from problem to problem.

## Pseudocode

```pseudocode
mimic(optimise, number_of_samples, percentile, probability_constructor, stopping_condition):
	Input:
		optimise: The function you are looking to optimise.
		number_of_samples: The number of samples to draw.
		percentile: The percentile to use to cut samples.
		probability_constructor: Some method that uses a probability distribution and +/-ve samples to generate another probability distribution.
		stopping_condition: Some condition to stop.
	Output: Some a in A that hopefully is an optimum.
1. Let P be the uniform distrubution
2. Whilst the stopping_condition is not met
	1. Let S be number_of_samples drawn from P
	2. Let theta be the percentile of {f(s) for s in S}
	3. Let S' = {s in S such that f(s) >= theta}
	4. Let P = probability_constructor(S', S \ S', P)
3. Draw a sample from P and return it.
```

## Run time

This strongly depends on how we construct our probability distribution. However, normally this takes longer than other randomised algorithms though with fewer iterations.

This is useful when calculating the function on a set of points is hard. 

## Correctness

