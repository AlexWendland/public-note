---
aliases: [SRP, single responsibility principle]
type: theory
publish: true
created: 2023-03-18
last_edited: 2023-03-18
tags: programming
---
# Single Responsibility Principle (SRP)

This principle tells us:

>[!quote] [[Robert C. Martin]]
>"A module should be responsible to one, and only one, actor."

In other words, there should only ever be one reason to change a module. 

## Example

An example from the [wikipedia article](https://en.wikipedia.org/wiki/Single-responsibility_principle) about this is. If you have some code that compiles and then produces a report there might be two reasons you want to change the code.
1. You want to change the content of the report.
2. You want to change the format of the report.
These should be separate modules. 

A hidden point in this example is that you will have to define an interface to work between these two that standardises how this information will be passed from one to another.