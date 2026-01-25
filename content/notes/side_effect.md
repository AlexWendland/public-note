---
aliases:
  - side effect
  - side effects
created: 2023-07-14
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Side effect
type: concept
---

In programming, a side effect of a [subroutine](function_conventions.md) is the effect it has on things outside its domain. For example updating a database, changing a global variable, or changing an input [mutable](mutability.md) variable. It is [good practice](function_conventions.md#have-no-side-effects) to avoid doing this at all costs. It makes your code harder to understand and debugging even worse!
