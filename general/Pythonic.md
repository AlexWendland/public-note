---
aliases:
  - pythonic
created: 2023-03-03
last_edited: 2023-03-03
publish: true
tags: programming, python
type: notation
---
# Pythonic

[[Pythonic]] means code that doesn't just get the syntax right, but that follows the conventions of the Python community and uses the language in the way it is intended to be used. [^1]

For example:

``` python
for index in range(len(some_list)):
	some_list[index].do_something()
```

would not be considered [[Pythonic|pythonic]] however

```python
for item in some_list:
	item.do_something()
```

would be as it uses the built in iteration of the [[Python Index|python]] language.

[^1]:https://stackoverflow.com/questions/25011078/what-does-pythonic-mean
