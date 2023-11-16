---
aliases:
  - logs
  - rules of logarithms
  - logarithms
checked: false
created: 2023-08-28
last_edited: 2023-11-11
publish: true
tags:
  - maths
type: function
---
# Logarithms

A logarithm is the inverse operation to exponentiation. Given a base $b > 0$ and $b \not = 1$, the logarithm $\log_b(a)$ is the exponent $x$ you would raise $b$ to in order to get $a$.

> [!tldr] Logarithm
> This is defined as:
> $$ b^x = a \iff \log_b(a) = x.$$
## Interchange of bases

>[!important] Proposition
> We have the following equality
> $$\log_c(b) \ast \log_b(x) = \log_c(x).$$

Note this follows as if we let $\zeta = \log_c(b)$ then $b = c^\zeta$. So we have
$$b^y = (c^\zeta)^y = c^{y\zeta}$$
Lets equate this all to $x$ and use the definition above, on the left hand side we have
$$x = b^y \iff \log_b(x) = y$$
and on the right hand side
$$x = c^{\zeta y} \iff \zeta y = \log_c(x)$$
which combining these and substituting for $y$ gives
$$\log_c(b) \ast \log_b(x) = \zeta \log_b(x) = \zeta y = \log_c(x).$$
## Natural logarithms

A lot of people will only talk about logarithms using the base $e$ instead of using the notation $\log_e(x)$ they may use the notation $\ln(x)$. This is sort of implied when people just write $\log(x)$. The reason for this is $\log_a(x)$ and $\log_b(x)$ only differ by a constant $\log_c(b)$, as above showed us - in some fields people don't care about things up to scalar multiple.

>[!warning] Some people use $\log(x)$ to mean $\log_{10}(x)$ instead.
>You need to know the context of the field you are working in. If you are working in a particular base setting it might mean that base. Like in binary it might mean $\log_2(x)$.

## Logs turn multiplication into addition

Logs are useful as they bring the rules of exponential powers to regular terms.

>[!important] Proposition
> We have the following equality
> $$\log(A) + \log(B) = \log(AB).$$

Which is proven by the fact that
$$e^Ae^B = e^{A+B}.$$
This by extension gives
$$\log(A^n) = n\log(A).$$
The inverse also holds
$$ \log(A) - \log(B) = \log(\frac{A}{B}) \ \mbox{ which is similar to } \ \frac{e^A}{e^B} = e^{A-B}.$$
## Taylor expansion

> [!important] Proposition
> The [[Taylor expansion|Taylor series]] for $\ln(x)$ is as follows
> $$\ln(x) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{(x-1)^n}{n}.$$
