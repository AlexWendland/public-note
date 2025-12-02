---
aliases:
  - variables
checked: false
created: 2023-07-17
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - python
title: Variables in python
type: fundamentals
---

To understand how variables work in python it is good to keep in mind the separation between [computer memory](random_access_memory_(ram).md) and references to places in [computer memory](random_access_memory_(ram).md). In [Python Index](python_index.md), variables are more like tags or labels that are attached to objects, rather than containers that store data, as they are in many other programming languages.

When you assign a value to a variable, what [Python Index](python_index.md) actually does is create an object in [computer memory](random_access_memory_(ram).md) representing that value, and then creates a name in the appropriate [namespace](namespaces.md) that points to that object. This happens regardless of whether the value is [immutable](mutability.md) (like an integer or a string) or [mutable](mutability.md) (like a list or a dictionary).

Here's an example:

```python
x = 10
print(id(x)) #140703625587904
```

In this case, [Python Index](python_index.md) creates an integer object with the value `10`, and then creates the name `x` in the current [namespace](namespaces.md).  `x` is a reference to the `10` object. You can see the location of the object `10` in [computer memory](random_access_memory_(ram).md) by me using the `id` function in python.

If you then do:

```python
y = x
print(id(y)) #140703625587904
```

[Python Index](python_index.md) doesn't create a new object. Instead, it creates a new name, `y`, that references the same object `x` does. Both `x` and `y` are names for the same `10` object. You could imagine it as two tags ('x' and 'y') attached to the same object ('10'). Which you can see when you look at the local [namespace](namespaces.md):

```python
print(locals())
 {
 '__name__' : '__main__',
 ...
 '__cached__' : None,
 'x' : 10,
 'y' : 10
 }
```

You can also see the [reference count](reference_counting_in_python.md) of these objects using the `sys.getrefcount` function.

```python
import sys

x = (1,2)
print(sys.getrefcount(x)) # 2
y = x
print(sys.getrefcount(x)) # 3
```

On line 4, there are two references to the object `(1,2)`, first `x` but also the parameter of the function `sys.getrefcount`. After we assign `y`  to `(1,2)` the reference count has gone up to 3 on line 6.
