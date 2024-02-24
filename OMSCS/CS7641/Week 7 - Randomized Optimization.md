---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Randomized Optimization

We are now moving onto to [[Unsupervised learning]].

![[Unsupervised learning]]

The difference from [[Supervised learning|supervised learning]] is we don't get given labels - so how we actually learn the function is beyond me!

## Optimisation problem

![[Optimisation problem]]

There are lots of examples of this.
- Process control or optimisation, think chemical factory.
- Finding a route on a map.
- Find a root of a function!
- Neural network weights.
- Minimising error in another model!

There are a couple of good methods here: 
- Generate and test
	- Good when we have a small input space but complex function.
- Calculus:
	- We need the function to have a derivative and solvable!
- Search method like [[Newton Raphson method]]
	- Similar problems to calculus.
- Random Optimisation, todays lecture :)

## Hill climbing

![[Hill climbing]]

## Restart Hill climbing

![[Restart hill climbing ]]

## Simulated Annealing

The next class of algorithms is like hill climbing but we allow for a bit more random walking.

![[Simulated Annealing]]

Notice with the formula that if $T \rightarrow 0$ then this will make $P(x, x_t, T) \rightarrow 0$ for points where $f(x_t) < f(x)$ so it will start acting like [[Hill climbing]] whereas as $T \rightarrow \infty$ we have $P(x, x_t, T) \rightarrow 1$ so it will be close to a random walk.  

![[Simulated annealing ending probability]]

## Genetic Algorithms

In all the above examples, we just updated our next guess based on local properties. However, we might find a couple of points with good fitness and want to combine them to find out what properties they have that provide that good fit. 

![[Genetic algorithm (meta)]]

For the [[Crossover (genetic algorithms)|crossover function]] lets consider a concrete example.

>[!example] 8-bit strings crossover example
>Suppose $A = \{0,1\}^8$, how could we design a [[Crossover (genetic algorithms)|crossover function]]?

Suppose we are merging $00011011$ and $00110010$.

### One point crossover

We could choose an arbitrary point and do a switch of bit before and after this point. For example $C(00011011, 00110010) = (00010010, 00111011)$ where the first 4 bits of the first output is from the 1st input and the second 4 bits if from the second input - then vice versa for the second output.

### Uniform crossover

We could instead choose bits at random - either uniformly or weighted by their fitness. For example $C(00011011, 00110010) = (00010010, 00111011)$ where for the 3rd, 5th and 8th bit we choose from the first, second and second for the first output and vice versa for the second.

## Crossover choice

Notice that any choice of [[Crossover (genetic algorithms)|crossover function]] relies heavily on how you represent your data!

## Randomised algorithms

All the randomised algorithms here have been fairly simply and don't use history. There are more complicated ones that combine ideas from different algorithms and try to model the area they are searching. 

## MIMIC

Suppose we have some [[Optimisation problem]] with input space $A$ and fitness function $f: A \rightarrow \mathbb{R}$. Then for any $\theta \in \mathbb{R}$ define
$$
P^{\theta}(a) = \begin{cases} \frac{1}{Z_{\theta}} & \mbox{if } f(a) \geq \theta\\ 0 & \mbox{otherwise.} \end{cases}$$
(Where $Z_{\theta}$ is some normalisation coefficient to make this a [[Probability distribution|probability distribution]].) Then let $\theta_{min} = \min_{a \in A} f(a)$ and $\theta_{max} = \max_{a \in A} f(a)$ then $P^{\theta_{min}}$ is the uniform distribution over $A$ whereas $P^{\theta_{max}}$ is the uniform distribution over the optimum.

The goal if MIMIC is to simulate $P^{\theta}$ whilst slowing increasing $\theta$ to find the maximum.

