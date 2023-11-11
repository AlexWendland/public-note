---
aliases:
  - reference count
  - reference counting
checked: false
created: 2023-07-17
last_edited: 2023-07-17
publish: true
tags: programming, python
type: definition
---
# Reference counting in Python

In [[Python Index]] when objects are created, it also stores the number of references there are to that object. This is what we mean when we say the reference count of an object.

You can access this reference count by using the `sys` library with the function `sys.getrefcount`.

```python
import sys

x = [1,2]
print(sys.getrefcount(x)) # 2
y = x
print(sys.getrefcount(x)) # 3
print(sys.getrefcount(y)) # 3
del y
print(sys.getrefcount(x)) # 2
```

(Note the numbers are 1 more than you would expect, this is due to the object `[0,1]` being passed into the function `sys.getrefcount` which then has a reference to that object also.)

When the reference count of any variable goes to zero it is deleted by [[Garbage collection in python|Python's garbage collector]].
