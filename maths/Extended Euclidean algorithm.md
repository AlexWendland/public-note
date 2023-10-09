---
aliases: 
type: algorithm
publish: false
created: 2023-10-09
last_edited: 2023-10-09
tags:
  - maths
chatgpt: false
---
# Extended Euclidean algorithm

This algorithm extends the [[Euclidean algorithm]] to be able to calculate the [[Greatest common divisor|greatest common divisor]] of two integers.

## Algorithm

```pseudocode
extended_euclidean(x,y):
	Input: integers x, y where x >= y >= 0
	Output: integers d, a, b where d = gcd(x,y) and d = xa + yb

```