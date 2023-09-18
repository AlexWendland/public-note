---
aliases: 
type: lecture
publish: true
created: 2023-09-18
last_edited: 2023-09-18
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "4"
chatgpt: false
---
# Week 4 - Fast Fourier Transforms

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

## Applications

When you want to reduce noise or add a visual effect to some data $y = (y_1, \ldots, y_n)$ - normal approaches are to take an average of close by terms.

### Mean filter

You replace $y_i$ by the average of the closest $2m$ terms for some $m$. i.e. 
$$\hat{y_j} = \frac{1}{2m+1} \sum_{i=m}^{-m} y_{j + i}.$$
This is the same as calculating
$$\hat{y} = y \ast f \mbox{ where } f = \left ( \frac{1}{2m+1}, \ldots, \frac{1}{2m+1} \right ).$$

### Gaussian filtering

Similarly you could take a Gaussian distribution instead of using a uniform one and switch out $f$ for
$$ f = \frac{1}{z} \left ( e^{-m^2}, e^{-(m-1)^2}, \ldots, e^{-1}, 1, e^{-1}, \ldots e^{-m^2} \right )$$
with $z$ being a normalisation constant.

### Guassian blur

There are 2-dimensional analogies of this used to generate a blur effect in games.

## Polynomial representations

Any polynomial $A(x) = \sum_{i=0}^{n-1} a_i x^i$ has two natural representations:
1. The coefficients $a = (a_0, a_1, \ldots, a_{n-1})$, or
2. the values $A(x_1), A(x_2), \ldots A(x_n)$ for some distinct $x_i$.

> [!important] Lemma
> Polynomials of degree $n-1$ is uniquely determined by its values at any $n$ distinct points. 

The fast Fourier transform is just a nice way of going between these two representations. Though it determines what $x_i$ it uses.

## Why polynomials are quick to multiply when represented by values

Given $A(x_1), \ldots A(x_{2n})$ and $B(x_1), \ldots, B(x_{2n})$ then to uniquely determine $C(x)$ we just calculate $C(x_i) = A(x_i)B(x_i)$.

Note here we used $2n$ points. The plan of attack will be to convert polynomials from coefficients into values using [[Fast Fourier Transform|fast Fourier transforms]], multiply them, then transform back using the same technique. 

## Picking the points 

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

## Summary

To get $A(x)$ of degree $\leq n-1$ at $2n$ points $x_1, \ldots, x_{2n}$ we
1. Define $A_{even}$ and $A_{odd}$ as above of degree $\leq \frac{n}{2} - 1$.
2. Recursively evaluate at $n$ points. $y_i = x_i^2 = x_{i+n}^2$.
3. In $O(n)$ time, we get $A(x)$ at $x_1, \ldots, x_{2n}$.

This has running time
$$T(n) = 2 T\left( \frac{n}{2}\right ) + O(n)$$
which by masters theorem is $O(n\log(n))$.

>[!note] We need $y_i$ to also have $y_i = - y_{i + n/2}$ which will start to get interesting!

## Complex numbers

To achieve this we will need to look at the polynomials in the [[Complex Numbers|complex numbers]].  

To work with complex numbers remember we set $i = \sqrt{-1}$ and think of them as sums $a + bi$. 

These can be represented as $(a,b)$ or we can represent them using [[Polar Coordinates]] using $r$ and $\theta$, where
$$(a,b) = (r \cos(\theta), r \sin(\theta)).$$
This can also be summaries using [[Euler's formula]] by saying
$$a + bi = r(\cos{\theta} + i \sin(\theta)) = r e^{i\theta}.$$
## Roots of unity




