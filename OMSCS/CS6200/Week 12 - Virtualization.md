---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-04-12
last_edited: 2025-04-12
publish: false
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Virtualization

## Additional reading

- ["Formal Requirements for Virtualizable Third Generation Architectures"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-popek-goldberg-paper.pdf)

## Virtualization

![[Virtualization]]

![[Virtual machine monitor (VMM)]]

Benefits for vitualisation:
- *Consolidation*: Allows you to split one machine into many, allowing you to consolidate different applications that need different environments to run.
- *Migration*: Makes it easy to move applications from one machine to another.
- *Security*: Isolates applications from one another.
- *Debugging*: Makes it easy to spin up similar instances of crashed programs to debug.
- *Support for legacy OS*: Easy to host an application that needs a legacy operating system to run.
- *Support for OS research*: Makes it easy to change an operating system and observe the effects of that.

There are two main methods of virtualization: 
- *Bare-metal*: This is where a [[Virtual machine monitor (VMM)|hypervisor]] is installed on top of the hardware.
- *Hosted*: This is where the [[Virtual machine monitor (VMM)|hypervisor]] is installed on top of another [[Operating system (OS)|OS]].

## Bare-metal

In this model the [[Virtual machine monitor (VMM)|hypervisor]] is in direct control of the hardware. The main difficulty of the model is integrating different devices - as device manufacturers would need to write a device driver for the hypervisor also. The way most [[Virtual machine monitor (VMM)|hypervisors]] get around this is by hosting a privileged VM that integrates with devices. This also runs other management tasks. 

![[bare-metal.png]]

There are two main hypervisor producers:
- Xen (open source or Citrix):
	- This uses a privilaged VM.
- ESX (VMware):
	- Largest market share.
	- Can force server device manufacturers to release drivers.
	- Controlled using APIs

## Hosted

In the hosted model the [[Virtual machine monitor (VMM)|VMM]] runs as  module on a host [[Operating system (OS)|OS]]. This module provides hardware interfaces to VM's and deals with VM context switching. The advantage of this mode is you can utilize all the components of the host VM making the [[Virtual machine monitor (VMM)|VMM]] smaller in size. 

![[hosted_virtualization.png]]

Examples:
- Kernel-based VM (KVM) which is linux based.
	- Uses an [[Operating system (OS)|OS]] module on the host and a QEMU for hard ware virtualization in the VM.
	- Leverages the linux open source community.

## Hardware protection levels

