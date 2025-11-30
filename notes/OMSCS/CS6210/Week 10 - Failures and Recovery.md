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
Therefore, we break the redo logs into epoch's so we can clean up one epoch at a time.
