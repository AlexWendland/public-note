---
aliases:
  - variables
checked: false
created: 2023-07-17
last_edited: 2023-11-11
publish: true
tags: programming, python
type: fundamentals
---
# Variables in python

To understand how variables work in python it is good to keep in mind the separation between [[Random Access Memory (RAM)|computer memory]] and references to places in [[Random Access Memory (RAM)|computer memory]]. In [[Python Index]], variables are more like tags or labels that are attached to objects, rather than containers that store data, as they are in many other programming languages.

When you assign a value to a variable, what [[Python Index]] actually does is create an object in [[Random Access Memory (RAM)|computer memory]] representing that value, and then creates a name in the appropriate [[Namespaces|namespace]] that points to that object. This happens regardless of whether the value is [[Mutability|immutable]] (like an integer or a string) or [[Mutability|mutable]] (like a list or a dictionary).

Here's an example:

```python
x = 10
print(id(x)) #140703625587904
```

In this case, [[Python Index]] creates an integer object with the value `10`, and then creates the name `x` in the current [[Namespaces|namespace]].  `x` is a reference to the `10` object. You can see the location of the object `10` in [[Random Access Memory (RAM)|computer memory]] by me using the `id` function in python.

If you then do:

```python
y = x
print(id(y)) #140703625587904
```

[[Python Index]] doesn't create a new object. Instead, it creates a new name, `y`, that references the same object `x` does. Both `x` and `y` are names for the same `10` object. You could imagine it as two tags ('x' and 'y') attached to the same object ('10'). Which you can see when you look at the local [[Namespaces|namespace]]:

```python
print(locals())
# {
# '__name__' : '__main__',
# ...
# '__cached__' : None,
# 'x' : 10,
# 'y' : 10
# }
```

You can also see the [[Reference counting in Python|reference count]] of these objects using the `sys.getrefcount` function.

```python
import sys

x = (1,2)
print(sys.getrefcount(x)) # 2
y = x
print(sys.getrefcount(x)) # 3
```

On line 4, there are two references to the object `(1,2)`, first `x` but also the parameter of the function `sys.getrefcount`. After we assign `y`  to `(1,2)` the reference count has gone up to 3 on line 6.
