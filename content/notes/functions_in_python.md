---
checked: false
created: 2023-02-25
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - python
title: Functions in Python
type: feature
---

[Functions](functions.md) in [Python Index](python_index.md) are a class and have type 'function'. i.e.

>\>\>\> type(my_function)
>\<class 'function'\>

They have their own [namespace](namespaces.md) that gets destroyed once the function call has ended. In [Python Index](python_index.md) functions are [First-class objects](first-class_object.md), meaning they can be assigned to variables.

You can see this in the below example.

```python
def some_function():

    b = 2

    print(locals())

a = 1
print(locals())
 {
 '__name__' : '__main__',
 ...
 '__cached__' : None,
 'some_function': <function some_function at 0x0000026EB32BD1F0>
 'a': 1
 }

some_function()
 {
 'b': 2
 }
```

# Properties

# \_\_doc\_\_

This returns the [Docstring](docstring.md) of the function.
