---
aliases: []
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
title: Trampolining
tags:
  - programming
type: algorithm
---
# Trampolining

When using [recursion](recursion.md) you generate a large number of [namespaces](namespaces.md) for each function call you make. To get around this in the case of [tail recursion](recursion.md#tail-recursion) instead of leaving the function open whilst you call itself again - you can instead return a function to be called with the parameters already inside it. The runner for a trampoline looks like the following.

```python
from typing import Callable, Union, Any

def run_trampoline(func_to_trampoline: Union[Callable, Any]) -> Any:
    """
    A trampoline function that makes tail-recursive functions stack-safe.
    """
    result = func_to_trampoline
    while callable(result):
        result = result()
    return result
```

Then you could write your [recursion](recursion.md) problem so that it either returns the answer or another function to get that answer.

## Example

If you wanted to calculate the greatest common devisor of two positive integers you would apply the [Euclidean algorithm](euclidean_algorithm.md). This can be done by [recursion](recursion.md) using the following trampoline-able function.

```python
from typing import Callable, Union

def greatest_common_divisor(first_number: int, second_number: int) -> int:
    """
    Calculate the greatest common divisor of two integers using a trampoline.
    """
    def gcd_trampoline(
	    larger_number: int,
	    smaller_number: int)
	-> Union[int, Callable]:
        if smaller_number == 0:
            return larger_number
        else:
            return lambda: gcd_trampoline(
	            smaller_number,
	            larger_number % smaller_number
	        )

    # Swap the numbers if needed
    if first_number < second_number:
        first_number, second_number = second_number, first_number

    return run_trampoline(gcd_trampoline(first_number, second_number))

if __name__ == "__main__":
    result = greatest_common_divisor(252, 105)  # Should return 21
    print("Greatest Common Divisor of 252 and 105 is", result)

```

## Advantages

This method will stop

## Limitations
