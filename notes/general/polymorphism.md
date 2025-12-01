---
aliases:
  - polymorphic
  - Polymorphic
  - polymorphism
checked: false
created: 2023-03-19
draft: false
last_edited: 2023-11-11
name: Polymorphism
tags:
  - programming
type: theory
---
# Polymorphism

This is the ability of a single interface or base class to represent multiple concrete types or classes. This allows objects of different classes to be treated as objects of a common superclass or interface.

Polymorphism enables developers to write code that is more flexible, extensible, and easier to maintain because it helps decouple the implementation details from the code that uses those implementations. By interacting with the abstract interface, code can work with different concrete implementations without needing to know their specific details.

There are two main types of polymorphism in object-oriented languages:

1.  **Subtype (or inclusion) polymorphism**: This occurs when a subclass inherits from a superclass or when a class implements an interface. In this case, objects of the subclass can be treated as objects of the superclass or the interface. This type of polymorphism is typically achieved through inheritance and method overriding.
2.  **Parametric (or generic) polymorphism**: This form of polymorphism enables the creation of generic classes or functions that can work with different data types without depending on the specific type. This is often seen in languages that support generic programming, such as C++, Java, and C#.
