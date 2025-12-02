---
aliases: []
checked: false
created: 2023-08-05
draft: false
last_edited: 2023-11-11
title: The Law of Demeter
tags:
  - programming
  - clean-code
type: principle
---
# The Law of Demeter

This is a heuristic to determine what an object should and shouldn't know about. It says:

A method `f` of an object `C` should only call the methods of the following:
- The class `C`,
- An object created in `f`, and
- An object held in an instance variable of `C`.

It should explicitly not call methods on objects that are returned by any of the allowed functions.

You know this has been violated this when you see [Train Wrecks](train_wrecks.md) in the code.

## Why should I follow this

As you increase the depth of a methods access, you also increase its [coupling](coupling.md) with other bits of code. In other words, you are making this bit of code rely on the structure of more of your other code. This increases the risk you are going to need to change this code from unrelated changes.
