---
aliases: [exceptions, exception, Exceptions]
type: definition
publish: true
created: 2023-08-20
last_edited: 2023-08-20
tags: programming,
chatgpt: true
---
# Exception

An exception is a mechanism used in many programming languages to interrupt the normal flow of execution when an error occurs. In languages like Java and Python, an exception is represented as an [[object]]. When an error condition is encountered, an exception is "thrown," interrupting the current process and propagating up through the program's call stack to find an appropriate "catch" block to handle the error.

Exceptions can be raised for various reasons, such as attempting to access an unavailable external [[API]], failing to find a specified file, or encountering a division by zero operation. When raised, these exceptions disrupt the normal flow of code execution.

Handling exceptions is typically done using "try-catch" blocks. The code inside the "try" block is executed until an exception is encountered. When that happens, the code inside the corresponding "catch" block is executed to manage the error.

![[When to Use Error Codes and Exceptions]]