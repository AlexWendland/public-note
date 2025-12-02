---
aliases:
checked: false
course: CS6215 Introduction to Graduate Algorithms
created: 2023-09-18
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 4 - Fast Fourier Transforms
type: lecture
week: '4'
---

> [!tldr] Polynomial multiplication problem
> Given polynomials
> $$A(x) = \sum_{i=0}^{n-1} a_i x^i, \mbox{ and } B(x) = \sum_{i=0}^{n-1} b_i x^i.$$
> We want to compute the product
> $$\sum_{i=0}^{2n-2} c_i x^i = C(x) := A(x) B(x).$$

This can be restated as the following problem.

> [!tldr] Convolution problem
> Given a vector $a = (a_0, a_1, \ldots, a_{n-1})$ and $b = (b_0, b_1, \ldots b_{n-1})$ we want to compute the convolution $c = a \ast b = (c_0, \ldots, c_{2n-2})$. Where
> $$ c_k = \sum_{i=\max\{0,k-n+1\}}^{\min\{n-1,k\}} a_i b_{k-i}.$$

If you where to just do those computations, it would take you $O(n^2)$ time as you need to do $O(n)$ steps computing up to $O(n)$ terms for each step. However, this can be improved to $O(n\log(n))$.

# Applications

When you want to reduce noise or add a visual effect to some data $y = (y_1, \ldots, y_n)$ - normal approaches are to take an average of close by terms.

## Mean filter

You replace $y_i$ by the average of the closest $2m$ terms for some $m$. i.e.
$$\hat{y_j} = \frac{1}{2m+1} \sum_{i=m}^{-m} y_{j + i}.$$
This is the same as calculating
$$\hat{y} = y \ast f \mbox{ where } f = \left ( \frac{1}{2m+1}, \ldots, \frac{1}{2m+1} \right ).$$

## Gaussian filtering

Similarly you could take a Gaussian distribution instead of using a uniform one and switch out $f$ for
$$ f = \frac{1}{z} \left ( e^{-m^2}, e^{-(m-1)^2}, \ldots, e^{-1}, 1, e^{-1}, \ldots e^{-m^2} \right )$$
with $z$ being a normalisation constant.

## Guassian blur

There are 2-dimensional analogies of this used to generate a blur effect in games.

# Polynomial representations

Any polynomial $A(x) = \sum_{i=0}^{n-1} a_i x^i$ has two natural representations:
1. The coefficients $a = (a_0, a_1, \ldots, a_{n-1})$, or
2. the values $A(x_1), A(x_2), \ldots A(x_n)$ for some distinct $x_i$.

> [!important] Lemma
> Polynomials of degree $n-1$ is uniquely determined by its values at any $n$ distinct points.

The fast Fourier transform is just a nice way of going between these two representations. Though it determines what $x_i$ it uses.

# Why polynomials are quick to multiply when represented by values

Given $A(x_1), \ldots A(x_{2n})$ and $B(x_1), \ldots, B(x_{2n})$ then to uniquely determine $C(x)$ we just calculate $C(x_i) = A(x_i)B(x_i)$.

Note here we used $2n$ points. The plan of attack will be to convert polynomials from coefficients into values using [fast Fourier transforms](../../general/fast_fourier_transform.md), multiply them, then transform back using the same technique.

# Picking the points

We get to pick the points $x_i$ we want to evaluate our polynomial around. So we will pick $2n$ points such that $x_i = - x_{i+n}$ for $1 \leq i \leq n$. That way we know
- $a_{2j}x_i^{2j} = a_{2i}x_{i+n}^{2j}$ and
- $a_{2j+1}x_i^{2j+1} = - a_{2i+1}x_{i+n}^{2j+1}$.
So it is meaningful to split up the polynomial into odd and even terms and defining
$$A_{even}(y) = \sum_{i=0}^{n-2/2} a_{2i} y^i, \mbox{ and } A_{odd}(y) = a_{2i + 1} y^i.$$
so we have $A(x) = A_{even}(x^2) + x A_odd(x^2)$. This will begin our divide and conquer approach.

>[!Note] We have only reduced the degree of $A_{even}$ and $A_{odd}$.
>We have not reduced the number of points we need to evaluate $A_{even}$ or $A_{odd}$ at. Though this is where our choice of $x_i$ comes in.

Note that
$$A(x_i) = A_{even}(x_i^2) + x_i A_{odd}(x_i^2), \mbox{ and } A(x_{n+1}) = A(-x_i) = A_{even}(X_i^2) - x_iA_{odd}(x_i^2)$$
so given we $A_{even}(y_i)$ and $A_{odd}(y_i)$ for $y_i = x_i^2$ for $1 \leq i \leq n$ we get $A(x_j)$ for $1 \leq j \leq 2n$.

This halves the number of points we need to consider.

# Summary

To get $A(x)$ of degree $\leq n-1$ at $2n$ points $x_1, \ldots, x_{2n}$ we
1. Define $A_{even}$ and $A_{odd}$ as above of degree $\leq \frac{n}{2} - 1$.
2. Recursively evaluate at $n$ points. $y_i = x_i^2 = x_{i+n}^2$.
3. In $O(n)$ time, we get $A(x)$ at $x_1, \ldots, x_{2n}$.

This has running time
$$T(n) = 2 T\left( \frac{n}{2}\right ) + O(n)$$
which by masters theorem is $O(n\log(n))$.

>[!note] We need $y_i$ to also have $y_i = - y_{i + n/2}$ which will start to get interesting!

# Complex numbers

To achieve this we will need to look at the polynomials in the [complex numbers](../../general/complex_numbers.md), which we denote as $\mathbb{C}$.

To work with complex numbers remember we set $i = \sqrt{-1}$ and think of them as sums $a + bi$.

These can be represented as $(a,b)$ or we can represent them using [Polar Coordinates](../../general/polar_coordinates.md) using $r$ and $\theta$, where
$$(a,b) = (r \cos(\theta), r \sin(\theta)).$$
This can also be summaries using [Euler's formula](../../general/euler's_formula.md) by saying
$$a + bi = r(\cos{\theta} + i \sin(\theta)) = r e^{i\theta}.$$
# Roots of unity

The $k$'th [roots of unity](../../general/roots_of_unity.md) are those $z \in \mathbb{C}$  such that $z^k = 1$. For $k=2$ these are simply $1, -1$ however for $k=4$ they are $1, -1, i, -i$.

More generically these are $e^{\frac{j2\pi}{k} i}$ for $0 \leq j < k$. In the notation of this course set $\omega_k = e^{\frac{2 \pi}{k} i}$ and express the roots of unity as $\omega_k^j$ for $0 \leq j <k$.

> [!note] Properties of use
> When $k = 2n$ is even note that $\omega_k^2 = \omega_n$ as well as $\omega_k^j = - \omega_k^{j + n}$ as $\omega_k^n = -1$.

This means that even powers of the [roots of unity](../../general/roots_of_unity.md) are perfect choices for our $x_i$ in the [fast Fourier transform](../../general/fast_fourier_transform.md) algorithm.

# Pseudocode for FFT

``` pseudocode
FFT(a, w):
	input: coefficents a = (a_0, a_1, ..., a_{n-1}) for polynomial A(x) where
		n is a power of 2 and w is a nth root of unity.
	output: A(w^0), A(w), A(w^2), ...., A(w^{n-1})
	if n = 1
		return A(1)
	Let A_even = (a_0, a_2, ..., a_n-2) and A_odd = (a_1, a_3, ..., a_{n-1})
	A_even(w^0), A_even(w^2), ..., A_even(w^{n-2}) = FFT(A_even, w^2)
	A_odd(w^0), A_odd(w^2), ..., A_odd(w^{n-2}) = FFT(A_odd, w^2)
	Set:
	A(w^j) = A_even(w^2j) + w^j A_odd(w^2j)
	A(w^{n/2 + j}) = A_even(w^2j) - w^j A_odd(w^2j)
	Return (A(w^0), A(w^1), ..., A(w^{n-1}))
```

If $T(n)$ is the run time of our algorithm - lets analyse this. The steps to split up the polynomial and glue the answers back together takes $O(n)$ for each of them. Then we make two recursive calls that both take $T(n/2)$ so the run time is $T(n) = 2T(n/2) + O(n)$ like we said above.

> [!question] How do we go backwards?

# Linear algebra of FFT

The [linear algebra](../../general/linear_algebra.md) of what we are doing here is important to how we compute the inverse.

For a point $x_j$ we have
$$A(x_j) = \sum_{i=0}^{n-1} a_i x_j^i = (1, x_j, \ldots, x_j^{n-1}) \cdot (a_0, a_1, \ldots, a_{n-1}).$$
So to compute it for points $x_0, \ldots, x_{n-1}$ we do this via [matrices](../../general/matrix.md) using the following form
$$ \left [ \begin{array} \ A(x_0)\\ A(x_1)\\ \vdots \\ A(x_{n-1}) \end{array} \right] = \left [ \begin{array} \ 1 & x_0 & x_0^2 & \cdots & x_0^{n-1}\\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1}\\ \vdots & \vdots & \vdots & \ddots & \vdots\\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{array} \right ]  \left [ \begin{array} \ a_0 \\ a_1\\ \vdots \\ a_{n-1} \end{array} \right]$$
when $x_j = \omega_n^j$ we denote this as $A = M_n(\omega_n) a$. So computing the inverse of the [FFT](../../general/fast_fourier_transform.md) is simply calculating $M_n(\omega_n)^{-1} A = a$,

>[!important] Lemma
>$$M_n(\omega_n)^{-1} = \frac{1}{n} M_n(\omega_n^{-1}) = \frac{1}{n} M_n(\omega_n^{n-1})$$

## Proof
Lets examine
$$M_n(\omega_n^{-1}) M_n(\omega_n) := \{m_{i,j}\}.$$
For these terms we have
$$ \begin{align*} m_{j,k} & = \left( 1, \omega_n^{-j}, \omega_n^{-2j}, \ldots, \omega_n^{-(n-1)j} \right ) \cdot \left( 1, \omega_n^{k}, \omega_n^{2k}, \ldots, \omega_n^{(n-1)k} \right )\\
& = \sum_{i=0}^{n-1} \omega_n^{i(j-k)}\\
& = \sum_{i=0}^{n-1} \left ( \omega_n^{j-k} \right )^n
\end{align*}$$
Which splits into cases if $j = k$ then $\omega_n^{j-k} = 1$ and we have this sum is $n$. Whereas if $j \not = k$ from the [sum of roots of unity](../../general/sum_of_roots_of_unity.md) we have this sum is 0. Therefore
$$ M_n(\omega_n^{-1}) M_n(\omega_n) = n I_n$$
giving us the desired result.

$\square$

Now the problem once again is of the form $n a = M_n(\omega_n^{n-1}) A$ we can use the [FFT](../../general/fast_fourier_transform.md) algorithm detailed before to solve the inverse of the [FFT](../../general/fast_fourier_transform.md).

# Pseudocode for Polynomial Multiply

``` pseudocode
FFT(a, w):
	input: coefficents a = (a_0, a_1, ..., a_{n-1}) for polynomial A(x) and
		coefficents b = (b_0, b_1, ..., b_{n-1}) for polynomial B(x)
	output: coefficents c = (c_0, c_1, ..., c_{2n-2}) for polynomial C(x) =
		A(x) B(x)
	Let w_{2n} be the first 2n'th root of unity
	(r_0, r_1, ..., r_{2n - 1}) = FFT(a, w_{2n})
	(s_0, s_1, ..., s_{2n - 1}) = FFT(b, w_{2n})
	for j = 0 -> 2n-1
		t_j = r_j x s_j
	(c_0, c_1, ..., c_2n-1) = 1/2n FFT(t, w_{2n}^{2n-1})
```

The running time of this algorithm is $O(2n\log(2n)) = O(n \log(n))$ for the three FFT steps. then $O(n)$ for calculating the entries for $t_j$ giving that it runs in $O(n\log(n))$.
