---
aliases: []
created: 2023-07-11
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
  - clean-code
title: Data - Object Anti-Symmetry
type: convention
---

> [!quote] Clean Code
> [Objects](object.md) hide their data behind abstractions and expose functions that operate on that data. [Data structures](data_structure.md) expose their data and have no meaningful functions.

When we create objects, we should consider whether this is simply a grouping of data or whether variables will be managed internally and should not be directly accessible to external users.

# Hybrids

In [Python Index](python_index.md) especially, this distinction might seem more like a spectrum than a strict anti-symmetry. However, occupying a middle ground tends to be bad practice and suggests you may have low [Cohesion](cohesion.md) in your code.

# [Procedural Programming](procedural_programming.md) vs [Object Oriented Programming (OOP)](object_oriented_programming_(oop).md)

When we programme in a procedural manner—that is, creating [Data structures](data_structure.md) and using functions to extract features—it is easy to add new functions to all objects. This does not require rewriting any of the data structures but will involve handling the cases for each [Data structure](data_structure.md). However, this does make it hard to add new [Data structures](data_structure.md) as we will need to modify every function that uses them.

On the other hand using an [object oriented](object_oriented_programming_(oop).md) paradigm makes it really easy to add new objects - as we can just use [Inheritance](inheritance.md) to define the new object. However, if we want to add a new function to all the objects it means we will need to open up each of the objects.

Whilst in both examples we have to write essentially the same function, just placing it in different parts of the code. In larger applications this can have serious consequences. Not least because as other people use and extend your code you will lose ownership of the changes. Suddenly many changes will break [Backwards compatibility](backwards_compatibility.md). Therefore, when making design decisions early on, think about how your code is likely to be extended before choosing which paradigm to work in.
