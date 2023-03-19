---
aliases: [OCP, Open Closed principle]
type: theory
publish: false
created: 2023-03-18
last_edited: 2023-03-19
tags: programming
chatgpt: true
---
# The Open Closed Principle (OCP)

This is one of the [[SOLID principles]] and states: 

>[!quote] [[Bertrand Meyer]] - 
>software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification

In simpler terms, this principle suggests that a well-designed software component should be easily extendable with new functionality without requiring modifications to its existing code. This approach aims to improve maintainability, reduce the risk of introducing new bugs, and promote reusability.

To achieve this, developers often use the following techniques:

1.  **Abstraction and interfaces**: Define interfaces or abstract classes to establish contracts that concrete implementations must adhere to. This allows developers to extend functionality by creating new classes that implement these interfaces without altering the original code.
2.  **Inheritance and polymorphism**: Leverage inheritance to create specialised sub classes that extend or override the behaviour of their parent classes, while retaining the original structure and behaviour.
3.  **[[Dependency Inversion Principle (DIP)|Dependency inversion]]**: Rely on abstractions rather than concrete implementations, making it easier to swap or extend components without affecting the existing code-base.

By adhering to the Open/Closed Principle, developers can create more flexible and robust software systems that are easier to maintain and extend over time.
  