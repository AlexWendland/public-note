---
aliases:
created: 2023-11-02
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: The k-colourings problem is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> The [k-colourings problem (graphs)](k-colourings_problem_(graphs).md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

The problem is of the correct form for a [search problem](search_problems.md) as you either have to provide a [proper vertex k-colouring](proper_vertex_colouring.md) or you have to say no such colouring exists.

If you are given $G$ and a $k$-colouring $c$ it takes $O(\vert E \vert)$ time to check the colouring is proper by checking each edge's endpoints.
