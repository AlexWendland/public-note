---
aliases:
  - coupling
  - coupled
chatgpt: false
created: 2023-08-05
last_edited: 2023-08-05
publish: true
tags: programming
type: meta
---
# Coupling

Two bits of code are 'Coupled' if they rely on one another. In other words if one changes then you are required to change the other bit of code. When we write programs we really want low coupling as these are easier to change and maintain.

There are lots of methods to decrease coupling, such as introducing [[Interface|interfaces]] and [[The Law of Demeter]].

Decreasing coupling also makes it easier to [[Testing conventions|test]] your applications as you need to mock/patch out less of your code.

This is a **key concept** in good system design.
