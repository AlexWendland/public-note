---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-20'
date_checked: '2026-02-20'
draft: true
last_edited: '2026-02-20'
tags:
  - OMSCS
title: Week 7 - IR code generation
type: lecture
week: 7
---

Currently, we have checked the submitted code is valid and have an abstract syntax tree.
Next we will generate an intermediate representation (IR) of the program.
In fact, the AST is already a high level IR of the code.

# Intermediate Representation (IR)

An IR is a representation between the target and source languages.
A good IR maximises the goal of achieving a retargatable compiler.
One reason to use an IR is to perform machine independent optimizations.

There are three types of IRs:

- Structural IR: These are large graph-oriented representations that tend to be used in source-to-source translators.
An example of one is an AST.

- Linear IR: These are pseudo-code for an abstract machine that use simple compact data structures and are easy to rearrange.
The level of abstraction used in this varies.
For example, 3 address code, or a stack machine.

- Hybrid IR: A combination of the above.
For example a control-flow graph.

# Three address code

In this lecture we are going to focus on the linear IR 3 address code.
It generally takes the form of two operands with a result - but can use less than this.
Some examples are below:

- Arithmetic operations: x := y + z, or x := -y

- Data movement: x := y[z], x[y] := z, x := y

- Control flow: if y goto x, or goto x

- Function calls: param x, return y, call foo

In three address code we use temporary variables usually denoted t*.
We use these to group together operations, for example to evaluate `x - 2 * y` we could generate the following code:

```
t1 := 2
t2 := y
t3 := t1 * t2
t4 := x
t5 := t4 - t3
```

We can use these temporary variables to remove redundant operations.
For example, if `x + y` is computed in lots of locations - instead of recomputing it we will just reference the temporary value it was assigned in the first case.

## Helper functions

In what follows we will show how to implement a couple of expressions but first it is useful to discuss some helper functions.
For context, it is good to think that we will implement this on top of an AST.
Each statement we will encounter will be a node and could potentially have children.
Most of the time we will need to process the children in a particular order.
Whilst we are operating on an AST we are outputting to a linear file - converting our tree structure into a linear sequence of instructions.

- `emit(string)`: Writes the string to the output file as one line - it always writes it to the end of the file.

- `new_label()`: This generates a unique label name, this doesn't write this to the code but lets us use it in some code generation.

- `new_temp()`: This generates a unique temporary variable name, this doesn't write this to the code but lets us use it in some code generation.

- `generate(sub-tree)`: When describing how to make different types of operations, we use generate to essentially recursively call our generation on the sub-tree.
If the sub-tree is an expression we assume it has an output temporary variable, so often you will see `t = generate(expression)` - this means let `t` be the output variable from generating that expression.

Using these we will now show how to implement some example expressions.

## Simple binary operation

Suppose we have a simple operation like `exp1 + exp2` that could be represented in the AST as below.

```
      |
      v
    +---+
    | + |
    +---+
     / \
    /   \
   v     v
+----+ +----+
|exp1| |exp2|
+----+ +----+
  |       |
```

We will process this in the following way:

```
t1 = generate(exp1)
t2 = generate(exp2)
R = new_temp()
emit(R = t1 + t2)
```

> [!note] Output variable
> Here the output variable would be `R`.

This can be used for any binary operation rather than just plus:

- Binary arithmetic,

- Unary arithmetic, and

- Logical operations.

However, with logical operations there are some tricks we can use to speed up run time.

## Control flow

With more complex expressions we will start to use `goto` syntax.
If we generate a new label like so `E = new_label()`.
Then we can use this in our code by adding the line `emit( E: )`.
Then elsewhere in our code we can jump to this use by using `emit( goto E )`.

A lot of the time we actually want to conditionally jump to code based on a temporary variable `t`.
For this we introduce two jump conditions.

- `emit( if_goto t, E )`: If `t` is true then we jump to `E` otherwise we continue in the control flow.

- `emit( if_not_goto t, E )`: If `t` is false then we jump to `E` otherwise we continue in the control flow.

Sometimes we will write `if_goto expr, E` this is a short hand for:

```
t = generate(expr)
emit( if_goto t, E )
```

## If statements

Basic if statement use the `goto` as defined above.

```
if (exp) {
  statement
}
```
Which gets converted to:

```
end = new_label()
t = generate(exp)
emit( if_not_goto t, end )
generate(statement)
emit( end: )
```

We can extend this to if-else statements:

```
if (exp) {
  statement1
} else {
  statement2
}
```

as below:

```
end = new_label()
false_path = new_label()
t = generate(exp)
emit( if_not_goto t, false_path )
generate(statement1)
emit( goto end )
emit( false_path: )
generate(statement2)
emit( end: )
```

This can also be extended into `switch` and `elif` statements quite naturally.

## Short circuit evaluation

When evaluating logical or and logical and, within an if statement we can short circuit the evaluation.
Suppose we have the below code:

```
if (exp1 || exp2) {
  statement1
} else {
  statement2
}
```

Instead of calculating the whole of `exp1 || exp2` we can skip `exp2` if `exp1` is true. 

```
true_path = new_label()
end = new_label()
t1 = generate(exp1)
emit( if_goto t1, true_path )
t2 = generate(exp2)
emit( if_goto t2, true_path )
generate(statement2)
emit( goto end )
emit( true_path: )
generate(statement1)
emit( end: )
```

Notice that the order of `statement1` and `statement2` are reversed as we let the false path follow the if statement.

Similarly, we can do the same for logical and on the code below:

```
if (exp1 && exp2) {
  statement1
} else {
  statement2
}
```

By using the following interpretation:

```
false_path = new_label()
end = new_label()
t1 = generate(exp1)
emit( if_not_goto t1, false_path )
t2 = generate(exp2)
emit( if_not_goto t2, false_path )
generate(statement1)
emit( goto end )
emit( false_path: )
generate(statement2)
emit( end: )
```

This can be extended for more complex logical expressions to ensure as quick a pass through as possible!

## While loops

A while loop given below:

```
while (exp) {
  statement
}
```

On each loop evaluates `exp`, if it is true it runs statement and repeats.
Whereas if the expression is false breaks out of the loop.
So the code does exactly this.

```
start = new_label()
end = new_label()
emit( start: )
t = generate(exp)
emit( if_not_goto t, end )
generate(statement)
emit( goto start )
emit( end: )
```

## For loops

Whilst while loops are the only loops you need, for loops are a convenience that a lot of languages support as a structured while loop.

```
for (setup; exp; update) {
  statement
}
```

These use 3 sections, the `setup` ran only once at the start.
The `exp` is the same as the while loop.
The `update` is ran after each iteration.
This is converted down into essentially

```
setup
while (exp) {
  statement
  update
}
```

(Though setup is within the scope of the while loop - so it is a little more technical.)
This comes out to be:

```
start = new_label()
end = new_label()
generate(setup)
emit( start: )
t = generate(exp)
emit( if_not_goto t, end )
generate(statement)
generate(update)
emit( goto start )
emit( end: )
```

## Arrays

Arrays are referenced by pointer rather than having a temporary variable assigned for each value.
Therefore, to use the array values we need to `load` them from memory and we tend to have another temporary variable that will reference their location in memory.
Similarly, to 'set' values into arrays we use the `store` operation.

Suppose we have an array access like `exp1[exp2]`.
Let us assume `exp1` evaluates to some variable which has a type and importantly a `size` in our symbol table.
Then we can evaluate `exp1[exp2]` as below:

```
r = new_temp()
a = generate(exp1)
o = generate(exp2)
emit( o = o * a.size )
emit( r = a + o )
```

Where here the output temporary is the `r` which only points to the value in memory.

If the array value is being used in an expression, then we `load` the value like `x = exp1[exp2]`.

```
value = new_temp()
r = generate(exp1[exp2])
value = load(r)
```

Whereas if we are assigning to an array we use the store, for example `exp1[exp2] = exp3`.

```
value = generate(exp3)
r = generate(exp1[exp2])
emit( store *r = value )
```

Therefore array access require the context of how they are being used to evaluate them.

## Function calls

If we would like to evaluate `x = f(exp1, exp2, ...);` we need to know how functions are defined.
In this we will assume that a function has a label within our code path.
More than that, we will assume a special instruction `call_jump f` this will not only jump to `f` but once that code has terminated it will know to jump back to this instruction.
To parse variables into `f` we will assume it takes arguments from the top of the stack - therefore for us to load arguments for `f` we will use `push var` to put it on the stack.
Similarly, to get the return of the function we will assume it has put the result on the stack and we can get that from a special call `get_result`.
With all this context we will now show how to implement function calls - but there is still a lot to cover on this topic.

```
foreach exp-i
  ti = generate(expi)
  emit( push ti )
emit( call_jump f )
emit( x = get_result )
```

## Leaf values

The leaves of our AST are values like constants, and variables in memory.
Therefore, we need to know how to call `generate(v)` on these.
How we handle these depends on the type of machine we are running on.

- Virtual registers: We can use some finite number of virtual registers (just think holding area for values) and call `return v` on this.

- Strict register machine: Here we need to load the value of `v` for us to use like `emit( r = load v )`.

- Lower level machine: This may be implemented using an stack and we need to look up the value using a base and offset like `emit( r = base + offset )`.
Where `base` is the stack pointer and `offset` will come from the symbol table.

For constants these will normally be stored in the `data` component of our code - so may be handled differently.

# Optimizations

As mentioned above, there are optimisations we can make at this level by removing repeated calculations using the same temporary values.
This actually has a bigger implication on how we convert code.
For example if we had `a + b + c` the grammar may use left-associativity to convert it to `(a + b) + c` however - when 'looking ahead' we might realise that we need to calculate `a + c` later.
With this knowledge instead of following the grammar we could instead calculate `(a + c) + b` so we can reuse the temporary value `a + c`.
Therefore, deciding on the shape of the code is non-trivial if you are looking to make optimisations.

Similarly, if you consider a switch statement with multiple clauses there are multiple ways you could implement this.
First you could use a cascade of if else statements - meaning entering the first case only takes one evaluation but later ones grow for `O(n)` run time.
Or you could implement it using a jump table for dense integer cases with `O(1)` direct array lookup.
Alternatively, you could use a hash table for sparse or non-integer cases, which has `O(1)` average lookup but with hash computation overhead.
Otherwise if the comparison is on a numeric we could binary search for a `O(log(n))` cost.
No one option is better than the other all the time, it depends on the usage pattern whose context may not be known at compile time.

## Jump tables

A jump table is an efficient way to implement switch statements when the cases are dense, consecutive integers.
Instead of using a series of conditional checks, a jump table uses direct array indexing to find the correct code location to jump to.

For example, consider this switch statement:

```c
switch (x) {
  case 0: // code A
  case 1: // code B
  case 2: // code C
  case 3: // code D
}
```

A jump table implementation would create an array of code addresses (or labels):

```
jump_table = [label_A, label_B, label_C, label_D]
```

Then the switch statement compiles to something like:

```
if x < 0 or x > 3: goto default_case
goto jump_table[x]
```

This achieves `O(1)` lookup time regardless of which case is executed.
The main requirement is that the case values are integers and relatively dense (not too many gaps).
If the cases are sparse (e.g., `case 0`, `case 100`, `case 1000`), a jump table becomes wasteful as it would need a large array with mostly empty entries, making a hash table or binary search more appropriate.

