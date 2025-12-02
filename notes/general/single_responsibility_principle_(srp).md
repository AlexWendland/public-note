---
aliases:
  - SRP
  - single responsibility principle
checked: false
created: 2023-03-18
draft: false
last_edited: 2023-11-11
title: Single Responsibility Principle (SRP)
tags:
  - programming
type: theory
---
# Single Responsibility Principle (SRP)

This is one of the [SOLID principles](solid_principles.md) and it states:

>[!quote] [Robert C. Martin](robert_c._martin.md)
>"A module should be responsible to one, and only one, actor."

In simpler terms, a module should have only one reason to change.

## Example

Let's consider an example from the [Wikipedia article](https://en.wikipedia.org/wiki/Single-responsibility_principle) on SRP. Suppose you have some code that compiles and then produces a report. There might be two reasons for wanting to change the code:

1.  To modify the content of the report.
2.  To alter the format of the report.

According to SRP, these two functionalities should be implemented in separate modules.

An important takeaway from this example is that you'll need to define an interface between the two modules. This interface standardizes how information is passed from one module to another, ensuring proper separation of concerns.
