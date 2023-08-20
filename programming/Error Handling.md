---
aliases: [error handling, exception handling, Exception handling, exception handler, Exception handler]
type: concept
publish: true
created: 2023-08-20
last_edited: 2023-08-20
tags: programming, clean-code
chatgpt: false
---
# Error Handling

To build robust software you must handle things going wrong. In code this comes in the form of error handling. There are many ways of handling errors, some common methods include: [[Exception|exceptions]], [[Error code|error codes]], and return objects.

We must build robust code, however this should be done in a way that maintains the readability and reusability of the code. For which there are some helpful principles here.

## Prefer [[Exception|exceptions]] to [[Error code|error codes]]

Whilst there are times when [[Error code|error codes]] are a better architectural solution than [[Exception|exceptions]] ([[When to Use Error Codes and Exceptions]]) within your own code [[Exception|exceptions]] increase the readability of your code due to the lack of case analysis after functions execute. Within [[Exception|exceptions]] you can provide the full context of why it was thrown, and should do this!

## Write your Try-Catch-Finally statement first

At the end of the Try and Catch blocks if your code is continuing on you should have a consistent state. i.e. if in your try block you define a return object within the catch blocks you will also need to have defined a return object.