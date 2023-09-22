---
aliases: 
type: exercise
publish: false
created: 2023-09-11
last_edited: 2023-09-11
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: int
chatgpt: false
---
# Week 4 - Homework 3 (unassessed) 

> [!question] FFT design
> Let $A(x) = 1 - 2x -2x^2 + x^3$. You wish to run FFT to evaluate this polynomial.
> a. What is $A_{odd}(y)$ and $A_{even}(y)?
> b. What is the appropriate root of unity to use?

a. $A_{even}(x) = 1 - 2x$ and $A_{odd} = -2 + x$.
b. $i$

>[!question] FFT as a black box
>Design an algorithm that takes as input a set $S = \{s_1, s_2, \ldots, s_n\}$ of distinct natural numbers such that $0 \leq s_i \leq 100n$, and a natural number $N$, and outputs True if the equation $s_i + s_j + s_k = N$ has at least one solution, and return False otherwise. There is a simple solution that runs in $O(n^3)$ time (can you find an $O(n^2)$ solution?), but you can improve on these times using FFT!
>
> Example: For $N = 6$ and $S = \{ 1, 2, 3, 5, 10 \}$ your design should output True since $1+2+3 = 6$. For $N = 20$ and the same set $S$ the answer should be True again since $5+5+10 = 20$ (yes, you can have $s_i = s_j = s_k$) but for $N = 19$ the answer is False since no three numbers add up to $19$.

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] Problem 2.7 Sum and product of roots of unity
> What is the sum of the $n$'th roots of unity? What is their product if $n$ is odd? If $n$ is even?



>[!question] Problems 2.8 Practice with the fast Fourier transform.
>a. What is the FFT of $(1,0,0,0)$? What is the appropiate value of $\omega$ in this case? And which sequence is $(1,0,0,0)$ the FFT?
>b. Repeat for $(1,0,1,-1)$.

## a) FFT of (1,0,0,0) = 1

$A^1_{even} = (1, 0)$ and $A^1_{odd} = (0,0)$ 

### FFT of (1,0)

$A^2_{even} = (1)$ whereas $A^2_{odd}$ = (0) so FFT($A^2_{even}$, 1) = 1 and FFT($A^2_{odd}, 1) = 0$ so

$A^1_{even}(1)$ = 1 + 0

$A^1_{even}(-1) = 1 - 0$

Giving $FFT(A^1_{even}, -1) = (1,1)$

Similarly $FFT(A^1_{odd}, -1) = (0,0)$

So $A(1) = 1 + 1 \cdot 0 = 1$ and $A(i) = 1 + i \cdot 0$  whereas $A(-1) = 1 - 1 \cdot 0 = 1$ and $A(-i) = 1 - i \cdot 0 = 1$.

Giving $FFT(A, i) = (1,1,1,1)$ as expected.

## b) FFT of (1,0,1,-1)



>[!question] 2.9 (a) Practice with polynomial multiplication by FFT.
>a. Suppose that you want to multiply the two polynomials $x + 1$ and $x^2 + 1$ using the FFT. Choose an appropriate power of two, find the FFT of the two sequences, multiply the results component wise, and compute the inverse FFT to get the final result.
>b. Repeat for the pair of polynomials $1 + x + 2x^2$ and $2 + 3x$.

a. $x+1 = (1, 1, 0, 0)$ and $x^2+1 = (1, 0, 1, 0)$ we will want to evaluate this around the 8'th roots of unity. 
### FFT for $x + 1$

