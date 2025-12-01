---
aliases:
checked: false
course: '[[CS6210 Advanced Operating Systems]]'
created: 2025-09-04
draft: true
last_edited: 2025-09-04
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Virtualization

As a refresher please read:

[[Week 12 - Virtualization]]

# Memory Virtualisation

## Address Translation

When hosting guest operating systems on top of a hyper visor we need to make memory appear as it would to a normal OS.
For the CPU cache which is physically tagged, there is no special operations we need to perform.
However, for virtual memory we need to be able to map it to 'machine memory' correctly.

Within Virtualisation there are two mappings involved with any virtual to machine memory mapping.

1. The Guest OS maps from a Virtual Page Number (VPN) to what it thinks is a Physical Page Number (PPN).

2. The Hypervisor then maps from that PPN to what we are calling a Machine Page Number (MPN) (what is a PPN for a normal OS, and what is tagging the CPU cache).
We refer to this second mapping as a Shadow Page Table (S-PT).

In a typical OS, these mappings are done by the MMU (Memory Management Unit) assisted by the TLB (Translation Lookaside Buffer) which are both hardware.
This is to speed up this translation as memory access is a very frequent operation.
However, having to do two mappings would dramatically slow this down - not only also require more memory to store the S-PT.
Different approaches are taken when we are fully Virtualised vs Para Virtualised.
In the Para Virtualised setting the guest OS is aware that it is running on a hypervisor.

### Full Virtualisation

For full virtualisation we can't change how the guest OS works.
Therefore, we need to hook into the system calls it will make - namely when it tries to write entries to its page tables/update the TLB.

#### Shadow Page Tables Implementation

The hypervisor maintains **shadow page tables** that store mapping PPN -> MPN directly. When the guest OS tries to update its page table (VPN -> PPN), the hypervisor:

1. **Traps the write operation** (expensive VMM trap)
2. **Looks up the PPN -> MPN mapping** from its shadow page table
3. **Calculates the composite VPN -> MPN mapping**
4. **Writes the composite mapping** to the actual hardware PT/TLB

This allows hardware to operate with direct VPN -> MPN translations, avoiding two-level lookups on every memory access.

#### Memory Overhead Challenges

Shadow page tables create significant memory overhead:

- **Doubled memory consumption**: The hypervisor must maintain complete shadow page tables for each VM, duplicating all guest page table structures
- **Scales linearly with VMs**: Each additional VM requires its own complete set of shadow page tables
- **Two mappings stored**: Both VPN -> PPN (guest PT) and PPN -> MPN (shadow PT) must be kept in memory

#### Performance Trade-offs

Shadow paging creates a complex **optimization problem**:

- **Page table updates become expensive**: Each guest PT update requires VMM traps and composite mapping calculations
- **Context switching overhead**: VM switches require reloading shadow page tables
- **TLB management complexity**: Frequent VM switches cause TLB flushes, destroying cached translations
- **Tracing strategy trade-off**: The hypervisor must choose between:
  - **Aggressive tracing**: Intercept every guest page table update to keep shadow tables synchronized, reducing hidden page faults but causing frequent expensive VMM traps
  - **Lazy tracing**: Intercept fewer operations, reducing VMM trap overhead but allowing guest and shadow page tables to become out of sync, leading to "hidden page faults" when hardware encounters stale shadow mappings

The key insight is that **page table updates are infrequent compared to memory accesses**, so the approach trades slower PT updates for faster memory access performance.

### Para Virtualisation

In the para virtualised setting, the guest OS is aware it is running on a hypervisor.
This means the guest OS can also be aware of what MPN's it as an operating system has been allocated.
This will uses these addresses to assign to VPN's when dealing with applications it controls.
Therefore, it can make special hypercalls to the hypervisor when it wants to update its page tables.
In Zen, this is done using 3 special hypercalls:

1. **Create PT**: When it needs to create a new page table

2. **Switch PT**: When it needs to switch to a different process and therefore page table.

3. **Update PT**: When it needs to update an entry in the page table.

The hypervisor then is completely responsible for managing the page tables.
The guest OS is responsible for managing the page entries it has been given.
This way page faults are still handled by the guest OS.
This is different to the full virtualisation setting as there is no double mappings that get applied.
Instead, the guest OS is trusted to only use the MPN's it has been allocated - though this is checked by the hypervisor.

## Reallocating memory

When hosting multiple Guest OS's on one hypervisor, it needs to have a way to reallocate memory when there is contention for resources.
The most obvious way when one OS needs more resources is to take it away from another Guest OS.
However, the hypervisor has no idea what each of the memory is being used for - so it needs some way to signal to each Guest OS that it has more or less memory to use.

### Ballooning

The idea behind ballooning, is to install a device driver on each Guest OS.
This device driver is controlled by the hypervisor and just takes up memory.
When the hypervisor needs to take memory away from the guest OS it tells the balloon driver to increase the amount of memory it is using.
When the hypervisor needs to give memory to the guest OS it can tell the balloon driver to decrease the amount of memory it is using.
The memory the balloon is using can be communicated to the hypervisor which can then reallocate it to other Guest OS's.

Note this will mean the balloon driver's memory should not be allowed to be paged out of memory.
Also, the hypervisor needs to know what memory the balloon driver is using and be able to map that back to MPN.
The hypervisor needs a private channel to each of the balloon drivers.
This strategy can be used in both the full virtualisation and para virtualisation settings.

## Memory Sharing

When running multiple guest OS's on the same hypervisor you may have memory that is identicle in both guest OS's (for example the code of an application running on both OS's).
In this setting, it would be optimal to reuse the same MPN for both VPN.
If the memory is likely to be read only, then it would be safe to do this mapping and save the settings for that memory as COW (Copy On Write).

### Cooperative Sharing

If the guest OS's are aware they are running on a hypervisor, and are cooperative then they can make pages (such as code) that are likely to be duplicated as that.
Then the hypervisor can make decisions about optimally cross mapping these pages.

### Oblivious page sharing

Even if the guest OS's are not cooperative, it is still possible to do page sharing.
Whenever a guest OS allocates a new page, we can use a hash map on the content of the page for a quick lookup.
Then whenever a new page gets allocated we can check it against the hash map to see if there are any other pages 'likely' to be duplications of it.
If there are, we can perform a bit by bit comparison to check if they are identical.
If they are we can allocate them the same MPN and set the page to COW.

To make this work, the hypervisor needs to store a new data structure containing the hash and number of references to each MPN.
Whilst it might be non-optimal to do this at write time - this checking can be ran as a background operation of the hypervisor to optimise memory over time.
This technique can be done on both fully virtualised and para virtualised systems.

## Memory Policies

In a commercial setting there are two policies when it comes to memory allocation.

- Pure share based: You may for exactly the memory you get, and you get allocated exactly that.

- Working-set based: You pay for the working set of your applications.

Both these extremes have downsides and upsides, however a hybrid approach is often adopted.
In this you claim an amount of memory but for the unused memory only a certain percentage is guaranteed to be reserved, the rest will be freed up for other machines.

# CPU Virtualisation

When virtualising a CPU you need to give the Guest OS the illusion they are in full control of the CPU's.
This not only involves allocating CPU's to the guest OS's but handling discontinuities arising from interruptions.
For simplicity, we assume there is only one CPU core.
(Note: This is particularly important in commercial settings where you need to bill guest OS's for the time they are running on the CPU.)

## Proportional Share Scheduling

The idea behind proportional share scheduling is to give each guest OS a weight.
Then when scheduling the CPU, you allocate time slices to each guest OS proportional to their weight.
There are different implementations of this such as Lottery Scheduling, or Stride Scheduling.
These take a random or deterministic approach to the same idea.

## Delivering events

When a process is running for a particular Guest OS, there are certain operations which will cause an interrupt:

- The process makes a system call,

- The process triggers a page fault,

- The process raises an exception, or

- There is an external interrupt that is raised.

The issue with all of these is the process is running on the hypervisor at hardware speeds.
Therefore any event needs to be passed from the hypervisor into the guest OS.
These will all need to be delivered as software interrupts to the guest OS.

## Historic note: Geust OS -> Hypervisor

For fully virtualised systems, old version of the x86 architecture has some system calls that would fail silently.
Whilst most of these would raise a trap to the hypervisor, these few set of operations would not.
The only way to fix this was to scan the OS binary for these operations and patch them to raise a trap instead.
This has been fixed in the latest version of the x86 architecture.
This was only an issue in fully virtualised systems as para virtualised systems would use special hypercalls to make these operations instead.

# Device Virtualisation

When running a hypervisor you need for the guest OS's to think they have fully control of the devices on the system.

## Full Virtualisation

In full virtualisation you have to use the 'trap and emulate' technique.
This means each time a guest OS tries to access a device, it will raise a trap to the hypervisor.
It is then the hypervisors job to emulate the system call it thought it was carrying out.
The hypervisor can hand back control to the guest OS using software interrupts.

For data transfer between the guest OS and hypervisor, this is explicit.
As the guest OS thinks it is in full control, the hypervisor must first take ownership of the data before passing it to or from the guest OS.
This has the overhead of copying the data between the guest OS and hypervisor.

## Para Virtualisation

In para virtualisation, the set of devices that the Guest OS can access is exactly the set of devices that the hypervisor has.
The hypervisor can pass events from the device to the guest OS's using software interrupts.
As well as the hypervisor can manage access to the devices in a much more fine grained way as the guest OS will call the hypervisor through a particular API.
This enables the hypervisor to manage shared buffers between the device and guest OS's which saves on copy data between processes.
One additional benefit of using hypercalls is the guest OS has control of when event notifications should be delivered to the guest OS.

Within Xen, it uses a data structure called an Async I/O ring to manage the data buffers between the guest OS and hypervisor.
This consists of a set of descriptors which point to the data buffers, indexed in a circular queue.
Both the hypervisor and the guest OS can read and write to these descriptors.
Then there are two sets of pointers within this ring data structure:

- The request set, where the guest OS puts new requests at the 'head' pointer and the hypervisor read requests using the 'tail' pointer.

- The response set, where the hypervisor puts new responses at the 'head' pointer and the guest OS read responses using the 'tail' pointer.

The requests and responses are identified with an ID which allows the guest OS and hypervisor to link requests and responses.
Note that as these are just descriptors they lead to a page of machine memory.
This enables a data transfer without excessive copying of data, it goes straight from the device into machine memory and is read from there.
To ensure smooth operation, the hypervisor pins the pages of machine memory to make sure it can always write them directly into memory.

Some examples of this are:

- Network transfer: For communication with a NIC, the hypervisor reserves two rings: one for packets out, and the others for packets in.

- Disk I/O: Disk operations, it reserves one ring for each guest OS.
This enables requests to be reordered for competing domains (i.e. two guest OS's requesting pages at the same time).
However, this can be limited by the use of a Reorder barrier if the OS requests need to happen in a fixed order.

# Concluding remarks

For commercialisation, with all these operations measuring resource usage is very important to give fair billing to customers.

The preferences for a virtualisation platform are for protection and flexibility at the expense of usually performance.
Customers need to be sure that their applications are safe from other OS's and can dynamically scale the resources they need.
