---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-07-07'
date_checked: '2026-07-07'
draft: false
last_edited: '2026-07-07'
tags:
  - OMSCS
title: Week 10 - Query Execution
type: lecture
week: 10
---

In this lecture we cover how to make Query Execution generic.
We will do this by making query logic modular so we can compose them to make larger queries.
This provides the following benefits:

- Modularity: Each module encapsulates a specific manipulation.

- Isolation: With a defined interface we don't need to consider how changes to the logic of one component affects others.

- Flexibility: Enables us to choose different ways to execute the same query, meaning we can pick the best approach at run time.

- Reusability: We can use the same logic to execute different queries.

The basic unit of this framework is called an `Operator`.
Operators act on a set of tables and return a single table.
For example a 'Select' operator may take one table and filter it based on a criteria - or a join operator may take two tables and return a single table using a criteria to match tuples from each table.

# Abstract Operator class

So that all the Operators have a consistent API we define an abstract interface for them to implement:

```cpp
class Operator {
public:
  virtual ~Operator() = default;
  // Initializes the operator.
  virtual void open() = 0;
  // Progresses to the next tuple, returning true if there are more tuples to get.
  virtual bool next() = 0;
  // Gets the actual tuples.
  virtual std::vector<std::unique_ptr<Field>> getOutput() = 0;
  // Closes the operator.
  virtual void close() = 0;
};
```

> [!note] Volcano/Iterator model
> Rather than taking a `Table` directly, it takes a child `Operator*` and calls `next()` on it — this is the *Volcano/Iterator model*: operators chain together by holding a pointer to their child operator.

## Aside: Abstract base classes in C++

An abstract base class gives an interface and can implement some shared functionality between classes.
In C++ this is similar to an interface in other languages.

```cpp
class Shape {
// Protected members are accessible to derived classes.
protected:
  float x, y;
  std::string colour;
public:
  // Abstract constructor can be used by derived classes.
  Shape(float x, float y, std::string colour) : x(x), y(y), colour(colour) {}

  // Pure virtual functions must be implemented by derived classes.
  virtual void draw() const = 0;

  // Virtual functions can be used by derived classes as is or be overridden.
  virtual void move(float newX, float newY) {
    x = newX;
    y = newY;
    cout << "Moved to (" << x << ", " << y << ")" << endl;
  }
};
```

A derived class inherits the base class and can use the protected members and methods.
It can also override the virtual functions.

```cpp
class Circle : public Shape {
private:
  float radius;
public:
  Circle(float x, float y, float radius, std::string colour) : Shape(x, y, colour), radius(radius) {}

  // When derived classes override virtual functions they must use that keyword.
  void draw() const override {
    cout << "Drawing a circle at (" << x << ", " << y << ") with radius " << radius << endl;
  }
};
```

Abstract base classes can have multiple derived classes.

There are two concepts when it comes to abstract base classes:

- Inheritance: Allows the Derived class to use and extend behaviour within the Base class.

- Polymorphism: Allows the Derived class to override the Base class methods with different implementations.

> [!note] Liskov substitution principle
> A good coding practice is the Liskov substitution principle (LSP), part of the SOLID principles.
> LSP states that if something is provably true for the Base class it should still hold for all Derived classes.
> Usual violations of this come from overriding base class behaviour in a non-consistent way.

# Scan Operator

This is a simple operator that retrieves tuples that are stored on disk.
This works with the BufferManager to bring tuples into a query.

```cpp
class ScanOperator : public Operator {
private:
  size_t currentPageIndex = 0;
  std::unique_ptr<SlottedPage> currentPage;
  size_t currentSlotIndex = -1;
  std::unique_ptr<Tuple> currentTuple;
  BufferManager& bufferManager;

  void loadNextTuple() {
    bool loaded = false;
    while(!loaded && currentPageIndex < bufferManager.getNumPages()) {
      currentPage = bufferManager.getPage(currentPageIndex);
      currentSlotIndex++;
      while (!loaded && currentSlotIndex < MAX_SLOTS) {
        if (!currentPage->getSlot(currentSlotIndex).empty()) {
          currentTuple = currentPage->getTuple(currentSlotIndex);
          loaded = true;
        } else {
          currentSlotIndex++;
        }
      }
      // We need to move to the next page.
      currentPageIndex++;
      currentSlotIndex = -1;
    }
    currentPage.reset();
    currentTuple.reset();
  }

public:
  void open() override {
    currentPageIndex = 0;
    currentSlotIndex = -1;
    loadNextTuple();
  }

  bool next() override {
    if (!currentTuple)
      return false;
    loadNextTuple();
    return currentTuple != nullptr;
  }

  std::vector<std::unique_ptr<Field>> getOutput() override {
    if (!currentTuple)
      return {};
    return std::move(currentTuple->getFields());
  }

  void close() override {
    currentPage.reset();
    currentTuple.reset();
  }
};
```

# Select Operator

The select operator uses predicates to determine which tuples to use from a table.
For example:

```sql
SELECT * FROM employees WHERE salary > 10000;
```

The predicate here is `salary > 10000`.
Select queries can use multiple predicates.

## Predicates

Predicates compare two fields with an operator.

```cpp
enum class PredicateType {
  EQ, // Equal
  NE, // Not equal
  GT, // Greater than
  GE, // Greater than or equal
  LT, // Less than
  LE, // Less than or equal
};

class Predicate {
  Operand left;
  Operand right;
  PredicateType type;

public:
  enum OperandType { DIRECT, INDIRECT };
  struct Operand {
    std::unique_ptr<Field> directValue;
    size_t index;
    OperandType type;
    Operand(std::unique_ptr<Field> value) : directValue(std::move(value)), type(OperandType::DIRECT) {}
    Operand(size_t index) : index(index), type(OperandType::INDIRECT) {}
  };

  bool checkPredicate(const std::vector<std::unique_ptr<Field>>& tupleFields) const {
    const Field *leftField = (left.type == OperandType::DIRECT) ? left.directValue.get() : tupleFields[left.index].get();
    const Field *rightField = (right.type == OperandType::DIRECT) ? right.directValue.get() : tupleFields[right.index].get();
    return compareBasedOnType(leftField, rightField);
  }

  bool compareBasedOnType(const Field *leftField, const Field *rightField) const {
    switch (leftField->getType()) {
    case FieldType::INT: {
      int leftVal = static_cast<const IntField *>(leftField)->getValue();
      int rightVal = static_cast<const IntField *>(rightField)->getValue();
      return compare(leftVal, rightVal);
    }
    // Implement type specific comparisons.
    }
  }

  template <typename T> bool compare(const T &left_val, const T &right_val) const {
    switch (type) {
    case PredicateType::EQ: return left_val == right_val;
    case PredicateType::NE: return left_val != right_val;
    case PredicateType::GT: return left_val > right_val;
    case PredicateType::GE: return left_val >= right_val;
    case PredicateType::LT: return left_val < right_val;
    case PredicateType::LE: return left_val <= right_val;
    default: throw std::runtime_error("Unknown predicate type");
    }
  }
};
```

Here the predicate compares two operands that can either be direct, such as a value like 10000, or indirect, such as a tuple's field value like `salary`.

## Select Logic

The select class now uses the predicates to filter rows from the child operator.

```cpp
class SelectOperator : public Operator {
private:
  Operator* input; // child operator (e.g. ScanOperator)
  std::vector<Predicate> predicates;
  std::vector<std::unique_ptr<Field>> currentOutput;

  bool checkAllPredicates(const std::vector<std::unique_ptr<Field>>& fields) {
    for (const auto& pred : predicates)
      if (!pred.checkPredicate(fields)) return false;
    return true;
  }

public:
  SelectOperator(Operator* input, std::vector<Predicate> predicates)
    : input(input), predicates(std::move(predicates)) {}

  void open() override {
    input->open();
  }

  // Advances through the child operator until a tuple passes all predicates.
  bool next() override {
    while (input->next()) {
      auto fields = input->getOutput();
      if (checkAllPredicates(fields)) {
        currentOutput = std::move(fields);
        return true;
      }
    }
    return false;
  }

  std::vector<std::unique_ptr<Field>> getOutput() override {
    return std::move(currentOutput);
  }

  void close() override {
    input->close();
  }
};
```

Usage composes operators by passing child operators as constructor arguments:

```cpp
ScanOperator scan(bufferManager);
SelectOperator select(&scan, {Predicate(salaryIndex, 10000, PredicateType::GT)});

select.open();
while (select.next()) {
  auto row = select.getOutput();
  // process row...
}
select.close();
```
