---
aliases:
  - error handling
  - exception handling
  - Exception handling
  - exception handler
  - Exception handler
checked: false
created: 2023-08-20
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - clean-code
title: Error Handling
type: concept
---

To build robust software you must handle things going wrong. In code this comes in the form of error handling. There are many ways of handling errors, some common methods include: [exceptions](exception.md), [error codes](error_code.md), and return objects.

We must build robust code, however this should be done in a way that maintains the readability and reusability of the code. For which there are some helpful principles here.

# Prefer [exceptions](exception.md) to [error codes](error_code.md)

Whilst there are times when [error codes](error_code.md) are a better architectural solution than [exceptions](exception.md) ([When to Use Error Codes and Exceptions](when_to_use_error_codes_and_exceptions.md)) within your own code [exceptions](exception.md) increase the readability of your code due to the lack of case analysis after functions execute. Within [exceptions](exception.md) you can provide the full context of why it was thrown, and should do this! Whilst doing this follow the [Exception](exception.md) good practices.
[Exception good practices](exception.md#exception-good-practices)

# Write your Try-Catch-Finally statement first

At the end of the Try and Catch blocks if your code is continuing on you should have a consistent state. i.e. if in your try block you define a return object within the catch blocks you will also need to have defined a return object.

# Don't return null

Similar to [Error codes](error_code.md) but far worse - if you return null you have no context on what caused this issue and it can be **REALLY HARD** to track down what is causing it if it is not caught (especially in languages like python). Even if you do implement good typing and linting and handle them it litters your code with `if null` statements that are highly unreadable. Consider replacing this with an [exception](exception.md) or a [special case pattern](special_case_pattern.md).

## Aside: Don't pass null

Unless into a [Data structure](data_structure.md) that has optional values, having to handle null input has all the issues of returning null but just in the other direction. This is one of the [function conventions](function_conventions.md).


