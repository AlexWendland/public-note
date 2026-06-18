---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-05-27'
date_checked: '2026-05-27'
draft: false
last_edited: '2026-05-27'
tags:
  - OMSCS
title: Week 3 - Slotted Pages
type: lecture
week: 3
---

In the previous lecture we introduced the Page for Tuples.
In this lecture we develop the ideas to abstract away the management of data in memory vs on disk.

# Slotted Page

Previously we used a Page to collect Tuples into a single object.
However, we lazily placed these into a vector to store them within the page.
Each time we delete a Tuple from this Page, the page has to reshuffle all the data in the vector to remove the gap.
Also, this means the index into the vector is not a stable identifier for any Tuple, thus making it hard to form indexes on top of it.
Therefore, we introduce the concept of a Slotted page.

Think of a Slotted page as a block of memory with some metadata at the start to identify where data is stored.
Each 'slot' is metadata (an offset and length) pointing to where a Tuple's bytes live in the data region of the page, and the data region entries can be dynamically sized based on need.
Deleting a slot then involves marking it as empty.
This has the following advantages:

- Indexing into the pages slots is a stable identifier.

- Using pointers we can have a zero-copy page loading.
This comes from using raw bytes in the pages data.

- We can do inplace updates to the data without needing to rewrite the whole page.

However, this comes with a downside which is internal fragmentation that can form from gaps appearing between slots.
Therefore this is something we will need to manage going forward.

First, let's introduce the slot.

```cpp
static constexpr size_t PAGE_SIZE = 1024;  // Fixed page size
static constexpr size_t MAX_SLOTS = 100;   // Fixed number of slots
static constexpr uint16_t INVALID_VALUE = std::numeric_limits<uint16_t>::max(); // Sentinel value (should be max)

struct Slot {
  bool empty = true;                 // Is the slot empty?
  uint16_t offset = INVALID_VALUE;    // Offset of the slot within the page
  uint16_t length = INVALID_VALUE;    // Length of the slot
};
```

Then the structure of a slotted page is as follows:

- A fixed sized metadata section to hold the slots.

- A fixed sized page of data that can have data written to it in whichever order as long as the slots track active records.

```cpp
class SlottedPage {
public:
  std::unique_ptr<char[]> page_data = std::make_unique<char[]>(PAGE_SIZE);
  size_t metadata_size = sizeof(Slot) * MAX_SLOTS;

  SlottedPage(){
    // Empty page -> initialize slot array inside page
    Slot* slot_array = reinterpret_cast<Slot*>(page_data.get());
    for (size_t slot_itr = 0; slot_itr < MAX_SLOTS; slot_itr++) {
      slot_array[slot_itr].empty = true;
      slot_array[slot_itr].offset = INVALID_VALUE;
      slot_array[slot_itr].length = INVALID_VALUE;
    }
  }

  // Add a tuple, returns true if it fits, false otherwise.
  bool addTuple(std::unique_ptr<Tuple> tuple) {

    // Serialize the tuple into a char array
    auto serializedTuple = tuple->serialize();
    size_t tuple_size = serializedTuple.size();

    std::cout << "Tuple size: " << tuple_size << " bytes\n";

    // Check for first slot with enough space.
    // Fresh slots have length = INVALID_VALUE (uint16_t max), which is larger than any
    // real tuple, so they always pass the size check. Deleted slots retain their old
    // length, enabling reuse if the new tuple fits within the previously allocated space.
    size_t slot_itr = 0;
    Slot* slot_array = reinterpret_cast<Slot*>(page_data.get());
    for (; slot_itr < MAX_SLOTS; slot_itr++) {
      if (slot_array[slot_itr].empty == true and
        slot_array[slot_itr].length >= tuple_size) {
        break;
      }
    }
    if (slot_itr == MAX_SLOTS) {
      std::cout << "Page does not contain an empty slot with sufficient space to store the tuple.";
      return false;
    }

    // Identify the offset where the tuple will be placed in the page
    // Update slot meta-data if needed
    size_t offset = slot_array[slot_itr].offset;
    if (offset == INVALID_VALUE) {
      if (slot_itr != 0) {
        auto prev_slot_offset = slot_array[slot_itr - 1].offset;
        auto prev_slot_length = slot_array[slot_itr - 1].length;
        offset = prev_slot_offset + prev_slot_length;
      } else {
        offset = metadata_size;
      }
    }

    if (offset + tuple_size >= PAGE_SIZE) {
      slot_array[slot_itr].empty = true;
      slot_array[slot_itr].offset = INVALID_VALUE;
      return false;
    } else {
      slot_array[slot_itr].empty = false;
      slot_array[slot_itr].offset = offset;
    }

    assert(offset != INVALID_VALUE);
    assert(offset >= metadata_size);

    if (slot_array[slot_itr].length == INVALID_VALUE) {
      slot_array[slot_itr].length = tuple_size;
    }

    // Copy serialized data into the page
    std::memcpy(page_data.get() + offset,
                serializedTuple.c_str(),
                tuple_size);

    return true;
  }

  void deleteTuple(size_t index) {
    Slot* slot_array = reinterpret_cast<Slot*>(page_data.get());
    if (index >= MAX_SLOTS)
      return;
    if (slot_array[index].empty == false) {
        slot_array[index].empty = true;
    }
  }

  void print() const {
    Slot* slot_array = reinterpret_cast<Slot*>(page_data.get());
    for (size_t slot_itr = 0; slot_itr < MAX_SLOTS; slot_itr++) {
      if (slot_array[slot_itr].empty == false) {
        assert(slot_array[slot_itr].offset != INVALID_VALUE);
        const char* tuple_data = page_data.get() + slot_array[slot_itr].offset;
        std::istringstream iss(tuple_data);
        auto loadedTuple = Tuple::deserialize(iss);
        std::cout << "Slot " << slot_itr << " : [";
        std::cout << (uint16_t)(slot_array[slot_itr].offset) << "] :: ";
        loadedTuple->print();
      }
    }
    std::cout << "\n";
  }
};
```

Here we use `reinterpret_cast<type>(value)` a lot - this allows us to reinterpret objects in C++ without having to create a new object.
This is convenient for this use case but can be dangerous if you are not careful.

# Storage Manager

To offload the responsibility of managing the file from the main BuzzDB class we create a separate storage manager.
This will hold all the responsibilities to do with the file and flushing the in-memory versions of the pages to the disk.
This manager will constantly have the file open in read/write mode.
It then can seek the file to write SlottedPages to the correct location - using the max file size to find the offset within the file.

```cpp
const std::string database_filename = "buzzdb.dat";

class StorageManager {
public:
  std::fstream fileStream;
  size_t num_pages = 0;

  // a vector of Slotted Pages acting as a table
  std::vector<std::unique_ptr<SlottedPage>> pages;

public:
  StorageManager(){
    fileStream.open(database_filename, std::ios::in | std::ios::out);
    if (!fileStream) {
      // If file does not exist, create it
      fileStream.clear(); // Reset the state
      fileStream.open(database_filename, std::ios::binary | std::ios::out);
    }

    fileStream.seekg(0, std::ios::end);
    num_pages = fileStream.tellg() / PAGE_SIZE;

    std::cout << "Num pages: " << num_pages << "\n";

    if(num_pages == 0){
      extend();
    }
    else{
      std::cout << "Loading " << num_pages << " pages \n";

      for (size_t page_itr = 0; page_itr < num_pages; page_itr++) {
        auto page(load(page_itr));
        pages.push_back(std::move(page));
      }
    }

  }

  ~StorageManager() {
    // Not needed but good practice
    if (fileStream.is_open()) {
      fileStream.close();
    }
  }

  // Read a page from disk
  std::unique_ptr<SlottedPage> load(uint16_t page_id) {
    fileStream.seekg(page_id * PAGE_SIZE, std::ios::beg);
    auto page = std::make_unique<SlottedPage>();
    // Read the content of the file into the page
    if(fileStream.read(page->page_data.get(), PAGE_SIZE)){
      std::cout << "Page read successfully from file." << std::endl;
    }
    else{
      std::cerr << "Error: Unable to read data from the file. \n";
      exit(-1);
    }
    return page;
  }

  // Write a page to disk
  void flush(uint16_t page_id) {
    size_t page_offset = page_id * PAGE_SIZE;

    // Move the write pointer
    fileStream.seekp(page_offset, std::ios::beg);
    fileStream.write(pages[page_id]->page_data.get(), PAGE_SIZE);
    fileStream.flush();
  }

  // Extend database file by one page
  void extend() {
    std::cout << "Extending database file \n";

    // Create a slotted page
    auto empty_slotted_page = std::make_unique<SlottedPage>();

    // Move the write pointer
    fileStream.seekp(0, std::ios::end);

    // Write the page to the file, extending it
    fileStream.write(empty_slotted_page->page_data.get(), PAGE_SIZE);
    fileStream.flush();

    // Update number of pages
    num_pages += 1;

    std::cout << "Loading page \n";

    // Load page into memory
    auto page_itr = num_pages - 1;
    auto page(load(page_itr));
    pages.push_back(std::move(page));
  }

};
```

We can now use the StorageManager's API to handle file based interactions - it will also own all the SlottedPages.
