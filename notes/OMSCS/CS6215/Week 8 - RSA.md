---
aliases:
checked: false
course: '[[CS6215 Introduction to Graduate Algorithms]]'
created: 2023-10-09
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - RSA

To talk about the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] algorithm we first need a little more theory.

![[Fermat's little theorem]]

In fact we need a generalisation of [[Fermat's little theorem]] called [[Euler's theorem (modular arithmetic)]].

![[Euler's theorem (modular arithmetic)]]

Where we define [[Euler's totient function]] as follows.

![[Euler's totient function]]

For example if $n$ was a prime power we would have.

![[Eulers product formula (totient function)#Claim 2]]
![[Eulers product formula (totient function)#Proof of Claim 2]]

For [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] it is also good to know

![[Eulers product formula (totient function)#Claim 1]]
![[Eulers product formula (totient function)#Proof of Claim 1]]

Which as a corollary has $\phi(pq) = (p-1)(q-1)$ for two distinct prime numbers.

## [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] idea

Here we want to pass a message $z \in \mathbb{Z}$ from one person to another where the message sent between them is unintelligible without more information.

Let $p$ and $q$ be distinct primes. We are going to use [[Euler's theorem (modular arithmetic)]] that
$$z^{(p-1)(q-1)} = z \ (mod \ pq)$$
to recover a message.

![[Rivest-Shamir-Adleman algorithm (RSA algorithm)]]

## Selecting random primes

The first stage of the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] algorithm is to select two random $n$-bit primes. To do this we first select a random number by randomly selecting each bit in this number.

As [[Prime|primes]] are dense the probability that this number is prime is $1/n$. So we just keep repeating ourselves until we hit a [[Prime|prime]] number.

```pseudocode
random_prime(n):
	Input: n the length of the number in bits.
	Output: A prime number that has n-bits.
1. Select a random n-bit number.
2. If it is prime return it
3. Go back to step 1.
```

Though how do we check if a number is [[Prime|prime]].

## Fermat's test

If $r$ is a [[Prime|prime]] then for all $1 \leq z < r$ we have
$$z^{r-1} = 1 \ (mod \ r).$$
So if we find $z$ where $z^{r-1} \not = 1$ (mod $r$) we know $r$ is composite.

Such $z$ are called a [[Fermat witness]] for $r$ and every composite number has one.

![[Existence of a Fermat witness if and only if composite]]

However, the [[Fermat witness]] constructed in the proof are not dense in the numbers between $1$ to $r-1$. We need the existence of [[Fermat witness|non-trivial Fermat witness]] to guarantee this.

![[Carmichael number]]

Luckily for us the existence of [[Carmichael number|Carmichael numbers]] is rare. The first couple are 561, 1105, 1729, ...

![[Non-trivial Fermat witnesses are dense]]

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
1. $r$ is a [[Carmichael number]], then it is quite likely we will return it is prime, or
2. We are unlucky $r$ is composite and not a [[Carmichael number]] then
$$ \mathbb{P}(\mbox{algorithm says } r \mbox{ is prime}) \leq \frac{1}{2^k}.$$
We can adapt this algorithm to search for non-trivial square roots of 1 mod $r$ that only exist when $r$ is not prime also. This doesn't take into account [[Carmichael number|Carmichael numbers]] so makes the algorithm slightly safer.

