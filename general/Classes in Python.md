---
checked: false
created: 2023-03-03
last_edited: 2023-03-03
publish: true
tags: programming, python
type: feature
---
# Classes in Python

[[Classes]] in python are defined by the `class` [[Keywords in Python|keyword]] for example.

```python
class NewThing:

	def __init__(self, variable):
		self.variable = variable
```

When using classes you use the `self` [[Keywords in Python|keyword]] to refer back to the object. Therefore a class [[Methods|method]] requires to have the first argument as `self`.

# [[Special functions|Special]] functions

## \_\_call\_\_

When a class has this property it makes it callable. For example:

```python
class SayMyName:

	def __call__(self):
			print("Alex Wendland")

>>> say_it = SayMyName()
>>> say_it()
Alex Wendland
```
