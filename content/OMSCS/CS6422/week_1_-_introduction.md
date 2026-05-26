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
title: Week 1 - Introduction
type: lecture
week: 1
---

Relational databases have uses all across industry.
First we motivate why they are useful by comparing it to a flat file database.

# Flat file database

A flat file database keeps all data in flat files - there can be multiple of these each representing individual tables.
Then custom code can be written to access or query the data in these files.
There are multiple issues with this approach.

> [!note] This is implementation specific
> Here we compare against simply keeping data in csv files on disk with custom code accessing it.
> In the era of big data more complicated ways to do this have mitigated some of the issues in this approach - for example Iceberg.

## Data redundancy

Without the use of keys within the data, we might need to use data values to link tables together.
This not only duplicates the data we are keying but makes it harder to update values across tables.

## Slow operations

Saving the data down to disk means operations such as deleting a row could involve rewriting the entire file.
This means a fairly minor operation requires the entire file to be rewritten and saved to disk, which could be very slow.

(There are hardware/software speedups that could speed this up.)

## Slow Queries

In CSV format, to do operations such as finding rows with a given value in a column we need to scan the entire file.
Again if this file is large this could be very slow.
This only gets slower as you want to do more complex operations that use multiple tables.

## Concurrent updates: Incorrect data

Concurrent writes to the same file could happen without knowledge of one another - this could lead to incorrect data state.
For example, consider two concurrent operations both reading a user's record: one updates their name, the other updates their location.
Without any coordination, one write may overwrite the other, resulting in a lost update — e.g. the name change is silently discarded.

## Handling disk failures

Without a transactional write to disk if a failure occurs it can leave the files in an inconsistent state upon restart.
This will mean the data is unrecoverable without manual intervention - which can be hard in large databases.

## Memory management

To speed up operations it will be handy to hold an in memory version of the database.
However, this means coordinating writes to disk as the in-memory database changes so we don't lose changes upon system shutdown.

## Usability

With the use of a flat file, it means writing custom code for each query.
This means that the storage layer and the query layer are coupled and makes the data inaccessible to people without a programming background.

# Relational databases

A relational database was introduced by Ted Codd in 1970 who was working as a scientist at IBM.
This uses the table abstraction which stores data in a tabular format with pre-specified columns in rows.

> [!note] Relation in relational
> A relation is a term within set theory, this is a set of tuples and is what a table is.
> Here each row is a tuple.

The main concept behind relational database was to decouple the 'logical' design of our data from the 'physical' design of it.
The logical design is the tables and columns that the data owner has chosen to store the data in.
The physical design is how the data is stored and indexed on disk.
Normally the logical component of the data is orchestrated in SQL - the use of which does not require a general programming background (though it does require familiarity with query syntax and domain knowledge).
This enables the database owner to make changes to the physical design of the data without the data owner needing to know about it.

Another key concept in relational databases is primary/foreign key relations.
Each table is provided with a primary key that is used to de-duplicate and link data onto other tables.
Tables can contain foreign keys to other tables - the primary key - that links the tables together and ensures there are no empty references.

This structure comes with many benefits.

## No data redundancy

Using the primary/foreign key means we no longer need to duplicate fields as references.
This makes changes to fields easier to propagate through other tables as well.

## Fast operations

The physical storage can be optimised to speed up common operations.
For example, deleting rows can be quick and finding related entries on other tables can cost less using the primary/foreign key relation.

## Fast Queries

We can optimise the physical storage - mainly through choosing good indices - to speed up common queries.
This can be done in the backend without affecting users' SQL code.

## Concurrent updates

In a relational database we make changes in transactions which are atomic.
Atomicity guarantees that a transaction either commits fully or not at all — no partial changes are visible to other operations.
Concurrent transactions are isolated from one another through concurrency control mechanisms (e.g. locking or MVCC), preventing conflicting writes.

## Handling failures

Due to the transactions, we can handle failures such as disk issues.
Transactions are saved in totality - so they are either successfully applied or the previous state is known and can be rolled back to.

## Memory management

Relational databases use a Write-Ahead Log (WAL) — changes are recorded to the log before being applied to the data pages on disk.
This means that in the event of a crash, committed transactions recorded in the WAL can be replayed to recover the database to a consistent state.
Uncommitted transactions at the time of failure are simply discarded.

![Memory management](../../../static/images/memory_management_6422.png)

The diagram above shows a row being read into memory, changes are made, these are saved to the transaction log before being applied to the underlying data.

## Usability

Using SQL to access the data reduces the need to write custom code for each query.
This allows for the separation between the logical and physical storage of the data.

# Relational operations

Operators function over tables (or sets of relations/tuples).
There are standardised operations which we will use in this course.
Whilst SQL is a language it has many 'dialects' therefore below we talk about the generic operations rather than any specific implementation.

- *SELECT* ($\pi$): Selects specific columns from a table.

- *WHERE* ($\sigma$): Filters the rows of a table based on some specific conditions.

- *GROUP BY* ($\gamma$): Groups the rows of a table based on some specific column values.

- *AGG (aggregation)* ($\gamma_{agg}$): Aggregates values defined by a GROUP BY clause - common operations include SUM, COUNT, MIN, MAX, and AVG.

- *JOIN* ($\bowtie$): Links two tables together based on a common key.

## Relational algebra

Relational algebra allows us to combine the above operations in a way to create more complex queries.
This is the theoretical underpinning of operations on relational databases.

> [!example] Relational algebra
> Below is an example relational algebra query for getting the total 'likes' in a table.
> ```
> *SORT* ($\tau$) TotalLikes DESC
>   ($\pi$ PostID, TotalLikes, UsersWhoLiked
>     ($\gamma$ COUNT(*) -> TotalLikes,
>       GROUP_CONCAT(..) -> UsersWhoLiked
>     ($\sigma$ ReactionType = 'like'
>       (Interactions) $\bowtie$ Users)
>     )
>   )
> ```

## SQL

SQL is a language that implements this relational algebra.
Whilst SQL is referred to as a language it has many 'dialects' depending on the application that is implementing it.
Normally the core syntax is the same for example the operations above - but 'dialects' can add additional syntax or make different choices for what is considered a table identifier or string.

> [!example] SQL
> Below is an example SQL query for getting the total 'likes' in a table.
> ```sql
> SELECT Interactions.PostID, COUNT(*) AS TotalLikes,
>   GROUP_CONCAT(DISTINCT Users.UserID || '-' || Users.Username)
> FROM Interactions
> JOIN Users ON Interactions.UserID = Users.UserID
> WHERE Interactions.ReactionType = 'like'
> GROUP BY Interactions.PostID
> ORDER BY TotalLikes DESC
> LIMIT 1;
> ```
> This query gets the most liked post by id and shows the users who liked it.
> The output might look something like:
> ```
> PostID, TotalLikes, UsersWhoLiked
> 1002, 3, 3-alex;4-bella;5-charlie
> ```

