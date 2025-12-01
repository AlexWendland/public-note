---
aliases:
  - sequence
  - sequences
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
name: Sequence
tags:
  - maths
type: definition
---
# Sequence

A sequence is a list of objects, potentially finite or infinite.

In [Maths Index](maths_index.md) for a finite sequence of length $n$ this will be denotes by
$$a_1, a_2, \ldots a_n$$ which secretly is a function
$$a: [1,n] \rightarrow D$$ where $D$ is your domain of interest.

However for 1 way finite sequences we use
$$a_1, a_2, \ldots, a_n, \ldots$$ or $a: \mathbb{N} \rightarrow D$. For 2 way infinite sequence we would use
$$\ldots, a_{-n}, \ldots, a_{-1}, a_0, a_1 \ldots, a_n, \ldots$$ or $a: \mathbb{Z} \rightarrow D$.

When I say $D$ just think of the [Integers](integers.md) $\mathbb{Z}$ so such a sequence could be
$$
5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3
$$
