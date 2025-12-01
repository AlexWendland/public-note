---
aliases:
  - SOLID
checked: false
created: 2023-03-18
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: theory
---
# SOLID principles

The SOLID principles are a set of five design guidelines for writing maintainable, scalable, and robust software in object-oriented programming. These principles were introduced by Robert C. Martin and are an acronym formed from the first letters of each principle:

1.  [[Single Responsibility Principle (SRP)|**S**ingle Responsibility Principle (SRP)]]: A class or module should have only one reason to change, meaning it should have a single responsibility or job. By adhering to this principle, developers can create more modular and focused code, making it easier to understand, maintain, and modify.
2.  [[Open Closed Principle (OCP)|**O**pen/Closed Principle (OCP)]]: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This principle encourages creating code that can be easily extended with new functionality without altering the existing code, which reduces the risk of introducing new bugs and improves maintainability.
3.  [[Liskov Substitution Principle (LSP)|**L**iskov Substitution Principle (LSP)]]: Subtypes must be substitute for their base types, meaning objects of a derived class should be able to replace objects of the base class without affecting the correctness of the program. By following this principle, developers can create more reusable and flexible code that adheres to the proper inheritance hierarchy.
4.  [[Interface Segregation Principle (ISP)|**I**nterface Segregation Principle (ISP)]]: Clients should not be forced to depend on interfaces they do not use. This principle suggests that interfaces should be small, focused, and specific to a particular client's needs, resulting in more modular and easier-to-understand code.
5.  [[Dependency Inversion Principle (DIP)|**D**ependency Inversion Principle (DIP)]]: High-level modules should not depend on low-level modules; both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle promotes the use of abstractions (interfaces or abstract classes) to reduce the coupling between software components, making the system more flexible, maintainable, and easier to change.

By adhering to the SOLID principles, developers can create more robust, maintainable, and scalable software systems in object-oriented programming.
