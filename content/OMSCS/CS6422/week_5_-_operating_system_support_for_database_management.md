---
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-18'
date_checked: '2026-06-18'
draft: true
last_edited: '2026-06-18'
tags:
  - OMSCS
title: 'Week 5 - Operating System Support for Database Management'
type: lecture
week: 5
---

Paper: [Operating System Support for Database Management](https://dl.acm.org/doi/10.1145/358699.358703) — Michael Stonebraker, CACM July 1981.

Stonebraker examines four core OS services — buffer management, the file system, scheduling and IPC, and consistency control — and makes the same finding in every single case: **the OS gets it wrong, and DBMSs end up reimplementing the service themselves in user space**. The paper's conclusion is essentially that a DBMS would be better served by a minimal real-time OS than by a general-purpose one, and that OS designers have things backwards: DBMS-level storage abstractions should be the primitive, with character arrays built on top.

> [!note]
> This paper is from 1981, written in the context of UNIX on PDP-11/70 and VAX 11/780 hardware, and the INGRES and System R relational DBMSs. The specific instruction counts are dated, but every architectural tension Stonebraker identifies is still visible in modern systems — including in Umbra's buffer manager design and the "why DBMSs bypass the OS page cache" discussion that comes up constantly.

The central pattern Stonebraker documents throughout the paper: the OS provides a service, the service is subtly wrong for DBMS workloads, the DBMS builds its own version in user space, and the OS version goes unused. The result is two parallel implementations of the same facility — one in the OS, one in the DBMS — with all the maintenance cost and interaction complexity that implies.

# 1. Buffer Pool Management

## The OS Cache Is Too Slow to Call

UNIX provides a main memory buffer cache for all file I/O. Conceptually useful — frequently accessed blocks stay warm. In practice, every access requires a system call and a core-to-core memory copy. On a PDP-11/70:

- Fetching 512 bytes: **>5,000 instructions**
- Fetching 1 byte: **~1,800 instructions**

These costs are high enough that both INGRES and System R chose to maintain their own buffer pool entirely in user space rather than use the OS-provided cache. The OS service exists but goes unused.

## LRU Is the Wrong Replacement Policy

UNIX uses LRU eviction, which works well when programs exhibit locality of reference. Database access patterns are fundamentally different. Stonebraker categorises INGRES's access patterns into four types:

| Access type | Example | Best policy |
|---|---|---|
| Sequential, no re-reference | Table scan at end of query | Toss immediately |
| Sequential, cyclic re-reference | Nested-loop join inner relation | Keep (if fits) or toss immediately |
| Random, no re-reference | Hash probes on large table | Toss immediately |
| Random, with re-reference probability | Index lookups on hot pages | LRU |

LRU only helps with the last case. For cyclic sequential access (type 2), LRU is actually the **worst possible** algorithm: the access pattern `1, 2, 3, …, n, 1, 2, 3, …` causes a cache miss on every access unless all `n` pages fit in cache simultaneously. If they don't, you should toss immediately instead.

A DBMS knows which category each access falls into — the OS does not. Initial studies showed DBMS-specific replacement cuts the miss ratio by 10–15% vs. LRU.

The fix would require the OS buffer manager to accept "advice" from application code about replacement strategy. No OS at the time provided this.

## Prefetch Gets It Wrong

UNIX prefetches pages when it detects sequential file access — a reasonable heuristic for most programs. For a DBMS it is insufficient: INGRES frequently knows exactly which block it will need next, but that block is not necessarily the next one in logical file order (e.g., following a B-tree pointer to a non-adjacent leaf). The OS has no way to implement the correct prefetch strategy without application guidance.

## Crash Recovery Needs Ordered Forced Writes

DBMS transaction recovery requires writing pages to disk in a specific order: the intentions list (the set of pending updates) must be flushed *before* the commit flag. Only after the commit flag hits disk can the transaction be confirmed. No OS buffer manager Stonebraker knew of provided **selective force-out** — the ability to flush specific pages to disk in a caller-specified order.

Without this, the DBMS must manage its own write ordering, which again means bypassing the OS cache entirely.

> [!note]
> This is exactly the "no steal / force" vs. "steal / no force" buffer manager policy distinction. Modern DBMSs almost universally use "steal / no force" (allowing dirty pages to be evicted before commit, using a WAL to recover) precisely because forced writes are too expensive. Stonebraker is identifying the root of why WAL became necessary: you can't trust the OS to order your writes.

## Summary

The OS buffer pool has the right shape (a cache) but the wrong defaults (LRU, no advice API, no ordered force-out, high call overhead). The consequence: "a 'not quite right' service provided by the OS going unused and a comparable application-specific service being provided by the DBMS." Stonebraker calls this the defining pattern of the whole paper — and it repeats in every section.

---

# 2. The File System

## The Wrong Primitive

UNIX exposes files as **character arrays of dynamically varying size**. This is the right abstraction for text editors, compilers, and shell tools. A DBMS does not want a character array — it wants a **record management system**: structured records, efficient keyed access, secondary indexes, multilevel directories.

The alternative (which systems like DEC RMS-11 and Tandem Enscribe implemented) is to put record management *inside* the OS. Stonebraker's point is that UNIX chose the wrong level of abstraction as the primitive.

## Physical Contiguity

UNIX allocates file blocks one at a time. Blocks of the same file often end up scattered across the disk volume — the next logical block is not physically adjacent to the previous one. Sequential access (which DBMSs do constantly) therefore causes excessive disk arm movement.

DBMSs prefer **extent-based** file systems (like IBM VSAM): pre-allocate contiguous runs of blocks, grow files an extent at a time. This matches the sequential access pattern and eliminates seek overhead for sequential scans.

## The Triple Tree Problem

UNIX implements two tree structures:
1. An inode tree — tracking which disk blocks belong to which file.
2. A directory tree — the user-visible hierarchical namespace.

A DBMS like INGRES then adds a third tree:
3. An access path tree — B-trees, ISAM indexes, hash directories for keyed record access.

Three separately managed trees, all storing overlapping location information about the same data. "One tree with all three kinds of information is more efficient than three separately managed trees." The overhead of maintaining three separate trees is substantial.

## The Inversion Stonebraker Proposes

Section 3.3 is the most radical part of the paper. Stonebraker argues:

> "OS designers should contemplate providing DBMS facilities as lower level objects and character arrays as higher level ones."

This is a complete inversion of the UNIX philosophy. Instead of a DBMS building structured record access on top of character arrays, the OS should expose records and structured storage as its native primitive, and character arrays (for editors, etc.) should be built on top of that. The observation is that editors can use record management structures just as efficiently as the raw character arrays they currently manage themselves.

---

# 3. Scheduling, Process Management, and IPC

## Two Models for Multiuser DBMSs

There are two ways to structure a multiuser DBMS:

**Process-per-user**: Each concurrent user runs in a separate OS process. All processes share the DBMS code segment and ideally share data segments (buffer pool, lock table). This is what System R does; INGRES approximates it.

**Server model**: One (or a pool of) DBMS server processes receive work requests via messages from user processes and schedule them internally. This is what Tandem Enscribe does.

Both are conceptually equivalent (Lauer & Needham 1979 proved they are duals). In practice, OS design strongly forces the first approach — UNIX's pipe-based IPC is incompatible with a true server model.

## Problems with Process-Per-User

**Task switch overhead**: When a DBMS process issues an I/O request and the required block is not in the buffer pool, the OS suspends it and runs another process. On many OSes, a task switch costs 1,000+ instructions due to large per-process state (accounting data, sophisticated scheduler). Paying 1,000 instructions for a buffer pool miss is expensive when buffer misses are frequent.

**The convoy problem** (Blasgen et al., 1979): DBMS processes have critical sections — portions of the buffer pool manager that only one process can execute at a time. System R implements these as short-term locks (simulated semaphores). If the OS scheduler deschedules a process while it holds one of these locks, every other DBMS process that needs the buffer pool queues up behind it. The probability of this is low, but when it happens the performance impact is severe — a "convoy" of blocked processes all waiting for one descheduled lock holder.

## Problems with the Server Model

The server model avoids both problems above, but creates new ones:

- A server must implement its own internal **scheduling and multitasking** — painful duplication of OS facilities.
- A non-multitasking server (FCFS, no internal parallelism) wastes disk bandwidth: it can only have one I/O outstanding at a time, leaving all other disks idle.
- A multitasking server pool still needs shared lock tables and is barely different from the process-per-user model.
- Replacing a task switch per I/O with a **message per I/O** doesn't help: on PDP-11/70 UNIX, a round-trip message costs ~5,000 instructions — potentially more expensive than the task switch it replaces.

## Stonebraker's Proposed Escape

The only clean exit Stonebraker sees: the OS creates a **special scheduling class for the DBMS**. Processes in this class would:
- Never be forcibly descheduled (solving the convoy problem).
- Voluntarily yield the CPU at appropriate points.
- Have a fast path through the task switch loop to hand control to a sibling DBMS process at low overhead.

This is essentially cooperative scheduling for trusted DBMS processes — the OS gets out of the way and lets the DBMS manage its own concurrency.

> [!note]
> This is precisely the design space that modern userspace threading (green threads, coroutines, async/await) inhabits. Systems like VoltDB and SEDA, and more recently the io_uring model in Linux, are direct descendants of this reasoning: give the application control over its own scheduling to avoid OS overhead and convoy effects.

---

# 4. Consistency Control

## What the OS Provides

Most OSes provide file-level locking (shared/exclusive). Few support finer-grained locks at the page or record level — which DBMSs need for acceptable concurrency. Most OSes also provide some cleanup after crashes, but not at the transaction level.

The proposal that concurrency control and crash recovery should live entirely inside the OS is conceptually sound and could be as efficient as user-space implementations — but only if the buffer management problems from Section 2 are also solved first.

## The Commit Point Problem

When a transaction commits, the user-space buffer manager must flush all dirty pages and signal the OS. This means the buffer manager cannot be ignorant of transaction boundaries — it must know when a commit is happening to issue the right forced writes in the right order. Buffer management and transaction management become entangled.

If the OS handles consistency control but the DBMS still handles buffering (the mixed case), both layers must coordinate on every commit — duplicating logic across the boundary.

## The Ordering Dependency Problem

Consider:

```
Empname  Salary  Manager
Smith    10,000  Brown
Jones     9,000  None
Brown    11,000  Jones
```

Update: give a 20% pay cut to all employees earning more than their manager. Only Brown should be affected (earns 11,000, manager Jones earns 9,000).

If the DBMS updates rows as it scans and Brown is updated before Smith is examined, then when Smith's manager (Brown) is looked up, Brown now earns 8,800 — less than Smith's 10,000 — and Smith incorrectly receives a pay cut too.

The correct result depends on whether updates are applied to the *before* image of the data or the *after* image as the scan progresses. If the OS maintains the buffer pool and an intentions list for crash recovery, it can enforce the correct semantics. If the DBMS runs its own buffer pool in user space, it must maintain its own intentions list to get this right — again duplicating OS-level facilities.

## The Three-Way Split Problem

Stonebraker identifies three combinations:

| Buffering | Consistency | Result |
|---|---|---|
| OS | OS | Clean — but requires solving Section 2's performance problems |
| DBMS | DBMS | Clean — both services in one place |
| DBMS | OS | Broken — commit points and ordering require duplication across both layers |

The mixed case (DBMS buffer management + OS consistency control) is the worst option: it forces code duplication and creates coordination overhead at every transaction boundary.

---

# 5. Paged Virtual Memory

An alternative proposal to explicit file I/O: bind files directly into the process's virtual address space. The program accesses file data as if it were ordinary memory variables; the OS paging hardware moves blocks in and out transparently.

## Problem: Large File Page Tables

Paging hardware typically allocates 4 bytes of page table entry per 4 KiB page. A 100 MB file needs **100 KB of page table**. This page table itself may not fit in main memory, causing two page faults per I/O access: one for the page table entry, one for the actual data. The workaround — wiring the entire page table in RAM — is expensive.

Conventional file systems handle this more compactly: an extent-based file control block represents 1,000 consecutive blocks as a starting address + length, using far less space than 1,000 individual page table entries. The file control block is made resident when the file is opened, so only one I/O is ever needed per access.

## Problem: Buffering Is Unchanged

Binding files into virtual memory does not solve any of the buffer management problems from Section 2. The same issues apply: wrong replacement policy, no prefetch advice API, no ordered force-out. Paged virtual memory changes the call interface but not the underlying semantics.

---

# Conclusion

Stonebraker's verdict: **"Operating system services in many existing systems are either too slow or inappropriate. Current DBMSs usually provide their own and make little or no use of those offered by the operating system."**

The ideal OS for a DBMS would be a **small, efficient, minimal system** — closer to a real-time OS than a general-purpose one. General-purpose OSes offer all things to all programs at high overhead; a DBMS only needs a subset of those services, and needs them fast.

The repeated pattern across every section:

```
OS provides service X
  → service is wrong or too slow for DBMS workloads
  → DBMS reimplements X in user space
  → result: two parallel implementations of X, OS version unused
```

> [!note]
> This is why modern high-performance DBMSs still bypass the OS page cache (`O_DIRECT`), implement their own threading models (coroutine-per-transaction in VoltDB/HyPer), and use write-ahead logging rather than relying on OS crash recovery. Stonebraker identified in 1981 that the fundamental mismatch between OS and DBMS assumptions is architectural, not just a tuning problem. Forty years later the DBMSs have simply gotten better at working around it.

The truly radical suggestion — that OS designers should invert the abstraction stack and expose DBMS-style structured storage as the primitive, with character arrays built on top — never happened in mainstream systems. But it did happen in one narrow context: mobile platforms. iOS and Android require all applications to use SQLite as their durable storage layer, with the raw file system deliberately inaccessible to apps. The OS's storage primitive *is* a database. Stonebraker would approve.
