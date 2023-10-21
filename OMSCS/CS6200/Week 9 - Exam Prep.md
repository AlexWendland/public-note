---
aliases: 
type: exercise
publish: false
created: 2023-10-18
last_edited: 2023-10-21
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 9
chatgpt: false
---
# Week 9 - Exam Prep (unassessed) 

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

# [[Modular arithmetic]]

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

If $a$ has an inverse mod $b$ then $gcd(a,b) = 1$ by the [[Modular multiplicative inverse existence|modular multiplicative inverse existence lemma]]. Which is the required property for $b$ to have an inverse modulo $a$. 

> [!question] Problem 1.24
> If $p$ is prime, how many elements of $\{0,1, \ldots, p^n-1\}$ have an inverse mod $p^n$?

For the elements to have an inverse mod $p^n$ we know then need $gcd(e,p^n) = 1$. Therefor this is simply [[Euler's totient function]] $\phi(p^n) = (p-1)p^{n-1}$. 

> [!question] Problem 1.25
> Calculate $2^{125}$ mod $127$ using any method you choose?

As $127$ is prime we have $2^{126} =_{127} 1$ so $2^{125} = 2^{-1}$ mod $127$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 127 | 2   | 63  | 1   | -63 | 
| 2   | 1   | 1   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $2^{-1} = 64$ mod 127.

> [!question] Problem 1.26
> What is the least significate decimal digit of $17^{17^{17}}

We need to calculate $17^{17^{17}}$ mod 10. Therefore we need to calculate $17^{17}$ mod $4$. Which involves finding $17$ mod $2$. So $17^{17} = 1^{1} = 1$ mod $4$ giving $17^1 = 7$ mod $10$. 

> [!question] Problem 1.27
> Consider an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] key set with $p=17$, $q=23$, $N=391$, and $e=3$. 
> a) What is the value of $d$ to make this a secrete key?
> b) What is the encryption of the message $M = 41$?

To find $d$ we need to find $e = 3$'s inverse mod $(17-1) \cdot (23-1) = 352$

| x   | y   | c   | a   | b    |
| --- | --- | --- | --- | ---- |
| 352 | 3   | 117 | 1   | -117 |
| 3   | 1   | 3   | 0   | 1    |
| 1   | 0   | -   | 1   | 0    |

So $235 \cdot 3 = 1$ mod $352$. So we have $d = 235$.

This is $M = 41^3 = 105$ mod 391. Which successfully decrypts as $105^{235} = 41$ mod 391.

> [!question] Problem 1.28
> In an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] crypto system, $p=7$ and $q=11$. Find appropriate exponents $d$ and $e$.

Note $(7-1) \times (11 - 1) = 60$ so we can't use 3, 5 but we could use 7.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 60  | 7   | 8   | 2   | -17 | 
| 7   | 4   | 1   | -1  | 2   |
| 4   | 3   | 1   | 1   | -1  |
| 3   | 1   | 1   | 0   | 1   |

Therefore we have inverse $60 - 17 = 43 = d$. 

> [!question] Problem 1.42
> Suppose that instead of using a composite $N = pq$ in the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] cryptosystem, we simply use a prime modulus $p$. As in [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]], we would have an encryption exponent $e$, and the encryption of a message $m$ mod $p$ would be $m^e$ mod $p$. Prove that this new cryptosystem is not secure, by giving an efficient algorithm to decrypt: that is, an algorithm that given $p$, $e$, and $m^e$ mod $p$ as input, computes $m$ mod $p$. Justify the correctness and analyze the running time of your decryption algorithm.

1. Find $d := e^{-1}$ mod $p-1$ using [[Modular inverse algorithm (extended Euclidean algorithm)]].
2. Calculate $(m^e)^d = m$ mod $p$ using [[Modular exponent algorithm]].

The correctness follows from [[Fermat's little theorem]].

If $p$ is an $n$-digit number so is $e$ and $d$. Therefore step 1 and 2 has run time $O(n^3)$ giving the overall run time as $O(n^3)$. 

# [[Depth-first search (DFS)|DFS]] and [[Strongly connected components (directed graphs)|Strongly Connected Component]]

> [!question] Problem 3.1/2
> Perform a [[Depth-first search (DFS)|DFS]] on the following graphs; whenever there’s a choice of vertices, pick the one that is alphabetically first. Classify each edge as a [[DFS tree (algorithm)|Tree edge]] or [[DFS tree (algorithm)|Back edge]], and give the pre and post number of each vertex.

## 3.1

![[ex_3_1]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 12   |
| B      | 2   | 11   |
| C      | 3   | 10   |
| D      | 13  | 18   |
| E      | 5   | 6    |
| F      | 4   | 9    |
| G      | 14  | 17   |
| H      | 15  | 16   |
| I      | 7   | 8    |

We get the follow [[DFS tree (algorithm)|DFS tree]] with black [[DFS tree (algorithm)|tree edges]] and orange [[DFS tree (algorithm)|back edges]].

![[ex_3_1_dfs]]

## 3.2.a

![[ex_3_2_a]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 16   | 
| B      | 2   | 15   |
| C      | 3   | 14   |
| D      | 4   | 13   |
| E      | 8   | 9    |
| F      | 7   | 10   |
| G      | 6   | 11   |
| H      | 5   | 12   |

We get the following [[DFS tree (algorithm)|DFS tree]] with [[DFS tree (algorithm)|tree edges]] as black, [[DFS tree (algorithm)|back edges]] as orange and [[DFS tree (algorithm)|forward edges]] as purple.

![[ex_3_2_a_dfs]]

## 3.2.b

![[ex_3_2_b]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 16   | 
| B      | 2   | 11   |
| C      | 4   | 5    |
| D      | 6   | 9    |
| E      | 7   | 8    |
| F      | 3   | 10   |
| G      | 13  | 14   |
| H      | 12  | 15   |

We get the following [[DFS tree (algorithm)|DFS tree]] with [[DFS tree (algorithm)|tree edges]] as black, [[DFS tree (algorithm)|back edges]] as orange, [[DFS tree (algorithm)|forward edges]] as purple, and [[DFS tree (algorithm)|cross edges]] in green.

![[ex_3_2_b_dfs]]

> [!question] Problem 3.7
> Perform a [[Depth-first search (DFS)|DFS]] on the following graphs; whenever there’s a choice of vertices, pick the one that is alphabetically first. Classify each edge as a [[DFS tree (algorithm)|Tree edge]] or [[DFS tree (algorithm)|Back edge]], and give the pre and post number of each vertex.

Problems 3.7, 3.8, 3.11, 3.15, 3.16, 3.22, 3.24.

# [[Breath-first search (BFS)|BFS]] and Shortest path problems

Problems 4.1-4.3, 4.8, 4.11, 4.12-4.14, 4.20, 4,21.

# [[Minimum Spanning Tree problem (MST)]]

Problems 5.1, 5.2, 5.5, 5.6, 5,7, 5.9, 5.20, 5.22, 5.23.

# Flow problems

Problems 7.18, 7.19, 7.21, 7.22, 7.24(\*), 7.28(\*)