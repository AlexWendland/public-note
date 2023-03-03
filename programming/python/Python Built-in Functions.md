---
type: feature
publish: true
created: 2023-03-03
last_edited: 2023-03-03
tags: programming, python
---
# Python Builtin Functions
[[Python]] has some built in functions that make using the language slightly easier. You can find a full list of these in the [python documentation](https://docs.python.org/3/library/functions.html).

# Functions
## callable(object)
This returns `True` or `False` depending on if the object is callable. For example
- User-defined function using the `def` or `lambda` [[Keywords in Python|keywords]].
- Built-in [[Functions in Python|functions]], like these.
- Class [[Methods|methods]], functions attached to class objects.
- [[Classes in Python|Classes]], to instantiate them.
- Class instances, if the have implemented the .\_\_call\_\_ method.
- Generators, that have a `yield` method.

## dir(object)
This returns a list of names in the [[Namespace]] of the object, i.e. variables and functions you can call on it. This normally involves calling the .\_\_dir\_\_ function of the object. 

You can call it with no arguments and it returns all the names in the current [[Namespace]].

## enumerate(iterable, start = 0)
This returns a tuple which contains the next element of the iterable with a count that by default starts at 0 but can be set using start.

## eval(expression: str, globals: dict | None=None, locals: dict | None=None)
This will evaluate the expression as if it were python script and use the global and locals variables as if it where in that [[Namespace]] (i.e. you can provide values for the variables in the expression). The return value is the return value of the expression, which could be the last line of the expression.
```python
>>> x = 1
>>> eval('x+1')
2
```

## isinstance(object, classinfo: object | tuple)
If the first argument is a subtype of the second it returns true otherwise false. The second object can be a tuple of classes, then it returns true if it is a subtype of any of them. 

## len(object)
The returns the length of the object, it calls the .\_\_len\_\_  [[Special functions|special]] function of the object.

## max(iterable, _default_, key=None) or min(iterable,  _default_, key=None)
Will return the max/min of an iterable. You can provide a key function to evaluate items in the iterable (i.e. a certain value of a key in a dictionary). If you set a default value that will be returned if the list is empty, if you do not set it it will raise a [[Errors in Python|ValueError]] instead.

## open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
To understand this completely read the [documentation](https://docs.python.org/3/library/functions.html#open). However in short, it opens a file and returns a file object that can be read from or written to. The mode specifies what can be done to the object.

| Character | Meaning                                                         |
| --------- | --------------------------------------------------------------- |
| `'r'`     | open for reading (default)                                      |
| `'w'`     | open for writing, truncating the file first                     |
| `'x'`     | open for exclusive creation, failing if the file already exists |
| `'a'`     | open for writing, appending to the end of file if it exists     |
| `'b'`     | binary mode                                                     |
| `'t'`     | text mode (default)                                             |
| `'+'`     | open for updating (reading and writing)                         |

The encoding specifies the encoding of the object. 

The buffering specifies that, 0 is off, 1 is line buffering and an integer large than that is the size of bytes to buffer. 

Newline specifies what is a new line, None here is a universal set of newline characters.

I haven't used closefd or opener before.

## print(\*objects, sep=' ', end='\\n', file=None, flush=False)
This will print the objects provided to a file (if file is None then to [[Standard In Out and Error|Standard Out]]), it will seperate the objects using the _sep_ keyword and will end the string with _end_. It will call the str function to all objects if they are not already strings. If flush is true it will force the object to stop buffering and write.

## range(stop) or range(start, stop, step=1)
This returns a custom type object that holds numbers between start (inclusive) and stop (exclusive) where you increment in step. i.e.
$$
\mbox{range(start,stop,step)} = \{start + step*k\ |\ k \in \mathbb{N} \mbox{ if } start + step*k < stop\}.
$$
If only stop is specified then start = 0 and step = 1.

## reversed(iterable)
This will reverse the iterable, though only if it has a .\_\_reversed\_\_ function implemented in the class(or .\_\_len\_\_ and .\_\_getitem\_\_ implemented). 

## round(number, ndigits=None)
This will round a number to the nearest $10^{\mbox{ndigits}}$ where if ndigits is None the result will be an integer. When inbetween choices it will round to the nearest event choice, so 0.5 to 0 and 1.5 to 2. For numerical types it implements the .\_\_round\_\_ function.

> [!note] Floats
> For floats the behaviour is slightly different where it will simply truncate the expression to the required precision. 

## sorted(interable, key=None, reverse=False)
This returns a sorted list from the objects in the interable object. You can provide a key to apply to each of the objects in the iterable objects to get the key (i.e. getting one item in a dictionary). If reverse is True it will reverse the list of the items.

The sorting algorithm will use the .\_\_lt\_\_ [[Special functions|special]] function to sort the list.

## sum(iterable, start=0)
This will add the values in the iterable with the start value.

## super
Return a proxy object that delegates method calls to a parent or sibling class of _type_. This is useful for accessing inherited methods that have been overridden in a class.

## type(object)
This returns the object type, which is generally the same as .\_\_class\_\_ [[Special functions|special]] function (users can override the .\_\_class\_\_ function, which will cause this to differ). If you don't care about subtypes this is the best way to check an objects type.

If you provide it more than one argument, this can initiate an object. I have never done this before.

## zip(\*iterables, strict=False)
Iterate over several iterables in parallel, producing tuples with an item from each one.

By default zip will stop once the shortest iterable is finished, if you believe they should all be of the same length set strict=True if they are not of the same length a [[Errors in Python|ValueError]] will be returned.