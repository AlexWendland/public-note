---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-03-20'
date_checked: '2026-03-20'
draft: true
last_edited: '2026-03-20'
tags:
  - OMSCS
title: Week 12 - Instruction Selection
type: lecture
week: 12
---

In this lecture, we will learn how to map from the IR to the target instruction set.

> [!definition] Instruction Set Architecture (ISA)
> The ISA is the set of instructions that a processor can execute.
> These cover 4 major categories:
> - Load/Store instructions,
> - Arithmetic and logical instructions,
> - Control flow instructions, and
> - Coprocessor instructions for concurrency.

There are two main types of ISAs:

- Reduced instruction set computer (RISC): As the name suggests, this is a simple set of instructions optimised for control.
It uses the load-store model where only the load and store instructions operate on memory.
The reduced set of instructions means the complexity is in the compiler rather than the hardware.

- Complex instruction set computer (CISC): This has a large set of instructions that combine multiple lower-level instructions.
Lots of different instructions operate on memory, so the cost of each operation might be harder to work out.
This pushes the complexity into the processor, which allows simpler compilers.

> [!note] Historical note
> CISC historically was the dominant type of instruction set, allowing programs to reduce their size and memory footprint.
> However, in the 1980's there was a shift to RISC processors due to the increase in memory and the need to simplify processors to increase performance.
> Modern processors normally use a RISC architecture internally even if they offer a CISC interface with the processor doing the simplification from CISC to RISC.

# Translation

There are normally multiple ways to go from your IR to ISA.
Therefore it is important to choose the optimal path.
Each instruction in the target ISA comes with a size and time cost.
Therefore it is usual for you to try multiple different approaches and measure the performance of the output.
To do this we associate a cost with each instruction and then measure the cumulative cost of all instructions to pick a translation.
Normally this cost is cycles, but it is impossible to do this completely accurately as we need to make assumptions about what is in cache, etc.

> [!example] Swapping two variables of the same type
> Suppose we want to swap the values of rx and ry. There are two ways to do this.
> ```
> mov rx, rt
> mov ry, rx
> mov rt, ry
> ```
> This uses a 3rd register rt to temporarily hold the value of x whilst we copy y into x.
> Instead we could use `xor` the exclusive or operator.
> ```
> xor rx, ry
> xor ry, rx
> xor rx, rx
> ```
> This uses a cheeky trick that `xor a a` is 0 and `xor 0 a` is a.
> This way `ry = ry xor (rx xor ry) = rx` and `rx = rx xor (rx xor ry) = ry`.
> Using a conventional processor, the first way will be faster but uses an additional register.
> This is where trade-offs come in - if you have spare registers, the first approach is better, but if you're short on registers the XOR trick avoids needing memory.

## Tree representation

The first step of the translation is to take our IR and represent it as an operation tree - similar to our AST.

> [!example] IR to tree
> Suppose we have the following IR:
> ```
> t1 = j*4
> t2 = b + t1
> t3 = *t2
> t4 = i + 1
> t5 = t4*4
> t6 = a + t5
> *t6 = t3
> ```
> We can regroup operations into a tree as below.
> ![IR to tree](../../../static/images/instruction_set_tree.png)

Then we want to cover this tree in 'tiles' in a minimal way.

> [!definition] Tile
> A tile is a contiguous piece of the tree that corresponds to a machine instruction.

In the example, j x 4 might be represented as `muli 4, rj` which would be a single tile and come with an associated cost.

A covering of the tree in tiles is called a tiling of a tree.
We try out multiple different tilings of the tree and choose the one with the lowest cost.
We do this using a 'post-order tree walk' i.e. starting at the bottom of the tree and working our way up.
To then implement this tiling we write down the instructions associated with the tiles bottom up.

## Dynamic programming

As we get larger trees and lots of different options at each node, we will find the solution space gets very large.
This is where dynamic programming and memoisation comes into play.
We can solve the solutions on smaller sub-problems and use those solutions to help us come up with a larger solution.

This can be implemented in an ad-hoc manner for your particular problem. However, there are many generic solutions to this problem, such as:

- BURG,
- Twig,
- BEG, and
- Bottom-Up Rewrite System (BURS).

# Modern processors

Determining cost in modern processors is complicated by features such as:

- Pipelining: Allowing parts of different instructions to overlap.
- Superscalar: Some operations can be executed in parallel.

This means that the cost of instructions is very difficult to work out and depends heavily on the architecture.
