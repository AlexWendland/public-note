---
aliases: []
type: algorithm
publish: true
created: 2023-08-26
last_edited: 2023-08-26
tags: programming
chatgpt: false
---
# Trampolining

When using [[Recursion|recursion]] you generate a large number of [[Namespaces|namespaces]] for each function call you make. To get around this instead of leaving the function open whilst you call itself again - you can instead return a function to be called with the parameters already inside it. The runner for a trampoline looks like the following.

```python
from typing import Any

def _trampoline(trampoline_function: Any):
	trampoline_result = trampoline_function
	while callable(trampoline_result):
		trampoline_result = trampoline_result()
	return trampoline_result
```

Then you could write your [[Recursion|recursion]] problem so that it either returns the answer or another function to get that answer.

## Example

If you wanted to calculate the greatest common devisor of two positive integers you would apply the [[Euclidean algorithm]]. This can be done by [[Recursion|recursion]] using the following trampoline-able function.

```python
def _greatest_common_devisor_trampoline(larger_multiple:int, smaller_multiple:int):
	if smaller_multiple == 0:
		return larger_multiple
	else:
		return lambda: gcd(
			smaller_multiple, 
			larger_multiple % smaller_multiple
		)

def greatest_common_devisor(first_multiple:int, second_multiple:int):
	if first_multiple < second_multiple:
		first_multiple, second_multiple = (second_multiple, first_multiple)
	return _trampoline(_greatest_common_devisor_trampoline(a,b))
```