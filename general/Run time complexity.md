---
aliases:
  - run time complexity
  - runtime
checked: false
created: 2023-08-26
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: theory
---
# Run time complexity

There are 3 main ways people use to analyse the run time complexity of algorithms.

## Big-O notation

[[Big-O notation]] is the main way people determine the run time of algorithms. (Rightly or wrongly.) It is the worst case analysis and has a formal mathematical definition
$$ f = O(g) \mbox{ if } \exists \ x_0 \in \mathbb{N}, m \in \mathbb{R}_{>0} \mbox{ such that } f(x) \leq m \ast g(x)\ \forall x > x_0.$$
This is just saying that $f$ eventually is at most a scalar multiple of $g$.

> [!note] This is **only** an upper bound
> If $f = O(x^2)$ then we also have that $f = O(2^n)$, as $x^2 < 2^x$ eventually.
>

## Big-Omega notation

[[Big-Omega notation]] is said to be the best case running time. However formally it is simply a lower bound on the run time - the same as [[Big-O notation]] is simply an upper bound. This has a similar formal definition
$$ f = \Omega(g) \mbox{ if } \exists \ x_0 \in \mathbb{N}, m \in \mathbb{R}_{>0} \mbox{ such that } 0 \leq m \ast g(x) \leq f(x) \ \forall x > x_0.$$
This is just saying that $f$ eventually is at least a scalar multiple of $g$.

## Big-Theta notation

[[Big-Theta notation]] is the tight bound on the run time. This is only really defined when some function is the following $f = O(g)$ and $f = \Omega(g)$ then we have $f=\Theta(g)$ this is also an equivalence relation, so $g = \theta(f)$ as well.

## Comments

In some algorithmic disciplines, these notions are not sufficient and people talk about average run time of an algorithm. Whilst [[Big-O notation]] determines a functions complexity in practical terms if that run time is only really recognised in very specific circumstances - it could have a much better average run time on most cases people care about and come across in real life.
