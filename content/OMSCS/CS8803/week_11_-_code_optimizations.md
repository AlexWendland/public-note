---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-03-20'
date_checked: '2026-03-20'
draft: false
last_edited: '2026-03-20'
tags:
  - OMSCS
title: Week 11 - Code optimizations
type: lecture
week: 11
---

In the middle of the compiler we look at making the code more optimal in terms of runtime, resource usage, and code size whilst keeping the same functionality.
There are multiple ways we can do this:

- Discover and propagate some constant values,

- Move a computation to a less frequently executed place (eliminate repeated steps in loops),

- Specialize some computation based on context (e.g. compile time operations on constants and saving them as constants),

- Remove redundant computations,

- Remove useless or unreachable code, and

- Encode commonly used patterns in efficient forms.

We do this in a static manner (i.e. we can only look at the source of the code; we don't see runtime behaviour). To do this we use control flow analysis and data flow analysis.

> [!note] Never optimal
> There is no such thing as optimal code, due to the various requirements on code, we are doing optimisations but knowing we will never be optimal.

As there are many ways to optimise code we may have multiple steps here, where the IR output of one step is fed into the next step.

# Code redundancy

> [!definition] Redundant expression
> An expression is redundant if and only if along every path from the procedure's entry, it has been evaluated and its constituent sub-expressions have not been redefined.

If expressions are redundant we can use their previous computation instead of redoing the calculation.

## Local Value Numbering (LVN)

Let's first optimise at the basic block level by linearly going through each block.
The simple idea here is to assign a value $v(e)$ to each expression, then use this to check for redundancy.
We do this using a hash table $v$ and a hash function.
For constants and variables we have a method to generate a unique value for these.
For operations such as `t = op a, b` we take the hash of `<op, v(a), v(b)>` and assign this as the new value of `t`.
This gives us the following fact:

> For two expressions `e1` and `e2` within a basic block, if `v(e1) = v(e2)` then expressions `e1` and `e2` are syntactically equivalent and will compute the same value (assuming no intervening redefinitions).

Therefore we can use the value function to check for redundancy.
We will linearly go through the code and where we find the value of the expression is already in our hash table we use assignment rather than recalculating the value.

There are further optimisations we can add into this step:

- If we have an operation on two constant values, we can replace this with a new constant and add it to the data section - replacing the expression with a load operation for the new constant.
This is called constant folding.

- Handle algebraic identities like left-shifting by 1 is the same as multiplying by 2, etc.
This includes sorting the operands for commutative or associative operations.

- Handle special cases of operators such as multiplication by 1 or adding 0.

> [!example] Simple example
> Suppose we had the code below:
> ```
> a = x + y
> b = x + y
> a = 17
> c = x + y
> ```
> Then we create identifiers for everything:
> ```
> a3 = x1 + y2
> b3 = x1 + y2
> a4 = 17(4)
> c3 = x1 + y2
> ```
> This way we notice lines 2 and 4 are repeats of line 1, so we carefully need to replace these lines.
> ```
> t1 = x + y
> a = t1
> b = t1
> a = 17
> c = t1
> ```

In the above example we use a temporary variable to get around `a` taking on a new value half way through. An alternative approach that simplifies analysis and enables more powerful optimisations is **single static assignment (SSA) form**, where each new assignment gives a variable a new name. This makes data flow explicit and is fundamental to many compiler optimisations.

## Super-local Value Numbering (SVN)

The previous technique only operated over a single block.
However, for blocks with a single predecessor it is easy to expand out the technique above to larger sub-graphs of the control flow graph.

> [!definition] Extended basic block (EBB)
> A EBB is a maximal connected sub-graph of the control flow graph with a root block $B_0$.
> Each block in the EBB other than the root $B_0$ has a single predecessor in the control flow graph - that predecessor must be in the EBB.

Functionally EBBs look like 'sub-trees' of the control flow graph allowing to branch off but never join back.

![EBB example](../../../static/images/EBB_example.png)

The extension of LVN to EBB's then uses scoped symbol tables.
For each basic block build a symbol table - then extend that for a child block.
Making the algorithm exactly as you would expect - doing a kind of depth first search over the EBB's within the control flow graph.

```
// Input:
//   controlFlowGraph: The control flow graph where the blocks contain the code we need to transform.
//   root: The root block of the EBB we are analysing.
// Output:
//   Inplace transforms the control flow graph
SVN(controlFlowGraph, root) {
  workList <- [root]
  globalTable <- new table
  while workList is not empty:
    block <- workList.pop()
    SVNIterator( block, controlFlowGraph, globalTable, workList)
}

SVNIterator( block, controlFlowGraph, parentTable, workList) {
  thisTable <- new table extending parentTable with a new scope
  LVN( block, thisTable)
  for (block, childBlock) in controlFlowGraph:
    if childBlock has only one predecessor:
      SVNIterator( childBlock, controlFlowGraph, thisTable, workList)
    else if childBlock has not been processed yet:
      workList.append(childBlock)
  unallocate thisTable
}
```

## Single Static Assignment (SSA)

When looking at variables within the control graph it is very important to ensure unique assignment between blocks.
We do this through single static assignment (SSA) where for each assignment of a variable we give that variable a new name.
Notationally we do this by using an incrementing subscript for each variable assignment, in the example above this would be as below.

```
a_0 = x + y
b_0 = x + y
a_1 = 17
c_0 = x + y
```

We can do this in linear time by going through the IR.
The trouble with this approach is when two branches join - variables may be one of two names.
To allow for this we use a $\phi$ function - which chooses a variable name based on the branch it has come down.
For example if our code was as follows:

```
1. a = 1
2. if x goto 4
3. a = 2
4. y = a
```

Using SSA we would get:

```
1. a_0 = 1
2. if x goto 4
3. a_1 = 2
4. a_3 = phi(a_0, a_1)
5. y = a_3
```

This expands to larger examples like below.

![SSA example](../../../static/images/SSA_example.png)

In the example above, we see how SSA handles multiple control flow paths with $\phi$ functions at join points. Each variable has a unique version number, and the $\phi$ functions merge different versions that arrive from different paths. This makes the data flow graph explicit and enables powerful analyses.
