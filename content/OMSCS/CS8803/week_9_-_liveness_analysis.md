---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-03-02'
date_checked: '2026-03-03'
draft: false
last_edited: '2026-03-02'
tags:
  - OMSCS
title: Week 9 - Liveness Analysis
type: lecture
week: 9
---

In this lecture, we move from the front end (whose task it was to generate the IR and check the code for user errors) to the backend (whose need is to optimise the code and produce machine code for the target architecture).
The first part of this builds on the control flow graph in the previous lecture.
We need to study 'liveness analysis' the study of what variables are used where.
This will enable us to optimise for register allocation.

Whilst the IR generation was a local process, we will find that liveness analysis is a global process.
This means we need to consider the whole control flow graph to work out what variables are live at any given point.

# Program points

Given a program, that we have broken into basic blocks and have a control flow graph for we define a 'program point' which will have a particular set of variables being alive at.

> [!definition] Program point
> Given a basic block, there is a program point before and after each line of code.
> This means for a basic block of size $n$ there are $n + 1$ program points, as lines of code that follow one another the first lines after point is the same as the next lines previous point.

> [!definition] IN and OUT sets
> For each line of code $L$ we define $IN[L]$ to be the variables that are live at the program point before $L$ and $OUT[L]$ to be the variables that are live at the program point after.
> Given a basic block $B$ that consists of lines $L_1, \ldots, L_n$ we define $In[B] = IN[L_1]$ and $OUT[B] = OUT[L_n]$.
> Notice that $OUT[L_i] = IN[L_{i+1}]$ (but only for lines in the same block).

To perform liveness analysis we need to determine what $IN[L]$ and $OUT[L]$ is for each line of code.

> [!definition] Liveness
> A variable $x$ is live at a given program point if it has been allocated a value before that program point and that value is used later on in the code.

> [!example] Basic liveness example
> Consider the following code:
> ```
> 1. a = 0
> 2. b = a + 1
> 3. c = c + b
> 4. a = b * 2
> 5. if a < 9 goto 2
> 6. return c
> ```
> In this example we include the liveness sets below:
> | Line | Block | Live in | Live out |
> | :--- | :---- | :------ | :------- |
> | 1    | 1     | $\{c\}$ | $\{a, c\}$ |
> | 2    | 2     | $\{a, c\}$ | $\{b, c\}$ |
> | 3    | 2     | $\{b, c\}$ | $\{b, c\}$ |
> | 4    | 2     | $\{b, c\}$ | $\{a, c\}$ |
> | 5    | 2     | $\{a, c\}$ | $\{a, c\}$ |
> | 6    | 3     | $\{c\}$ | $\{\}$ |

Note that $IN[6] \neq OUT[5]$ as they are in different blocks!
An important nuance: a variable is not live if it is only defined later without being used; the variable must be both defined earlier and used later to be live.

# Liveness analysis

In small examples it is fairly easy to visually solve which variables are used later, however over larger code bases we need to automate this procedure.
You will notice from solving the problem above that you need to start from the end of the code to work which variables are used later.
Then you use the data within the line itself to adjust the $IN$ set from the previous line to get the $IN$ set of the current line.
Let's formalise the data from a given line.

## Within block analysis

> [!definition] DEF and USE
> For a given line $L$ we define $DEF[L]$ to be the variables that are assigned (defined) on the left-hand side of the assignment.
> We define $USE[L]$ to be the variables that are used (read) on the right-hand side of the statement.

For our previous example we have:

> [!example] Basic DEF and USE example
> Consider the code from the previous example, we have the following
> | Line number | line | DEF | USE |
> | :--- | :------ | :-- | :-- |
> | 1    | $a = 0$ | $\{a\}$ | $\{\}$ |
> | 2    | $b = a + 1$ | $\{b\}$ | $\{a\}$ |
> | 3    | $c = c + b$ | $\{c\}$ | $\{b, c\}$ |
> | 4    | $a = b * 2$ | $\{a\}$ | $\{b\}$ |
> | 5    | $if a < 9 goto 2$ | $\{\}$ | $\{a\}$ |
> | 6    | $return c$ | $\{\}$ | $\{c\}$ |

Now let's formalise the intuition I mentioned at the top of this section.
For a line $L$ we have the following relation:

$$
IN[L] = (OUT[L] - DEF[L]) \cup USE[L]
$$

Let's consider this intuitively. Given we know the variables that are used later ($OUT[L]$), we want to compute $IN[L]$.
If a variable is defined in $L$, then its value before this line doesn't matter since it gets overwritten - so we remove it from our $OUT[L]$ set.
However, to compute the values defined in this line, we need the variables in $USE[L]$ to be available, so they must be live before this line.

Using this relationship we can calculate the live variables at each program point within blocks as $OUT[L_i] = IN[L_{i+1}]$.
However, for this we need $OUT[B]$.

## Between block analysis

Given the control flow graph $G$ of blocks we can once again propagate values from the extremities.
For basic blocks with no child then we have $OUT[B] = \{\}$ as no variables are used after the point.
For blocks with children then we have the following:

$$
OUT[B] = \bigcup_{(B, C) \in E[G]} IN[C]
$$

In simple terms the live variables after a block must be the required variables for all its child blocks.

## Putting it all together

Putting this all together we can now iteratively solve which variables are live at each point in our program.

```
// Input:
//  P - the lines of the program
//  G - the control flow graph (with a mapping from P -> V(G))
// Output:
//  IN & OUT as defined above.
liveness_analysis(P, G):
  for all L in P:
    IN[L] = {}
    OUT[L] = {}
    DEF[L] = calculate_def(L)
    USE[L] = calculate_use(L)

  for all B (with lines L_i) in V[G]:
    OUT[B] = OUT[L_|B|] // equate
    IN[B] = IN[L_1] // equate
    For i = 1 to |B| - 1:
      Identify OUT[L_i] = IN[L_{i+1}]

  while IN/OUT has changed:
    // Update block internals
    For each L in reverse(P):
      IN[L] = (OUT[L] - DEF[L]) ∪ USE[L]

    // Update dependencies between blocks
    For each B in reverse(V[G]):
      OUT[B] = union_{(B, C) in E[G]} IN[C]
```

This will allow us to get liveness intervals for variables, which will assist in the next lecture on register allocation.
