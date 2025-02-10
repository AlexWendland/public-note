---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-02-10
last_edited: 2025-02-10
publish: true
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Thread Performance Considerations

## Additional reading

- [Flash: an efficient portable web-server](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-pai-paper.pdf)

## Choosing a threading model

![[threading_comparison.png]]

When choosing a model for threading it is important to pick the metric you care about before deciding on implementation. In the example above the server would prefer the pipeline as it is cheaper in terms of CPU time whereas for clients they would prefer the boss-worker model as it reduced average order time completion.

### Metric

A metric is a measurement standard. I needs to be a measurable and quantifiable property of the system we are interested in that can be used to evaluate the system behavior. 

Some examples are:
- Execution time: The amount of time it takes to complete a job.
- Throughput: The amount of jobs completed per unit of time. This measures the actual work done.
- Request rate: The amount of requests received per unit of time. This represents how many requests the system can accept but not necessarily complete. 
- Resource utilization: How much of the CPU time is idling or memory used, ect.
- Wait time: The average amount of time spent waiting to start a request.
- Platform efficiency: How well I can utilize the resources within my platform. 
- Performance / currency spent: This is useful when comparing different hardware choices for a data center.
- Performance / Watts: This is useful when considering environmental impacts of your operation.
- Percentage of SLA violations: The amount of requests that violate your service level agreement with your users.
- Client perceived performance: For example with videos human can't see more than 30 frames per second - therefore maintaining it at that would give a good client perceived performance. More frames per second than that will not increase their perception of performance.
- Aggregate performance: Normally you care about balancing off different factors against one another so taking an average is useful here.

To evaluate impacts of changes on our metrics we build a test bed to see the impact of changes we are making:
- Real experiments with real payload.
- Toy experiments with mocked payload.
- Simulations.

![[are_threads_useful.png]]

## Simple web server comparison

In the rest of this lecture we are comparing different implementations for a web-server to see the pros and cons of each.

![[simple_web_server.png]]

The steps within a file server have different needs - some may be CPU bound such as parsing headers, others may be i/O bound like reading a file. 

### Multi-processing

We implement this by simply take a working single process single threaded implementation for the webserver. Then spin up multiple processes for this. This has the following payoffs:
- Simple in terms of coding.
- High overheads to context switch.
- High memory usage for different [[Process control block (PCB)|PCB]].
- Complicated to make is share resources like a bound port, or file handlers. 

### Simple multi-threading approach

We implement this similarly to the multi-process approach. With one thread handling the whole request start to finish. This has the following payoffs:
- Cheaper context switching due to shared state and address space.
- Not as simple implementation as it requires synchronization.
- Library will need to support threads (not an issue in modern platforms).

### Event driven model

In this model we will use an event-bus to determine what our machine needs to do. This will then switch to the appropriate action associated to that message. Operations will be non-blocking for I/O events. This will be running on a single process with a single thread.

![[event_driven_model.png]]

This can be spun out to support multiple CPU's but it adds complexity to ensure each CPU only gets the correct tasks. However, for this analysis we will not consider this.

This model has some payoffs also:
- More complicated to program as you need to use non-blocking I/O calls.
- More efficient as you do not waste any time on context switching.

