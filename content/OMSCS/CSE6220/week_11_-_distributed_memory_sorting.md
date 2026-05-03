---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-04-07'
date_checked: '2026-04-07'
draft: false
last_edited: '2026-04-07'
tags:
  - OMSCS
title: Week 11 - Distributed memory sorting
type: lecture
week: 11
---

In this lecture, we will see different approaches to sorting on a distributed memory system.

# Bitonic Sort

As a reminder on Bitonic sort review [Comparison based sorting](./week_4_-_comparison-based_sorting.md).

## Bitonic Merge

Bitonic sort is essentially iterative stages of performing a Bitonic merge on incrementally larger input sequences, therefore we first look at the bitonic merge.
Throughout suppose we have $n$ and $p$ both powers of 2 where $p \vert n$.
Therefore each node will start with $n/p$ elements of the list.

We can arrange elements in different ways; we could simply assign elements in order by machine so machine $k$ gets elements $[k*n/p, (k+1)*n/p)$.

![Simple split](../../../static/images/simple_bitonic_split.png)

Otherwise we could use a cyclic fashion where node $k$ gets elements $k + i*p$ for $i \in [0, n/p)$.

![Cyclic split](../../../static/images/cyclic_bitonic_split.png)

In either case we have $\log(p)$ rounds where a node is comparing elements between another node and $\log(n/p)$ rounds where it is comparing elements on its node.
For the simple split the between node rounds come first whereas for the cyclic split the between node rounds come last.
As we communicate with nodes that are always a power of 2 away, this communication can be done in an uncongested manner on a hypercube. However, there are networks optimised for this called butterfly networks.
Let's assume from this point on we are in one of these networks.

> [!note] Butterfly Networks
> Butterfly networks are also used within the Fast Fourier Transform (FFT) algorithm.
> In fact the techniques here can be used to parallelise FFT.

In the $\alpha-\beta$ cost model for communication we get the following costs.
First we have already established we only need to communicate with $\log(p)$ other nodes so we have $\log(p)\alpha$ cost.
Each communication we need to exchange all data on the node, that is $n/p$, giving us a $\log(p)n/p \beta$ term.
Making the total communication cost to be:
$$
\log(p)\alpha + \log(p)n/p \beta
$$

## Transpose trick

In the scheme above we might be worried about the $\beta$ term as this doesn't scale well as we increase $p$ and therefore may dominate the costs.
However, we may be able to reduce the $\beta$ term by increasing the $\alpha$ to make a more level cost.
To do this notice that the cyclic scheme above does no communication between nodes for the first $\log(n/p)$ rounds, whereas in the simple split the last $\log(n/p)$ rounds have no communication.
So if we could go between these two schemes at a switch over point we could reduce the amount of data being communicated at the pay off for having to move all the data.

![Transpose bitonic merge](../../../static/images/transpose_bitonic_merge.png)

> [!warning] Simplified idea
> Note that the picture only works when $n = p^2$; however, we can generalise this with other schemes to 'patch' over the gaps so we always go between schemes which only need to communicate within nodes.

To calculate the communication costs of the transpose where every node needs to send to every other node a $1/p$'th of its data, that is $n/p^2$.
We get the following costs:
$$
\alpha (p-1) + \beta \frac{n (p-1)}{p^2}
$$
This means we have a slightly larger $\alpha$ term for a reduced $\beta$.

In practical applications, the transpose scheme always performs better than sticking with a simple network.

## Bitonic Sort

Bitonic sort consists of $\log(n)$ stages of bitonic merges.
In stage $1 \leq i \leq \log(n)$ the merges have size $2^i$ of which there are $n/2^i$ merges in that stage.

![Bitonic sort stages](../../../static/images/bitonic_sort_stages.png)

(Note: The negative merges just use less than comparisons instead of greater than comparison - giving us bitonic subsequence at each sub-stage.)

Now let's try to compute the running time of the algorithm when we partition it across $p$ processors.
A single element at the $i$-th stage has $i$ comparisons done to it.
So on a single processor of $n/p$ elements it has $n \cdot i/p$ comparisons done to it.
Then supposing a $\tau$ operation cost we get the compute cost of Bitonic sort to be:

$$
T_{comp}(n,p) = \tau \sum_{i=1}^{\log(n)} ni/p = O(\tau \frac{n \log^2(n)}{p})
$$

This matches the run time of Bitonic sort $n \log^2(n)$ but perfectly scales with $p$.

Next the communication cost of the algorithm.
Let's assume a simple split scheme like above.

![Simple split communication cost](../../../static/images/bitonic_sort_communication.png)

Then we only require communication when on stage $i > \log(n/p)$.
In stage $i$ there are only $p_i = 2^{i - \log(n/p)}$ processes communicating.
Therefore the total communication cost for a single process is:

$$
T_{comm}(n,p) = \sum_{k=\log(n/p) + 1}^{\log(n)} T^{merge}_{comm}(2^k, 2^{k -\log(n/p)}) = \alpha \log(p) + \beta \frac{n}{p} \log^2(p)
$$

# Bucket sort

You can read about the implementation of bucket sort [here](../../../notes/bucket_sort.md).
It feels like a good candidate for parallelisation as there are already $k$ separate buckets which could be separate machines.

So let's distribute bucket sort across $p = k$ machines.
This means each machine starts with $n/p$ elements it needs to sort.
The first stage is to work out what numbers belong on each machine.
In a traditional bucket sort we would split the interval into $k$ even sized buckets - however this can lead to 'lumpy' buckets of uneven sizes leading to worse splits.
Therefore each bucket should locally sort their elements and sample $p-1$ elements evenly spaced in their selection of elements.
Then each bucket sends their selection to a 'root bucket' who then performs this operation again on all the samples.
These samples provide the dividing lines between different nodes.
Then we just perform bucket sort.

```pseudocode
// Input:
//   elements: array of elements to sort for this node
//   rank: rank of this node
//   root: rank of the root node
//   p: number of nodes
// Output:
//   A array of sorted elements for this nodes region.
bucket_sort(elements[1:n/p], rank, root, p):
  local_sort(elements[1:n/p])

  // Root node chooses dividing lines between nodes
  if rank == root:
    samples = 2d array of side p, p-1
    // Get the p-1 samples evenly spaced throughout the local elements
    samples[rank][1:p-1] = elements[n/(2p(p-1)) : n/p - n/(2p(p-1)) : n/(p(p-1))]
    for i in [1, p] \ root:
      async_recv(samples[i], i, p-1)
    wait(*)
    sorted_samples = local_sort(flatten(samples))
    // Get the p-1 samples from the samples from all the nodes.
    dividing_lines = sorted_samples[p/2 : p*p - p/2 : p]
    for i in [1, p] \ root:
      async_send(dividing_lines[i], i, p-1)
    wait(*)

  // Non-root nodes send their samples and get the dividing lines
  else:
    samples = elements[n/(2p(p-1)) : n/p - n/(2p(p-1)) : n/(p(p-1))]
    async_send(samples, root, p-1)
    dividing_lines = array of size p-1
    async_recv(dividing_lines, root, p-1)
    wait(*)

  // Send local samples to correct node
  node_elements = 2d array of size p, n/p (can get a better bound)
  for i in [1, p] \ rank:
    async_recv(node_samples[i], i, *)
  current_samples = {}
  current_node = 1
  for element in elements:
    if current_node == p or element < dividing_lines[current_node]:
      current_samples.append(element)
    else:
      if current_node != rank:
        async_send(current_samples, current_node, p-1)
      else:
        node_elements[rank] = current_samples
      current_samples = {element}
      current_node += 1
  if p != rank:
    async_send(current_samples, current_node, p-1)
  else:
    node_elements[rank] = current_samples

  // Sort local samples
  sorted_node_elements = local_sort(flatten(node_elements))
  return sorted_node_elements
```

Here the time taken is dominated by the root node so let's analyse the runtime for its perspective.
Let's also make the assumption that nodes end up with roughly $n/p$ elements to sort each after the whole splitting process.
Then the root node needs to locally sort 2 lists of $n/p$ elements and 1 list of $p(p-1)$ elements.
Then lastly search through in order a list of $n/p$ elements to divide up the list.
Computationally this takes:

$$
T_{comp}(n,p) = \tau \left( 2 \frac{n}{p}\log\left(\frac{n}{p}\right) + p(p-1) \log(p(p-1)) + n/p \right) = O\left(\tau \left( \frac{n}{p}\log\left(\frac{n}{p}\right) + p^2 \log(p) \right) \right)
$$

Communication costs there are 3 major ones:

- Everyone sending the root node p-1 samples.

- The root node sending everyone p-1 dividing lines.

- Everyone sending to everyone else $n/p^2$ elements (another assumption).

Assuming we are on a fully connected network this costs us:

$$
T_{comm}(n,p) = \alpha 3 (p-1) + \beta (2(p-1)^2 + n(p-1)/p^2)
$$

In sequential bucket sort, achieving near-linear time requires $k = \Theta(n)$ buckets.
However, in the parallel version analyzed above, setting $p = \Theta(n)$ processors creates a scalability problem: the root node's computation grows like $p^2\log(p)$ and communication costs grow like $p^2$.
This means the root becomes a bottleneck when $p$ is large.

In practice, parallel bucket sort remains highly effective because:

- The number of processors $p$ is typically much smaller than $n$ (often $p = O(\sqrt{n})$ or less), avoiding the quadratic root bottleneck.

- The constant factors are favorable compared to other parallel sorting algorithms.

- Implementations can use variations like hierarchical sampling or distributed root selection to reduce the bottleneck.

Despite the theoretical concerns, bucket sort (and its variant sample sort) is the most commonly used technique in parallel sorting competitions!
