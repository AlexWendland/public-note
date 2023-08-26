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

When using [[Recursion|recursion]] you generate a large number of [[Namespaces|namespaces]] for each function call you make. To get around this instead of leaving the function open whilst you call itself again - you can instead return a function to be called with the parameters already inside it. 

```python
def trampoline(function, **kargs):
	
```