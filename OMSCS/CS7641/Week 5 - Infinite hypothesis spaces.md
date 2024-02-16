---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-16
last_edited: 2024-02-16
publish: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Infinite hypothesis spaces

In [[Week 5 - Computational Learning Theory]] we developed a method to build a [[Probably approximately correct learnable (PAC)|PAC learner]] on a finite dimensional hypothesis space. However this breaks down in infinite dimensions. We need to get around this. 

## Lets just cheat

Whilst the [[Modelling paradigm|hypothesis space]] might be infinite theoretically, the actual number of distinct hypothesises could be finite. Then we can fall back on the previous work.

>[!example] Discrete problem domain
>Let $A=\{i \in \mathbb{N} \vert i \leq 10\}$ and $B = \{T,F\}$. Then notice that $Fun(A,B) = 2^10$ which is finite. If we had $H = \{\ln(x) \geq \theta \ \vert \ \theta \in \mathbb{R}\}$  then $H$ is finite as $\theta \in \mathbb{R}$. However, in reality there are at most 11 realised functions here $\{x > n \vert 0 \leq n \leq 10, \ n \in \mathbb{Z}\}$ so we have a finite hypothesis space. 


