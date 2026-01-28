---
aliases:
  - bitwise operation in python
created: 2023-04-20
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
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
> In [Python](python_index.md) integers are [signed](signed_or_unsigned_integers.md) and stored using [Two's complement](two's_complement.md).

The operations in Python are as follows (applied to x = 11 or `0000 1011` and y = 6 or `0000 0110`)

| Operation | Meaning             | Example                 |
| --------- | ------------------- | ----------------------- |
| &         | Bitwise AND         | x & y = 2 `0000 0010`   |
| \|        | Bitwise OR          | x \| y = 15 `0000 1111` |
| \~        | Bitwise NOT         | ~ x = -12 `1111 0100`   |
| \^        | Bitwise XOR         | x \^ y = 13 `0000 1101` |
| >>        | Bitwise right shift | x >> 2 = 2 `0000 0010`  |
| <<        | Bitwise left shift  | x << 2 = 44 `0010 1100` |
