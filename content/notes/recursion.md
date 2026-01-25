---
aliases:
  - recursion
  - recursive
  - recursively
created: 2023-08-26
date_checked:
draft: false
last_edited: 2023-11-13
tags:
  - programming
  - algorithms
title: Recursion
type: algorithm
---

This is the technique of a function calling itself recursively to find an answer and returning at some given condition. This is in opposition to [Iterative algorithms](iterative_algorithms.md) that achieve what they want in a for or while loop.

The important thing to remember is to set up a return condition that will always be met otherwise, this could go on forever (see [Halting problem](halting_problem.md)).

# Example

Given a set of single characters $C$ and a length $k$  print all strings of length $k$ using characters from $C$.

```python
from typing import Set

def print_characters_string(
    length: int,
    characters: Set[str],
    previous_string: str
):

    if length <= 0:
        print(previous_string)
        return

    for character in characters:
        print_characters_string(
            length - 1,
            characters,
            previous_string + character
        )

if __name__ == "__main__":
    length = 5
    characters = {"a", "b"}
    print_characters_string(5, characters, '')
```

# Versions

Recursion can be further classified into different forms.

## Simple (direct) Recursion

In simple or direct recursion, a function calls itself directly but not necessarily as the last operation. It might perform some calculations after the recursive call.

```python
def factorial(step: int):
    if step <= 0:
        return 1
    return step * factorial(step-1)
```

## Multiple or Tree Recursion

Here, a function calls itself more than once. This creates a tree-like call structure. The Fibonacci sequence is a classic example.

```python
def fibonacci(step:int):
    if step <= 0:
        return 0
    elif step == 1:
        return 1
    return fibonacci(step-1) + fibonacci(step-2)
```

Note these algorithms are likely to have exponential run time and in the case of the [Fibonacci sequence](fibonacci_sequence.md) this can be speed up with [Dynamic programming](dynamic_programming.md) instead.

## Tail Recursion

In tail recursion, the recursive call is the last operation in the function. Tail-recursive functions can be easily optimized by compilers or other techniques like [Trampolining](trampolining.md).

```python
def factorial_tail(step: int, accumulator=1 : int):
    if n == 0:
        return accumulator
    return factorial_tail(n-1, n * accumulator)
```

## Indirect Recursion

Indirect recursion involves a function `A` calling another function `B`, which in turn might call another function `C`, which eventually leads back to a call to `A`. Essentially, function `A` is indirectly calling itself through one or more intermediate function calls.

### Mutual Recursion

This is a subset of indirect recursion, where functions form a call cycle.

```python
def is_even(step: int) -> bool:
	"""
	Returns true if the positive integer is even.
	"""
    if step == 0:
        return True
    return is_not_odd(step - 1)

def is_not_odd(step:int):
	"""
	Returns false if the positive integer is odd.
	"""
    if step == 0:
        return False
    return is_even(step - 1)
```

# Advantages

1. **Simplicity and Readability**: Recursion can make some algorithms simpler and easier to understand. The reduction of complex tasks into simpler sub-tasks can result in more readable code.

2. **Elegant Solutions**: Problems that have recursive structures or can be divided into similar sub-problems can be naturally solved with recursion.

3. **Less Code**: Recursive methods can lead to shorter code, which is often easier to maintain.

4. **Immutable State**: In functional programming, recursion can help maintain [immutability](mutability.md), as you don't need loops and mutable variables.

5. **Easy to Parallelise**: Some recursive algorithms are easier to [parallelise](parallelisation.md) than their [iterative](iterative_algorithms.md) counterparts.

6. **Mathematical Induction**: Recursion is a direct implementation of mathematical [induction](induction.md), allowing you to solve problems in a mathematically sound way.

# Limitations

1. **Stack Overflow**: Each recursive call adds a new layer to the [stack](stack_(os).md), so if your recursion goes too deep, you risk running out of stack space and causing a stack overflow.

2. **Performance Overheads**: Recursive calls can be more expensive than simple loops due to the overhead of maintaining the [stack](stack_(os).md) and the function calls.

3. **Memory Usage**: Due to the use of the stack to keep track of operations, recursion can be memory-intensive.

4. **Hard to Debug**: Recursive functions can sometimes be tricky to debug because of their non-linear execution pattern.

5. **Limited Language Support**: Not all languages are optimized for recursion. For example, languages that don't optimize for tail recursion can run into performance issues for certain problems.

6. **Base Case**: Failing to define a base case can result in infinite recursion!

7. **Cognitive Load**: For some people, recursion is harder to understand than iteration, adding to the cognitive load of reading or maintaining the code.

8. **Side Effects**: In languages that allow [side effects](side_effect.md), care must be taken to understand how recursive function calls might affect shared state or variables.

9. **Optimization**: Some compilers or interpreters may not optimize recursion well, leading to inefficient code.
