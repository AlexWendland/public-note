---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-20'
date_checked:
draft: true
last_edited: '2026-02-20'
tags:
  - OMSCS
title: Week 8 - Control flow graphs
type: lecture
week: 8
---

A control flow graph dictates how the flow of the code works in an IR of the program.
This is a graph whos nodes are 'basic blocks' and edges are potential changes of control.

# Basic blocks

> [!definition] Basic block
> A basic block is a sequence of consecutive IR statements in which flow of control can only enter at the beginning and leave at the end.

To identify basic blocks we look for 'leader statements' these are statements that follow from some kind of branch.
They follow these rules:

- Rule 1: The first statement in a program is a leader statement.

- Rule 2: Any statement that is the target of a branch statement is a leader.

- Rule 3: Any statement that immediately follows a branch or return statement is a leader.

Then to split a linear representation into basic blocks read the program down starting a new block at each leader statement.

> [!example] Basic block example
> Consider the following code:
> ```
> 1. prod = 0
> 2. i = 1
> 3. t1 = 2 ^ prod
> 4. prod = t1
> 5. t2 = i + 1 
> 6. i = t2
> 7. if i <= 20 goto 3
> 8. ...
> ```
> We have the following leader statements:
>
> - Line 1) This follows from rule 1.
>
> - Line 3) This follows from rule 2 with line 7.
>
> - Line 8) This follows from rule 3.
>
> Therefore our code has 3 basic blocks lines 1-2, 3-7, and 8 onwards.

# Control flow graph

> [!definition] Control flow graph
> A control flow graph is a multi-graph derived from a linear IR.
> The graph's nodes are the IR's basic blocks.
> There is a directed edge between two basic blocks if one of the following rules is met:
>
> - Rule A: There is directed edge from block B1 to B2 if the last statement of B1 branches to block B2 - blocks B1 and B2 can be the same.
> 
> - Rule B: There is a directed edge from block B1 to B2 if B2 immediately follows from B1 and B1 does not end in a unconditional branching operation.
>
> It is possible that there maybe two edges between blocks B1 and B2, in this case we label these edges for the different reasons they enter the block to distinguish them.
> For example, it maybe that a variable has a different value.

> [!example] Control flow graph example
> Consider the example from before we had 3 basic blocks.
>
> - B1: lines 1-2
>
> - B2: lines 3-7
>
> - B3: lines 8-
>
> From rule A we get the edge 'B2-B2' as line 7 goes back to the start of the block.
> From rule B we get edges 'B1-B2' and 'B2-B3', as whilst B2 does end in a jump statement it is conditional on the value of i.

> [!example] Control flow multi-graph
> Suppose we have the following code:
> ```
> ...
> 4. if i > n goto L1
> 5. L1:
> ...
> ```
> In this case 4 and 5 belong to different blocks by rule 2.
> However, both rule A and B give an edge between the two blocks - the edge from rule A happens if i > n, whereas the edge from rule B happens if i <= n.
> Therefore, the control graph in this case is a multi-graph having two edges between these nodes.

This covers the definition of a control flow graph.
It is used to reason about where the control of the program to go as we will see in later lessons.
