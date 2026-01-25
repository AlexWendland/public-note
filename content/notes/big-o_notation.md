---
aliases:
  - worst case run time
created: 2023-08-27
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - maths
title: Big-O notation
type: notation
---

[Big-O notation](big-o_notation.md) is the main way people determine the [runtime](run_time_complexity.md) of algorithms. (Rightly or wrongly.) It is the worst case analysis and has a formal mathematical definition
$$ f = O(g) \mbox{ if } \exists \ x_0 \in \mathbb{N}, m \in \mathbb{R}_{>0} \mbox{ such that } f(x) \leq m \ast g(x)\ \forall x > x_0.$$
This is just saying that $f$ eventually is at most a scalar multiple of $g$.

> [!note] This is **only** an upper bound
> If $f = O(x^2)$ then we also have that $f = O(2^n)$, as $x^2 < 2^x$ eventually.
>
