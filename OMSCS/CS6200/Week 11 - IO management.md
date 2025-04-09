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

