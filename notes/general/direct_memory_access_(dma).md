---
aliases:
  - DMA
  - direct memory access
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
title: Direct memory access (DMA)
tags:
  - OS
  - computer-science
type: definition
---
>[!tldr] Direct memory access (DMA)
>Direct memory access instead of [Programmed IO (PIO)](programmed_io_(pio).md) uses a DMA controller to write data into and out of devices. Whilst the [CPU](central_processing_unit_(cpu).md) still directly accesses the status and command registers.
>![Dma Device](../../images/dma_device.png)
>To utilize the DMA controller the [CPU](central_processing_unit_(cpu).md) needs to configure it - which is not a small operation. Therefore for small data transfers it is not worth the operation. Another restriction is that the message to be used by the DMA controller needs to be kept in physical memory whilst the transfer happens.

