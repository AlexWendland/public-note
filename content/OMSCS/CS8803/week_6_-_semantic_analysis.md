---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-05'
date_checked:
draft: true
last_edited: '2026-02-05'
tags:
  - OMSCS
title: Week 6 - Semantic Analysis
type: lecture
week: 6
---

Next we move on to the Semantic analysis stage of the compiler.
This answers questions like:

- Has a variable $x$ been declared?

- Does $x$ have the correct type?

- Are there variables that are declared but not used?

- Do two variables reference the same memory location?

The answers to these question are beyond the scope of what a CFG can check.
These questions rely on information such as:

- The value of a variable.

- Requires non-local information such as the type it was assigned before or the result type of a computation.

- Answers may involve computation and more complex logic.

There are two methods used to answer these questions within modern compilers:

- Attribute grammars.

- Ad-hoc techniques, such as:

  - Symbol tables.

  - Ad-hoc code for particular operations.

  - Use of a semantic stack to speed up analysis.

We will focus on the formalised version of attribute grammars, this is a specification on how to structure solutions to these questions.
This separates the what needs to be done from how it is done.
Though with this comes some issues - such as too much overhead in compilers, information that is not needed being passed around.
In reality, both attribute grammars and ad-hoc techniques are used in practice.

# Attribute grammars

> [!definition] Attribute grammar
> A attribute grammar consists of the following information:
> - A context-free grammar $G$ that describes the language of the program.
> - Each symbol in $G$ is associated with a set of named values or attributes.
> - For each value or attribute a rule on how to compute it using the values of their parent or children.
> - Attribute rules are functional; they uniquely define the value.

> [!example] Evaluating a signed binary number
> Suppose we have the grammar:
> ```
> <number> ::= <sign> <list>
> <sign> ::= "+" | "-"
> <list> ::= <list> <bit> | <bit>
> <bit> ::= "0" | "1"
> ```
> Now to evaluate the value of an expression we will associate the following attributes.
> | Symbol | Attribute |
> | ------ | --------- |
> | <number> | val |
> | <sign> | neg |
> | <list> | pos, val |
> | <bit> | pos, val |
> Then we define the rules as follows:
> ```
> bit.pos = parent_list.pos
> bit.val = 2^{bit.pos} if bit == "1" else 0
> list.pos = parent_list.pos + 1 if parent_list else 0
> list.val = child_bit.val + ( child_list.val if child_list else 0 )
> sign.neg = (sign == "-")
> number.val = - list.val if sign.neg else list.val
> ```
> Then when evaluating the expression `-1010` we get the following tree:
> 
> ```
> number()
> │       number.val = - 10 (calculated from children)
> ├── sign() -> "-"
> │             sign.neg = true
> └── list()
>     │     list.pos = 0
>     │     list.val = 10 (calculated from children)
>     ├── list()
>     │   │     list.pos = 1
>     │   │     list.val = 10 (calculated from children)
>     │   ├── list()
>     │   │   │     list.pos = 2
>     │   │   │     list.val = 8 (calculated from children)
>     │   │   ├── list()
>     │   │   │   │     list.pos = 3
>     │   │   │   │     list.val = 8 (calculated from children)
>     │   │   │   └── bit() "1"
>     │   │   │             bit.pos = 3
>     │   │   │             bit.val = 8
>     │   │   └── bit() "0"
>     │   │             bit.pos = 2
>     │   │             bit.val = 0
>     │   └── bit() "1"
>     │             bit.pos = 1
>     │             bit.val = 2
>     └── bit() "0"
>               bit.pos = 0
>               bit.val = 0
> ```
> Note: There is a left recursion here - which is why the outside most list has the 0 value bit.

Attributes can come from a number of sources:

- Synthesized: They are dependent on child values and constants.

  - These are called S-attributed grammars.

  - They can be evaluated on a single bottom-up pass.

- Inherited: They are dependent on parent values, constants and siblings.

  - Due to the dependence on siblings, they can not be completely calculated in a top-down approach.

- Both: They are dependent on both parent and child values.

- Neither: They are independent of parent and child values.
For example, sign.neg which depends only on the value of the sign symbol.

These dependencies make a dependency graph for how to calculate their values.
We require this graph to be acyclic else we will not be able to calculate them.

Attribute grammars allow us to:

- Take values from the syntax.

- Perform computations with the values.

- Insert tests of input values (which can raise errors).

To calculate these there are multiple approaches.

## Dynamic methods

1. Calculate the parse tree.

2. Build a dependency graph of the attributes.

3. [Topologically sort](../../notes/topological_sorting_(dag).md) the attributes based on their dependencies.

4. Calculate the attributes in topological order.

## Tree methods

1. Analyse the rules at compiler-generation time.

2. Determine a fixed (static) ordering.

3. Calculate the parse tree.

4. Evaluate nodes attributes in that order.

Functionally, this might involve defining some variables we calculate before calculating children and pass them down - whereas others we might calculate after and pass back up to the parent.

## Oblivious methods

These ignore the rules and parse tree and just do it in a convenient order (at design time) and use that.

# Circularity

Generally, determining if the dependency graph is acyclic is exponentially hard.
Though certain grammars can be proven to always generate an acyclic dependency graph.

> [!definition] Non-circular grammars
> An attribute grammar is non-circular if every possible input to it creates an acyclic dependency graph.

However, proving non-circularity is itself hard. There are families of grammars for which this can be done efficiently — the largest such class is:

> [!definition] Strongly non-circular grammars (SNC)
> An attribute grammar (or family of attribute grammars) is SNC if and only if there is a polynomial time test that can be run on the grammar to verify that it is a non-circular grammar.

Note: If we fail this test, it is not conclusive that the grammar is circular.
It just shows that it is not verifiably non-circular using this test.

# Summary

There are some key points when using attribute grammars:

- Non-local computation need lots of supporting rules to ensure non-circularity.

- Complex local computation is relatively easy.

- Lots of attributes adds considerable overhead when calculating attribute grammars.
This is extra bad when we need to copy information within a note to propagate it to the children.

- A compiler touches all the space it allocates, usually multiple times.
(This is why lots of compilers use semantic stacks - here we don't need to copy data for propagate it between nodes instead we can just grab it from the stack when we need it.)
