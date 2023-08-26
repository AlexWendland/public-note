---
aliases: []
type: algorithm
publish: true
created: 2023-08-26
last_edited: 2023-08-26
tags: programming, algorithms
chatgpt: false
---
# Recursion

This is the technique of a function calling itself it iteratively find an answer and returning at some given condition.

## Example

Given a set of single characters $C$ and a length $k$  print all strings of length $k$ using characters from $C$.

```python
def print_charracter_string(
	length: int, 
	charracters: set[str], 
	previous_string: str
):
	if length <= 0:
		print(previous_string)
	for charracter in charracters:
		print_charracter_string(
			length - 1, 
			charracters, 
			previous_string + charracter
		)

if __name__ == "__main__":
	length = 5
	charracters = {"a", "b"}
	print_charracter_string(5, charracters, '')
```