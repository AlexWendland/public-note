---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-11-20
last_edited: 2025-11-20
draft: true
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - Internet Computing

Normally web based issues are called 'embarrassingly parallel'.

> [!definition] Embarrassingly parallel
> These problems can be broken down into easy to do parallel operations, such as accessing email, doing a web search, or downloading files.
> No two clients rely on each other so all computation can be broken down on the per user level.

## Issues in giant scale systems

The structure of giant scale internet services normally follows the below pattern:

- Clients on the outside of the network.

- You come through some IP network.

- There is some load manager moving load between different back end servers.

- Back end servers, often on the order of 100 to 1000 servers

![Giant Scale System Structure](../../images/giant_scale_systems_structure.png)

With running one of these services, you need to know how to handle server failures - as in this case it is when rather than if one happens.

### Sense of scale

As of 2000:

| Service               | Nodes   | Queries    | CPUs/Node |
| --------------------- | ------- | ---------- | --------- |
| AOL Web               | > 1,000 | 10B/day    | 4-CPU     |
| Inktomi search engine | > 1,000 | > 80M/day  | 2-CPU     |
| Geocities             | > 300   | 25M/day    | ???       |
| Anon Web-based email  | > 5,000 | 1B/day     | ???       |

There are distinct advantages of structuring a system like this:

- Horizontal scaling: adding more nodes to the system scales it up.
- Cost control: 

### Load manager

There are different strategies we can take for load balancing requests:

- Round robin: Each requests gets sent to a different server to be handled.
This is done at the server level which makes it very efficient.
However, we struggle with handling servers that are down.
This also assume all machines on the network are equal and for the same thing.

- Layer 4 switches (Transport layer): This can inspect who the packet is intended to be for and make decisions on where to send that packet based on that.
For example this allows us to act as a reverse proxy to send packets intended for one application to a specific subset of servers.
This can also hide down servers from the client using a Backplane with the servers it is serving.
This Backplane can also be used for higher level semantics such as sending requests with particular body to different instances - this allows for different nodes to only replicated limited data for their preferred queries.

### DQ Principle

This theory is about matching demand with supply and varying parameters around this.
We start with some definitions:

- Q_0: The total number of queries we need to server in this time step.

- Q_c: The number of queries we handled in this time step.

- Yield: Q = Q_c/ Q_0 \in [0,1] the proportion of the queries we handled in this time step.

- D_f: The full amount of data the system holds to handle this query.

- D_v: The amount of data we use to server requests in this time step.

- Harvest: D = D_v/ D_f \in [0,1] the proportion of the data we used to server requests in this time step.
This is a proxy for how 'well' we handled the request - did we use all possible websites to check against your query or just a limited set of them.

It is assumed for a given set up the product DQ is a constant.
This means that there is a payoff to have if the constant DQ is not 1.
We can either server a limited set of requests at the full quality or we can offer all the queries at a degraded quality.

When thinking about D, what it is in reality depends on how the system is limited.
For example you could be I/O bound, as you simply need to process a lot of data to handle a request.
However, in most giant scale services it is more likely that they are network bound.
This means it is hard to scale up the DQ constant at some points - as getting more network may be out of your control.

There are some metrics people talk about for huge data centers:

- I/O ops per second: How many I/O operations per second the system can handle.

- Mean time to repair: How long does it take for a server to recover after a failure.

- Mean time between failure: How long does it take for a server to go down.

- Uptime: This is defined by MTTR and MTBF as (MTBF - MTTR)/MTBF and expressed as number of 9's so 5 9's is 0.99999 as this ratio.

However, uptime has its limitations.
For example if a failure happens in down time - then no one really cares.

### Replication vs partitioning

Replicating data means we have more servers with each bit of the data.
This makes our systems robust to server failures.
Therefore, when failures occur in a replicated system D remains unchanged but Q goes down.

Partitioning data means we have more servers but they only have access to a subset of the data.
This can be useful if the data itself is too large to be processed on a single machine or we want to keep the cache hot on a particular subset of the data.
Therefore, when a failures occurs in a partitioned system D goes down but Q remains the same.
(In this case, we assume a query still gets served but it does not get the data from the severs that are down.)

NOTE: In both cases, DQ is defined by the number of servers - therefore if we have failures DQ goes down but we get too choose what constant in DQ to reduce.

Exception: If the queries involve 'significant' write traffic then replication is a slower option, due to the need to replicate those writes.
(This is a rare exception.)

### Graceful degradation

When our system is at full saturation system administrators can decide how to degrade their service.
The two options are as expected:

- Keep D fixed and lower Q: Keep the quality of the results the same but lower the number we server.

- Lower F and keep Q fixed: Degrade the quality of results but keep up with demands.

These options practical implementation depends on the service - for example if you are video streaming platform you could either:

- Keep D fixed and lower Q: Keep users in a hold queue until they are able to get their video.

- Lower F and keep Q fixed: Degrade the quality of results but keep up with demands.

### Online evolution and growth

With new releasing getting cut, we need to decide how to release them.
There is a spectrum of options here:

- Fast: Bring down all servers, update them and bring them back up.
(Good option for service with natural down time - such as financial markets or diurnal - sleep times.)

- Rolling: Bring down one server at a time, update it and bring it back up.
(Good for services with high uptime - such as web servers, this is fairly common in industry.)

- Big flip: Bring down half the nodes, then the next half.
(Here half is arbitrary and we can do it in different fractions - essentially this is the middle ground.)

Any strategy will reduce total DQ in the service over time - however different strategies spread this out differently.
It will be very sector dependent what strategy is best and it may change over time.
For example code freezes during busy times to not reduce the total DQ.

## Map Reduce

Computations in internet services are commonly simple but over large data sets.
Map reduce is a framework to handle such computations.
It breaks each computation down into two parts:

- Map: Take some input and produce some key value paired set of outputs.

- Reduce: Take all values associated to the same key and reduce it to a single output value for that key.

These simplistic steps can be parallelised over multiple machines and only require coordination between steps.
This enables the large scale services to work over these computations.

### Example: Counting words

Suppose we want to find the number of occurrences of each word over a large set of documents.
The input is a key value pair being the file name (key) and file content (value).
The output of our application is a key value pair with the key being the word and the value being the number of times it appears in the collection of documents.
For the end user to define this - they just need to provide the map and reduce function.
The framework will handle everything else.

The map function, when ran on a file then goes through the content breaking up the words.
Each time it sees a word it emits a key-value pair, the key will be the word and the value will be 1.
(We could instead implement this counting the number of times the word appears in the file - but this would either take more memory or to parse the content multiple times.)

The reduce function then takes all the key-value pairs for each word and then sums the values of the pairs.
Then it emits a key-value pair being the word and the total times it appears in all collections.

This is all the user needs to provide - however the framework between the map and reduce step aggregates key-value pairs based on the key.
That means whilst multiple map jobs may emit the same word, a single reduce job gets all the emits from all the files for the same word.


### Example: Page links

Part of the page rank algorithm requires we know how many other pages link to a given page.
This has input key-value pairs where the key is the url and the value is the page content.
This expects an key-value pair output of a url and the number of pages that link to it.

The map function takes a url and page content.
It then looks through the page content finding each link within it.
For each link it emits a key-values pair with the url being the key and the value being 1.

The reduce function then takes all the key-value pairs for each url and sums the values.

The advantage of this system is the user just needs to know the business logic of how to find links.
Whereas, as we will see the framework implementer handles all the coordination of the map and reduce steps.

### Why map-reduce?

As we have seen above, map-reduce is sufficiently abstract that we can implement different problems within it.
We also see that the user just needs to know the business logic of the system and the framework handles the rest.
We will see later that this scales very well both in the sense of the query size increasing but also the number of machines available to use.

### Framework

Below is a high level overview of what the framework does for a given execution:

1. Users program spawns a master process to coordinate the work.

2. The master takes the user input and further slits it (optional) this can either be specified by the user or could be automatic like chunking files.

3. The master then allocates these splits to workers.
Likely the number of jobs will exceed the number of workers but then it just iteratively hands out work to the workers.

4. The emits from the maps will be saved to a disk based on the key of the key-value pair.
That way the master knows which files relate to which key.
Once all the maps are completed it can use these key's to start up reduce tasks for each key.
(Normally the number of reducers is specified by the user up front.)

5. Each reduce task hands back its outputs to the master, which can provide these to the user.

![Map Reduce Framework](../../images/map_reduce_framework.png)

### Issues to be handled by the run time.

There is a lot of admin to be handled by the master, this includes:

- Location of the files created by the completed mappers.

- Assignments of mapper/reducer tasks to workers.

- Fault tolerance:

  - If one of the workers bugs or crashes we need to be able to handle this.

  - Slow workers hold up the whole system if for example the reducers are waiting for all the map tasks to finish.
    This can be a cause for serious performance issues, so the master can choose to run multiple jobs for 'straggler' tasks to combat this.

  - The master needs to be able to handle redundant messages for straggler or crashed workers gracefully.

- Locality management: If your workers are on remote nodes, the master needs to make available the files required for map/reduce tasks.

- Task granularity: It might be that we have more tasks than workers, so the master controls how to break up these tasks amongst workers and load balance them correctly.
  Users can also aggregate outputs from map if the so choose - to make similar keys get processed by the same reduce task.

## CDN


