---
aliases:
  - hash
  - hash function
  - hash functions
  - Hash functions
checked: false
created: 2023-10-10
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: definition
---
> [!tldr] Hash function
> A *hash function* $h$ is a function that takes an input in a given domain and returns a fixed-size string of [[Byte|bytes]] $h: K \rightarrow B$, this output is normally called the hash value. It should ideally be:
>
> - Uniformly distributed over its output,
> - Fast to compute, and
> - Minimize collisions - $h(k) = h(k')$ with $k \not = k'$.
>
>In security  settings it may also be useful to have them be:
>
> - Non-reversible - it is very hard to compute the inverse, and
> - Randomly distributed - so keys close in the input space are not close in the output space.

