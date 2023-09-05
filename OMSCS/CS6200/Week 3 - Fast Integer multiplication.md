---
aliases: []
type: lecture
publish: true
created: 2023-09-05
last_edited: 2023-09-05
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "3"
chatgpt: false
---
# Week 3 - Fast Integer multiplication

> [!tldr] Multiplying $n$-bit integers problem
> Given $n$-bit integers $x$ and $Y$ what is $z = xy$? 

Naïve approaches will do this in $O(n^2)$ time but you can do it faster with [[Divide and conquer algorithms|divide and conquer]].

## Gauss's trick (aside)

Suppose have two [[Complex Numbers|complex numbers]] $a + bi$ and $c + di$ where you want to compute the product $(a + bi)(c + di)$ in the fastest way possible.

Multiplication of real numbers uses $O(n^2)$ whereas addition/subtraction takes $O(n)$. So if you want to do it faster - it would be best to avoid multiplication.

Looking at the expansion
$$(a + bi)(c + di) = ac - bd + (ad + bc)i$$
it may look like you need to calculate 4 multiplications. However, note the following
$$(a + b)(c + d) = ac + bd + (ad + bc).$$
This tells us from computing $ac$, $bd$ and $(a+b)(c+d)$ we can in fact get all the components we need to work out the complex multiple:
$$(a + bi)(c + di) = ac - bd + ((a + b)(c+d) - bd - ac)i.$$

## Naïve divide and conquer approach

Suppose we have $x$ and $y$ which are $2^k=n$-bit numbers. We cut $x$ and $y$ in half so 
$$x = X_L2^{2^{k-1}} + X_R \mbox{ and } Y = Y_L2^{2^{k-1}} + Y_R.$$
then there multiple is
$$xy = X_LY_l2^{2^k} + (X_LY_R + X_RY_L)2^{2^{k-1}} + X_RY_R.$$
At which point we have broken the problem into sub-problems. We can then turn this into a [[Recursion|recursive]] algorithm.

```pseudo
EasyMultiply(x,y):
Input: n=2^k-bit integers x & y
Output xy
if k = 1:
	return xy
else:
	X_L = 1st 2^(k-1)-bits of x, X_R = Last 2^(k-1)-bits of x
	Y_L = 1st 2^(k-1)-bits of y, Y_R = Last 2^(k-1)-bits of y
	A = EasyMultiply(X_L, Y_L), B = EasyMultiply(X_R, Y_L)
	C = EasyMultiply(X_L, Y_R), D = EasyMultiply(X_R, Y_R)
	return 2^nA + 2^(2^k-1)(B + C) + D
```

To analyse the run time of this algorithm not the split and shift operations take $O(n)$ time, just the same as addition. So dividing $x$ and $y$ and computing the addition of the multiplied components are both $O(n)$ operations. However, if you let the run time of the algorithm be $T(n)$ then the sub multiplications take $4T(n/2)$. This gives
$$T(n) = 4 T(n/2) + O(n) = O(n^2).$$

## Better approach

