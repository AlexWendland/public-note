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
title: Week 11 - Operator Framework
type: lecture
week: 11
---

In this lecture, we extend the Query framework.

# Logical Predicates

In the previous lecture we saw support for simple predicates such as comparisons.
However, this did not support logical operations like AND and OR.
Here we extend the Predicates to do exactly that.
First we implement a predicate interface.

```cpp
class IPredicate {
public:
  virtual ~IPredicate() {}
  virtual bool check(const std::vector<std::unique_ptr<Field>> &tupleFields) const = 0;
};
```

Our previous `Predicate` class implements this interface with the only important interface being the `check` method.
Though we extend this further with the `ComplexPredicate` class that supports logical operators.

```cpp
enum class LogicalOperator{
  AND,
  OR
};

class ComplexPredicate : public IPredicate {
  std::vector<std::unique_ptr<IPredicate>> predicates;
  LogicalOperator logical_operator;

  virtual bool check(const std::vector<std::unique_ptr<Field>> &tupleFields) const override {
    if (logical_operator == LogicalOperator::AND) {
      for (const auto &pred : predicates) {
        if (!pred->check(tupleFields)) {
           return false;
        }
      }
      return true;
    } else if (logical_operator == LogicalOperator::OR) {
      for (const auto &pred : predicates) {
        if (pred->check(tupleFields)) {
          return true;
        }
      }
      return false;
    }
    return false;
  }
};
```

This method allows us to chain predicates together to make arbitrarily complex predicates.
We can extend it further to support more complex operations by adding more `LogicalOperators`.

# Hash Aggregation Operation

It is common to want to group data by field values.
For example, the below groups on the Category_ID and sums the profit column.

```sql
SELECT Category_ID,
  SUM(Profit) AS Total_Profit
FROM Sales_Data
GROUP BY Category_ID;
```

To do this we need to go through the data and group it whilst performing the proper aggregation.

```cpp
class HashAggregationOperator : public Operator {
private:
  // The field positions to group by.
  std::vector<size_t> group_by_attrs;

  // The aggregation functions to perform.
  std::vector<AggrFunc> aggr_funcs;

  // The output tuples.
  std::vector<Tuple> output_tuples;
  size_t current_tuple_index = 0;

  // The child operator.
  Operator* input;

  // Custom hash function for a std::vector<Field>.
  struct FieldVectorHasher {
    std::size_t operator()(const std::vector<Field> &fields) const {
      std::size_t hash = 0;
      for (const auto &field : fields) {
        std::hash<std::string> hasher;
        std::size_t fieldHash = 0;
        fieldHash = hasher(...);
        hash ^= fieldHash + 0x9e3779b9 + (hash << 6) + (hash >> 2);
      }
      return hash;
    }
  };

public:
  void open() override {
    input->open();

    // Hash tuples by group-by key and aggregate.
    std::unordered_map<std::vector<Field>, std::vector<Field>, FieldVectorHasher> hash_table;
    while (input->next()) {
      auto fields = input->getOutput();

      // Extract only the group-by fields to form the hash key.
      std::vector<Field> key;
      for (size_t idx : group_by_attrs) {
        key.push_back(*fields[idx]);
      }

      // On first sight of a key, initialize accumulators for each aggr function.
      if (hash_table.find(key) == hash_table.end()) {
        std::vector<Field> accumulators;
        for (const auto &func : aggr_funcs) {
          accumulators.push_back(func.initialize());
        }
        hash_table[key] = std::move(accumulators);
      }

      // Update each accumulator with the current tuple's relevant field.
      auto &accumulators = hash_table[key];
      for (size_t i = 0; i < aggr_funcs.size(); i++) {
        aggr_funcs[i].update(accumulators[i], *fields[aggr_funcs[i].field_index]);
      }
    }

    // Flatten the hash table into output tuples (key fields + aggregate fields).
    for (auto &[key, aggregates] : hash_table) {
      std::vector<std::unique_ptr<Field>> tuple_fields;
      for (const auto &field : key) {
        tuple_fields.push_back(field.clone());
      }
      for (const auto &agg : aggregates) {
        tuple_fields.push_back(agg.clone());
      }
      output_tuples.emplace_back(std::move(tuple_fields));
    }

    input->close();
  }

  bool next() override {
    if (current_tuple_index >= output_tuples.size()) {
      return false;
    }
    return true;
  }

  virtual std::vector<std::unique_ptr<Field>> getOutput(){
    return std::move(output_tuples[current_tuple_index++].getFields());
  }

  virtual void close() {
    // Clean up.
  }
};
```

The design above allows for multiple aggregation functions to be applied to the same group-by key through multiple `AggrFunc`s.
We also support grouping by multiple columns using the `group_by_attrs` vector, where each unique combination of column values forms a distinct key.

# Complex operations

So far we have been defining individual operators.
To make more complex operations we need to compose them together.
This follows a pipeline pattern where we pipe the output of the previous operator into the next operator.
This follows the design of the Unix operating system which was designed in AT&T Bell Labs at the same time as relational databases were being designed in IBM in the 1970s.
Both these systems used the idea of a tool doing a single thing well.
They also both share the idea of a standardised input/output model.
In Unix this was a file object.
Whereas in a relational database this was a table.
This will be expanded upon more in the next lecture.

# Create Index Executor

There are two sub-languages within SQL:

| Data Definition Language (DDL) | Data Manipulation Language (DML) |
| ------------------------------ | -------------------------------- |
| Used to define or modify database design | Used to manipulate data in the database |
| Create Table, Create Index, ... | Select, Insert, ... |
| Drop Table, Drop Index, ... | Update, Delete, ... |

The DDL language operates on tables, indexes and views—enabling us to create, alter and drop them.

We will focus on the create index operator.
To do this, we specify which columns to index.
This then implements the `Operator` interface where it doesn't return any output.

```cpp
class CreateIndexOperator : public Operator {
private:
  // The table to create the index on.
  Operator* input;

  // The columns to create the index on.
  std::vector<size_t> column_indices;

  // The index to create.
  Index index;
public:
  void open() override {
    // This runs the whole query.
    input->open();
    while (input->next()) {
      const auto &tuple = input->getOutput();
      // Implement a hasher for the tuple fields.
      int key = hash(tuple, column_indices);
      index.insertOrUpdate(key, tuple);
    }
  }

  bool next() override {
    return false;
  }

  std::vector<std::unique_ptr<Field>> getOutput() override {
    return {};
  }

  void close() override {
    // Clean up.
  }
};
```

Above is a simplified version using a hash-based index.
However, we can implement more complicated versions that support R-trees for example.
