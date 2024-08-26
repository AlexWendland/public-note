---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-08-26
last_edited: 2024-08-26
publish: false
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Introduction to Operating systems

![[Operating system (OS)]]

## Metaphor

The [[Operating system (OS)|OS]] is a lot like a toyshop manager. They are required to:

- Direct the operational resources
	- Controls use of employees time,
	- Distribute tools and parts between workers
- Enforces working policies
	- Ensures fairness between workers,
	- Make sure toys are made safely,
	- How to cleans-up after the job has been completed.
- Mitigates difficulty of complex tasks
	- Simplifies operations for each worker to do,
	- Chooses optimal task allocation to improve performance.

In comparison an [[Operating system (OS)|OS]] does the following:

- Direct the operational resources
	- Controls the use of CPU and memory,
	- Controls the use of peripheral devices.
- Enforces working policies
	- Can ensure fair use of the resources between different processes,
	- Limit resources a certain process has access to.
- Mitigates difficulty of complex tasks
	- Abstracts hardware (system calls).

## Examples

- Desktop
	- Microsoft Windows
	- UNIX-based 
		- Mac OS X (BSD)
		- Linux
- Embeded
	- Android
		- A form of linux
	- IOS
	- Symbian

We will focus on Linux in this course.

## OS elements

There are 3 main OS elements:

Abstractions:
- process,
- thread,
- file,
- socket, and
- memory page.

Mechanisms:
- create,
- schedule,
- open,
- write, and
- allocate.

Policies:
- [[ Least-recently used (LRU)]],
- [[Earliest deadline first (EDF)]]

### Example: Memory management

![[memory_management_example.excalidraw]]

## Design principles

- Separation of mechanism and policy 
	- Implement flexible mechanisms that support many policies
	- In different settings different policies make more sense.
- Optimise for common case
	- Where will the [[OS]] be used?
	- What wil the user want to execute on that machine?
	- What are the workload requirements?

## User/Kernel protection

![[Proccess modes]]

![[Trap instruction]]

User mode application have to access hardware through system calls. The [[Operating system (OS)|OS]] can notify applications through signals. 

## System call flow chart

![[System call]]




