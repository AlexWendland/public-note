---
created: 2023-02-26
last_edited: 2023-02-26
publish: true
tags: programming, python, functional
type: feature
---
# Lambda functions
These are [[Anonymous Functions]] that take multiple inputs and evaluate the output in a single statement. It has the following syntax:

```python
lambda arguments : expression
```

> [!note] Syntactic Sugar
> A `lambda` expression creates a function object just like the `def` statement.

## Lundh's lambda Refactoring Recipe

If you find a piece of code hard to understand because of a `lambda`, follow this refactoring procedure:
1. Write a comment explaining what that `lambda` does.
2. Summarise that comment by a single statement.
3. Convert the `lambda` expression into a `def` expression with the name you found in (2) and the docstring with the comment you made in (1).
4. Remove the comment and use of the `lambda` statement with the new function.

## Examples

### Invert strings

```python
lambda string : string[::-1]
```

### Custom key to sort by

```python
>>> test = [
>>> 	{"name": "julian", "age": 10},
>>> 	{"name": "sandra", "age": 8},
>>> 	{"name": "jemima", "age": 9}
>>> ]
>>> sorted(test, key = lambda entry : entry["age"])
[
	{"name": "sandra", "age": 8},
	{"name": "jemima", "age": 9},
	{"name": "julian", "age": 10}
]
```
