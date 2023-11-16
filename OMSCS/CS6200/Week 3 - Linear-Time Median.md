---
aliases: []
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-09-07
last_edited: 2023-11-11
publish: true
tags:
  - OMSCS
type: lecture
week: '3'
---
# Week 3 - Linear-Time Median

> [!tldr] Median list problem
> Given an unsorted list $A = [a_1, \ldots, a_n]$ of $n$ numbers - you want to find the [[Median|median]] ($\lceil \frac{n}{2} \rceil$) element.

> [!Note] Not usual [[Median]] definition
> This isn't the usual definition of median, which in the case of odd $n$ would return the mean of the $\lceil \frac{n}{2} \rceil$ and $\lfloor \frac{n}{2} \rfloor$ elements.

Though we can solve a more generic problem.

> [!tldr] $k$th smallest element
> Given an unsorted list $A = [a_1, \ldots, a_n]$ of $n$ numbers - you want to find the $k$'th smallest element.

## Using [[Merge sort]]

A basic algorithm would be to use [[Merge sort]] on $A$ then output the $k$-th element of that list which would take $O(n\log(n))$. Though is it possible to do this without sorting $A$?

## Using [[Divide and conquer algorithms|divide and conquer]] better

>[!Note] [[Quick sort]]
>We are going to use ideas from [[Quick sort|quick sort]] algorithm.

The basic idea is summed up in following [[Pseudocode|pseudocode]]

```pseudo
Select(A, k):
1. Choose a piviot p.
2. Partition A into A_{<p}, A_{=p}, and A_{>p}.
3. If k <= |A_{<p}| then return Select(A_{<p}, k)
4. If |A_{<p}| < k <= |A_{<p}| + |A_{=p}| then retrun p.
5. Otherwise return Select(A_{>p}, k - (|A_{<p}| + |A_{=p}|))
```

Though we have skipped how we choose a pivot. We need that pivot is close to the median to get a good running time. Lets assume the running time of this algorithm is $T(n)$ for input of size $n$.

## Choosing the pivot

We say a pivot is good if
$$\vert A_{<p}\vert \leq \frac{3n}{4}, \mbox{ and } \vert A_{>p} \vert \leq \frac{3n}{4}.$$
We want to find such a $p$ in $O(n)$ time. This will give us
$$ T(n) = T(\frac{3n}{4}) + O(n),$$
which by [[Masters theorem]] gives $T(n) = \Theta(n)$.

### Random pivot

If I choose any random element $p \in A$ then it has
$$\mathbb{P}(p \mbox{ is good}) = \frac{3n/4 - n/4}{n} = \frac{1}{2}$$
It takes $O(n)$ time to check if $p$ is good and if we kept randomly drawing elements we have
$$\mathbb{E}(\mbox{draws untill } p \mbox{ is good}) = 2.$$
Therefore this algorithm has expected runtime of $2n$ - though this is not [[Big-O notation|worst case run time]].

### Recursive pivot

Instead of finding a median of $A$ we could instead aim for a median of a "representative sample".

> [!info] Trick
> Divide $A$ into sets of 5 and find the median of each of these sets. Call this set $S$. Then find the median of the set $S$.

Let $G_i$ be the sets of size $5$ and $1 \leq i \leq \frac{n}{5}$ (assume $n$ is a multiple of $5$). Then the median $m_i$ of $G_i$ each have 2 elements less than $m_i$ and 2 elements greater than $m_i$. Therefore the median of $S = \left \{m_i \vert 1 \leq i \leq \frac{n}{5} \right \}$  $p$ has $\frac{3n}{10}$ less than or equal to it and $\frac{3n}{10}$ elements greater or equal to it.

Which gives $\vert A_{>p} \vert \leq \frac{7n}{10}$ and $\vert A_{<p} \vert \leq \frac{7n}{10}$. This gives that $p$ is a good pivot from the definition.

```pseudocode
FastSelect(A,k):
1. Break A into ceiling of n/5 groups, G_i with atmost 5 elements in.
2. For i = 1 -> n/5 sort G_i and let m_i = median(G_i)
3. Let S = {m_1, ..., m_{n/5}}
4. Let p = FastSelect(S,n/10)
5. Partition A into A_{<p}, A_{=p}, A_{>p}.
6. Return based on the following conditions.
	1. If k <= |A_{<p}| then return FastSelect(A_{<p}, k)
	2. If k > |A_{<p}| + |A_{=p}| then return
	   FastSelect(A_{>p}, k - |A_{<p}| + |A_{=p}|)
	3. Else return p.
```

Breaking $A$ into groups requires one sweep through $A$ so that takes us $O(n)$ time.

Sorting a single $G_i$ takes $s$ where $s$ is the constant runtime of your favourite sorting algorithm on 5 elements.

We run this sort on $n/5$ elements giving step 2 takes $O(n)$ time.

We then run our algorithm on a subproblem of size $\frac{n}{5}$ having run time $T\left ( \frac{n}{5}\right )$.

> [!note] Pivot runtime
> So finding this pivot takes $T\left ( \frac{n}{5}\right ) + O(n)$ time.

Partitioning the set takes $O(n)$ time.

The last step of the algorithm takes at most $T\left (\frac{3n}{4}\right ) + O(1)$ from the assumption about the good pivot.

Combining this all together we have
$$T(n) = T\left (\frac{3n}{4}\right ) + T\left ( \frac{n}{5}\right ) + O(n) + O(n) + O(1) = T\left (\frac{3n}{4}\right ) + T\left ( \frac{n}{5}\right ) + O(n).$$
As $\frac{3}{4} + \frac{1}{5} < 1$ we have that $T(n) = O(n)$.

> [!Note] Why is this true?
> I don't know, but this looks like it could be solved using [[Akra–Bazzi method]] or [[Recursion tree method]].

### Useful discussion about this

Let me see if I can help explain this. I find the best way to solve recurrences with multiple sub-problems is to think in terms of the "recursive tree".

For the recurrence $T(n) = T\left(\frac{3n}{4}\right) + T\left(\frac{n}{5}\right) + O(n)$ what do we know? We know there is $O(n)$ work at each level, and that we generate two recursive calls, each with a shrinking portion of $n$. At the first level of recursion we have two sub-problems, one of size $\frac{3n}{4}$, and a second of size $\frac{n}{5}$​, so the total work at that level is ${n}{0.95}$. What about the second level down? Let's visualize it:

![[recursion_tree_multiple_recursions.png]]

And the work at this second level? Sum up the four leaves, and you get:
$$0.75^2n + 2*0.2*0.75n + 0.2^2n = 0.9025n.$$
So the amount of work at each level is shrinking! This tells us that the work at the top level, O(n), dominates.

Now, what happens with the recurrence $T(n) = T\left(\frac{3n}{4}\right) + T\left(\frac{n}{3}\right) + O(n)$? Draw the tree, do the math:

![[recursion_tree_multiple_recursions_expanding.png]]

Now we see that at each level the work increases, so we no longer have a linear overall run time. The work at the bottom of the recursive stack will dominate the overall runtime.

What's the intuition behind this? The overall number of operations at each level is bounded by the total n at that level. As you make successive recursive calls, does n shrink? does it grow? or is it held constant?

## Further questions

> [!question] Change 5 in the analysis
> What happens to the run time if we switch out 5 for 3 or 7 in the analysis of this algorithm?

If we use $7$ instead of $5$ the run time is the same.
$$T(n) = T\left(\frac{9n}{14}\right) + T(\frac{n}{7}) + O(n).$$
If we use $3$ instead of 5 we get
$$T(n) = T\left(\frac{4n}{6}\right) + T\left(\frac{n}{3}\right) + O(n) = O(n\log(n)).$$


