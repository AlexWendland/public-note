---
aliases:
  - mutable
  - Mutable
  - immutable
  - Immutable
  - mutability
  - immutability
  - mutability
checked: false
created: 2023-06-29
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: concept
---
# Mutability

An [[Object|object]] is considered *mutable* if if can be changed after it is created, whereas it is *immutable* if it can not be changed. If you change a mutable object all references to that object will also be changed.

In [[Python Index]], lists, sets and dictionaries are *mutable* whereas numbers, strings, tuples and frozen sets are *immutable*.

This is commonly used in interview questions, for example:

```python
a = [0,0]
b = [a,a]
a[1] = 1
print(b) # [ [0,1], [0,1] ]
```

whereas

```python
a = (0,0)
b = (a,a)
a[1] = 1 # TypeError: 'tuple' object does not support item assignment
```

though read more about this in [[Mutability in Python]].
