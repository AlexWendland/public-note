---
aliases:
  - pass by reference
  - pass by value
  - passing variables
  - passing variables to a function
  - passed by reference
  - passed by value
checked: false
created: 2023-07-17
last_edited: 2023-11-11
draft: false
tags:
  - programming
  - fundamentals
type: definition
---
# Passing variables to a function

When you pass a variable to a [[Function conventions|function]], what does the function actually receive?

First lets name things to make this a little simpler. The variable we pass to the function will be called the `argument` whereas the variable used by the function will be called the `parameter`.

```python
def function(parameter):
	# The variable used by the function is called the parameter
	...

argument = ...

# The variable we pass to the function is called the argument

function(argument)
```

There are two main choices of what can happen to the argument when it gets passed into the parameter, it can be:

- copied so the function has a new object to play with, this is called [[Passing variables to a function#Passed by value|Passed by value]], or
- given directly to the function so changes made to the parameter in the function will effect the argument that was passed, this is called [[Passing variables to a function#Passed by reference|Passed by reference]].

Different approaches can be useful in different contexts and what happens is language specific.

## Passed by value

Passing by value means that you make a copy of that argument when it is passed to the function (or something similar - [[Mutability in Python|Python example]]). This reduces the chances of [[Side effect|side effects]] and makes the code simpler to use but can mean slower programs with less efficient use of [[Random Access Memory (RAM)|computer memory]].

## Passed by reference

Passing by reference means the parameter points to the same object as the argument. This is very efficient for larger data structures both in terms of [[Random Access Memory (RAM)|computer memory]] and program speed however it complicates your code by increasing the changes of [[Side effect|side effects]].

In [[Python Index]] functionally all arguments are passed by reference - however their [[Mutability in Python|mutability]] allows for something similar to passing by value.
