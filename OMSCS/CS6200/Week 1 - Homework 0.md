---
aliases: []
type: exercises
publish: false
created: 2023-08-27
last_edited: 2023-08-27
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 1
chatgpt: false
---
# Homework 0

>[!question] Problem 1 (a)
>Let $f(n) = 100n + \log(n)$ and $g(n) = n + \log(n)^2$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

Note the following two inequalities

- $\log(n) < n$ for $n > 1$,
- $\log(n)^2 < n$ for $n > 2$,

therefore $100n <f(n) < 101n$ and $n < g(n) < 2n$ giving us $g(n) = \Theta(n)$ and $f(n) = \Theta(n)$ and $f(n) = \Theta(g(n))$.

So the answer is 3.

>[!question] Problem 1 (b)
>Let $f(n) = n\log(n)$ and $g(n) = 10n\log(10n)$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

Note that from the [[Logarithms|rules of logarithms]] we have
$$g(n) = 10n\log(10n) = 10n(\log(10) + \log(n)) = 10n\log(10) + 10n\log(n).$$
Which for $n > 10$ gives us
$$n \log(n) < g(n) < 20n\log(n)$$
providing the bounds to give $g(n) = \theta(n\log(n)) = \theta(f(n))$.

So the answer is 3.

>[!question] Problem 1 (c)
>Let $f(n) = \sqrt{n}$ and $g(n) = \log(n)^3$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

As linear powers of $n$ outgrow [[Logarithms|logs]] we have $g(n) = O(f(n))$.

So the answer is 2.

>[!question] Problem 1 (d)
>Let $f(n) = \sqrt{n}$ and $g(n) = 5^{\log_2(n)}$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

From [[Logarithms#Interchange of bases|base interchange of logs]] we have that
$$g(n) = 5^{\log_2(n)} = 5^{\log_2(5)\log_5(n)} = 5^{\log_2(5)}5^{\log_5(n)} = 5^{\log_2(5)}n$$
which gives $f(n) = O(g(n))$.

So the answer is 1.

>[!question] Problem 2
> Show that $g(n) = 1 + a + a^2 + \ldots + a^n$ is $O(a^n)$ when $a > 1$ and $O(1)$ when $a < 1$.  
> (Hint: You may try to prove $g(n) =\frac{a^{n+1} - 1}{a-1}$ at first.)

Consider
$$ (a - 1)g(n) = a \sum_{i=0}^n a^i - \sum_{i=0}^n a^i = \sum_{i=0}^n a^{i+1} - a^i = a^{n+1} - 1$$
giving the hinted inequality
$$g(n) =\frac{a^{n+1} - 1}{a-1}.$$
