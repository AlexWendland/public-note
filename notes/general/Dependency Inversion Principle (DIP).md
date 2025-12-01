---
aliases:
  - dependect inversion principle
  - DIP
  - Dependency inversion
checked: false
created: 2023-03-18
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: theory
---
# Dependency Inversion Principle (DIP)

The Dependency Inversion Principle (DIP) is one of the five principles of the SOLID acronym in object-oriented programming and design. It states that:

1.  High-level modules should not depend on low-level modules. Both should depend on abstractions.
2.  Abstractions should not depend on details. Details should depend on abstractions.

In simpler terms, the Dependency Inversion Principle promotes the idea that software components should depend on abstractions (interfaces or abstract classes) rather than concrete implementations. This principle aims to reduce the coupling between modules, making the system more flexible, maintainable, and easier to change or extend.

To apply DIP in practice, developers often use the following techniques:

1.  **Interfaces and abstract classes**: Define interfaces or abstract classes as contracts that concrete implementations must adhere to. This allows high-level modules to communicate with low-level modules through a shared abstraction, decoupling the two layers.
2.  **Dependency injection**: Instead of creating dependencies directly within a class, pass them as external parameters (constructor injection, method injection, or property injection). This makes the class more reusable and easier to test, as dependencies can be easily replaced or mocked.
3.  **Inversion of Control (IoC) containers**: Use IoC containers or dependency injection frameworks to manage and instantiate dependencies. These tools automatically resolve and inject the required dependencies at runtime, further decoupling the components and improving maintainability.

By following the Dependency Inversion Principle, developers can create modular and flexible software systems that are more resilient to change, easier to extend, and simpler to test.
