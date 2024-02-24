---
aliases:
  - genetic algorithms
  - genetic algorithm
checked: false
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - programming
  - machine-learning
type: algorithm
---
# Genetic algorithm (meta)

Suppose we have a [[Optimisation problem|optimisation problem]] which as two properties associated to is [[Function domain|domain]] $A$ 
- There is a method to make a small change to any $a \in A$ called a [[Mutation (genetic algorithms)|mutation]] $M: A \rightarrow \mathcal{P}(A)$ where any of $m(a)$ are a small change to $a$. 
- It has some [[Crossover (genetic algorithms)|crossover function]] $C: A \times A \rightarrow A^k$.

Then for a collection of points $P \subset A$ called a *population* the algorithm assess the fitness of each point $f(a)$ for $a \in P$.

It then selects a subset $S \subset P$ to make the next generation. There are multiple ways to do this:
- Take the most fit as ranked by fitness, or
- Use ideas for [[Simulated Annealing]] and select points based on some weighted probability distribution based on $f(a)$.

The from our subset $S \subset P$ use the [[Mutation (genetic algorithms)|mutation]] $M$ and [[Crossover (genetic algorithms)|crossover function]] $C$ to generate a new population.  

We keep doing this for a number of *generations* and then stop at some point determined by a stopping criteria.
## Pseudocode

```pseudocode
genetic_algorithm(optimise, selection_function, mutation, crossover, stopping_condition, population_size):
	Input:
		optimise: The function you are looking to optimise
		selection_function: The function that picks which population to keep
		mutation: A function that generates small mutations.
		crossover: A function that can make new points from two other.
		stopping_condition: Some condition to stop.
		population_size: The size of the population each itteration (can change on some parameters).
	Output: Some a in A that hopefully is an optimum.
1. Generate a random starting population of population_size.
2. While stopping_condition is not met
	1. Let survivors = selection_function({(a, optimise(a)) for a in popluation})
	2. Use mutation and crossover to generate a new population of size population_size.
3. Return argmax optimise(a) for a in popluation
```

## Run time



## Correctness

