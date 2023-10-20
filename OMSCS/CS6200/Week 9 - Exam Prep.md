---
aliases: 
type: exercise
publish: false
created: 2023-10-18
last_edited: 2023-10-18
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 8
chatgpt: false
---
# Week 8 - Exam Prepr (unassessed) 

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

## [[Modular arithmetic]]

> [!question] Problem 1.11 
> Is $4^{1536} - 9^{4824}$ divisible by 35?

Note that $1536*2 = 0$ mod $(5-1) \times (7-1) = 24$ and $4824*2 = 0$ mod $24$. So the question resolves to is $2^{0} - 3^{0} = 0$ mod $35$ which it is!   

> [!question] Problem 1.12 
> What is $2^{2^{2006}}$ (mod 3)?

1

> [!question] Problem 1.13 
> Is the difference of $5^{30,000}$ and $6^{123,456}$ a multiple of 31?

Note 31 is prime and $30,000 = 0$ mod $30$ and $123456 = 6$ mod $30$ so this problem boils down to $5^0 - 6^6 = 0$ mod $31$. $(6^2)^3 = 36^3 = 5^3 = 125 = 1$ mod $31$. So the answer is yes. 


> [!question] Problem 1.14
> Suppose you wish to compute the $n$th [[Fibonacci sequence|Fibonacci number]] $F_n$, modulo an integer $p$. Can you find an efficient way to do this?

Given there are only $p^2$ possible combinations of $(a,b)$ mod $p$ within the first $p^2$ $F_n$ there must be a repeating pattern $F_i, F_{i+1}$ and $F_j, F_{j+1}$ for $0 \leq i < j < p^2$.

1. Calculate up to the first $p^2$ values until we find repeating pattern $F_i, F_{i+1}$ and $F_j, F_{j+1}$ for $0 \leq i < j < p^2$.
2. If $n \leq j + 1$ output $F_n$.
3. Calculate $n - i = k$ mod $(j-i)$.
4. Return $F_{i+k}$ 

> [!question] Problem 1.18
> Compute $gcd(210,588)$ two different ways: by finding the factorisation of each number, and by the [[Euclidean algorithm]].

Way 1,

$210 = 21 \times 10 = 3 \times 7 \times 2 \times 5 = 2 \cdot 3 \cdot 5 \cdot 7$ 
$588 = 294 \times 2 = 2^2 \times 147 = 2^2 \times 3 \times 49 = 2^2 \times 3 \times 7^2$ 

so $gcd(210,588) = 2 \cdot 3 \cdot 7 = 42$.

Way 2,

| a   | b   | c   |
| --- | --- | --- |
| 588 | 210 | 2   |
| 210 | 168 | 1   |
| 168 | 42  | 4   |
| 42  | 0   | -   |

So $gcd(210,588) = 42$.

> [!question] Problem 1.20
> Find the inverse of 20 mod 79, 3 mod 62, 21 mod 91, and 5 mod 23.

We do this via the [[Extended Euclidean algorithm]]

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 79  | 20  | 3   | -1  | 4   |
| 20  | 19  | 1   | 1   | -1  |
| 19  | 1   | 19  | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $4 \times 20 = 1$ mod $79$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 62  | 3   | 20  | -1  | 21  |
| 3   | 2   | 1   | 1   | -1  |
| 2   | 1   | 2   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $3 \times 21 = 1$ mod $62$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 91  | 21  | 4   | 1   | -4  |
| 21  | 7   | 3   | 0   | 1   |
| 7   | 0   | -   | 1   | 0   |

So there is no inverse.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 23  | 5   | 4   | 2   | -9    |
| 5   | 3   | 1   | -1  | 2   |
| 3   | 2   | 1   | 1   | -1  |
| 2   | 1   | 2   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

So $5 \cdot 14 = 1$ mod $23$.

> [!question] Problem 1.22
> Prove or disprove: If $a$ has an inverse modulo $b$, then $b$ has an inverse modulo $a$.

Inverse existance followed by Euclids rule.

> [!question] Problem 1.24
> If $p$ is prime, how many elements of $\{0,1, \ldots, p^n-1\}$ have an inverse mod $p^n$?


> [!question] Problem 1.25
> Calculate $2^{125}$ mod $127$ using any method you choose?


> [!question] Problem 1.26
> What is the least significate decimal digit of $17^{17^{17}}

> [!question] Problem 1.27
> Consider an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] key set with $p=17$, $q=23$, $N=391$, and $e=3$. 
> a) What is the value of $d$ to make this a secrete key?
> b) What is the encryption of the message $M = 41$?

> [!question] Problem 1.28
> In an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] crypto system, $p=7$ and $q=11$. Find appropriate exponents $d$ and $e$.

> [!question] Problem 1.42
> Suppose that instead of using a composite $N = pq$ in the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] cryptosystem, we simply use a prime modulus $p$. As in [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]], we would have an encryption exponent $e$, and the encryption of a message $m$ mod $p$ would be $m^e$ mod $p$. Prove that this new cryptosystem is not secure, by giving an efficient algorithm to decrypt: that is, an algorithm that given $p$, $e$, and $m^e$ mod $p$ as input, computes $m$ mod $p$. Justify the correctness and analyze the running time of your decryption algorithm.

## [[Depth-first search (DFS)|DFS]] and [[Strongly connected components (directed graphs)|Strongly Connected Component]]

Problems 3.1-3.5, 3.7, 3.8, 3.11, 3.15, 3.16, 3.22, 3.24.

## [[Breath-first search (BFS)|BFS]] and Shortest path problems

Problems 4.1-4.3, 4.8, 4.11, 4.12-4.14, 4.20, 4,21.

## [[Minimum Spanning Tree problem (MST)]]

Problems 5.1, 5.2, 5.5, 5.6, 5,7, 5.9, 5.20, 5.22, 5.23.

## Flow problems

Problems 7.18, 7.19, 7.21, 7.22, 7.24(\*), 7.28(\*)