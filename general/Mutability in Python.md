---
aliases: [mutability in Python]
type: concept
publish: true
created: 2023-07-17
last_edited: 2023-07-17
tags: programming, python
chatgpt: false
---
# Mutability in Python

In [[Python Index]] all [[Variables in python|variables]] are references to objects. These objects come with a [[Mutability|mutability]] property. Objects that are [[Mutability|mutable]] in python behave as you would expect. When a variable pointing to a mutable object is altered the object itself is altered.

```python
x = [1,2]
y = x
x.append(3)
print(y) # [1,2,3]
```

Here `x` and `y` point to the [[Mutability|mutable]] list object and when `x` is altered to add `3` to the list, as `y` points to the same object as `x` when you look at `y` it also has been changed.

Whereas when a variable pointing to an [[Mutability|immutable]] object in [[Python Index]] is altered, it creates a new object for the altered variable to point to and leaves the rest of the variables pointing to the old object.

```python
x = 1
y = x
print(x, id(x)) # 1 140703625587616
print(y, id(y)) # 1 140703625587616
x += 1
print(x, id(x)) # 2 140703625587648
print(y, id(y)) # 1 140703625587616
```

(The `id` function tells you the location in [[Random Access Memory (RAM)|computer memory]].)

## Passing arguments to functions

In [[Python Index]] all arguments are [[Passing variables to a function|passed by reference]] to functions. Though the [[Mutability|mutability]] of that [[Variables in python|variable]] dictates how the object is treated by that function.

For [[Mutability|immutable]] objects any alteration a function does to the object will not be reflected outside the scope of that function.

```python
def become_worldly(value):
    value += ' world'
    print("Inside function: ", value)

greeting = 'Hello'
print("Before function: ", greeting) # Before function: Hello
become_worldly(greeting)             # Inside function: Hello world
print("After function: ", greeting)  # After function: Hello
```

These essentially acts as if they have been [[Passing variables to a function|passed by value]], however this technique can reduce [[Random Access Memory (RAM)|computer memory]] usage if multiple variables hold the same value.

For [[Mutability|mutable]] objects any alteration the function does to the passed object will be reflected outside the scope of that function.

```python
def become_worldly(value):
    value.append('world')
    print("Inside function: ", value)

greeting = ['Hello']
print("Before function: ", greeting) # Before function: ['Hello']
become_worldly(greeting)             # Inside function: ['Hello', 'world']
print("After function: ", greeting)  # After function: ['Hello', 'world']

```

> [!Warning] Beware [[Side effect|side effects]]!
> When passing a [[Mutability|mutable]] argument to a function. This function can alter the argument causing an intended [[Side effect|side effect]] of that function. It is [[Function conventions#Have no side effects|good practice]] to not have [[Side effect|side effects]] of your function and to not use [[Function conventions#Don't use input arguments to output the result|input parameters as the functions output]]. 

## Mutable and Immutable types in python

In [[Python Index]], lists, sets and dictionaries are [[Mutability|mutable]] whereas numbers, strings, tuples and frozen sets are [[Mutability|immutable]]. User defined objects are by default [[Mutability|mutable]] however you can make them [[Mutability|immutable]] if you so wish. 