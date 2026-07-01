---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-06-29'
date_checked: '2026-06-29'
draft: false
last_edited: '2026-06-29'
tags:
  - OMSCS
title: Week 8 - Structured Representations
type: lecture
week: 8
---

So far in the course we have covered fully connected layers and CNNs.
The fully connected layer is ambiguous about the structure it represents - whereas with the CNN we put some architectural bias in how the data should behave.
I.e. there should be similar small patterns that could appear anywhere in our data.
However, sometimes we want to represent structured data like in an image we want to pull out the relationships in the image—e.g., 'man riding horse', 'horse in front of mountain'.
We will talk about 3 network architectures that can help us with this:

- Recurrent Neural Networks

- Attention-based Networks

- Graph-Based Networks

When we talk about structure of information - this will mainly be a graph where things are represented as nodes and relationships are represented as edges.
A representation of something would then be a mapping from that thing into a graph.
When representing information there are several important properties:

- *State*: Compactly representing all the data we have processed so far.

- *Neighborhoods*: Which other elements to incorporate.
Can be seen as selecting from a set of elements.
Typically done with some similarity measure or attention.

- *Propagation of information*: How to update information given selected elements.

These three properties act as a useful lens for comparing the architectures above.
Each architecture makes different choices: what constitutes a neighborhood, how similarity is measured, and how information from neighbors is aggregated into the new state.

# Attention mechanisms

Suppose you have embedded your state into a vector space — i.e., each node in a graph becomes a vector.
Then given a collection of items $u_i$ for $1 \leq i \leq N$ you want to find the closest weighted linear combination of them to a new vector $q$ (query vector).
This is an attention mechanism: the *neighborhood* is all $u_i$, and the weights define how much each contributes.
It is common in this case to use softmax, e.g.

$$
a_j = \frac{e^{u_j \cdot q}}{\sum_k e^{u_k \cdot q}}, \quad \text{output} = \sum_k a_k u_k.
$$

The advantage of doing this is it is differentiable with respect to $q$ and $u_i$.

This allows us to combine information in a structured way to give a new output that is close to another bit of information.

## Keys, Queries, and Values

In the formulation above, $u_i$ plays a dual role: it is both what we match against (to compute the weight $a_i$) and what we return in the weighted sum.
In practice these are often separated into three distinct projections:

- *Query* $Q$: what we are looking for.
- *Key* $K$: what we match the query against to compute attention weights.
- *Value* $V$: what we actually retrieve and aggregate.

This separation gives the model more flexibility and is the formulation used in transformers.

# Non-local layer

CNNs are *local* — each output depends only on a small spatial neighborhood of the input.
A non-local layer breaks this constraint, allowing any position to attend to any other position regardless of spatial distance.

Concretely, assume we have an input $x_i$ and we want to produce an output $y_i$.
We define $y_i$ by how $x_i$ relates to *all* $x_j$:

$$
y_i = \frac{1}{C(x)} \sum_{j} f(x_i, x_j) g(x_j)
$$

where $f$ is some similarity measure, $g$ is a learned linear transform of the value, and $C(x) = \sum_j f(x_i, x_j)$ is a normalisation factor (analogous to the softmax denominator) so the output is a weighted average rather than a weighted sum.
Some examples are:

$$
f(x_i, x_j) = e^{x_i^Tx_j}, \quad g(x_j) = W_g x_j
$$

In this example we are similar to a fully connected layer with $g$, but we weight each contribution by how similar $x_i$ is to $x_j$ — a dynamic, input-dependent weighting rather than a fixed learned one.
