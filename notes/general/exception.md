---
aliases:
  - exceptions
  - exception
  - Exceptions
checked: false
created: 2023-08-20
draft: false
last_edited: 2023-11-11
title: Exception
tags:
  - programming
  - ''
type: definition
---
# Exception

An exception is a mechanism used in many programming languages to interrupt the normal flow of execution when an error occurs. In languages like Java and Python, an exception is represented as an [object](object.md). When an error condition is encountered, an exception is "thrown," interrupting the current process and propagating up through the program's call stack to find an appropriate "catch" block to handle the error.

Exceptions can be raised for various reasons, such as attempting to access an unavailable external [API](api.md), failing to find a specified file, or encountering a division by zero operation. When raised, these exceptions disrupt the normal flow of code execution.

Handling exceptions is typically done using "try-catch" blocks. The code inside the "try" block is executed until an exception is encountered. When that happens, the code inside the corresponding "catch" block is executed to manage the error.

[When to Use Error Codes and Exceptions](when_to_use_error_codes_and_exceptions.md)

>[!Note] [Checked exceptions](checked_exceptions.md) are a way of declaring [exceptions](exception.md) however you can have [exceptions](exception.md) that are unchecked.

## Exception good practices

- **Provide context to an exception**: The only time an exception is going to be read is when something has gone wrong in the program. Therefore write enough context in the exception for the person to quickly identify the cause of the issue.
- **Define exception classes in terms of the callers needs**: When considering how to define exceptions, via type of error or cause think about what will help the caller the most. This will likely be grouping errors based on how they will handle it.
- **Wrap 3rd party libraries and group exceptions**: It is a good practice to [wrap 3rd party libraries](wrap_3rd_party_libraries.md) and join up similar exceptions into one internally named exception. This saves people having to remember all the exceptions that can be thrown for a given library.
- **Only split exception classes if you want to handle them differently**: When deciding if a type of error needs its own class in your code, only choose to split it up if there are cases when you need to handle the two errors differently.
- **Handle errors at the lowest possible level**: Try to avoid try-catch logic wherever possible. If you need to use an [exception](exception.md) for a special cases consider using the [Special case pattern](special_case_pattern.md).
