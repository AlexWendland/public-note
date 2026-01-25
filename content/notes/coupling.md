---
aliases:
  - coupling
  - coupled
created: 2023-08-05
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Coupling
type: meta
---

Two bits of code are 'Coupled' if they rely on one another. In other words if one changes then you are required to change the other bit of code. When we write programs we really want low coupling as these are easier to change and maintain.

There are lots of methods to decrease coupling, such as introducing [interfaces](interface.md) and [The Law of Demeter](the_law_of_demeter.md).

Decreasing coupling also makes it easier to [test](testing_conventions.md) your applications as you need to mock/patch out less of your code.

This is a **key concept** in good system design.
