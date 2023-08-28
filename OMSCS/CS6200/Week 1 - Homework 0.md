---
aliases: []
type: exercises
publish: false
created: 2023-08-27
last_edited: 2023-08-27
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 1
chatgpt: false
---
# Homework 0

>[!question] Problem 1 (a)
>Let $f(n) = 100n + \log(n)$ and $g(n) = n + \log(n)^2$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

Note the following two inequalities

- $\log(n) < n$ for $n > 1$,
- $\log(n)^2 < n$ for $n > 2$,

therefore $100n <f(n) < 101n$ and $n < g(n) < 2n$ giving us $g(n) = \Theta(n)$ and $f(n) = \Theta(n)$ and $f(n) = \Theta(g(n))$.

So the answer is 3.

>[!question] Problem 1 (b)
>Let $f(n) = n\log(n)$ and $g(n) = 10n\log(10n)$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

Note that from the [[Logarithms|rules of logarithms]] we have
$$g(n) = 10n\log(10n) = 10n(\log(10) + \log(n)) = 10n\log(10) + 10n\log(n).$$
Which for $n > 10$ gives us
$$n \log(n) < g(n) < 20n\log(n)$$
providing the bounds to give $g(n) = \theta(n\log(n)) = \theta(f(n))$.

So the answer is 3.

>[!question] Problem 1 (c)
>Let $f(n) = \sqrt{n}$ and $g(n) = \log(n)^3$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

As linear powers of $n$ outgrow [[Logarithms|logs]] we have $g(n) = O(f(n))$.

So the answer is 2.

>[!question] Problem 1 (d)
>Let $f(n) = \sqrt{n}$ and $g(n) = 5^{\log_2(n)}$. Which of the following holds?
>- $f(n) = O(g(n))$
>- $g(n) = O(f(n))$
>- $f(n) = \Theta(g(n))$

From [[Logarithms#Interchange of bases|base interchange of logs]] we have that
$$g(n) = 5^{\log_2(n)} = 5^{\log_2(5)\log_5(n)} = 5^{\log_2(5)}5^{\log_5(n)} = 5^{\log_2(5)}n$$
which gives $f(n) = O(g(n))$.

So the answer is 1.

>[!question] Problem 2
> Show that $g(n) = 1 + a + a^2 + \ldots + a^n$ is $O(a^n)$ when $a > 1$ and $O(1)$ when $a < 1$.  
> (Hint: You may try to prove $g(n) =\frac{a^{n+1} - 1}{a-1}$ at first.)

Consider
$$ (a - 1)g(n) = a \sum_{i=0}^n a^i - \sum_{i=0}^n a^i = \sum_{i=0}^n a^{i+1} - a^i = a^{n+1} - 1$$
giving the hinted inequality
$$g(n) =\frac{a^{n+1} - 1}{a-1}.$$
Let $a > 1$ then
$$g(n) = \frac{a^{n+1}}{a - 1} - \frac{1}{a-1} \leq \frac{a^{n+1}}{a-1} = \frac{a}{a-1} a^n.$$
This gives $g(n) = O(a^n)$.

If $a = 1$ then $g(n) = n$ giving $g(n) = O(n)$.

Let $-1< a < 1$ then note that
$$ \vert a^{n+1} - 1 \vert < \vert a - 1 \vert$$
so we have that 
$$\vert g(n) \vert < 1$$
giving the required $g(n) < 1$ and $g(n) = O(1)$.

If $a = -1$ then $g(n) = \frac{1 + (-1)^n}{2}$ so $g(n) = O(1)$.

If $a < -1$ then $g(n)$ is divergent and we can't talk about run time.

>[!question] Problem 3 (a)
> For all parts, $G = (V, E)$ represents an undirected, simple [[Graph|graph]] (i.e.: no multiple edges and no loops).
>   
> Denote by deg(v), the degree of vertex v, the number of edges incident to v. Check that
> $$ \sum_{v \in V} \mbox{deg}(v) = 2 \vert E \vert$$

Lets prove this by induction on the number $\vert E \vert$ within a graph.

Suppose a graph has no edges. Therefore $\deg(v) = 0$ for all $v \in V$ as there are no edges to be incident to $v$. Thus 
$$\sum_{v \in V} \mbox{deg}(v) = 0 = 2 \vert E \vert.$$
Suppose we have shown the statement true for all graphs where $\vert E \vert < k$ and suppose we have a graph with $\vert E \vert = k$. Pick any edge $e = (x,y)$ and remove it from the graph to get $G^{\ast} = (V, E^{\ast})$ . From the induction hypothesis we have
$$ \sum_{v \in V} \mbox{deg}_{G^{\ast}}(v) = 2 (\vert E \vert - 1)$$
Where $\mbox{deg}_{G^{\ast}}$ is the degree in $G^{\ast}$. Note that $\mbox{deg}_{G}(v) = \mbox{deg}_{G^{\ast}}(v)$ for all $v \in V \backslash \{x, y\}$. Whereas, $\mbox{deg}_{G^{\ast}}(v) + 1 = \mbox{deg}_{G}(v)$ for $v \in \{x,y\}$ (as it is incident to $e = (x,y)$ as well as all the edges in $E^{\ast}$). Therefore
$$\begin{align*}
\sum_{v \in V} \mbox{deg}_{G}(v) & = \sum_{v \in V \backslash \{x,y\}} \mbox{deg}_{G^{\ast}}(v) + \sum_{v \in \{x,y\}} (\mbox{deg}_{G}(v) + 1)\\
& = 2 + \sum_{v \in V} \mbox{deg}_{G^{\ast}}(v) \\
& = 2 + 2 (\vert E \vert - 1)\\
& = 2 \vert E \vert. \end{align*}$$
This shows the inductive case and proves the statement.

>[!question] Problem 3 (b)
> Review the concepts of path, cycle, connectivity.  

![[Path (graph)]]

![[Cycle (graph)|cycle]]

![[Connected (graph)]]

> [!question] Problem 3 (c)
> $G$ is said to be a tree if it is connected and have no cycles. Think why the following three conditions are equivalent:  
> 1. $G$ is a tree.  
> 2. $G$ is connected and $\vert E \vert = \vert V \vert − 1$.  
> 3. $G$ has no cycles and $\vert E \vert = \vert V \vert − 1$.  

Proof of $(1) \Rightarrow (2)$.

We prove this by induction on the number of vertices.

Suppose $\vert V \vert = 1$ and set $V = \{v\}$ then if $G$ had an edge it must be $(v,v)$. However, we then have a cycle $(v,v)$ so it would not be a tree. So $\vert E \vert = 0 = \vert V \vert - 1$.

Suppose the induction hypothesis is correct on all graphs with $\vert V \vert < k$ and let $G$ be a [[Graph|graph]] with $\vert V \vert = k$.

As [[A finite tree that has more than one vertex must have at least two leaf vertices|a finite tree that has more than one vertex must have at least two leaf vertices]] let $v \in V$ be such a leaf vertex with single edge $e \in E$. Remove $v$ to form $G^{\ast} = (V \backslash \{v\}, E \backslash \{e\})$. Note that $G^{\ast}$ has to be a tree as if a [[Cycle (graph)|cycle]] existed in $G^{\ast}$ it would exist in $G$ and as $G$ was connected so is $G^{\ast}$ as no path would need to use $e$.

By the induction hypothesis $\vert E \backslash \{e\}\vert = \vert V \backslash \{v\}\vert - 1$. Giving
$$ \vert E \vert = \vert E \backslash \{e\}\vert + \vert \{e\} \vert = \vert V \backslash \{v\}\vert - 1 + 1 =  (\vert V \backslash \{v\}\vert + 1) - 1 = \vert V \vert - 1.$$
Thus proving our statement by induction.

Proof of $(2) \Rightarrow (3)$.

Suppose we have a graph $G$ that is connected and $\vert E \vert = \vert V \vert - 1$. Though $G$ has a [[Cycle (graph)|cycle]] in it. 

Take a minimal, in terms of $\vert V \vert$, counter example.  

Note that from problem 3(a) we have
$$ \sum_{v \in V} \mbox{deg}(v) = 2 \vert E \vert = 2 \vert V \vert - 2$$
that says one vertex in $V$ must have $\mbox{deg}(v) = 1$ (it has to be at least 1 as it is connected).

As $v$ can't be in the [[Cycle (graph)|cycle]] (this would require degree 2), it must be outside. We can now remove this vertex and the remaining graph will still satisfy $(2)$ with the same [[Cycle (graph)|cycle]]. The new graph will be a smaller example and contradict its minimality.

This proves the claim.

Proof of $(3) \Rightarrow (1)$.

Note all we need to show is that $G$ is connected. 

Lets use proof be contradiction. Suppose $G$ satisfies $(3)$ but is not a tree, let $G$ be a minimal such example.

If $G$ has a vertex of [[Degree (graph)|degree]] 1, we can remove it and find a smaller counter example. Therefore $G$ must not have any vertices of degree 1.

Take a connected component of $G$, as it has no vertices of degree 1 they must have vertices of degree $2$ or more. Repeat the argument in [[A finite tree that has more than one vertex must have at least two leaf vertices|a finite tree that has more than one vertex must have at least two leaf vertices]], this shows that this connected component has a cycle it in. This contradicts $(3)$ so no such graph exists.

This proves this claim and the equivalence.

> [!question] Problem 3 (d)
> A vertex is called a leaf if it has degree one. Show that every tree has at least two leaves.  
> Think of an example of a tree with exactly two leaves.

![[A finite tree that has more than one vertex must have at least two leaf vertices]]

The examples of graphs with exactly two [[Leaf (graph)|leaf vertices]] are the [[Path (graph)#The path graph|path graphs]].

> [!question] Problem 4
> For each example below, decide which functions are in [[Conjunctive normal form (CNF)|CNF]] and find an assignment of the variables such that the corresponding function evaluates to true, if such assignment exists.  
> - $(x \lor y \lor z) \land (x \lor w) \land (y \lor \lnot w)$
> - $( \lnot x \lor  \lnot y) \land (x) \land (z \lor \lnot z)$
> - $x \land (y \land (z \lor \lnot w))$ 

For $(x \lor y \lor z) \land (x \lor w) \land (y \lor \lnot w)$.

This is in [[Conjunctive normal form (CNF)|CNF]] and $x = y = z = w = 1$ evaluates to true.

For $( \lnot x \lor  \lnot y) \land (x) \land (z \lor \lnot z)$.

This is in [[Conjunctive normal form (CNF)|CNF]] and $x = z = 1$, and $y = 0$ evaluates to true.

For $x \land (y \land (z \lor \lnot w))$.

This in not in [[Conjunctive normal form (CNF)|CNF]] and $x = y = z = w = 1$ equates to true.