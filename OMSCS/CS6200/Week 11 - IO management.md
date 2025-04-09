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

