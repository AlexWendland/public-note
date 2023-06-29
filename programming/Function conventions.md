---
aliases: [function, functions, function convensions]
type: convensions
publish: true
created: 2023-06-29
last_edited: 2023-06-29
tags: programming, clean-code, 
chatgpt: false
---
# Function conventions

Functions should be small encapsulated bits of code that does a single thing. It takes parameters which it does not alter and potentially returns some value or alters the state of the object they belong to.

## Function body

### Functions should do one thing

Function should do one thing, and one thing only. If you need to decide if it is doing more, write out in words what it is doing. 

### Functions should be short

Functions should be short, ideally under about 20 lines long. If you are needing to go longer think to yourself if you are doing too much within this function. 

### Functions should read like a book

The function should read like a book, top down. In fact all your code should do this. 

### Functions should stay at one level of abstraction

When reading your function, if you need to go into details - then that should be a separate function.

### Functions shouldn't be too nested

If your code goes into 3 levels of nesting - that seems like it is doing too much. [Here](https://www.youtube.com/watch?v=CFRhGnuXG-4&ab_channel=CodeAesthetic) is a nice video about how to not nest your code - There are 2 main methods to get around it. 

#### Extractions
Pulling code out into their own functions.

#### Inversion
Flipping an if condition around for an early return.
```python
def do_something():
	if a == b:
		stuff_when_a_=_b()
	else:
		stuff_when_a_/=_b()
	return the_thing

def do_something_better{}:
	if a != b:
		stuff_when_a_/=_b()
		return the_thing
	stuff_when_a_=_b()
	return the_thing
```

