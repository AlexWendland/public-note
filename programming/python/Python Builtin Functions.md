---
type: function
publish: true
created: 2023-03-03
last_edited: 2023-03-03
tags: programming, python
---
# Python Builtin Functions
[[Python]] has some built in functions that make using the language slightly easier. They normally call a [[Magic or dunder|special]] function from an object. You can find a full list of these in the [python documentation](https://docs.python.org/3/library/functions.html).

# Functions
## callable(object)
This returns `True` or `False` depending on if the object is callable.

## dir(object)
This returns a list of names in the [[Namespace]] of the object, i.e. variables and functions you can call on it. This normally involves calling the .\_\_dir\_\_ function of the object. 

You can call it with no arguments and it returns all the names in the current [[Namespace]].

## isinstance(object, classinfo: object | tuple)
If the first argument is a subtype of the second it returns true otherwise false. The second object can be a tuple of classes, then it returns true if it is a subtype of any of them. 

## len(object)
The returns the length of the object, it calls the .\_\_len\_\_  [[Magic or dunder|special]] function of the object.

## sorted(interable, key=None, reverse=False)
This returns a sorted list from the objects in the interable object. You can provide a key to apply to each of the objects in the iterable objects to get the key (i.e. getting one item in a dictionary). If reverse is True it will reverse the list of the items. To 

## type(object)
This returns the object type, which is generally the same as .\_\_class\_\_ [[Magic or dunder|special]] function (users can override the .\_\_class\_\_ function, which will cause this to differ). If you don't care about subtypes this is the best way to check an objects type.

If you provide it more than one argument, this can initiate an object. I have never done this before.
