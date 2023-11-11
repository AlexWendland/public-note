---
aliases: []
checked: false
created: 2023-07-11
last_edited: 2023-07-11
publish: true
tags: programming, clean-code
type: convention
---
# Data - Object Anti-Symmetry

> [!Quote] Clean Code
> [[Object|Objects]] hide their data behind abstractions and expose functions that operate on that data. [[Data structure|Data structures]] expose their data and have no meaningful functions.

When we make objects we should have in mind whether this is simply a grouping of data or variables are going to be managed internally and we do not want the outside user to change them.

## Hybrids

In [[Python Index]] especially this might seem more like a spectrum than an anti-symmetry. However, a mid point tends to be bad practice and indicative that you may have low [[Cohesion]] in your code.

## [[Procedural Programming]] vs [[Object Oriented Programming (OOP)]]

When we programme in a procedural manner, i.e. creating [[Data structure|Data structures]] and using functions to extract features, this makes it easy to to add new functions to all objects. This will not require rewriting any of the data structures but will involve handling the cases for each [[Data structure]]. However, this does make it hard to add new [[Data structure|Data structures]] as we will need to open up every function using these.

On the other hand using an [[Object Oriented Programming (OOP)|object oriented]] paradigm makes it really easy to add new objects - as we can just use [[Inheritance]] to define the new object. However, if we want to add a new function to all the objects it means we will need to open up each of the objects.

Whilst in both examples we have to write essentially the same function just place it in different bits of the code. In larger applications this can have serious consequences. Not least because as other people use and extend your code you will lose ownership of making the changes. Suddenly lots of changes will break [[Backwards compatibility]]. Therefore, when making design decisions early on think about how your code is likely to be extended before choosing paradigm to work in.
