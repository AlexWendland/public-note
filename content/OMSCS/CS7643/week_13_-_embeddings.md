---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-07-21'
date_checked:
draft: false
last_edited: '2026-07-21'
tags:
  - OMSCS
title: Week 13 - Embeddings
type: lecture
week: 13
---

When we have large quantities of data it can be useful to understand it in relation to one another.
By embedding this data into a high dimensional vector space so that the relative distances preserve some meaning, we can speed up asking questions about our data.
The most common example is embedding words into a vector space using the word2vec algorithm - which using vector distances can tell us how pairs of words relate to one another.

# Word embeddings

> [!quote] J.R.Firth 1957
> You shall know a word by the company it keeps.

To demonstrate this we will give the word2vec algorithm below.
To generate a word embedding we use n-grams.
This is a context window around a word within some text.
This is normally the $n$ words before and after it.
Given an n-gram which consists of $2n + 1$ words we either use the 2n context words to predict the word or the other way round.
We train a small neural network with a single hidden layer for this task.

There are two ways to do this:

- Skip-gram: given the word in the middle, predict the context words around it.

- Continuous bag of words: given the context words, predict the word they surround.

In this we will focus on the skip-gram model.
Formally for a series of words $\{w_i\}_{i=1}^T$ we define the loss for our parameters $\theta$ as the following:
$$
L(\theta) = \sum_{t=1}^T \prod_{-n \leq j \leq n, j \neq 0} \mathbb{P}(w_{t+j} \vert w_t; \theta) 
$$
With the objective function being the average negative log-likelihood:
$$
J(\theta) = - \frac{1}{T} \log L(\theta) = - \frac{1}{T} \sum_{t=1}^T \sum_{-n \leq j \leq n, j \neq 0} \log \mathbb{P}(w_{t+j} \vert w_t; \theta)
$$

Then to calculate the $\mathbb{P}(w_{t+j} \vert w_t; \theta)$ we use the embedding.
The small neural network has two weight matrices $U$ and $V$, each of shape $\vert \mathcal{W} \vert \times d$ where $\mathcal{W}$ is the vocabulary and $d$ is the embedding dimension.
For each word $w \in \mathcal{W}$ in our vocabulary, $u_w$ is the row of $U$ corresponding to $w$ and $v_w$ is the row of $V$ corresponding to $w$.
Concretely the forward pass is:

1. Look up the center word's row in $U$ to get $u_{w_t} \in \mathbb{R}^d$ (the hidden layer).
2. Compute the dot product of $u_{w_t}$ with every row of $V$ to score each candidate context word.
3. Apply softmax to get a probability distribution over the vocabulary:

$$
\mathbb{P}(w_{t+j} \vert w_t; \theta) = \frac{\exp(u_{w_t} \cdot v_{w_{t + j}})}{\sum_{w \in \mathcal{W}} \exp(u_{w_t} \cdot v_{w})}
$$

The reason for having two separate matrices rather than one is to break symmetry — a single matrix would force $\mathbb{P}(w' \vert w) = \mathbb{P}(w \vert w')$, which is not desirable.

Both $U$ and $V$ are learned via backpropagation.
After training, $U$ (the input/center-word matrix) is taken as the final word embeddings.
Some implementations use $V$ or the average of $U$ and $V$, but $U$ alone is the standard choice.

Word embeddings can convey information about the language.
For example: $u_{king} + u_{woman} - u_{man} \approx u_{queen}$.

# Graph embeddings

We can apply the same idea to graphs.
That is given a graph we want to embed it into a high dimensional space so that connected nodes are close together.
Different edges can have different types of connections and this should also be captured by the embedding as well.

## PyTorch-BigGraph

This is a particular kind of graph embedding.
Suppose we have a directed graph $G = (V,E)$ where edges have a type of relation $t: E \rightarrow R$.
It is handy to think of edges as triples $(s, d, r) \in V \times V \times R$.
We define a function of similarity for an edge:
$$
f(s,d,r) = \text{cosine-similarity}(\theta_s, \theta_r + \theta_d)
$$
Which gives us a loss function:
$$
L = \sum_{(s,d,r) \in E} \sum_{\substack{e' \in E \\ e' = (s',d,r) \text{ or } e' = (s,d',r)}} \max(f(e) - f(e') + \lambda, 0)
$$

Similarly to word embeddings this allows us to understand relationships within our graph that might not have been there in the first place - such as missing information about someone's partner or place of birth.

