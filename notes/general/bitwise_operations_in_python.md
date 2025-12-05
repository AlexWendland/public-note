---
aliases:
  - bitwise operation in python
checked: false
created: 2023-04-20
draft: false
last_edited: 2025-12-05
tags:
  - programming
  - python
  - language
title: Bitwise operations in python
type: operations
---
# Bitwise operations

Bitwise operations can apply to the [binary](binary.md) data type but also [integers](integer.md).

 > [!note] Representation of integers in [Python Index](python_index.md)
 > In [python](python_index.md) integers are [unsigned](signed_or_unsigned_integers.md) and stored using [Two's complement](two's_complement.md).

The operations in python are as follows (applied to x = 11 or `0000 1011` and y = 6 or `0000 0110`)

| Operation | Meaning             | Example                 |
| --------- | ------------------- | ----------------------- |
| &         | Bitwise AND         | x & y = 4 `0000 0010`   |
| \|        | Bitwise OR          | x \| y = 15 `0000 1111` |
| \~        | Bitwise NOT         | ~ x = -12 `1111 0100`   |
| \^        | Bitwise XOR         | x \^ y = 13 `0000 1101` |
| >>        | Bitwise right shift | x >> 2 = 2 `0000 0010`  |
| <<        | Bitwise left shift  | x << 2 = 44 `0010 1100` |
