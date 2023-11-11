---
aliases: null
checked: false
created: 2023-11-02
last_edited: 2023-11-11
publish: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> The [[k-colourings problem (graphs)]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

The problem is of the correct from for a [[Search problems|search problem]] as you either have to provide a [[Proper vertex colouring|proper vertex k-colouring]] or you have to say no such colouring exists.

If you are given $G$ and a $k$-colouring $c$ it takes $O(\vert E \vert)$ time to check the colouring is proper by checking every edges vertices.
