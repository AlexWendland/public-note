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
title: Week 12 - Query Compilation
type: lecture
week: 12
---

In this lecture we go from a text based query to something we can run.

# Query parsing

In real databases we will use a parser to convert a text query into an AST.
This then can be turned into a pipeline of operators based on the input.

However, for buzzdb we use a simpler approach using regex and a struct to carry query components.

> [!warning] Regex is not a real query parser
> Real databases use proper parsers (recursive descent, LALR, etc.) often defined with tools like yacc/bison or ANTLR.
> Regex cannot handle nested expressions, operator precedence, or subqueries — this is purely a teaching simplification.

```cpp
struct QueryComponents {
  std::vector<int> selectAttributes; // Indices of attributes selected in the query
  bool sumOperation = false; // Indicates whether a SUM operation is included.
  int sumAttributeIndex = -1; // Targets the attribute for the SUM operation.
  bool groupBy = false; // Specifies if there's a GROUP BY clause.
  int groupByAttribute = -1; // Determines which attribute to group by.
  bool whereCondition = false; // Checks for the presence of a WHERE clause with bounds.
  int whereAttributeIndex = -1; // Determines which attribute to check.
  int lowerBound = -1; // Lower bound for the WHERE clause.
  int upperBound = -1; // Upper bound for the WHERE clause.
};
```

The information for the above struct can be extracted using 4 regular expressions.

- Select parsing

- SUM detection

- GROUP BY parsing

- WHERE parsing

After parsing the query we can use the fields to build a chain of operators to enact it.
To output the result to the user we just use the next value of the root operator which in turn calls next on the child operators.

# Query Compilation

There are two main methods for query execution.

- Query interpretation: This involves query parsing, followed by query plan generation and finally query plan execution.

- Query compilation: This involves query parsing, generating a hard-coded C function and making machine code that can directly run on the CPU.

The query compilation will use the buffer manager and treat each page as a binary string - not reinterpreting the slots as tuples.

The query interpretation is very flexible however contains a lot of overhead from temporary objects, implementing the operator framework, and tuple deserialization.
When operating on a large amount of data this can generate very slow queries.
On the other hand for large queries compilation is much faster whilst running the query however it has the fixed overhead of compiling the query that can take longer than the execution if the query is small in nature.

> [!note] JIT compilation in real systems
> Real systems such as HyPer and DuckDB use LLVM to JIT-compile query plans directly to native machine code at runtime.
> This avoids the full AOT compilation overhead while still eliminating the interpreter overhead of the Volcano model.

