---
aliases:
  - Neural networks
  - neural net
  - hidden layer
  - input layer
  - output layer
  - neural networks
created: 2024-01-20
date_checked:
draft: false
last_edited: 2026-02-05
tags: []
title: Neural network
type: definition
---
>[!definition] Neural networks
>A *neural network* consists of the following information:
>- A [directed acyclic graph](directed_acyclic_graph_(dag).md) $N = (V,E)$ where the source vertices are called the *input layer* $I \subset V$ and the sink vertices are called the *output layer* $O \subset V$,  and
>- For each $v \in V \backslash I$ we have a [perceptron](perceptron_(neural_network).md) $p_v: \mathbb{R}^{\vert In(v) \vert} \rightarrow\mathbb{R}$.
>
>In the [Modelling framework](modelling_framework.md) this would simulate something with $A \subset \mathbb{R}^{\vert I \vert}$ and $B \subset \mathbb{R}^{\vert O \vert}$.
>To run the model you compute a value for each vertex $x_v \in \mathbb{R}$ for $v \in V$. For input $(a_i)_{i \in I}$ we associate $a_i =: x_i$ to vertex $i \in I$. Then for all $y \in V \backslash I$ once all of $In(y)$ have values we set
>$$x_y := p_y((x_v)_{v \in In(y)}).$$
>To generate output vector $(x_o)_{o \in O} \in B$.
>
>Normally the topology of $N$ is chosen so that the vertices $V$ can be [partitioned](partition_(set).md) into $L_i$ for some $1 \leq i \leq k$. Where for all $v \in L_i$ $In(v) = L_{i-1}$ and $Out(v) = L_{i+1}$. Where $L_1$ is the *input layer* and $L_k$ is the *output layer* all other layers are called *hidden layers*.

