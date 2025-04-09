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

