---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-07-14'
date_checked: '2026-07-14'
draft: false
last_edited: '2026-07-14'
tags:
  - OMSCS
title: Week 13 - Query Optimisation
type: lecture
week: 13
---

In this lecture we look at three optimisations for queries: row vs column storage, compression, and vectorised execution.

# Row vs Column Storage

In our current implementation we store tuples in pages.
This means that each row of data is stored together.
Whilst this is conceptually simple this means that we have to store mixed data types together on the same page.
This has a number of implications:

- Redundant I/O: If our query only requests data from a couple of columns, we still end up parsing all the others as they are stored within rows.

- Bad compression: If a row contains a mix of data types it is harder to meaningfully compress the data on the disk.

Instead we can store all column values together in a single page.
Then taking a selection of values from the same column involves reading less pages of data and enables compression for similar data types.

Whether to use row or column storage depends on your use case.

| Feature | Row Storage | Column storage |
| ------- | ----------- | -------------- |
| Data organisation | All attributes together | Each attribute on a different page |
| Ideal use case | Transactional workloads (OLTP) | Analytical workloads (OLAP) |
| Access pattern | Efficient for full rows | Efficient for specific columns |
| Compression | Limited | Great |

## Compression

In this lecture we will cover 4 techniques for compression:

| Method | Ideal use case |
| ------ | -------------- |
| Delta encoding | Numeric data which incrementally changes |
| Bit packing | Numerical data with small range |
| Huffman encoding | Categorical data with frequent values |
| Byte Dictionary encoding | Categorical data with few values |

Note that compression is not only useful for reducing the storage footprint but due to the save on I/O performance it increases query speed as well.

### Delta encoding

Delta encoding stores the first value and then stores subsequent values as differences between the previous value and the current value.
For example: 1000, 1001, 1004, 1005, 1008 would be saved as 1000, 1, 3, 1, 3.

### Bit packing

Normally integers are stored in 32 or 64 bits.
However, if you are storing an age column whose max value is 120 - this only requires 7 bits.
Therefore we can pack each value into 7 bits and add custom packing/unpacking of the data.
This can meaningfully compress data if the values are integers in small ranges.

### Huffman encoding

The idea behind Huffman encoding is to give frequently used values shorter codes and infrequently used values longer codes.
The tree is built bottom-up using a min-heap:

1. Count the frequency of every distinct value in the column.
2. Insert each value as a leaf node into a min-heap keyed by frequency.
3. Pop the two lowest-frequency nodes, merge them into a parent node whose frequency is their sum, and push the parent back.
4. Repeat until one node remains — that is the root.
5. Traverse the tree assigning `0` to left edges and `1` to right edges. The path from root to a leaf is that value's code.

For example, given a status column with frequencies `[A=50, B=30, C=15, D=5]`:

```
         root:100
        /        \
      A:50       DCB:50
      (0)          (1)
                 /     \
               B:30    DC:20
               (10)    (11)
                      /    \
                    C:15   D:5
                    (110)  (111)
```

This gives codes `A=0`, `B=10`, `C=110`, `D=111` — the most frequent value uses only 1 bit.

The result is a *prefix-free* code: no code is a prefix of another, so values can be concatenated into a bitstream and decoded unambiguously by walking the tree bit by bit.
Huffman encoding is provably optimal for this type of symbol-by-symbol coding (Shannon's source coding theorem).

> [!warning] Huffman codes are variable length
> Because codes are variable length you cannot jump directly to the Nth value — you must decode from the start of the bitstream to find it.
> This makes random access and filtered scans more expensive compared to fixed-length encodings.

### Byte Dictionary encoding

For categorical data with few distinct values (up to 256), we assign a byte code to each value and store the dictionary alongside the data.
Because codes are fixed length we can jump directly to the Nth value and read it in constant time.
Additionally, predicates like `WHERE category = 'Electronics'` can be converted into a fast byte comparison without decompressing the column.

Compared to Huffman, dictionary encoding is preferable when the value distribution is roughly uniform — in that case Huffman codes are ~8 bits each anyway, so there is no size benefit and you pay for the complexity.
Fixed-width codes also vectorise well with SIMD instructions, making bulk scans faster.

# Vectorised Execution

To utilise modern CPUs we can vectorise our queries using the Single Instruction, Multiple Data (SIMD) model, which executes a single instruction on multiple values simultaneously.
This reduces the number of function calls and allows for better CPU pipelining.

The core SIMD instructions are:

- Vector load: Loads multiple values from memory into a vector register.

- Filter masks: Creates a mask of values to be loaded into the vector register.

- Horizontal reduction: Reduces the values in the vector register to a single value.

DB queries have multiple good use cases for these, such as filtering, aggregations, and compression.
The number of values processed per instruction depends on the register width and value size — SSE2 handles 4 × 32-bit integers, while AVX-512 handles 16 × 32-bit integers.
This aligns well with columnar storage as we now have column values stored in contiguous memory.

