---
aliases:
checked: false
course: 'CS6215 Introduction to Graduate Algorithms'
created: 2023-10-09
draft: false
last_edited: 2023-11-11
title: Week 8 - RSA
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - RSA

To talk about the [RSA](../../general/rivest-shamir-adleman_algorithm_(rsa_algorithm).md) algorithm we first need a little more theory.

[Fermat's little theorem](../../general/fermat's_little_theorem.md)

In fact we need a generalisation of [Fermat's little theorem](../../general/fermat's_little_theorem.md) called [Euler's theorem (modular arithmetic)](../../general/euler's_theorem_(modular_arithmetic).md).

[Euler's theorem (modular arithmetic)](../../general/euler's_theorem_(modular_arithmetic).md)

Where we define [Euler's totient function](../../general/euler's_totient_function.md) as follows.

[Euler's totient function](../../general/euler's_totient_function.md)

For example if $n$ was a prime power we would have.

[Claim 2](../../general/eulers_product_formula_(totient_function).md#claim-2)
[Proof of Claim 2](../../general/eulers_product_formula_(totient_function).md#proof-of-claim-2)

For [RSA](../../general/rivest-shamir-adleman_algorithm_(rsa_algorithm).md) it is also good to know

[Claim 1](../../general/eulers_product_formula_(totient_function).md#claim-1)
[Proof of Claim 1](../../general/eulers_product_formula_(totient_function).md#proof-of-claim-1)

Which as a corollary has $\phi(pq) = (p-1)(q-1)$ for two distinct prime numbers.

## [RSA](../../general/rivest-shamir-adleman_algorithm_(rsa_algorithm).md) idea

Here we want to pass a message $z \in \mathbb{Z}$ from one person to another where the message sent between them is unintelligible without more information.

Let $p$ and $q$ be distinct primes. We are going to use [Euler's theorem (modular arithmetic)](../../general/euler's_theorem_(modular_arithmetic).md) that
$$z^{(p-1)(q-1)} = z \ (mod \ pq)$$
to recover a message.

[Rivest-Shamir-Adleman algorithm (RSA algorithm)](../../general/rivest-shamir-adleman_algorithm_(rsa_algorithm).md)

## Selecting random primes

The first stage of the [RSA](../../general/rivest-shamir-adleman_algorithm_(rsa_algorithm).md) algorithm is to select two random $n$-bit primes. To do this we first select a random number by randomly selecting each bit in this number.

As [primes](../../general/prime.md) are dense the probability that this number is prime is $1/n$. So we just keep repeating ourselves until we hit a [prime](../../general/prime.md) number.

```pseudocode
random_prime(n):
	Input: n the length of the number in bits.
	Output: A prime number that has n-bits.
1. Select a random n-bit number.
2. If it is prime return it
3. Go back to step 1.
```

Though how do we check if a number is [prime](../../general/prime.md).

## Fermat's test

If $r$ is a [prime](../../general/prime.md) then for all $1 \leq z < r$ we have
$$z^{r-1} = 1 \ (mod \ r).$$
So if we find $z$ where $z^{r-1} \not = 1$ (mod $r$) we know $r$ is composite.

Such $z$ are called a [Fermat witness](../../general/fermat_witness.md) for $r$ and every composite number has one.

[Existence of a Fermat witness if and only if composite](../../general/existence_of_a_fermat_witness_if_and_only_if_composite.md)

However, the [Fermat witness](../../general/fermat_witness.md) constructed in the proof are not dense in the numbers between $1$ to $r-1$. We need the existence of [non-trivial Fermat witness](../../general/fermat_witness.md) to guarantee this.

[Carmichael number](../../general/carmichael_number.md)

Luckily for us the existence of [Carmichael numbers](../../general/carmichael_number.md) is rare. The first couple are 561, 1105, 1729, ...

[Non-trivial Fermat witnesses are dense](../../general/non-trivial_fermat_witnesses_are_dense.md)

## Simple Primality testing algorithm

We want to use the above to test the primality of a number randomly.

```pseudocode
Primality Test(r)
	Input: An postive integer r.
	Output: If the algorithm thinks r is prime or not
1. Choose z_1, ..., z_k randomly from {1,2, ... , r-1}
2. For i = 1 -> k
	1. Compute z_i^{r-1} (mod r)
3. If for all i, z_i^{r-1} = 1 (mod r) then output r is prime
4. Otherwise output r is composite
```

This algorithm is always correct if $r$ is prime. However, there are two cases where we can be unlucky:
1. $r$ is a [Carmichael number](../../general/carmichael_number.md), then it is quite likely we will return it is prime, or
2. We are unlucky $r$ is composite and not a [Carmichael number](../../general/carmichael_number.md) then
$$ \mathbb{P}(\mbox{algorithm says } r \mbox{ is prime}) \leq \frac{1}{2^k}.$$
We can adapt this algorithm to search for non-trivial square roots of 1 mod $r$ that only exist when $r$ is not prime also. This doesn't take into account [Carmichael numbers](../../general/carmichael_number.md) so makes the algorithm slightly safer.

