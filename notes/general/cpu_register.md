---
aliases:
  - CPU registers
  - register
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
name: CPU register
tags:
  - OS
  - computer-science
type: definition
---
>[!tldr] CPU register
>A [CPU](central_processing_unit_(cpu).md) register is a small, fast storage location within the [Central processing unit (CPU)](central_processing_unit_(cpu).md) of a computer. They hold data that the [CPU](central_processing_unit_(cpu).md) is currently processing such as operands (the values to be operated on) or the result of operations. They also hold memory addresses or instruction pointers. They normally are small in size such as 32 or 64 [bits]([bit.md). (This often is referenced within the type of [CPU](central_processing_unit_(cpu).md) you have.) There are different types of registers:
>- **General-purpose registers (GRPs):** Used for all kinds of operations.
>- **Special-purpose registers**: These have specific purposes for [processes](process.md):
>	- **Instruction Register (IR)**: Holds the current instruction being executed.
>	- [Program counter (PC)](program_counter_(pc).md): Holds the address of the next operation to be executed.
>	- [Stack Pointer (SP)](stack_pointer_(sp).md): Points to the top of the [stack](stack_(os).md).
>	- **Status register**: Contains flags that indicate the state of the CPU, such as whether an operation resulted in zero or incurred an overflow.

