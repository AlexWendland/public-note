---
aliases: null
checked: false
course: '[[CS6210 Advanced Operating Systems]]'
created: '2025-11-30'
draft: true
last_edited: '2025-11-30'
tags:
  - OMSCS
type: lecture
week: 10
---

# Week 10 - Failures and Recovery

Within an operating system, crashes will occur.
When they do they need to leave us in state we can recover from.
To do this we need persistence and recovery.

## Lightweight Reliable Virtual Memory (LRVM)

Whilst the operating system and its subsystems are changing objects in memory if a crash occurs before it has a chance to save it to disk it can leave the OS in a broken state.
To combat this LRVM creates an interface to make some objects in virtual memory persistent on the disk.
The key to this working is to make this fast and have a clean, easy to use interface for subsystem designers.

If the writes to disk where random, this would be slow as disks need to seek to different positions.
So instead we use log based writes similar to the distributed file system.

### Interface

**Initialisation**

- `initialize(options)`: Set up the LRVM within this address space.

- `map(region, options)`: Map some region of virtual memory into persistent storage.

- `unmap(region)`: Remove a region from persistent storage.

**Operations**

- `begin_xact(tid, restore_mode)`: Start a transaction and get given an id for it.

- `set_range(tid, addr, size)`: Set what address ranges are going to be edited in this transaction.

- `end_xact(tid, commit_mode)`: End the transaction and save it down.

- `abort_xact(tid)`: Abort the transaction and discard it.

Transactions are not immediately reflected in the persistent storage - instead the new value of the memory are stored in a redo log which is saved to the disk for later compaction.
The above operations are all developers need to know - however there are a couple more operations if they would like to manually manage when these logs are applied.

**Management**

- `flush()`: Flush all the redo logs to disk.

- `truncate()`: Truncate the log file to the current size.

- `query_options(region)`: Get the options for a given region.

- `set_options(region, options)`: Set the options for a given region.

- `create_log(options, len, mode)`: Manually create a new log file.

#### Managing aborts

When the developer calls `set_range` the LRVM will make a 'undo record' of that range. 
Then if the transaction is aborted, this copy will be applied to the region to clear any changes made to it.
(This can be toggled off using no_restore mode in the `begin_xact` call.
This will make LRVM more performant.)

#### Managing flushes

In a flush we write to the disk, therefore as a matter of optimisation we may want to hold off flushing until multiple writes are ready.
For this we can set `no_flush` mode in the `end_xact` call.
However, this ability to have lazy persistence does leave a window of vulnerability where if a power outage or crash happens whilst redo logs are in memory rather than on disk - there is no recovery from this.

### Crash recovery

The redo logs are lists of the changes made to the persisted memory status.

![Redo log](../../../images/redo_log.png)

These redo logs are saved to disk before being applied to the persistent data structures representing the virtual memory.
So if when we restart we find un-applied redo logs we apply these before we reload the memory addresses.

### Log truncation

If we do not crash then we slowly accumulate redo logs on disk - which can take up a lot of disk space.
Therefore, there is either the explicit truncate call or the implicit cleanup ran by LRVM.

To run truncation we do as we laid out above.
We move the old redo logs to memory, apply them to disk representations.
After that we throw away the redo log.

![Log truncation](../../../images/log_truncation_struct.png)

Though we want to do this in parallel to letting the application code running.
Therefore, we break the redo logs into epoch's so we can clean up one epoch at a time whilst letting the application code to add new redo logs to the current epoch.
The truncation process is one of the most complex and time consuming parts of LRVM.

## Riovista

There are two sources of system failures:

- Power outages: Where the power for the whole system stops.

- Software bugs: Where the software causes the machine to crash.

In the LRVM system we handled both these cases.
However, if we attach an external battery to our virtual memory we could guarantee the first cause of outages never happens.
This is the premise of the Riovista system: We have a portion of main memory which has an external battery and is resilient to crashes, we call this persistent memory.

### Rio file cache

A file cache is a in memory representation of a file.
This allows for:

- Fast writes to a file without needing to go to disk.

- Mmapped files to be read and written to in memory - to be reflected on disk later.

If we make the region of this memory that we put the file cache into persistent, we can guarantee these writes will be reflected in the disk eventually.
Without the persistent storage, any writes that happen in memory but are not reflected on disk risk failure causing them to be eliminated leaving the disk in a broken state.
The Persistent file cache means that synchronous writes to disk no longer need to happen (space allowing).
Files that are written to are replicated back to disk after the program has stopped using it.

![Rio file cache](../../../images/rio_file_cache.png)

### Vista

Visa is an RVM that is built on top of the Rio file cache.

![Vista](../../../images/vista.png)

Vista follows the same interface as LRVM but uses the file cache instead of logs to persist the memory.
When we initialise the persistence of some virtual memory locations, we just back them onto our persistent file cache.
During `begin_xact` we make an in memory copy of the memory location we are persisting and save it as the undo log in the file cache.

During the critical section, edits are made to the original memory location which are persisted onto the persistent file cache.
In the case of a commit we simply delete the undo log and move on.
In the case of the abort we copy the undo log back to the original memory location restoring the state to what it was at the beginning of the transaction.
We treat system failures as an abort and use the undo log to wipe temporary changes.

This implementation is incredibly simple, a lot of heavy lifting is coming from the file cache.
This means that it has 3 orders of magnitude better performance than LRVM.
Though it does require having a battery backed persistent memory.

## Quick silver


