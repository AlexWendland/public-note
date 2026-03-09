---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-03-03'
date_checked: '2026-03-05'
draft: false
last_edited: '2026-03-03'
tags:
  - OMSCS
title: Week 10 - Register Allocation
type: lecture
week: 10
---

So far the front end has converted the input code into a format that assumes infinite registers - the three-address code.
However, real machines are limited by the number of registers they have available.
Ideally we would keep all numbers we need to use in registers and only use memory when we need it.
These may also be for different purposes such as function inputs, for floats or ints, or be restricted for the stack pointer.
We need to factor all this in when we go from our IR to assembly code.
Therefore, this process has two different stages:

- Register allocation: Deciding which numbers we need in registers and which we can use in memory.

- Register assignment: Which register each number should be in.

# Register Allocation

Register allocation is one of the single largest optimisations you can make on run time, energy efficiency and longevity of the processor.
The goal here is to minimise the amount of load and store operations.

## Definitions

We have multiple terms when we talk about variables that are good to differentiate:

- Gen: The first time a variable is defined within a program.

- Kill: Old value is no longer needed (occurs when a variable is redefined).

- Def: The variable appears on the LHS of an assignment statement.

- Use: The variable is used on the RHS of an assignment statement.

- Live: The variable's current value will be used later in the program.

- Dead: The variable value is no longer used in the program and the value will be overwritten before the next use.

Note: A "kill" of a variable is what separates one web from another - when a variable is killed (redefined), a new web begins for that variable name.

## Interference Graph

Suppose we have two variables `a` and `b` who have liveness ranges [1,5] and [3,4].
As the ranges overlap we say the variables `a` and `b` *interfere* with one another.
Given the liveness ranges for all our variables we can draw a graph of the interference graph $I$.
This has a vertex for each variable $V(I)$ and an edge in $E(I)$ for two variables who interfere with one another.
Given we have $k$ registers a register allocation is a colouring of this graph $c: V(I) \rightarrow \{1, 2, \ldots, k\}$ such that no two vertices sharing an edge have the same colour (a proper colouring).

Above is intuitively what we want to do - however this does not respect the control flow of our code.

> [!definition] Web
> A web is a maximal set of definitions and uses of a variable that share the same value.
> To construct webs: connect each `def` statement to any `use` statement that could use that definition (respecting control flow), then take the transitive closure of these connections.
> A web is any connected component in this def-use graph.
> Multiple webs can exist for the same variable name if it's redefined at points that kill the previous value.

The transitive closure means that if we connect definition A to use B, and use B to definition C (through control flow), then A and C are also connected.
In other words, a web captures all definitions and uses of a variable that are "reachable" from each other through the program's control flow without an intervening definition that overwrites the value.
This means a single variable name can have multiple webs if it's redefined in a way that kills the previous value.

![web example](../../../static/images/webs_example.png)

You can see in this example 4 blocks of a control flow graph.
We have 4 webs $s_1$, $s_2$, $s_3$ and $s_4$.
Via the transitive closure $s_2$ spans over all 4 control blocks.
Though it is separated from web $S_4$ using the same variable `x` as the def block means that the variable in $s_4$ does not use the same value.
Similarly the blocks $s_1$ and $s_3$ both use `y` the value is never the same and therefore they are in separate webs.

These webs then define 'live ranges' within the blocks that they have lines in.

> [!definition] Interference
> We say two webs interfere with one another if they have overlapping live ranges.

In the example above you can see $s_1$ interferes with $s_2$ and $s_2$ interferes with $s_3$ but nothing interferes with $s_4$.

> [!definition] Interference Graph
> The interference graph $I$ has vertices $V(I)$ as the web vertices and edges $E(I)$ as the interference edges.

Given we have $k$ registers a register allocation is a colouring of this graph $c: V(I) \rightarrow \{1, 2, \ldots, k\}$ such that no two vertices sharing an edge have the same colour (a proper colouring).
However, this colouring might not always be possible.

## Spill cost

If we can not colour the graph we will need to store the values in memory.
This is called spilling.
To help us prioritise which values to keep in registers and which to spill we can use a spill cost.
The spill cost intuitively is how much work it would be to spill a value.
However, with loops and conditionals at compile time it is not possible to know this value.
So instead we try to guess the spilling value using certain heuristics over the control flow graph.

For each load or store operation we have to introduce we multiply the cost of the operation by its 'loop depth'.
We assume each loop will iterate 10 times, so we say the spill cost of a load/store instruction that has loop depth `d` is `base_cost * 10^d`.
Using this we look at each web in the graph and find all the sites we would need a load/store instruction if this web spills.
Then we add up the spill costs of all the loads/stores in this web.
This will be our spill cost for this web.

> [!example] Spill Cost
> Consider the simple code below:
> ![spill cost example](../../../static/images/spill_cost_example.png)
> In this code we have two webs, one for `x` and the second for `y`.
> If we spill `x` we would need a store in the first basic block and a load in the second basic block.
> Therefore `x` has a spill cost of 2.
> Instead, look at `y` it would need a store cost in the first block, and second block then a load cost in the second block, and third block.
> As the second block is in a depth 1 loop we assume instruction cost here is 10.
> So `y` has a spill cost of `1 + 10 + 10 + 1 = 22`.

## Graph Colouring

To create this graph colouring is an NP-complete problem, so for large code bases it would be infeasible to do this perfectly.
However, there are good heuristics to make a graph colour which are not perfect but are good enough.

Suppose we are trying to colour the graph with $k$ registers.
Note that if in the interference graph it has degree less than $k$ we can definitely colour that vertex.
Using this idea we can develop a simple algorithm for colouring the graph:

```
// Input: Interference graph I, with spill costs c, and a set of registers k.
// Output: A set of spilling vertices S and a partial colouring c' : V(I) \ S \rightarrow \{1, 2, \ldots, k\}
optimisticRegisterAllocation(I, c, k) {
  St = stack()
  R = V(I)
  while (R is not empty) {
    let v have smallest degree in I|R (I restricted to the vertices in R) with the lowest split cost c(v)
    St.push(v)
    R.remove(v)
  }
  Initialise c' to be an empty map
  Let S be an empty set
  while (St is not empty) {
    let v = St.pop()
    if there exists a valid colour for v:
      c'[v] = smallest i in {1, 2, ..., k} such that no neighbour of v has colour i
    else:
      S.add(v)
  }
  return S, c'
}
```

There are two ideas here:
1. The algorithm is called "optimistic" because it pushes all vertices onto the stack regardless of degree, hoping that when we pop them back later, we can find valid colors.
If a vertex has degree less than k in I|R, it will definitely have a color available when we remove it (since it has fewer than k neighbors).
For vertices with degree ≥ k, we're optimistic that some neighbors will share colors, leaving at least one color available.

2. We put vertices on the stack with the lowest spill cost first, so that vertices with high spill cost are pushed later and colored first (since we pop from the stack in reverse order).
This prioritises keeping expensive-to-spill vertices in registers.

This algorithm has polynomial run time, so is workable even for large code bases.
There is an alternate version of this algorithm which runs a bit faster but leads to lower register utilisation.

```
// Input: Interference graph I, with spill costs c, and a set of registers k.
// Output: A set of spilling vertices S and a partial colouring c' : V(I) \ S \rightarrow \{1, 2, \ldots, k\}
pessimisticRegisterAllocation(I, c, k) {
  St = stack()
  R = V(I)
  Let S be an empty set
  while (R is not empty) {
    let v have smallest degree in I|R (I restricted to the vertices in R) with the lowest split cost c(v)
    if degree(v) < k:
      St.push(v)
    else:
      S.add(v)
    R.remove(v)
  }
  Initialise c' to be an empty map
  while (St is not empty) {
    let v = St.pop()
    c'[v] = smallest i in {1, 2, ..., k} such that no neighbour of v has colour i
  }
  return S, c'
}
```

In this "pessimistic" version, we assume that if the degree of a vertex in `I|R` is greater than or equal to `k`, we won't be able to colour it, so we immediately add it to the spill set S rather than pushing it onto the stack.
This is more conservative and guarantees that all vertices we try to color will succeed, but it may spill more variables than necessary.

## Splitting webs

Right now we have assumed if we can't colour a web we will spill it completely, i.e.:

- After each def we will store it, and

- Before each use we will load it.

However, there is a 3rd path - instead of completely spilling the web we could split it to reduce the impact that web has on the rest of the interference graph.

> [!definition] Splitting web
> We can split a web into two by partitioning the live ranges the variable uses.
> This means whenever we leave the live range for the first part we perform a store action.
> Whenever we enter the live range for the second part we perform a load action.
> Therefore similarly to split cost we can calculate the cost of each splitting as well.

When we want to decide which webs to split here are some heuristics to use:

- Nodes with large degree in the Interference graph.

- Nodes with low spill cost for a split.

Once we have split a vertex we get a new Interference graph where this web has now been split into two.
This comes with the cost of the split but has the upside of lower spill cost of colouring the graph - therefore choosing when to split is important.

### The iterative process

When we identify webs to spill or split (in the set S from our allocation algorithms), we must:
1. Rewrite the code to insert the necessary load/store instructions
2. Rebuild the interference graph with these changes (the loads/stores may introduce new short-lived webs)
3. Re-run the register allocation algorithm on the new interference graph

This process repeats until we successfully color the entire graph with no spills.
In practice, most programs converge quickly, but pathological cases may require multiple iterations.

## Further Optimisations

### Register Coalescing

When we have a assign operation between two registers, we can reduce the size of the Interference graphs nodes by just combining the two webs relating to these variables.
However, this comes at the risk of making the graph not colourable - so should be done with caution.

### Register Targeting

Some registers are required for a functions arguments or a functions return value.
These are common causes of register copy as above.
If instead we make sure the register used for these variables is the register needed then we avoid this copy all together.
This can be achieved by pre-colouring webs we know will be used for this registers.

### Pre-splitting webs

There are multiple cases you could detect to simplify the colouring stages by pre-splitting webs:

- Some live ranges that have large dead regions where the variables are not used at all.

- Large live ranges that have a small cost associated to splitting them into smaller live ranges.

- Strategic locations where there will be high spill cost for other variables such as call sites for functions or highly nested loops.

The cost of pre-splitting is the cost of the split which might not be needed to be paid.

### Interprocedural register allocation

When a function call is made you save all the registers in the current program and load the needed registers for the next function call.
Similarly when you return from a function call you restore these.
This can cause a large cost incurred especially if your programs have lots of small functions or they are called in tight loops.
However there are ways to get around this:

- Essentially, in-lining the function so we don't have to pay this cost at all.

- Developing a per-call site instance of the function which optimises its register usage for that call.

