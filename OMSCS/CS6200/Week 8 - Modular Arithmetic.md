---
aliases: 
type: lecture
publish: false
created: 2023-10-09
last_edited: 2023-10-09
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 
chatgpt: false
---
# Week 8 - Modular Arithmetic

First lets remind ourselves of the definition of [[Modular arithmetic|modular arithmetic]].

![[Modular arithmetic]]

Within a computers architecture as numbers are stored in [[Binary|binary]] calculating mod $2^k$ is simple as taking the $k$ least significant bits. Therefore it is quite cheap. However, when the value is not $2^k$ it can get harder.

