---
aliases:
  - bucket sort
created: 2026-04-07
date_checked:
draft: false
last_edited: 2026-04-07
tags:
  - programming
title: Bucket sort
type: algorithm
---

This is an algorithm used to solve the [sorting problem](sorting_problem.md) that distributes elements into buckets, sorts each bucket individually, and then concatenates the results. The algorithm works as follows:

1. Create $k$ empty buckets.
2. Distribute the $n$ elements into the buckets based on a mapping function (typically using the element's value range).
3. Sort each individual bucket (often using [insertion sort](insertion_sort.md) or recursively using bucket sort).
4. Concatenate the sorted buckets in order.

The key to efficient bucket sort is choosing an appropriate number of buckets $k$ and ensuring the input data is relatively uniformly distributed across the value range.

# Run time

The time complexity of bucket sort is $O(n + k)$ where $n$ is the number of elements and $k$ is the number of buckets.

## Near-linear performance

Bucket sort can achieve **near-linear time complexity** $O(n)$ when you choose $k$ correctly. Specifically:

- If you set $k = \Theta(n)$ (i.e., the number of buckets is proportional to the number of elements), the $O(n + k)$ complexity becomes $O(n + n) = O(n)$.
- This assumes the elements are uniformly distributed across buckets, so each bucket contains roughly $O(1)$ elements.
- With $O(1)$ elements per bucket, sorting each bucket takes constant time, and the total work is linear.

The algorithm performs best when the input data is uniformly distributed. If all elements end up in a single bucket, the performance degrades to the complexity of the sorting algorithm used for individual buckets (e.g., $O(n^2)$ for insertion sort).

# Space complexity

Bucket sort requires $O(n + k)$ additional space for the buckets and the elements being sorted.
