---
aliases:
  - DMA
  - direct memory access
created: 2024-08-26
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
  - computer-science
title: Direct memory access (DMA)
type: definition
---
> [!definition] Direct memory access (DMA)
> Direct memory access instead of [Programmed IO (PIO)](programmed_io_(pio).md) uses a DMA controller to write data to and from devices. The [CPU](central_processing_unit_(cpu).md) still directly accesses the status and command registers.
> ![Dma Device](../../static/images/dma_device.png)
> To utilise the DMA controller, the [CPU](central_processing_unit_(cpu).md) needs to configure it—which is not a small operation. Therefore, for small data transfers, it is not worth the overhead. Another restriction is that the data to be used by the DMA controller needs to be kept in physical memory while the transfer happens.

