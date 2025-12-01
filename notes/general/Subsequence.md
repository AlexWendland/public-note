---
aliases:
  - subsequence
  - subsequences
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: definition
---
# Subsequence

Given a [[Sequence|sequence]] $a_1, a_2, \ldots, a_n$ a subsequence is $a_{i_1}, a_{i_2}, \ldots a_{i_k}$ is such that $i_j < i_j + 1$ (note this can apply to infinite [[Sequence|sequences]] as well). In other words, it is a subset of the sequence ordered such that the indices are increasing.

## Example

For the sequence
$$
5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3
$$
the following are all subsequences
$$
5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3
$$
$$
-3, 9, 1, 10
$$
$$9, 10, 8$$
however
$$
9, 10, 1
$$
is not as the indices are not increasing.
