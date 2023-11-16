---
aliases:
  - Fourier matrix
checked: false
created: 2023-09-19
last_edited: 2023-11-11
publish: true
tags:
  - maths
  - programming
type: definition
---
# Fourier Matrix

The Fourier matrix is used in [[Fast Fourier Transform]]. Let $\omega$ be a $n$'th root of unity then define the *Fourier matrix to be*
$$F_n(\omega) = \left [ \begin{array} \ 1 & 1 & 1 & \cdots & 1\\ 1 & \omega & \omega^2 & \cdots & \omega^{n-1}\\ 1 & \omega^2 & \omega^4 & \cdots & \omega^{2(n-1)}\\ \vdots & \vdots & \vdots & \ddots & \vdots\\ 1 & \omega^{n-1} & \omega^{n-2} & \cdots & \omega \end{array} \right ].$$

