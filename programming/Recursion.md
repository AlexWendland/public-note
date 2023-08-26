---
aliases: [recursion]
type: algorithm
publish: true
created: 2023-08-26
last_edited: 2023-08-26
tags: programming, algorithms
chatgpt: false
---
# Recursion

This is the technique of a function calling itself it iteratively find an answer and returning at some given condition.

The important thing to remember is to set up a return condition that will always be met otherwise, this could go on forever (see [[Halting Problem]]). 

## Example

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

## Complexity

Normally these algorithms have an exponential [[Run time complexity|run time]], as at each step of the recursion you split into normally a fixed set of possibilities. There are techniques such as [[Dynamic Programming|dynamic programming]] that can solve similar problems but in a linear [[Run time complexity|run time]].

They can also suffer from a bad [[Spacial complexity|space complexity]] due to the amount of [[Namespaces|namespaces]] they create for each function call, however there are techniques from [[Functional Programming|functional programming]] to get around this like [[Trampolining]].