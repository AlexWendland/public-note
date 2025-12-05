---
aliases:
checked: false
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-04-13
draft: false
last_edited: 2025-04-13
tags:
  - OMSCS
title: Week 16 - Datacenter technologies
type: lecture
week: 16
---
# Week 16 - Data-center technologies

## Internet services

A internet service is simply one offered over a web interface. These normally consist of 3 layers:

- Presentation: Static content.
- Business logic: Dynamic content.
- Database tier: Data storage.

Whilst these layers are separated here they may be implemented on the same machine. Middleware can be offered to integrate the different layers together.

These different layers contact one another using [IPC](../../notes/inter-process_communication_(ipc).md) methods such as [RPC](../../notes/remote_procedure_calls_(prc).md) or shared memory (if they are located on the same machine).

To handle scale internet services are normally distributed across multi-process or multi-node "scale-out" architecture. This normally consists of a load-balancer that distributes load within the cluster. This follows the Boss-worker pattern where the workers could be:

- *Functionally homogeneous*: All workers are equal and the load-balancer round robins between them.
- *Functionally heterogeneous*: Nodes execute different tasks required for the internet service.

## Homogeneous architecture

These are ones where the workers are all equal. This enables a very simple load-balancer that does not need to keep much state about the different workers. It is very simple to scale up as you just add more of the same workers. However, this suffers from the workers not being able to utilize caching and if you need to process large amounts of data for each request - this can become slow.

![Homogeneous Architectures](../../../static/images/homogeneous_architectures.png)

## Heterogeneous architecture

These are ones where the workers are specialized to some kind of logic. This means each worker can optimism its cache or use devices that are specialized for that task.

However, this adds considerable complexity to the front-end. As workers now are different the load balancer needs to keep track of which workers can do what. When increased demand comes to the system scaling up is not as simple as adding more workers you need to work out what workers are needed.

![Hetrogeneous Architectures](../../../static/images/hetrogeneous_architectures.png)

## Cloud computing

Before cloud computing, companies would host their own infrastructure. This would involve physically buying machines and forecasting demand. Your goal would always be to have enough capacity for the peak usage. Though if you get this wrong you lose potential sales.

![On Premise Compute](../../../static/images/on_premise_compute.png)

As well as the potential risk, this also required a lot of expertise on running machines and managing a data center.

Instead the goal of cloud computing was to outsource this to someone who has much more compute and you can only request the amount of compute you need at any given time.

![Cloud Compute](../../../static/images/cloud_compute.png)

This allows for:

- Capacity that scales elastically with demand,
- Cost is proportional to demand/revenue,
- All of this happens automatically with no need for forecasting, and
- You can access the compute anytime and anywhere.

Though you will not own this compute.

The requirements to offer this kind of service are:

- On-demand, elastic resources and services.
	- Can either be through physical hardware rental or software/services based (e.g. AWS).
- Fine-grained pricing based on usage.
	- There has been a proliferation of different accounting models.
	- Usually practically discrete based on compute/resource size.
- Professionally managed and hosted compute.
	- Managed by the cloud provider.
	- Users don't need to think about physically where is their server or if it is being cooled sufficiently.
- API-based access.
	- Either web-based, open source libraries or command line utilities
- Scale
	- The business model is structured around scale, they must be able to manage the resource at large scale.
	- Dealing with hardware/software failures. As you own more stuff - more stuff breaks.
- Multi-tenancy:
	- You have to be able to support multiple users and keep them isolated from one another.

This is an economically viable model for cloud providers due to two main factors:

- [Law of large numbers](../../notes/law_of_large_numbers.md): With sufficiently many independent users the peaks in usage should average out to a fairly constant load.
- Economy of scale: Unit cost of providing resources or service drops at bulk.

The system as it is today was first though up by John McCarthy in 1961

>[!quote] John McCarthy, MIT Centennial, 1961
>If computers of the kind I have advocated become the computers of the future, then computing may some day be organised as a public utility ... The compute utility could become the basis of a new and important industry.

The goal was compute to be completely fungible. It would not matter what CPU you are using you just need the compute done. However we are currently far away from that with issues like API lock-in, hardware dependency, latency, privacy, ...

## Cloud deployment models

Cloud deployments can be for different purposes. This starts with who can use it:

- *Public*: Anyone with a credit card can use the cloud.
- *Private*: Access is limited to a company or organisation.
- *Hybrid*: This is a private cloud that utilities some functions of a public cloud for failover, handling spikes, or testing.
- *Community*: A public cloud where it is restricted to a particular type of user.

As well as the users they serve the level of autonomy they offer is a large differential.

![Cloud Models](../../../static/images/cloud_models.png)

## Cloud enabling technologies

To set up a cloud, there are some foundational technologies that have to be used:

- [Virtualization](../../notes/virtualization.md)
- Resource provisioning (scheduling)
- Big data processing (Hadoop map reduce, Spark)
- Storage:
	- Distributed file system,
	- No SQL,
	- Distributed memory
- Software defined resources such as networking, storage, ...
- Monitoring, real time monitoring and log processing to keep visibility over the whole system.

## Big data

Given the access to resources, the cloud has enabled the proliferation of 'big data' technologies. To act as a platform for big data cloud needs to offer:

- Data storage layer,
- Data processing layer,
- Caching layer,
- Language front-ends,
- Analytics libraries, and
- Continuous streaming data.

Some examples of these stacks are provided below.

![Hadoop Stack](../../../static/images/hadoop_stack.png)

![Bdas](../../../static/images/bdas.png)
