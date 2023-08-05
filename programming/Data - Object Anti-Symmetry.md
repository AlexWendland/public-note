---
aliases: []
type: convention
publish: true
created: 2023-07-11
last_edited: 2023-07-11
tags: programming, clean-code
chatgpt: false
---
# Data - Object Anti-Symmetry

> [!Quote] Clean Code
> [[Object|Objects]] hide their data behind abstractions and expose functions that operate on that data. [[Data structure|Data structures]] expose their data and have no meaningful functions.

When we make objects we should have in mind whether this is simply a grouping of data or variables are going to be managed internally and we do not want the outside user to change them.

In [[Python]] especially this might seem more like a spectrum than an anti-symmetry. However, a mid point tends to be bad practice and indicative that you may have low [[Cohesion]] in your code. 