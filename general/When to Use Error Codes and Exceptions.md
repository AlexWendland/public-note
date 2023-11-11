---
aliases: []
checked: false
created: 2023-08-20
last_edited: 2023-11-11
publish: true
tags: programming
type: opinion
---
## When to Use Error Codes and Exceptions

## HTTP Stack

In the [[HTTP Protocol|HTTP protocol]], status codes serve as a standardized way of communicating the result of a client's request to a server. These status codes are well-defined, universally understood, and cover a broad range of scenarios from success (`200 OK`) to client errors (`404 Not Found`) and server errors (`500 Internal Server Error`). Using status codes in [[HTTP Protocol|HTTP]] is important for interoperability, as multiple clients and servers across different platforms and languages interact with each other.

## Within Your Programs

In contrast, within your own program, using [[Exception|exceptions]] over [[Error code|error codes]] can be more beneficial for several reasons:

1. **Readability**: Using [[Exception|exceptions]] makes it easier to follow the program's logic. You can write the main path of execution in a straightforward manner without littering the code with error-checking conditionals.

2. **Maintainability**: With [[Exception|exceptions]], you separate the error-handling code from the regular code, making it easier to update or extend functionality without risking the introduction of errors.

3. **Rich Context**: [[Exception|Exceptions]] can carry more context about the error, as they can include not just a status but also additional metadata. This can be helpful for debugging or for providing more descriptive error messages.

4. **Stack Unwinding**: When an exception is thrown, the runtime system searches back through the call stack to find the nearest enclosing [[Error Handling|exception handler]]. This makes it easier to handle errors at the appropriate level of abstraction.
## Hybrid Approaches

Some modern languages and frameworks use a combination of both [[Error code|error codes]] and [[Exception|exceptions]] for different scenarios. For example, in [[Asynchronous programming|asynchronous programming]] or when dealing with third-party libraries, error codes might be more appropriate for indicating status without disrupting the flow of execution.

## Summary

While [[HTTP Protocol|HTTP]] and similar protocols make effective use of [[Error code|error codes]] for cross-system communication, within your own programs, using [[Exception|exceptions]] generally leads to cleaner, more maintainable code. However, the choice between [[Exception|exceptions]] and [[Error code|error codes]] can also depend on the programming language, performance considerations, and specific use cases.
