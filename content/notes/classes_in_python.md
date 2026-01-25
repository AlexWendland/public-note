---
created: 2023-03-03
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - python
title: Classes in Python
type: feature
---

[Classes](classes.md) in python are defined by the `class` [keyword](keywords_in_python.md) for example.

```python
class NewThing:

	def __init__(self, variable):
		self.variable = variable
```

When using classes you use the `self` [keyword](keywords_in_python.md) to refer back to the object. Therefore a class [method](methods.md) requires to have the first argument as `self`.

 [Special](special_functions.md) functions

# \_\_call\_\_

When a class has this property it makes it callable. For example:

```python
class SayMyName:

	def __call__(self):
			print("Alex Wendland")

>>> say_it = SayMyName()
>>> say_it()
Alex Wendland
```
