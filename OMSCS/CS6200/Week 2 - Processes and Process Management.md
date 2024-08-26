---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-08-26
last_edited: 2024-08-26
publish: true
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - Processes and Process Management

![[Process]]

### Aside

![[Heap (OS)]]

![[Stack (OS)]]

![[Address space (OS)|address space]]

## Metaphor

A process is line an order of toys:
- State of execution:
	- Completed,
	- waiting, or
	- In progress.
- Parts and temporary holding area
	- Pieces used to make the toy, or
	- Containers to put the pieces.
- May require special hardware:
	- Sewing machine or
	- glue gun.

This is analogy to an [[Operating system (OS)|OS]] where a [[Process|process]] has:
- State of execution:
	- Program counter, or
	- Stack
- Parts and temporary holding area
	- data, or
	- registered state in memory.
- May require special hardware:
	- I/O, or
	- access to sound output.

## Process execution state

For the [[Operating system (OS)|OS]] to stop and start running [[Process|processes]] it must keep track of what it is doing. For this it uses:
- [[Program counter (PC)]]
- [[CPU register]]
- [[Stack Pointer (SP)]]

All this information is stored in the [[Process control block (PCB)|PCB]]:

![[Process control block (PCB)|PCB]]

This block is fully instantiated when a [[Process|process]] starts however it is frequently updated as the process is executing. It is the job of the [[Operating system (OS)|OS]] to keep this up to date and correct - it will need this when it starts and stops [[Process|processes]].

### Switching [[Process|process]]

When running a given [[Process|process]] that [[Central processing unit (CPU)|CPU]] has the [[Process control block (PCB)|PCB]] loaded into the [[CPU register|CPU registers]]. If the [[Central processing unit (CPU)|CPU]] were to suspend that process it would have to write that [[Process control block (PCB)|PCB]] to memory and load the new [[Process|processes]] [[Process control block (PCB)|PCB]] into the [[CPU register|CPU registers]]. This is called a [[Context switch (CPU)]].

![[Context switch (CPU)]]

Context switching is costly for two reasons:
- Direct costs: This comes from physically having to write the [[Process control block (PCB)|PCB]] from the [[CPU register|CPU registers]] into memory and vice versa.
- Indirect costs: The [[Central processing unit (CPU)|CPU]] has multiple layers of [[Cache|caches]]. When switching from one process to another you have to switch the data present in all these [[Cache|caches]] normally making data access temporarily very costly.

