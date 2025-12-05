---
aliases:
  - namespaces
  - namespace
checked: false
created: 2023-07-17
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Namespaces
type: definition
---

A namespace in computer science is essentially a container where identifiers (names of types, variables, functions, etc.) live. It allows different developers, libraries, or parts of a program to use the same identifier names without causing conflicts, because the same identifier can be bound to different entities in different namespaces.

In other words, namespaces provide a way to disambiguate identifiers that might be common and likely to be used more than once. This way, even if the same identifier is used in different parts of a program, as long as they are in different namespaces, they are considered to be different entities.

# Example

In [Python Index](python_index.md), namespaces are implemented as dictionaries that map names to objects, and they have different lifetimes depending on where they are declared. For example, a local namespace in a function is created when the function is called and deleted when the function returns; a module's namespace lasts as long as the module is in memory; and the built-in namespace that contains Python's built-in functions exists for the life of the program.

``` python
 In the global namespace
x = 10

def my_func():
    # In the local namespace of my_func
    x = 20
    print(x)  # Prints: 20

my_func()
print(x)  # Prints: 10

```
