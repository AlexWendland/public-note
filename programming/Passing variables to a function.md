---
aliases: [pass by reference, pass by value, passing variables, passing variables to a function]
type: definition
publish: true
created: 2023-07-17
last_edited: 2023-07-17
tags: programming, fundamentals
chatgpt: false
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



## Passed by reference