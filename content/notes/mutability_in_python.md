---
aliases:
  - mutability in Python
created: 2023-07-17
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - programming
  - python
title: Mutability in Python
type: concept
---

In [Python Index](python_index.md) all [variables](variables_in_python.md) are references to objects. Every object has a [mutability](mutability.md) property. Objects that are [mutable](mutability.md) in Python behave as you would expect: when a variable pointing to a mutable object is altered, the object itself is altered.

```python
x = [1,2]
y = x
x.append(3)
print(y) # [1,2,3]
```

Here `x` and `y` point to the [mutable](mutability.md) list object. When `x` is altered to add `3` to the list, `y` also reflects this change because both variables point to the same object.

In contrast, when a variable pointing to an [immutable](mutability.md) object in [Python Index](python_index.md) is altered, it creates a new object for that variable to point to, whilst the remaining variables continue to point to the original object.

```python
x = 1
y = x
print(x, id(x)) # 1 140703625587616
print(y, id(y)) # 1 140703625587616
x += 1
print(x, id(x)) # 2 140703625587648
print(y, id(y)) # 1 140703625587616
```

(The `id` function tells you the location in [computer memory](random_access_memory_(ram).md).)

# Passing arguments to functions

In [Python Index](python_index.md) all arguments are [passed by reference](passing_variables_to_a_function.md) to functions. Though the [mutability](mutability.md) of that [variable](variables_in_python.md) dictates how the object is treated by that function.

For [immutable](mutability.md) objects any alteration a function does to the object will not be reflected outside the scope of that function.

```python
def become_worldly(value):
    value += ' world'
    print("Inside function: ", value)

greeting = 'Hello'
print("Before function: ", greeting) # Before function: Hello
become_worldly(greeting)             # Inside function: Hello world
print("After function: ", greeting)  # After function: Hello
```

This behaves as if they have been [passed by value](passing_variables_to_a_function.md); however, this approach can reduce [computer memory](random_access_memory_(ram).md) usage if multiple variables hold the same value.

For [mutable](mutability.md) objects, any alterations that the function makes to the passed object will be reflected outside the scope of that function.

```python
def become_worldly(value):
    value.append('world')
    print("Inside function: ", value)

greeting = ['Hello']
print("Before function: ", greeting) # Before function: ['Hello']
become_worldly(greeting)             # Inside function: ['Hello', 'world']
print("After function: ", greeting)  # After function: ['Hello', 'world']

```

> [!warning] Beware [side effects](side_effect.md)!
> When passing a [mutable](mutability.md) argument to a function, the function can alter the argument, causing an unintended [side effect](side_effect.md). It is [good practice](function_conventions.md#have-no-side-effects) to avoid [side effects](side_effect.md) in your functions and not to use [input parameters as the function's output](function_conventions.md#dont-use-input-arguments-to-output-the-result).

# Mutable and immutable types in Python

In [Python Index](python_index.md), lists, sets and dictionaries are [mutable](mutability.md), whereas numbers, strings, tuples and frozen sets are [immutable](mutability.md). User-defined objects are [mutable](mutability.md) by default; however, you can make them [immutable](mutability.md) if you wish.
