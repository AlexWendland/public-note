---
created: 2023-02-25
last_edited: 2023-02-25
publish: true
tags: programming, python
type: feature
---
# Functions in Python

[[Functions]] in [[Python Index]] are a class and have type 'function'. i.e.

>\>\>\> type(my_function)
>\<class 'function'\>

They have their own [[Namespaces|namespace]] that gets destroyed once the function call has ended. In [[Python Index]] functions are [[First-class object|First-class objects]], meaning they can be assigned to variables.

You can see this in the below example.

```python
def some_function():

    b = 2

    print(locals())

a = 1
print(locals())
# {
# '__name__' : '__main__',
# ...
# '__cached__' : None,
# 'some_function': <function some_function at 0x0000026EB32BD1F0>
# 'a': 1
# }

some_function()
# {
# 'b': 2
# }
```

## Properties

## \_\_doc\_\_

This returns the [[Docstring]] of the function.
