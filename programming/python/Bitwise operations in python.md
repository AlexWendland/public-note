---
aliases: [bitwise operation in python]
type: operations
publish: true
created: 2023-04-20
last_edited: 2023-04-20
tags: programming, python, language
chatgpt: false
---
# Bitwise operations

Bitwise operations can apply to the [[Binary|binary]] data type but also [[Integer|integers]].

 > [!Note] Representation of integers in [[Python]]
 > In [[Python|python]] integers are [[Signed or unsigned integers|unsigned]] and stored using [[Two's complement]].
 
The operations in python are as follows (applied to x = 11 or `0000 1011` and y = 6 or `0000 0110`)

| Operation | Meaning             | Example                 |
| --------- | ------------------- | ----------------------- |
| &         | Bitwise AND         | x & y = 4 `0000 0010`   |
| \|        | Bitwise OR          | x \| y = 15 `0000 1111` |
| \~        | Bitwise NOT         | ~ x = -12 `1111 0100`   |
| \^        | Bitwise XOR         | x \^ y = 13 `0000 1101` |
| >>        | Bitwise right shift | x >> 2 = 2 `0000 0010`  |
| <<        | Bitwise left shift  | x << 2 = 44 `0010 1100` | 
