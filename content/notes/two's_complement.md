---
aliases: []
created: 2023-04-20
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Two's complement
type: representations
---

This is a way to represent [signed integers](signed_or_unsigned_integers.md). Assuming the leftmost digit is the most significant [bit](bit.md) then:

- **Sign digit**: Whether the number is positive or negative
- **Numerical representation**: The magnitude of the number

So if you store your signed integer as a [byte](byte.md), the leftmost [bit](bit.md) would represent the sign and the other 7 [bits](bit.md) would represent the magnitude.

# Positive numbers

For example when representing 10 in 7 bits you would use

$$
000\ 1010 = 0*2^7 + 0*2^6 + 0*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
$$

Therefore, as 10 is positive, its full representation would be

0|000 1010

with the 0 representing positive numbers.

# Negative numbers

This is where things get interesting. Let's first start with the formula and work backwards to explain why this works.

Let's say we want to represent -10:

1. Start with the representation of the absolute value of number in binary e.g. 10 = 0000 1010
2. Flip all the digits e.g. 1111 0101
3. Add 1 to the representation and ignore overflow (this is pretty key as $-2^7$ is a legit option) e.g. 1111 0110

Excellent, so the leftmost digit is 1 (indicating it is not positive) and this representation is unique. Whilst this might require some mathematical justification, we actually use all the available space in the [byte](byte.md). For example, $0111\ 1111 = 2^7 - 1$, $0000\ 0000 = 0$, $1000\ 0000 = -2^7$, and $1111\ 1111 = -1$.

Let's also cover how to decimalise a binary representation of a negative number. Suppose we wanted to convert $1100\ 1100$:

1. First subtract 1 from the expression (or add -1 but we will come back to that) e.g. 1100 1011.
2. Flip all the digits e.g. 0011 0100.
3. Convert the binary number into decimal representation and put a negative sign on it e.g. 32 + 16 + 4 = 52, so the number is -52.

That seems straightforward enough, but surely there must be a simpler way to do this?

# Addition

You add two numbers just as you would [unsigned integers](signed_or_unsigned_integers.md) by starting from the least significant [bit](bit.md) (right most in our example) and carry the overflows forward. This works even when adding two negatives or a negative with a positive!

## Two positive

Let's add 10 = 0000 1010 with 12 = 0000 1100

$$
\begin{aligned}
10 + 12 & = 0000\ 1010\\
& + 0000\ 1100\\
& = 0001\ 0110\\
& = 16 + 4 + 2\\
& = 22.
\end{aligned}
$$
## Negative with a positive

Let's add -5 = 1111 1011 with 10 = 0000 1010

$$
\begin{aligned}
-5 + 10 & = 1111\ 1011 \\
& + 0000\ 1010\\
& = 0000\ 0101\\
& = 4 + 1\\
& = 5.
\end{aligned}
$$
## Two negative

Let's add -5 = 1111 1011 with -16 = 1111 0000

$$
\begin{aligned}
-5 + (-16) & = 1111\ 1011 \\
& + 1111\ 0000\\
& = 1110\ 1011\\
& = (-)\ 0001\ 0101\\
& = (-)\ (16 + 4 + 1)\\
& = -21.
\end{aligned}
$$

> [!note] Overflow detection
> You can use the sign digit to detect overflow, i.e. if you add two positive numbers, the outcome should be positive.

# Comparison

This essentially works the same as unsigned integers: starting from the most significant [bit](bit.md), work your way to the least significant until you see a difference. Whichever is 1 in the differing place is larger.

The only exception to this rule is if the sign [bits](bit.md) of the two numbers are different. In that case, the positive number is larger.

# Conclusion

Two's complement is indeed an elegant method for encoding negative numbers. It requires minimal additional logic compared to unsigned integer arithmetic.
