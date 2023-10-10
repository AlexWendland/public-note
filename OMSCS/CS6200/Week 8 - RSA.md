---
aliases: 
type: lecture
publish: true
created: 2023-10-09
last_edited: 2023-10-09
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 8
chatgpt: false
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

