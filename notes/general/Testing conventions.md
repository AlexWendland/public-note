---
aliases:
  - test
  - testing
  - testing conventions
  - test conventions
checked: false
created: 2023-06-29
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - clean-code
type: conventions
---
# Testing conventions

Tests are what makes your code safe to change. They are validate the assumptions that other bits of your code make. Without them you can not change your code without fearing the consequences. Though for this we pay a price with time, time to write them, time to run them and time to maintain them. This is a problem similar to the rest of your code but with different emphasis - tests do not need to be hyper efficient, however they will need to clearly state the assumption that has been broken.

## Writing tests

I am a proponent of [[Test Driven Development (TDD)|test driven development]], where you implement a very simple loop.

Write a minimal test that fails > write some production code > check test passes

Though you can read more about this in the [[Test Driven Development (TDD)]] note.
