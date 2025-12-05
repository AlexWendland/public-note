---
aliases:
checked: false
created: 2025-04-13
draft: false
last_edited: 2025-04-13
tags: []
title: Causal consistency
type: definition
---
>[!tldr] Causal consistency
>  This is a [consistency model](consistency_model.md) where a system is _causally consistent_ if, for any two operations `op1` and `op2`, where `op1` causally precedes `op2`, then every process that observes `op2` must have already observed `op1`.

