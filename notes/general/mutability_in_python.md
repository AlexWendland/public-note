---
aliases:
  - mutability in Python
checked: false
created: 2023-07-17
draft: false
last_edited: 2025-12-05
tags:
  - programming
  - python
title: Mutability in Python
type: concept
---

In [Python Index](python_index.md) all [variables](variables_in_python.md) are references to objects. These objects come with a [mutability](mutability.md) property. Objects that are [mutable](mutability.md) in python behave as you would expect. When a variable pointing to a mutable object is altered the object itself is altered.

```python
x = [1,2]
y = x
x.append(3)
print(y) # [1,2,3]
```

Here `x` and `y` point to the [mutable](mutability.md) list object and when `x` is altered to add `3` to the list, as `y` points to the same object as `x` when you look at `y` it also has been changed.

Whereas when a variable pointing to an [immutable](mutability.md) object in [Python Index](python_index.md) is altered, it creates a new object for the altered variable to point to and leaves the rest of the variables pointing to the old object.

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

These essentially acts as if they have been [passed by value](passing_variables_to_a_function.md), however this technique can reduce [computer memory](random_access_memory_(ram).md) usage if multiple variables hold the same value.

For [mutable](mutability.md) objects any alteration the function does to the passed object will be reflected outside the scope of that function.

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
> When passing a [mutable](mutability.md) argument to a function. This function can alter the argument causing an intended [side effect](side_effect.md) of that function. It is [good practice](function_conventions.md#have-no-side-effects) to not have [side effects](side_effect.md) of your function and to not use [input parameters as the functions output](function_conventions.md#dont-use-input-arguments-to-output-the-result).

# Mutable and Immutable types in python

In [Python Index](python_index.md), lists, sets and dictionaries are [mutable](mutability.md) whereas numbers, strings, tuples and frozen sets are [immutable](mutability.md). User defined objects are by default [mutable](mutability.md) however you can make them [immutable](mutability.md) if you so wish.
