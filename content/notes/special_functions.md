---
aliases:
  - special
  - dunder
  - magic
  - dunder functions
  - special functions
  - magic functions
checked: false
created: 2023-02-25
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - python
title: Special functions
type: notation
---
This are also known as [dunder](special_functions.md) (double underscore) or [magic](special_functions.md) functions. They are signified by two underscores before and after its name i.e. \_\_len\_\_.

These functions are not normally called by the user, the are for the python interpreter to use. For example if you call
```python
item in some_iterable:
	pass
```
to get the list of items this calls `some_iterable.__iter__()`. The same for `len(object)` this calls `object.__len__()`.

When you are writing an object in python it is good to define this if they are not inherited from the parent class. This will guarantee [pythonic](pythonic.md) behaviour.
