---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-04-06'
date_checked:
draft: false
last_edited: 2026-04-07
tags:
  - OMSCS
title: Week 13 - Procedure Abstraction
type: lecture
week: 13
---

In this lecture we cover how a compiler handles function calls.
These function calls could be to functions defined within the same code, or outside libraries that the compiler will need to 'link' to.

# Variable scopes

When we deal with function calls, where variables are defined becomes increasingly important.
We should choose which variables a function has access to carefully.
First a reminder of where variables could be stored within a virtual address space as below.

- Register: Just on the processor whilst executing.

- Stack: A last in first out (LIFO) stack, useful for variables with predictable lifetimes (function calls, local variables).

- Heap: A arbitrary bit of memory that can be allocated and deallocated on demand available throughout the programs execution.

- Data segment: A segment of memory that is used to store data which will need to be known ahead of time.

As a reminder, the structure of the virtual address space is shown below.

> ![Virtual Address space](../../../static/images/simple_virtual_address_space.png)

Normally, these are accessed through address pointers within the virtual address space - then we use an offset from that to get a location within the stack/heap/data segment.

There are different scopes variables can have:

- *Automatic & local variables* (Registers/stack)
  - These are variables that defined within the running of a function.
  - Lifetime: duration of the function call.
  - Scope: Limited to the function.
  - Size: Mostly known at compile time (exception: Variable length arrays which are not supported in all languages).

- *Static variables* (Data segment)
  - There are variables that are defined within the scope of a function/file but are not associated with any particular call of that function.
  - Lifetime: duration of the program execution.
  - Scope: Limited to the declaring scope.
  - Size: Known at compile time.

- *Global variables* (Data segment)
  - These are variables that are defined outside of any function.
  - Lifetime: duration of the program execution.
  - Scope: accessible anywhere from the program.
  - Size: Known at compile time.

- *Dynamic variables* (Heap)
  - This is data that is allocated and deallocated during the execution of the program.
  - Lifetime: Explicitly managed by the programmer.
  - Scope: Accessible via pointers from anywhere.
  - Size: Unknown at compile time.

## Local name translation

Local variable names are stored in the symbol table during compilation. The compiler uses this to generate code that computes addresses at runtime using level and offset.
This symbol table uses a two part address of `level` and `offset`.
The level identifies the nesting depth of scopes (used in languages with nested functions like Pascal; simpler in C where functions don't nest).
The offset is the position within that stack frame.

> [!note] Nested Function Definitions vs Function Calls
> "Nested functions" refers to defining one function **inside** another function's body (allowed in Pascal, Ada, nested JavaScript functions), NOT calling one function from another (which all languages support).
>
> In C, you cannot define functions inside other functions - all function definitions are at the top level. Function calls from one function to another are normal and don't create nesting levels.

This is possible to do with fixed sized data as we can calculate the offset during compile time.
For variable length local variables we use a two stage approach - the symbol table stores an offset to where a pointer variable lives, and that pointer holds the runtime address of the VLA data.
Then we append variable length data to the end of the stack of known fixed length data.
This way we still get our deterministic address lookup but we allow for variable length data that is only known at runtime.

![Variable length data](../../../static/images/variable_length_data.png)

## Global and static variable addressing

Global and static variables do not use the level and offset scheme described above.
Instead, they use **direct addressing** with fixed memory addresses in the data segment.
These addresses are determined at link time and baked directly into the machine code instructions.
At runtime, the program accesses them via absolute addresses (e.g., `mov eax, [0x804a020]`) with no frame pointer calculations needed.

# Activation records

An activation record is a data structure that contains all the information needed to execute a function call.
The areas within the activation record are:

- Parameters: The values of the parameters passed to the function.

- Register save area: The values of the registers that need to be saved before the function is called.

- Return value: The return value of the function.

- Return address: The address of the instruction that will return to the caller.

- Addressability: A section that helps with non-local access to variables.

- Caller's Activation Record Pointer (ARP): The address of the previous activation record.

- Local variables: The values of the local variables.

## Variable length data

The local variables section serves as the base address for accessing local variables during this function invocation, using the offsets calculated at compile time.
However, at compile time there is variable length data we do not want to spill into the next activation record so how do we handle this?

- If the activation record can be extended, then put the variable length data above the known length local variables.

- Otherwise, put variable-length data on the heap.

## Non-local data

If our function uses non-local stack variables (for example in nested functions) then we will need to access these using a display.
A *display* is a global lookup table of activation records, keying the level to the record itself.
With the level and the display we get back a pointer to the local variables which we can then use our offset to find the variable.
The display must be large enough to accommodate the maximum nesting depth of function definitions, which is known at compile time.
Note that recursion (a function calling itself) doesn't increase nesting depth - it reuses the same level.

![Display ARP](../../../static/images/display_arp.png)

# Linking

Linking is the process of going from one function to another - tldr it is how one function creates another activation record and hands over control, and how a function completes and hands back control to the calling function.
This whole process is called a linkage convention.
There are two sides to linking:

- *Caller*: The function that calls another function.

- *Callee*: The function that is being called.

The caller may not have access to the code for the callee, moreover the compiler will not know system code from user code.
Therefore, these conventions need to be followed by all compiled code that will work with this system.
The caller and callee each have responsibilities that depend on the other completing the correct sequence of operations.

## Saving registers

One of the most important jobs within linking is to save the registers of the caller, so when the callee returns the caller is returned into an operational state.
Both the caller and callee have different knowledge about what registers are used and are going to be used, critically we have:

- Caller knows which values are live across the call site.

- Callee Knows which registers are used within the function call.

Therefore, you can have different conventions on who does the saving but generally registers get divided into three groups:

- Caller-saved registers: Registers that the caller must save before the call IF their values are live (will be used after the call returns). The callee can freely modify these without preserving them.

- Callee-saved registers: Registers that the callee must save before using and restore before returning. The caller can assume these values are preserved across the call.

- Registers for linking: These are registers that are used to handle the linking process such as ARP, return address, etc.

## Linking code

To make this all work we need to pad function calls with code to save registers and generate the AR.
Suppose we have a function $p$ calling a function $q$ we have 4 additional bits of code that must be ran.

- $p$ normal operation

- $p$ calls function

- $p$ runs the *pre-call* code.

  - $q$ runs the *prolog* code.

  - $q$ normal operation.

  - $q$ runs the *epilog* code.

- $p$ runs the *post-return* code.

- $p$ continues normal operation.

![Procedure linkages](../../../static/images/procedure_linkages.png)

### Pre-call code

Within the pre-call code it needs to create the callee's activation record.
Then it needs to preserve the environment of $p$ saving the caller saved registers.
Lastly, it needs to update the registers for linking for $q$.
More precisely, it needs to:

- Allocate space for the callee's AR (except space for local variables).

- Evaluate each parameter and store the value or address in the AR (sometimes they use registers for this).

- Saves the return address in the callee's AR and puts the caller's ARP into it.

- Save any caller-saved registers (into the caller's AR).

- Jump to the callee's code.

### Prolog code

The main responsibilities here are setting up the callee's environment and preserve the last parts of the caller's environment that will be changed.
This entails:

- Save any callee-saved registers.

- If display is being used, then add itself to the display for the appropriate depth level.

- Allocate space for the local variables (easiest way to do this is extend the AR).

- Find any static data areas references in the callee.

- Handle any local variable initializations.

### Epilog code

Here we close up the callee's environment and restore the caller's environment.
This entails:

- Store the return value (different implementations might do this on the return call or in the epilog).

- Restore the callee-saved registers.

- Free any heap-allocated local variable storage (if applicable).

- Load return address from the AR.

- Restore caller's ARP.

- Jump to the return address.

### Post-return code

The main responsibility here is to finish restoring the caller's environment and place any value back to where it belongs so control can be fully handed back to $p$.
This entails:

- Copy return value from the callee's AR, if needed.

- Free the callee's AR.

- Restore any caller-saved registers.

- Restore any call-by-reference parameters to registers, if needed.

  - Also copy back call-by-value/result parameters.

- Continue normal operation.

## AR storage

There are two main ways to store the AR, either on the stack or in the heap.
Most languages use the stack (Algol rules) but some use the heap (ML heap).
For stack based AR's the callee-caller relationship is fairly simple:

- Easy to extend the AR by bumping the stack pointer.

- The caller and callee share this responsibility:

  - Caller can push parameters, etc. onto the stack and bump the pointer.

  - Callee can add local variables onto the stack and bump the pointer once again.

However if you have lots of variable length local variables using the stack can get messy.
Data intensive applications such as for ML tend to use heap storage for the AR's which make this relationship more complicated as it is hard to extend heap storage:

- One option is for the caller to pass everything to save into the AR via registers.

- Another option is to store parameters, return address, etc. in the caller's AR (but this means the callee is accessing the caller's AR which can lead to issues).

- Store the callee's AR size in a defined static constant for the caller to use (but this has problems with name mangling).

- Lastly, if your application does not have recursion you could allow activation records to be static and use the heap for variable length variables (fortran).

Though all of these approaches are uncommon and have drawbacks.
