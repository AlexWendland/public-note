---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
name: Simulated Annealing
tags:
  - programming
  - machine-learning
type: algorithm
---
# Simulated Annealing

Suppose we have a [optimisation problem](optimisation_problem.md) where $A$ has some sense of neighbourhood $N(a)$ for each point $a \in A$.

Then we want to emulate [Hill climbing](hill_climbing.md) but probabilistically allow for random walking. We do this by randomly deciding to take moves from $x$ to $x_t$ based on the temperature of the algorithm at that time $T$ this is given by
$$P(x,x_t,T) = \begin{cases} 1 & \mbox{if } f(x_t) \geq f(x)\\ \exp{\frac{f(x_t) - f(x)}{T}} & \mbox{otherwise.} \end{cases}$$
Then we just modify what is done in [Hill climbing](hill_climbing.md) with this and gradually decrease the temperature and we have simulated annealing.

## Pseudocode

```pseudocode
simulated_annealing(optimise, neighourhood, max_itterations, update_temperature, starting_temperature):
	Input:
		optimise: The function you are looking to optimise
		neighbourhood: A function that returns the neighbourhood of a point A -> P(A).
		max_itterations: An integer that tells us when to stop.
		update_temperature: A method to update the temperature.
		starting_temperature: The starting value of the temperature.
	Output: Some a in A that hopefully is a local optimum.
1. Pick a random start point current in A.
2. Set temperature = starting_temperature
3. For iteration in 1, ..., max_itterations
	1. Pick a random point to_switch in N(current).
	2. Set current = to_switch with probability P(current, to_switch, temperature)
	3. Set temperature = update_temperature(T, iteration)
4. Return current
```

## Run time



## Correctness

