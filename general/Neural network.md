---
aliases:
  - Neural networks
  - neural net
checked: false
created: 2024-01-20
last_edited: 2024-01-20
publish: true
tags: 
type: definition
---
>[!tldr] Neural networks
>A *neural network* consists of the following information:
>- A [[Directed acyclic graph (DAG)|directed acyclic graph]] $N = (V,E)$ where the source vertices are called the *input layer* $I \subset V$ and the sink vertices are called the *output layer* $O \subset V$,  and
>- For each $v \in V \backslash I$ we have a [[Perceptron (neural network)|perceptron]] $p_v: \mathbb{R}^{\vert In(v) \vert} \rightarrow\mathbb{R}$.  
>
>In the [[Modelling framework]] this would simulate something with $A \subset \mathbb{R}^{\vert I \vert}$ and $B \subset \mathbb{R}^{\vert O \vert}$. 
>To run the model you compute a value for each vertex $x_v \in \mathbb{R}$ for $v \in V$. For input $(a_i)_{i \in I}$ we associate $a_i =: x_i$ to vertex $i \in I$. Then for all $y \in V \backslash I$ once all of $In(y)$ all have values we set 
>$$x_y := p_y((x_v)_{v \in In(y)}).$$
>

