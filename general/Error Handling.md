---
aliases:
  - error handling
  - exception handling
  - Exception handling
  - exception handler
  - Exception handler
chatgpt: false
created: 2023-08-20
last_edited: 2023-08-20
publish: true
tags: programming, clean-code
type: concept
---
# Error Handling

To build robust software you must handle things going wrong. In code this comes in the form of error handling. There are many ways of handling errors, some common methods include: [[Exception|exceptions]], [[Error code|error codes]], and return objects.

We must build robust code, however this should be done in a way that maintains the readability and reusability of the code. For which there are some helpful principles here.

## Prefer [[Exception|exceptions]] to [[Error code|error codes]]

Whilst there are times when [[Error code|error codes]] are a better architectural solution than [[Exception|exceptions]] ([[When to Use Error Codes and Exceptions]]) within your own code [[Exception|exceptions]] increase the readability of your code due to the lack of case analysis after functions execute. Within [[Exception|exceptions]] you can provide the full context of why it was thrown, and should do this! Whilst doing this follow the [[Exception]] good practices.
![[Exception#Exception good practices]]

## Write your Try-Catch-Finally statement first

At the end of the Try and Catch blocks if your code is continuing on you should have a consistent state. i.e. if in your try block you define a return object within the catch blocks you will also need to have defined a return object.

## Don't return null

Similar to [[Error code|Error codes]] but far worse - if you return null you have no context on what caused this issue and it can be **REALLY HARD** to track down what is causing it if it is not caught (especially in languages like python). Even if you do implement good typing and linting and handle them it litters your code with `if null` statements that are highly unreadable. Consider replacing this with an [[Exception|exception]] or a [[Special case pattern|special case pattern]].

### Aside: Don't pass null

Unless into a [[Data structure]] that has optional values, having to handle null input has all the issues of returning null but just in the other direction. This is one of the [[Function conventions|function conventions]].


