---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-01'
date_checked: '2026-06-01'
draft: false
last_edited: '2026-06-01'
tags:
  - OMSCS
title: Week 4 - Buffer Management
type: lecture
week: 4
---

In the previous lectures we created the idea of the Slotted page.
This allows us to group together Tuples into blocks.
The pages then can be written onto the disk or into the memory directly.
However, we need something to decide which pages to keep in memory and which ones to write to the disk.
This is where the Buffer Manager comes in.

There are two things that are important here:

1. Moving pages from memory to disk and vice versa.

2. Deciding which pages to keep in memory and which ones to write to the disk.

This is a policy vs. mechanism problem.
The mechanism is the Buffer Manager which does (1) and the policy is the algorithm which does (2).
The Buffer Manager can be built agnostic of the algorithm which decides which pages stay and which pages go.

# Buffer Manager

Suppose we have a generic Policy interface as below.

```cpp
class Policy {
  int max_pages_in_memory;
public:
  // Inform the policy that this page was used.
  virtual bool touch(PageID page_id) = 0;

  // Ask the policy which page we should write to the disk.
  virtual PageID evict() = 0;
};
```

The `BufferManager` will manage the pages in-memory working with the `StorageManager` to write pages into/from disk.

> [!reminder] `StorageManager` interface
> The `StorageManager` has two important methods for us to use:
>
> 1. `flush(PageID page_id, const std::unique_ptr<SlottedPage>& page)` - Writes a page to disk.
>
> 2. `load(PageID page_id)` - Loads a page from disk.

Then the `BufferManager` will own the `PageMap` of `SlottedPages` that are currently in memory.
Then its core function is to get a page by id.

```cpp
constexpr size_t MAX_PAGES_IN_MEMORY = 10;

class BufferManager {
private:
  using PageMap = std::unordered_map<PageID, std::unique_ptr<SlottedPage>>;

  StorageManager storage_manager;
  PageMap pageMap;
  std::unique_ptr<Policy> policy;

public:

  std::unique_ptr<SlottedPage>& getPage(int page_id) {
    auto it = pageMap.find(page_id);

    if (it != pageMap.end()) {
      policy->touch(page_id);
      return pageMap.find(page_id)->second;
    }

    if (pageMap.size() >= MAX_PAGES_IN_MEMORY) {
      auto evictedPageId = policy->evict();
      if(evictedPageId != INVALID_VALUE){
        std::cout << "Evicting page " << evictedPageId << "\n";
        storage_manager.flush(evictedPageId,
                              pageMap[evictedPageId]);
        pageMap.erase(evictedPageId);
      }
    }

    auto page = storage_manager.load(page_id);
    policy->touch(page_id);
    std::cout << "Loading page: " << page_id << "\n";
    pageMap[page_id] = std::move(page);
    return pageMap[page_id];
  }
};
```

# Buffer Policy

The Buffer Policy needs to keep track of which pages are in memory and choose which pages to evict.
The goal of the Buffer policy is to cause as few cache misses as possible - that is requests for pages that are not in memory.
There are a number of basic policies that you might think of.

## FIFO policy

This is probably the most basic policy you could have.
Keep a list of pages in a FIFO ordering and push/pop the first/last page when a page is used.

```cpp
class FIFOPolicy : public Policy {
  std::deque<PageID> pageQueue;
public:
  bool touch(PageID page_id) override {
    auto it = std::find(pageQueue.begin(), pageQueue.end(), page_id);
    if (it == pageQueue.end()) {
      pageQueue.push_back(page_id);
    }
    return true;
  }

  PageID evict() override {
    PageID evictedPageId = pageQueue.front();
    pageQueue.pop_front();
    return evictedPageId;
  }
};
```

## LRU policy

The FIFO policy doesn't really use the information about pages getting used at all.
Instead of just keeping the list ordered by when it was first put into memory we could instead track when it was last used.
Then we could kick out the Least Recently Used (LRU) page.

```cpp
class LRUPolicy : public Policy {
  std::deque<PageID> pageQueue;
public:
  bool touch(PageID page_id) override {
    auto it = std::find(pageQueue.begin(), pageQueue.end(), page_id);

    if (it != pageQueue.end()) {
      pageQueue.erase(it);
    }

    pageQueue.push_front(page_id);
    return true;
  }

  PageID evict() override {
    PageID evictedPageId = pageQueue.back();
    pageQueue.pop_back();
    return evictedPageId;
  }
};
```

# Buffer Pool Flooding

Within a database there are queries that cause a 'sequential scan' of all pages.
For example, if a query is looking up on a key without an index we need to look at all pages to check which Tuples match the query.
These are nearly inevitable but completely destroy the policies we have presented previously.
In this case we throw away hot pages to load in the 'searching pages' even though they are unlikely to be needed by other queries.

However, we can get around this issue by preferably throwing away the pages that are used in the sequential scan rather than the hotter commonly used pages.

## 2Q Policy

The idea behind the 2Q policy is to keep 2 queues.
First are pages that have only been requested once in a FIFO ordering.
Second are pages that have been requested more than once in an LRU ordering.
Then when erasing the pages we first evict from the FIFO queue only when we have no 'sequential scan' pages do we choose to evict from the LRU queue.

```cpp

class TwoQPolicy : public Policy {
  enum QueueType { FIFO, LRU };

  std::unordered_map<PageID, QueueType> pageQueue;
  std::deque<PageID> pageQueueFIFO;
  std::deque<PageID> pageQueueLRU;
public:
  bool touch(PageID page_id) override {
    auto it = pageQueue.find(page_id);

    if (it == pageQueue.end()) {
      pageQueue[page_id] = FIFO;
      pageQueueFIFO.push_back(page_id);
      return true;
    }

    if (it->second == FIFO) {
      pageQueue[page_id] = LRU;
      auto fifoIt = std::find(pageQueueFIFO.begin(), pageQueueFIFO.end(), page_id);
      if (fifoIt != pageQueueFIFO.end()) pageQueueFIFO.erase(fifoIt);
    } else if (it->second == LRU) {
      auto lruIt = std::find(pageQueueLRU.begin(), pageQueueLRU.end(), page_id);
      if (lruIt != pageQueueLRU.end()) pageQueueLRU.erase(lruIt);
    }

    pageQueueLRU.push_back(page_id);
    return true;
  }

  PageID evict() override {
    PageID evictedPageId;

    if (pageQueueFIFO.empty()) {
      evictedPageId = pageQueueLRU.front();
      pageQueueLRU.pop_front();
    } else{
      evictedPageId = pageQueueFIFO.front();
      pageQueueFIFO.pop_front();
    }

    pageQueue.erase(evictedPageId);
    return evictedPageId;
  }
};
```
