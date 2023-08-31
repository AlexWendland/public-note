---
aliases: []
type: lecture
publish: true
created: 2023-08-31
last_edited: 2023-08-31
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 2
chatgpt: false
---
# Week 2 - Chain Matrix Multiply

The goal is this problem is, given a number of [[Matrix|matrices]] what is the most efficient way to multiply them together?

Lets say we have [[Matrix|matrices]] $A$, $B$, $C$ and $D$ and they have different sizes such that we can multiply $A B C D$. Whilst matrix multiplication might be [[Associativity|associative]] there might be a more efficient way to multiply them together!

## Cost of multiplying two matrices

Lets say with have two [[Matrix|matrices]] $W$ (of size $a \times b$) and $Y$ (of size $b \times c$) we set their product to be $Z = WY$ (of size $a \times c$). To calculate a single entry in $Z$ we need to multiply a row of $W$ (of size $b$) with a column of $Y$ (of size $b$)
$$ z_{ij} = \sum_{k = 1}^b w_{ik} \ y_{kj}$$
which takes $b$ multiplications and $b-1$ additions. As $Z$ has size $a \times c$ this involves $abc$ multiplications and $a(b-1)c$ additions.

Here the multiplications are the more costly operations so this is what we will focus on for the cost of this single operation.

> [!tldr] Chain Matrix Multiply problem
> For $n$ [[Matrix|matrices]] $A_1, A_2, \ldots, A_n$, where $A_i$ has size $m_{i-1} \times m_i$, what is the minimum cost for computing $A_1 A_2 \ldots A_n$?

## Dynamic program set up

Let $C(i,j)$ with $1 \leq i \leq j \leq n$ be the minimum cost of multiplying $A_i A_{i+1} \ldots A_j$.

The solution to the problem will be $C(1,n)$.

The base case will be $C(i,i) = 0$.

The [[Recursion|recursion]] step will be
$$ C(i,j) = \min\{C(i,k) + C(k,j) + m_im_km_j \vert i < k < j\}.$$

To calculate $C(i,j)$ we need to [[Iterative algorithms|iteratively]] increase the difference between $j - i$, the base case is $0$ the last case will be $n-1$.

