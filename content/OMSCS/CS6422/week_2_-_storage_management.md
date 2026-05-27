---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-05-26'
date_checked: '2026-05-27'
draft: true
last_edited: '2026-05-26'
tags:
  - OMSCS
title: Week 2 - Storage Management
type: lecture
week: 2
---

In database applications we use primarily two types of storage:

- DRAM (dynamic random access memory): To speed up queries and access.

- Disk: For permanent storage.

The interplay between these plays an important role in making a database both fast and reliable.

# Expanding Tuple

In the previous lecture we defined a tuple to have two integer values key and value.
However, in a proper database we want to support a dynamic table schema that is specified by the user.
Therefore, we add a polymorphic container for values of our rows called Field.
This uses an enum to specify its type and `unique_ptr` to support the value.

```cpp
enum FieldType { INT, FLOAT, STRING };

class Field {
  FieldType type;

  std::unique_ptr<char[]> data_s;
  size_t data_s_len;

public:
  Field(int i) : type(INT) { 
    data_length = sizeof(int);
    data = std::make_unique<char[]>(data_length);
    std::memcpy(data.get(), &i, data_length);
  }

  Field(float f) : type(FLOAT) { 
    data_length = sizeof(float);
    data = std::make_unique<char[]>(data_length);
    std::memcpy(data.get(), &f, data_length);
  }

  Field(const std::string& s) : type(STRING) {
    data_length = s.size() + 1;  // include null-terminator
    data = std::make_unique<char[]>(data_length);
    std::memcpy(data.get(), s.c_str(), data_length);
  }

  // Copy assignment
  Field& operator=(const Field& other) {
    if (&other == this) {
      return *this;
    }
    type = other.type;
    data_length = other.data_length;
    data = std::make_unique<char[]>(data_length);
    std::memcpy(data.get(), other.data.get(), data_length);
    return *this;
  }

  // Copy constructor
  Field(const Field& other) {
    type = other.type;
    data_length = other.data_length;
    data = std::make_unique<char[]>(data_length);
    std::memcpy(data.get(), other.data.get(), data_length);
  }

  FieldType getType() const { return type; }

  int asInt() const { 
    return *reinterpret_cast<int*>(data.get());
  }

  float asFloat() const { 
    return *reinterpret_cast<float*>(data.get());
  }

  std::string asString() const { 
    return std::string(data.get());
  }

  void print() const {
    switch (type) {
      case INT: std::cout << asInt() << std::endl; break;
      case FLOAT: std::cout << asFloat() << std::endl; break;
      case STRING: std::cout << asString() << std::endl; break;
    }
  }
};
```

Here we add a copy constructor so we can copy a Field into the Tuple's field vector, and a copy assignment operator to reassign fields in-place.

```cpp
class Tuple {
  std::vector<Field> fields;

public:

  void addField(std::unique_ptr<Field> field) {
    fields.push_back(std::move(field));
  }
};
```

Note here we are using the `unique_ptr` class to avoid issues with raw pointers such as:

- Memory leaks: If a pointer's memory is not cleared it will cause a leak.
Smart pointers clear up the memory allocation when going out of scope.

- Dangling pointers: If a pointer is freed but the pointer variable is not nulled out, it points to some arbitrary bit of memory which can cause issues if used later.
After a `unique_ptr` releases its resource (via `reset()` or `std::move`), it holds `nullptr`, preventing use-after-free.

- Double free: If a pointer is freed twice this causes an error.
Because a `unique_ptr` holds `nullptr` after releasing its resource, a second `reset()` is a safe no-op.

- Ownership: If a pointer is passed to another function, the ownership of the pointer is not clear.
Smart pointers use the `move` function to transfer ownership.

# Serialization and Deserialization

Right now we have stored the Tuples and Fields in memory - however as the database grows we need this to be written to disk.
Therefore, we need to serialize the Tuples and Fields to disk.
We can choose an efficient format later but now we keep it in a simple format.

```cpp
class Field {
  ...
  void serialize(std::ofstream& out) {
    out << type << ' ' << data_length << ' ';
    if (type == STRING) {
      out << data.get() << ' ';
    } else if (type == INT) {
      out << *reinterpret_cast<int*>(data.get()) << ' ';
    } else if (type == FLOAT) {
      out << *reinterpret_cast<float*>(data.get()) << ' ';
    }
  }

  static std::unique_ptr<Field> deserialize(std::ifstream& in) {
    int type; in >> type;
    size_t length; in >> length;
    if (type == STRING) {
      std::string val; in >> val;
      return std::make_unique<Field>(val);
    } else if (type == INT) {
      int val; in >> val;
      return std::make_unique<Field>(val);
    } else if (type == FLOAT) {
      float val; in >> val;
      return std::make_unique<Field>(val);
    }
    return nullptr;
  }
};

class Tuple {
  ...

  // Used to estimate the in-memory size. Note: this sums raw data_length values
  // and does not account for serialization overhead (type tags, length prefixes),
  // so it underestimates the true on-disk size.
  size_t getSize() const {
    size_t size = 0;
    for (const auto& field : fields) {
      size += field->data_length;
    }
    return size;
  }

  void serialize(std::ofstream& out) {
    out << fields.size() << ' ';
    for (auto& field : fields) {
      field->serialize(out);
    }
  }

  static std::unique_ptr<Tuple> deserialize(std::ifstream& in) {
    auto tuple = std::make_unique<Tuple>();
    size_t fieldCount; in >> fieldCount;
    for (size_t i = 0; i < fieldCount; ++i) {
        tuple->addField(Field::deserialize(in));
    }
    return tuple;
  }
}
```

Here note that we use a non-static member function for serialize but a static member function for deserialize.
This ensures we do not need to make an object simply to call the deserialize method - instead we can call it from the class.

# Paging

Similarly to an OS it is easier to keep Tuples in pages to easily page in and out whole selections of Tuples instead of needing to manage them at the Tuple level.
To do this we simply add containers for Tuples called Pages with a max page size in bytes. Pages are the unit moved between disk and DRAM — loading or evicting a whole page at once rather than individual tuples.

```cpp
const int PAGE_SIZE = 4096;

// Page class
class Page {
  size_t used_size = 0;
  std::vector<std::unique_ptr<Tuple>> tuples;

public:
  // Add a tuple, returns true if it fits, false otherwise.
  bool addTuple(std::unique_ptr<Tuple> tuple) {
    size_t tuple_size = tuple->getSize();

    if (used_size + tuple_size > PAGE_SIZE) {
      // If not enough space, run garbage collection and compaction first
      //garbageCollect();
    }

    // If there is still not enough space, reject the operation
    if (used_size + tuple_size > PAGE_SIZE) {
      std::cout << "Page is full. Cannot add more tuples. ";
      std::cout << "Page contains: " << tuples.size() << " tuples. \n";
      return false;
    }

    tuples.push_back(std::move(tuple));
    used_size += tuple_size;
    return true;
  }

  // Write this page to a file.
  void write(const std::string& filename) const {
    std::ofstream out(filename);
    // First write the number of tuples.
    out << tuples.size() << '\n';
    // Then write each tuple.
    for (auto& tuple : tuples) {
      tuple->serialize(out);
      out << '\n';
    }
    out.close();
  }

  // Read this page from a file.
  static std::unique_ptr<Page> deserialize(const std::string& filename) {
    std::ifstream in(filename);
    auto page = std::make_unique<Page>();

    // First read the number of tuples.
    size_t tupleCount; in >> tupleCount;
    std::cout << "Num Tuples: " << tupleCount << "\n";
    // Then read each tuple.
    for (size_t i = 0; i < tupleCount; ++i) {
      auto loadedTuple = Tuple::deserialize(in);
      std::cout << "Tuple " << (i+1) << " :: ";
      loadedTuple->print();
      page->addTuple(std::move(loadedTuple));
    }
    in.close();
    return page;
  }
};
```

# Data consistency

As we start to manipulate pages more within the database - for example with a delete Tuple function.

```cpp
void Page::deleteTuple(size_t index) {
  if (index >= tuples.size()) {
    std::cout << "Tuple index out of range. ";
    return;
  }

  used_size -= tuples[index]->getSize();
  tuples.erase(tuples.begin() + index);
}
```

We will start to see difference appear between the in-memory version of our database and the on-disk version.
Therefore it is critical that we write to disk changes that appear in the in-memory version.
Initially we can only do this via the serialisation command - but later on we will introduce the WAL.
