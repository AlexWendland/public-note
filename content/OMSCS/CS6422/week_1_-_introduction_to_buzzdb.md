---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-05-26'
date_checked: '2026-05-26'
draft: false
last_edited: '2026-05-26'
tags:
  - OMSCS
title: Week 1 - Introduction to BuzzDB
type: lecture
week: 1
---

In this course we will be using C++ to build a relational database called BuzzDB.
In this lecture we cover what BuzzDB is, and why we use C++.

> [!note] Simplified introduction
> The BuzzDB shown here is a simplified, introductory version to illustrate the core concepts.
> Over the course we will evolve it into a more complete database with generic tuple types, schemas, and proper disk-based storage.

# BuzzDB

In BuzzDB, the most basic data class is called the `Tuple`.

```cpp
class Tuple {
public:
  int key; // Identifier column
  int value; // Data associated with key
};
```

A `Tuple` here represents a full row in the table — it has exactly two integer columns: `key` (a grouping identifier, not necessarily unique) and `value` (the data for that row).
This gives us a simple two-column integer table, e.g:

| key | value |
|-----|-------|
| 1   | 10    |
| 1   | 20    |
| 2   | 50    |

> [!note] Simplified tuple
> In a real database a tuple would represent a row with arbitrarily many columns of mixed types.
> This would typically be implemented as a raw byte array with a separate `Schema` describing each column's type and offset — something C++'s low-level memory control makes practical.
> This simplified integer key-value form is used here to introduce the core concepts without the added complexity of a type system.

In comparison the heart of the BuzzDB is the class by that name.

```cpp
class BuzzDB {
public:
  // Stores all our tuples
  std::vector<Tuple> table;

private:
  // Index mapping each key to all values associated with it (supports multiple rows per key)
  std::map<int, std::vector<int>> index;
};
```

This has some key functions.

```cpp
void BuzzDB::insert(int key, int value) {
  Tuple newTuple = {key, value};
  table.push_back(newTuple);
  index[key].push_back(value);
}
```

The `insert` function appends the new `Tuple` to the table and also updates the index, grouping all values by their key.
This index is then used to efficiently implement operations like `selectGroupBySum` below, without scanning the full table.

```cpp
void BuzzDB::selectGroupBySum() {
  // Iterate over each key
  for (auto const &pair: index) {
    int sum = 0;
    for (auto const &value: pair.second) {
      sum += value;
    }
    std::cout << "key:" << pair.first << ", sum: " << sum << "\n";
  }
}
```

# Why C++?

In this course we will be using C++ to build BuzzDB.
C++ has the following advantages:

- It is a compiled language, making it fast.

- It has low-level control over system resources (memory, I/O, CPU).

- It has complex memory management allowing for optimisations on the disk/memory interactions.

- It has multi-threading support allowing for concurrency of operations.

