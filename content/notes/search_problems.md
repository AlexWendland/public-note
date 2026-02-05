---
aliases:
  - search problems
  - search problem
created: 2023-10-24
date_checked:
draft: false
last_edited: 2026-02-05
tags: []
title: Search problems
type: definition
---
>[!definition] Search problem
>A problem is a *search problem* if we can verify a solution in [polynomial time](polynomial_time.md).
>
>Formally:
>
>The problem is of the form, for a given instance $I$ of the problem you can either:
>- find a solution $S$ for $I$ if one exists, or
>- output no if $I$ has no solutions.
>
>Then this problem is a *search problem* if given an instance $I$ and a solution $S$ then we can verify that $S$ is a solution to $I$ in [polynomial time](polynomial_time.md) in $\vert I \vert$.

