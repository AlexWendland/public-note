---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-04-09
last_edited: 2025-04-09
publish: true
tags:
  - OMSCS
type: lecture
week: 11
---
# Week 11 - IO management

## Model of a [[Input output (IO)|IO device]]

Whilst an [[Input output (IO)|IO]] device can come in many forms we model them similarly.

![[IO device.png]]

These have 3 registers:
- Status: Some indicate the state of the device.
- Command: Used by the [[Central processing unit (CPU)|CPU]] to control the device.
- Data: Used to transfer data in and out of the device.

 Then what happens internally is controlled by the micro controller on the device. 

## Connections to the [[Central processing unit (CPU)|CPU]]

Devices are mainly connected to the [[Central processing unit (CPU)|CPU]] through the [[Peripheral component interconnect (PCI)]] or [[PCI Express (PCIe)]]. Though depending on the component it may be connected to that via another bus as well.

![[inter_connect_to_cpu.png]]

## Device driver

![[Device driver]]

![[device_drivers.png]]

Devices fall into one of 3 types:
- *Block device*: Read/writes blocks of data and offers an API to access a block at a particular index. E.g. Hard drive
- *Character device*: Offers an API that gets or puts a single character. e.g. keyboard.
- *Network device*: These offer ability to put or get data but no direct access to blocks of indexed data. E.g. [[Network Interface Card (NIC)|NIC]]

All these devices are represented as a special type of file. In linux these can be accessed in the `/dev` directory and are stored in a different file system `tempfs` or `devfs`.

![[Pseudo devices]]

There are two methods in which the [[Central processing unit (CPU)|CPU]] communicates with devices.

- *Memory-mapped I/O*: On boot some part of the main memory address space is registered for use by a device. The [[Central processing unit (CPU)|CPU]] can then write or read to these addresses to interact with the device.
- *Port-mapped I/O*: On boot they get loaded into a separate address space reserved for I/O devices. This uses separate instructions such as IN/OUT. This was more common in legacy systems.

Some architectures do support both. 

There are two ways for the device to communicate with the [[Central processing unit (CPU)|CPU]]:

- *Interrupts*: The device can generate interrupts that the [[Operating system (OS)|OS]] will need to handle. This gives the device the best access to the [[Operating system (OS)|OS]] but can be inefficient in terms of caching if the input is not needed.
- *Polling*: The [[Central processing unit (CPU)|CPU]] can poll the device for information by checking its status registers. This means the [[Central processing unit (CPU)|CPU]] can only get the information when it needs it - however it can generate delay or overhead if the [[Central processing unit (CPU)|CPU]] needs to repeatedly poll the device.

![[Programmed IO (PIO)]]

![[Direct memory access (DMA)|direct memory access]]

## Device access

Device access is an intensive action as we need to parse through many different layers and processes. Thus why [[Input output (IO)|IO]] is considered slow.

![[IO_access.png]]

Some devices support [[Operating system (OS)|OS]] bypass. This is where the [[Operating system (OS)|OS]] configures the device and the process to communicate directly through the [[Process|processes]] virtual address space with limited functionality. Though the device has some requirements for this:

- The device producer must offer a user-level library to enable this.
- The device must have sufficient registers for the process to have access but also for the [[Operating system (OS)|OS]] to have more fine-grained control over the device.
- If the device supports multiple accesses then it must be sufficiently complex to deduplex the requests and send them to the correct device (i.e. looking at [[Port|port]] numbers).

However, if the device does support this it can increase access speed dramatically.

When accessing [[Input output (IO)|IO]] devices this can either happen synchronously or [[Asynchronous programming|async]]. Normally when issuing commands to a device the process needs to wait for a response from the device. This can either block the process and it gets moved to a wait queue or in a non-blocking way. When using async the process can either poll or get interrupted to get output from the device. 

![[async_vs_sync_device_access.png]]

## Block device access

When interacting with block devices, user programs actually interact with files that are on the computers filesystem. Files are considered one 'logical' storage unit. The [[Operating system (OS)|OS]] will specify how to support writing to files through an API - normally the [[Portable operating system interface (POSIX)|POSIX]] API.

![[block_device_stack.png]]

As well as having a device driver for particular devices a further abstraction is placed on top of these to standardize the interaction - this is the generic block layer. This is an [[Operating system (OS)|OS]] standard for interfacing with different block devices.

## Virtual file system

The [[Operating system (OS)|OS]] abstracts the concepts of block devices away from the user through a virtual file system. It uses this to combine potentially different types of block devices into one directory structure which is easy for humans to grasp.

![[virtual_file_system.png]]

As well as making this easy for human to use - it also offers an API the block device device drivers must conform to.

This virtual file system supports a number of abstractions:

- *File*: The basic elements on which the virtual file system operates.
- *File descriptor*: An [[Operating system (OS)|OS]] representation of a file the supports standard operations like, read, write, lock, close ....
- *inode*: A persistent on block device representation of a file (Index node). This lists all the data blocks that make up this file as well as metadata such as device, permissions, size ....
- 