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

Function should do one thing, and one thing only. If you need to decide if it is doing more, write out in words what it is doing. If there are sections in your functions, then it for sure is doing too much.

#### Command Query separation

A function should either answer a question or do something, don't be tempted to include both.

#### Exception handling is one thing

Testing for an exception for another function call is one thing, then you can make handling the error another.

#### Switch statements are one thing

[[Switch statements]] are one thing and should appear only once. Normally these switch statements will be used to create a [[Polymorphism|polymorphic]] object and are hidden behind an [[Inheritance|inheritance]] relationship so the rest of the system can't see it. Look at the [[Constructor Pattern|constructor pattern]] to see example. 

#### Gluing functions together is one thing

A function can just be at a higher level of abstraction and just glue other functions together to make a higher order function.

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

## Function Arguments

The best functions are ones with no arguments (niladic). This makes it easier to read as regularly arguments are at a different level of abstraction to the function. Also easier for [[Testing|testing]] as you don't have to try the function with multiple different arguments. 

### Try to have less than 3 arguments

It is best to avoid functions with more than 3 arguments. There are obvious exceptions like a point in 4 dimensional space but this is a rule of thumb.

### Monadic functions

Monadic functions are ones that have one input argument. There are a couple reasons to use these.

#### Question

Ask a question about an input variable, such as `does_this_file_exist(fileName)`

#### Transformation

Something that takes an input argument and transforms it somehow. Then returns the altered variable as a return variable.

#### Event

This is an event trigger, such as if someone failed there password a given number of times. 

If the functions don't follow these sorts of patterns then it is unwise to use them.

### Dyadic functions

A function with two arguments is harder to understand than one.

### Make function variables instance variables

The arguments you might want to pass to the function could be instance variables. (This is a very [[Object Oriented Programming (OOP)|object oriented]] approach.)

### Flag variables

Flag variables should be avoided, they are an indicator that the function does more than one thing. They should either be an instance variable if it is effecting the class or hidden in one of the switch statements.

### Don't use input arguments to output the result

Most programmers won't expect the output to be given by an input variable such as using a [[Mutability|mutable]] variable. Provide the output as a new variable.

#### Don't pass in an object to write to

This is a tempting practice but instead call the write function on an object that can write. Or make the writer an instance variable of the object that owns the function. This makes it much more clear what is doing the writing or being written to. 

## Function organisation

### Use descriptive names
The name of the function should tell you exactly what it does. Look at [[Naming conventions|naming conventions]] to see how to do it.

#### Don't be afraid to use a long name
Remember writing a function should be like reading a book, functions are the sentences.

#### Start names with a Verb
A function should do or answer something, this should be the most dominant word in the name of the function.

### Step down rule

 > [!quote] [[Clean Code]]
> We want the code to read like a top-down narrative. We want every function to be followed by those at the next level of abstraction so that we can read the program, descending one level of abstraction at a time as we read down the list of functions. 

