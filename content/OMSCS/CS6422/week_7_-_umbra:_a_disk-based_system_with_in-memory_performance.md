---
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-17'
date_checked: '2026-06-17'
draft: false
last_edited: '2026-06-17'
tags:
  - OMSCS
title: 'Week 7 - Umbra: A Disk-Based System with In-Memory Performance'
type: lecture
week: 7
---

Paper: [Umbra: A Disk-Based System with In-Memory Performance](https://db.in.tum.de/~freitag/papers/p29-neumann-cidr20.pdf) — Neumann & Freitag, CIDR 2020.

Umbra is an evolution of the pure in-memory database HyPer towards a system that uses SSDs as a backing store, achieving in-memory performance for the cached working set while scaling transparently beyond RAM.

# Background: The Hardware Trend Problem

Pure in-memory databases (like HyPer) store all data in RAM and never page to disk. This gives excellent performance but has two problems:

1. **RAM growth has stalled** — commodity servers plateau around 2 TB, beyond which cost grows disproportionately.
2. **SSDs are now cheap and fast** — a 2 TB NVMe SSD costs ~$500 and reads at 3.5 GB/s. The equivalent DRAM costs ~$20,000 (40× more).

The goal of Umbra: in-memory performance when the working set fits in RAM, graceful SSD fallback when it doesn't — with minimal overhead for the common case.

> [!note]
> In-memory databases are fast because they skip the buffer manager entirely — tuples live at direct memory addresses with no paging indirection. Umbra's challenge is reintroducing a buffer manager without reintroducing its costs.

# Innovation 1: Variable-Size Page Buffer Manager

## The Problem

Traditional disk-based systems use a **fixed-size page** buffer manager (e.g. 8 KB pages).
This forces every data structure to deal with objects that may span multiple pages — a dictionary for compression, or a long string, must be split across pages and reassembled on read.
This complexity bleeds into every part of the system.

## The Innovation

Umbra uses **exponentially-sized page classes**: 64 KiB, 128 KiB, 256 KiB, 512 KiB, …

- A **single shared buffer pool** serves all size classes — no per-class memory budgets needed.
- Large objects (strings, dictionaries) are stored contiguously on one page — access is as simple as in-memory.

Fragmentation is eliminated via **virtual memory tricks**:
- `mmap` reserves a separate virtual address region per size class, each sized to the full buffer pool.
- Physical memory is only committed when a frame becomes active.
- On eviction, `madvise(MADV_DONTNEED)` releases physical memory — the virtual address range stays reserved but reads as zeroes.

> [!note]
> The buffer pool uses half of available RAM by default. The other half is left as scratch memory for query execution. This split doesn't need per-size-class tuning — all size classes share one pool.

# Innovation 2: Pointer Swizzling

## The Problem

In a traditional buffer manager, every inter-page pointer stores a **page ID** (just a number like `#4521`). To follow it, you always ask a central shared hash table "where is this page in RAM?" — even for hot pages accessed milliseconds ago. On many-core systems this shared hash table becomes a contention bottleneck.

## The Innovation

**Swips** — 64-bit values that encode either a direct RAM pointer or a disk page ID, distinguished by a single tag bit:

```
Swizzled   (in RAM):  [   63-bit RAM pointer      | 0 ]
Unswizzled (on disk): [ 57-bit page ID | 6-bit size | 1 ]
```

- **Lowest bit = 0** → real RAM pointer, dereference directly (~1 ns, no shared state touched).
- **Lowest bit = 1** → page is on disk, trigger the slow path: load page, rewrite the swip in the parent to the RAM address (swizzle it), future accesses are fast.

> [!note]
> This works because real RAM pointers are always 8-byte aligned on 64-bit systems, so their lowest bit is always 0 — it's free to steal as a tag. The size class is encoded in the unswizzled form so the buffer manager knows how much memory to allocate without a separate lookup.

The key asymmetry: eviction and cold-load are rare background events.
Access to hot cached data — which is every access in the common case — bypasses the buffer manager entirely, just like a pure in-memory system.

## Eviction with Swizzling

When a page is evicted:
1. Buffer manager acquires an **exclusive latch** on the parent page (the one containing the owning swip).
2. Rewrites the swip from RAM pointer → page ID (unswizzles it).
3. Flushes dirty data to disk.
4. Releases physical memory via `MADV_DONTNEED`.
5. Releases the latch.

This requires that **each page has exactly one owning swip** — so eviction only ever needs to update one location. B+-tree leaf nodes therefore have no sibling pointers (which would create multiple owners).

# Innovation 3: Versioned Latches

## The Problem

A latch is a reader/writer lock on a page used for thread safety.

> [!note]
> **Latch vs Lock** — these are two separate layers in a DB:
> - **Latch**: protects a physical page in RAM, held for microseconds during one operation. Managed by the buffer manager.
> - **Lock**: protects logical data (rows, tables), held for the entire transaction duration. Managed by the transaction manager.
>
> When two threads traverse a B+-tree simultaneously, latches stop them corrupting page data. When two *transactions* both want to update the same row, that's locks — a completely separate concern.

Even shared reader latches cause contention on many-core systems if acquired on every page access.

## The Innovation

Each buffer frame has a **versioned latch** — a 64-bit integer split into:
- **59 bits**: version counter, incremented on every page modification.
- **5 bits**: state (unlocked / shared / exclusive).

Three modes:

| Mode | Cost | Use |
|---|---|---|
| Exclusive | acquire + release, blocks all | writers modifying a page |
| Shared | acquire + release, pins page in RAM | readers that need the page to stay loaded |
| Optimistic | zero (just snapshot version counter) | read-heavy traversal |

**Optimistic reads** work by:
1. Snapshot the version counter. Check state bits are not exclusive — if they are, wait or restart.
2. Do the read.
3. Validate: are state bits still clear AND is version unchanged?

Two races are covered by two different checks:
- **State bits**: catches a writer currently holding exclusive mode mid-read.
- **Version counter**: catches a writer that completed entirely between two moments in the read.

> [!note]
> Even if a page is evicted mid-optimistic-read, this is safe. The virtual address range reserved for that buffer frame stays valid (from the `mmap` reservation) and reads as zeroes after `MADV_DONTNEED`. The optimistic validation then fails and restarts — no segfault.

# Innovation 4: B+-Tree as Table Storage

Relations in Umbra are stored in B+-trees keyed by **synthetic monotonically-increasing tuple IDs** (not user-facing keys). The leaf nodes contain the actual tuple data — the tree *is* the table, not a separate index on top of a heap.

```
          [50 | 100]            ← inner node (keys + swips to children)
         /     |     \
      [1-50] [51-100] [101+]   ← leaf nodes (actual row data in PAX layout)
```

- Inner nodes always use the smallest page size (64 KiB), giving a fanout of 8192.
- Monotonically increasing IDs mean nodes fill sequentially — no node splits on insert.
- Tuples within leaf pages use **PAX layout**: fixed-size attributes columnar at the start, variable-size data packed at the end.

> [!note]
> The tree structure exists primarily so each page has exactly one parent, satisfying the single-owner rule for pointer swizzling. The synthetic IDs are not user-visible — this is a storage structure, not a user-facing index. For actual user queries (e.g. `WHERE name = 'foo'`), separate indexes would be built on top.

# Innovation 5: String Storage Classes

In a pure in-memory system, a pointer to a string is always valid. In Umbra, the page containing a string could be evicted — making a raw pointer stale. Umbra classifies out-of-line strings by lifetime:

- **Persistent**: valid for database lifetime (e.g. query constants).
- **Transient**: valid during current query only — must be copied if materialised (e.g. strings read from base relations, since their page could be evicted mid-query).
- **Temporary**: created during execution (e.g. result of `UPPER()`), garbage collected after use.

Short strings (≤12 chars) are **inlined** into the 16-byte header to avoid pointer indirection entirely. Long strings store their first 4 chars in the header to short-circuit comparisons without loading the full string body.

# Innovation 6: Adaptive Query Compilation

HyPer compiled entire query plans monolithically to LLVM IR — even cheap queries paid full compilation cost, which could be 29× longer than query execution itself.

Umbra instead:
1. Splits plans into **pipelines → steps** (each step is a separate callable function, single- or multi-threaded).
2. Uses a **custom lightweight IR** (not LLVM IR directly) to generate code cheaply without the full LLVM overhead.
3. **Adaptive compilation**: steps always start interpreted via a fast bytecode VM. The runtime monitors progress and JIT-compiles to LLVM only when the expected remaining execution time justifies it.

This avoids over-compiling cheap queries while still getting fully optimised machine code for expensive long-running ones.

# Results

Benchmarks on JOB and TPCH (64 GiB RAM, Samsung 960 EVO SSD, warm caches):

| Comparison | JOB speedup | TPCH speedup |
|---|---|---|
| Umbra vs HyPer (overall) | 3.0× | 1.8× |
| Umbra vs HyPer (raw execution only) | ~comparable (±30%) | ~comparable (±10%) |
| Umbra vs MonetDB | 4.6× | 2.3× |

The overall speedup over HyPer is largely from better compilation strategy, not the buffer manager. The raw execution times are comparable — confirming that the buffer manager adds negligible overhead for cached data.

Buffer manager overhead vs bypassing it entirely: **<6%** on average.
I/O throughput with buffer manager: **1.13 GiB/s** vs 1.15 GiB/s without — saturates the SSD.

When data exceeds RAM the primary bottleneck is storage throughput, not the buffer manager. Adding more SSDs linearly increases available bandwidth.
