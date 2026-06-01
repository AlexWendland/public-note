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
title: Week 5 - Multi-threading
type: lecture
week: 5
---

Within database applications to speed up query performance we will use multi-threading.
Though we need to pay attention to race-conditions and dead-locks between threads for this.
To handle this we will use locks.

The level of granularity of the locks will affect your program's complexity and performance.
For example, you could have database lock, table lock, or even down to the row level locks.
Each come with a payoff for performance gains vs complexity and overhead costs.

# Thread starvation

Thread starvation occurs when a thread is perpetually denied access to a resource because other threads continuously acquire it first, often due to priority inversion or unfair scheduling.
A related problem is forgetting to release a lock — if a thread never unlocks, all waiting threads are blocked indefinitely.
To prevent this in C++ we use `std::lock_guard`, which applies RAII: the lock is automatically released when the guard goes out of scope, even if an exception is thrown.

# Database configuration

To make the database more specialised to the system it is running on we expose configuration parameters.
Parameters we have seen so far are:

- PAGE_SIZE: The size of each page in bytes.

- MAX_SLOTS: The number of slots per page.

- MAX_PAGES_IN_MEMORY: The number of pages to keep in memory.

Changing these parameters all have payoffs.
Increasing the page size and number of pages in memory means the database will increase the memory the system uses.
Increasing the max slots per page means the average slot size will decrease, allowing for smaller tuples.
These all can be fine tuned to the system and application the database is for.
Some of these parameters can be optimised using a grid-search and running performance tests.
Whereas others can use the system setting to be auto-configured.

## Mutable vs Immutable Parameters

Some parameters need to be set at DB start-up or they will trigger a database rewrite when changed.
For example if we change the page size we will need to rewrite out the whole database with this new page size.
Therefore, these parameters are immutable.
On the other hand, parameters like `MAX_PAGES_IN_MEMORY` can be changed at runtime so are mutable.

## Configuration in cloud

When running the database in the cloud you may not be resource constrained but instead the use of more resources has an associated cost with it.
In these settings you will need to measure system performance and measure that against the additional cost of the system.

Different workloads tend to be limited by different resources.

### Online Transaction Processing (OLTP)

This is the most common workload for databases.
Workloads consist of many short, simple transactions (reads/writes of individual rows), with occasional longer queries.
For example, a banking application may have a lot of short transactions with a few long transactions.
These databases tend to be larger than DRAM ~1 TB.
The short transactions mean that they are normally bound at the CPU or I/O level due to the speed at which the transactions happen.

### Online Analytical Processing (OLAP)

These are large complex databases with complex queries run for large reports.
They are commonly called data warehouses and are used in AI and data intensive applications.
The database is typically larger than DRAM starting anywhere from 4TB up-wards.
These queries are typically I/O or DRAM bound due to the amount of data they are querying.

### Web Applications

These databases are normally tiny used for simple queries relating to the operation of a web application.
They are smaller than DRAM at about 4GB.
These are normally CPU bound due to the database fitting into memory.

# Debugging

Databases are large complex systems that can be difficult to debug.
Though there are tools to help with this.

- GDB: The GNU debugger.

- Logging: Logging is a way to record events that happen in the system.

- Stress Testing: Reducing the resources to your system allows for stress testing the system on small amounts of data.
This will help you find corner cases and common performance issues with your system.

- Modular design: Building the system to have small well defined classes helps you reduce cognitive load when debugging your system.

- Literate Programming: Writing docstrings and comments to say your intent allows you to write code that is easy to read and understand.

- Robustness: Writing your systems to handle failure gracefully means less crashing out or brittleness for the end users.
