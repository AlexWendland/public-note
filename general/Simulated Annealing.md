---
aliases: 
checked: false
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - programming
  - machine-learning
type: algorithm
---
# Simulated Annealing

Suppose we have a [[Optimisation problem|optimisation problem]] where $A$ has some sense of neighbourhood $N(a)$ for each point $a \in A$.

Then we want to emulate [[Hill climbing]] but probabilistically allow for random walking. We do this by randomly deciding to take moves from $x$ to $x_t$ based on the temperature of the algorithm at that time $T$ this is given by
$$\mathbb{P}[x,x_t,T] = \begin{cases} 1 & \mbox{if } f(x_t) \geq f(x)\\ \exp{\frac{f(x_t) - f(x)}{T}} & \mbox{otherwise.} \end{cases}$$
Then we just modify what is done in [[Hill climbing]] with this and gradually decrease the temperature and we have simulated annealing.

## Pseudocode

```pseudocode
hill_climber(optimise, neighourhood, max_itterations, update_temperature, starting_temperature):
	Input:
		optimise: The function you are looking to optimise
		neighbourhood: A function that returns the neighbourhood of a point A -> P(A).
		max_itterations: An integer that tells us when to stop.
		update_temperature: A method to update the temperature.
		starting_temperature: The starting value of the temperature.
	Output: Some a in A that hopefully is a local optimum.
1. 
```

## Run time



## Correctness

