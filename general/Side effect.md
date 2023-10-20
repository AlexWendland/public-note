---
aliases: [side effect, side effects]
type: concept
publish: true
created: 2023-07-14
last_edited: 2023-07-14
tags: programming
chatgpt: false
---
# Side effect

In programming, a side effect of a [[Function conventions|subroutine]] is the effect it has on things outside its domain. For example updating a database, changing a global variable, or changing an input [[Mutability|mutable]] variable. It is [[Function conventions#Have no side effects|good practice]] to avoid doing this at all costs. It makes your code harder to understand and debugging even worse!