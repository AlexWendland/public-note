---
aliases: 
type: exercise
publish: false
created: 2023-10-18
last_edited: 2023-10-21
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 9
chatgpt: false
---
# Week 9 - Exam Prep (unassessed) 

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

# [[Modular arithmetic]]

> [!question] Problem 1.11 
> Is $4^{1536} - 9^{4824}$ divisible by 35?

Note that $1536*2 = 0$ mod $(5-1) \times (7-1) = 24$ and $4824*2 = 0$ mod $24$. So the question resolves to is $2^{0} - 3^{0} = 0$ mod $35$ which it is!   

> [!question] Problem 1.12 
> What is $2^{2^{2006}}$ (mod 3)?

1

> [!question] Problem 1.13 
> Is the difference of $5^{30,000}$ and $6^{123,456}$ a multiple of 31?

Note 31 is prime and $30,000 = 0$ mod $30$ and $123456 = 6$ mod $30$ so this problem boils down to $5^0 - 6^6 = 0$ mod $31$. $(6^2)^3 = 36^3 = 5^3 = 125 = 1$ mod $31$. So the answer is yes. 


> [!question] Problem 1.14
> Suppose you wish to compute the $n$th [[Fibonacci sequence|Fibonacci number]] $F_n$, modulo an integer $p$. Can you find an efficient way to do this?

Given there are only $p^2$ possible combinations of $(a,b)$ mod $p$ within the first $p^2$ $F_n$ there must be a repeating pattern $F_i, F_{i+1}$ and $F_j, F_{j+1}$ for $0 \leq i < j < p^2$.

1. Calculate up to the first $p^2$ values until we find repeating pattern $F_i, F_{i+1}$ and $F_j, F_{j+1}$ for $0 \leq i < j < p^2$.
2. If $n \leq j + 1$ output $F_n$.
3. Calculate $n - i = k$ mod $(j-i)$.
4. Return $F_{i+k}$ 

> [!question] Problem 1.18
> Compute $gcd(210,588)$ two different ways: by finding the factorisation of each number, and by the [[Euclidean algorithm]].

Way 1,

$210 = 21 \times 10 = 3 \times 7 \times 2 \times 5 = 2 \cdot 3 \cdot 5 \cdot 7$ 
$588 = 294 \times 2 = 2^2 \times 147 = 2^2 \times 3 \times 49 = 2^2 \times 3 \times 7^2$ 

so $gcd(210,588) = 2 \cdot 3 \cdot 7 = 42$.

Way 2,

| a   | b   | c   |
| --- | --- | --- |
| 588 | 210 | 2   |
| 210 | 168 | 1   |
| 168 | 42  | 4   |
| 42  | 0   | -   |

So $gcd(210,588) = 42$.

> [!question] Problem 1.20
> Find the inverse of 20 mod 79, 3 mod 62, 21 mod 91, and 5 mod 23.

We do this via the [[Extended Euclidean algorithm]]

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 79  | 20  | 3   | -1  | 4   |
| 20  | 19  | 1   | 1   | -1  |
| 19  | 1   | 19  | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $4 \times 20 = 1$ mod $79$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 62  | 3   | 20  | -1  | 21  |
| 3   | 2   | 1   | 1   | -1  |
| 2   | 1   | 2   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $3 \times 21 = 1$ mod $62$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 91  | 21  | 4   | 1   | -4  |
| 21  | 7   | 3   | 0   | 1   |
| 7   | 0   | -   | 1   | 0   |

So there is no inverse.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 23  | 5   | 4   | 2   | -9    |
| 5   | 3   | 1   | -1  | 2   |
| 3   | 2   | 1   | 1   | -1  |
| 2   | 1   | 2   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

So $5 \cdot 14 = 1$ mod $23$.

> [!question] Problem 1.22
> Prove or disprove: If $a$ has an inverse modulo $b$, then $b$ has an inverse modulo $a$.

If $a$ has an inverse mod $b$ then $gcd(a,b) = 1$ by the [[Modular multiplicative inverse existence|modular multiplicative inverse existence lemma]]. Which is the required property for $b$ to have an inverse modulo $a$. 

> [!question] Problem 1.24
> If $p$ is prime, how many elements of $\{0,1, \ldots, p^n-1\}$ have an inverse mod $p^n$?

For the elements to have an inverse mod $p^n$ we know then need $gcd(e,p^n) = 1$. Therefor this is simply [[Euler's totient function]] $\phi(p^n) = (p-1)p^{n-1}$. 

> [!question] Problem 1.25
> Calculate $2^{125}$ mod $127$ using any method you choose?

As $127$ is prime we have $2^{126} =_{127} 1$ so $2^{125} = 2^{-1}$ mod $127$.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 127 | 2   | 63  | 1   | -63 | 
| 2   | 1   | 1   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

so $2^{-1} = 64$ mod 127.

> [!question] Problem 1.26
> What is the least significate decimal digit of $17^{17^{17}}

We need to calculate $17^{17^{17}}$ mod 10. Therefore we need to calculate $17^{17}$ mod $4$. Which involves finding $17$ mod $2$. So $17^{17} = 1^{1} = 1$ mod $4$ giving $17^1 = 7$ mod $10$. 

> [!question] Problem 1.27
> Consider an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] key set with $p=17$, $q=23$, $N=391$, and $e=3$. 
> a) What is the value of $d$ to make this a secrete key?
> b) What is the encryption of the message $M = 41$?

To find $d$ we need to find $e = 3$'s inverse mod $(17-1) \cdot (23-1) = 352$

| x   | y   | c   | a   | b    |
| --- | --- | --- | --- | ---- |
| 352 | 3   | 117 | 1   | -117 |
| 3   | 1   | 3   | 0   | 1    |
| 1   | 0   | -   | 1   | 0    |

So $235 \cdot 3 = 1$ mod $352$. So we have $d = 235$.

This is $M = 41^3 = 105$ mod 391. Which successfully decrypts as $105^{235} = 41$ mod 391.

> [!question] Problem 1.28
> In an [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] crypto system, $p=7$ and $q=11$. Find appropriate exponents $d$ and $e$.

Note $(7-1) \times (11 - 1) = 60$ so we can't use 3, 5 but we could use 7.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 60  | 7   | 8   | 2   | -17 | 
| 7   | 4   | 1   | -1  | 2   |
| 4   | 3   | 1   | 1   | -1  |
| 3   | 1   | 1   | 0   | 1   |

Therefore we have inverse $60 - 17 = 43 = d$. 

> [!question] Problem 1.42
> Suppose that instead of using a composite $N = pq$ in the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] cryptosystem, we simply use a prime modulus $p$. As in [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]], we would have an encryption exponent $e$, and the encryption of a message $m$ mod $p$ would be $m^e$ mod $p$. Prove that this new cryptosystem is not secure, by giving an efficient algorithm to decrypt: that is, an algorithm that given $p$, $e$, and $m^e$ mod $p$ as input, computes $m$ mod $p$. Justify the correctness and analyze the running time of your decryption algorithm.

1. Find $d := e^{-1}$ mod $p-1$ using [[Modular inverse algorithm (extended Euclidean algorithm)]].
2. Calculate $(m^e)^d = m$ mod $p$ using [[Modular exponent algorithm]].

The correctness follows from [[Fermat's little theorem]].

If $p$ is an $n$-digit number so is $e$ and $d$. Therefore step 1 and 2 has run time $O(n^3)$ giving the overall run time as $O(n^3)$. 

# [[Depth-first search (DFS)|DFS]] and [[Strongly connected components (directed graphs)|Strongly Connected Component]]

> [!question] Problem 3.1/2
> Perform a [[Depth-first search (DFS)|DFS]] on the following graphs; whenever there’s a choice of vertices, pick the one that is alphabetically first. Classify each edge as a [[DFS tree (algorithm)|Tree edge]] or [[DFS tree (algorithm)|Back edge]], and give the pre and post number of each vertex.

## 3.1

![[ex_3_1]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 12   |
| B      | 2   | 11   |
| C      | 3   | 10   |
| D      | 13  | 18   |
| E      | 5   | 6    |
| F      | 4   | 9    |
| G      | 14  | 17   |
| H      | 15  | 16   |
| I      | 7   | 8    |

We get the follow [[DFS tree (algorithm)|DFS tree]] with black [[DFS tree (algorithm)|tree edges]] and orange [[DFS tree (algorithm)|back edges]].

![[ex_3_1_dfs]]

## 3.2.a

![[ex_3_2_a]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 16   | 
| B      | 2   | 15   |
| C      | 3   | 14   |
| D      | 4   | 13   |
| E      | 8   | 9    |
| F      | 7   | 10   |
| G      | 6   | 11   |
| H      | 5   | 12   |

We get the following [[DFS tree (algorithm)|DFS tree]] with [[DFS tree (algorithm)|tree edges]] as black, [[DFS tree (algorithm)|back edges]] as orange and [[DFS tree (algorithm)|forward edges]] as purple.

![[ex_3_2_a_dfs]]

## 3.2.b

![[ex_3_2_b]]

| vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 16   | 
| B      | 2   | 11   |
| C      | 4   | 5    |
| D      | 6   | 9    |
| E      | 7   | 8    |
| F      | 3   | 10   |
| G      | 13  | 14   |
| H      | 12  | 15   |

We get the following [[DFS tree (algorithm)|DFS tree]] with [[DFS tree (algorithm)|tree edges]] as black, [[DFS tree (algorithm)|back edges]] as orange, [[DFS tree (algorithm)|forward edges]] as purple, and [[DFS tree (algorithm)|cross edges]] in green.

![[ex_3_2_b_dfs]]

> [!question] Problem 3.7
> A [[Bipartite graph|bipartite graph]] is a graph $G = (V, E)$ whose vertices can be [[Partition (set)|partitioned]] into two sets ($V = V_1 \cup V_2$ and $V_1 \cap V_2 = \emptyset$) such that there are no edges between vertices in the same set (for instance, if $u, v \in V_1$, then $(u,v), (v,u) \not \in E$).
> a) Give a linear-time algorithm to determine whether an undirected graph is bipartite.
> b) There are many other ways to formulate this property. For instance, an undirected graph is bipartite if and only if it can be colored with just two colors. Prove the following formulation: an undirected graph is bipartite if and only if it contains no cycles of odd length
> c) At most how many colors are needed to color in an undirected graph with exactly one odd length cycle?

### Part a

Use [[Depth-first search (DFS)|DFS]] where you update a mapping $m: V \rightarrow \{-,0,1\}$. Start by assigning the first vertex $0$. If you explore a vertex $u$ from $v$ and $m(v) = -$ then set $m(v) =_2 m(u) + 1$ if $m(v) =_2 m(u) + 1$ continue exploring $u$ and if $m(v) = m(u)$ return that it is not bipartite. Once we have explored every vertex return $m$. 

The run time is the same as that of [[Depth-first search (DFS)|DFS]] so $O(\vert V \vert + \vert E \vert)$.

If it returns $m$ then for all edges $(u,v) \in E$ we have checked $m(u) =_2 m(v) + 1$ so it is a [[Bipartite graph|bipartite graph]].

If we return false but it was bipartite with $V_0 \cup V_1 = V$. For simplicity lets say $V$ is connected (if it is disconnected apply this argument to the [[Connected components (graph)|connected component]] we found the error in). Let $v$ be the start vertex and without loss of generality assume $v \in V_0$. Therefore $v \in V_{m(v)}$. We can prove this generally by induction on the size of explored $v$. Therefore for the contradiction edge $(u,v) \in V$ we would have $u \in V_{m(u)}$ so by the rules of a [[Bipartite graph|bipartite graph]] $v \in V_{m(u) + 1}$ however $v \in V_{m(u)}$ meaning the original [[Bipartite graph|bipartition]] was not valid. Therefore, we are correct to say it can't be a [[Bipartite graph|bipartite graph]].

## Part b

Suppose we had a [[Bipartite graph|bipartite graph]] with an odd length cycle 
$$(v_1, v_2) \ldots (v_{2k}, v_{2k+1}), (v_{2k+1}, v_1)$$
Let $V_0 \cup V_1$ be the [[Bipartite graph|bipartition]] without loss of generality assume $v_1 \in V_1$. Then as $(v_i, v_{i+1}) \in E$ we know $v_i \in V_{i \ mod \ 2}$ so $v_{i+1} \in V_{i + 1 \ mod \ 2}$. However as $(v_{2k+1}, v_1) \in E$ with $v_1, v_{2k+1} \in V_{2k+1 = 1 \ mod \ 2}$ we know no such odd cycle can exist.

Suppose we have no odd cycles and run the algorithm in part a. Suppose we have some contradiction edge $(u,v)$ with $u, v = m(u)$ follow [[DFS tree (algorithm)|tree edges]] taken back to the common parent $x \in V$. This will give us
$$(u, u_1), \ldots, (u_{k-1}, x) \mbox{ and } (v, v_1) \ldots, (v_{t-1}, x).$$
We have that
$$ m(u) + k = m(x) = m(v) + t \mbox{ mod } 2.$$
therefore we have a cycle of length
$$
k + t + 1 = 2k + 1 = 1 \mbox{ mod } 2
$$
contradicting our original assumption. Therefore no such contradiction edge exists and we have that it is a [[Bipartite graph|bipartite graph]].

## Part c)

We need 3.

Remove a single edge from the odd length cycle. The new graph has no odd length cycles as otherwise there would have been more than one in the original graph.

As this new graph has no odd length cycles it is a [[Bipartite graph|bipartite graph]] and we can colour it using 2 colours. To reintroduce the edge colour one of the end vertices with the colour 3.

> [!question] Problem 3.8
> Pouring water. We have three containers whose sizes are 10 pints, 7 pints, and 4 pints, respectively. The 7-pint and 4-pint containers start out full of water, but the 10-pint container is initially empty. We are allowed one type of operation: pouring the contents of one container into another, stopping only when the source container is empty or the destination container is full. We want to know if there is a sequence of pourings that leaves exactly 2 pints in the 7- or 4-pint container.
> a) Model this as a graph problem: give a precise definition of the graph involved and state the specific question about this graph that needs to be answered.
> b) What algorithm should be applied to solve the problem?
> c) Find the answer by applying the algorithm.

## Part a)

Define our vertex set as 
$$V = \{(a, b, c) \vert 0 \leq a \leq 10, \ 0 \leq b \leq 7, \ 0 \leq c \leq 4, \ a + b + c = 11  \}$$
Then we have edge set
$$
E = \left \{ \begin{array} \ ((a,b,c), (a - m,b + m, c)) \\ ((a,b,c), (a - n,b, c + n)) \\ ((a,b,c), (a + o,b - o, c)) \\ ((a,b,c), (a,b - p, c + p)) \\ ((a,b,c), (a + q,b, c - q)) \\ ((a,b,c), (a,b + r, c - r))  \end{array} \Big \vert\begin{array} \ m = \min\{a, 7 - b\} \mbox{ if } m > 0 \\ n = \min\{a, 4 - c\} \mbox{ if } n > 0 \\ o = \min\{b, 10 - a\} \mbox{ if } o > 0\\ p = \min\{b, 4 - c\} \mbox{ if } p > 0 \\ q = \min\{c, 10 - a\} \mbox{ if } q > 0 \\ r = \min\{c, 7-b\} \mbox{ if } r > 0  \end{array}, \ (a,b,c) \in V  \right \}
$$

We need to find a path between $(0, 7, 4)$ and $(a,2,c)$ or $(a,b,2)$.

## Part b)

Run [[Breath-first search (BFS)|BFS]] on the graph.

## Part c)

Did it ... it took a while.

> [!question] Problem 3.11
> Design a linear-time algorithm which, given an undirected graph $G$ and a particular edge $e \in E$, determines whether $G$ has a cycle containing $e$.

## Algorithm

Let $e = (u,v)$

1. Define $G' = (V, E \backslash \{e\})$
2. Run [[Breath-first search (BFS)|BFS]] starting at $u$.
3. If $v$ is in $u$'s branch return true else false.

## Correctness

If it returns true there is a path from $u$ to $v$ in $G$ without $e$. So we have a cycle involving $e$.

If we had a cycle involving $e$ then removing it from the cycle gives us a path from $u$ to $v$ in $G'$.

## Runtime

Step 1 and 3 are $O(\vert E \vert)$ and $O(\vert V \vert)$ as they are removing or looking up an element of an array of length at most $\vert E \vert$ or $\vert V \vert$.

Step 2 is [[Breath-first search (BFS)|BFS]] which takes $O(\vert E \vert + \vert V \vert)$

All together this gives $O(\vert E \vert)$ + $O(\vert  V \vert)$ + $O(\vert E \vert + \vert V \vert)$ = $O(\vert E \vert + \vert V \vert)$.

> [!question] Problem 3.16
> Suppose a CS curriculum consists of $n$ courses, all of them mandatory. The prerequisite graph $G$ has a node for each course, and an edge from course $v$ to course $w$ if and only if $v$ is a prerequisite for $w$. Find an algorithm that works directly with this graph representation, and computes the minimum number of semesters necessary to complete the curriculum (assume that a student can take any number of courses in one semester). The running time of your algorithm should be linear.

Note if the graph is not a [[Directed acyclic graph (DAG)|dag]] then can't complete the course.

1. Run the [[DFS for finding strongly connected components]]
2. If any strongly connected components are larger than 1 return that the course is impossible to pass.
3. Define function $f: V \rightarrow \mathbb{N}$ 
4. Run through the vertices in the [[Topological sorting (DAG)|topological sorting]].
	1. If the vertex is a leaf node set $f(v) = 1.
	2. Otherwise set $f(v) = 1 + \max_{(u,v) \in E} f(u)$.
5. Return $\max_{v \in V} f(v)$

## Correctness

We know [[DFS for finding strongly connected components]] is correct.

If any connected component is larger than 1 then we have circular dependencies so we can't complete the course.

Note $f(v)$ is the maximum number of vertices between that vertex and a leaf node. Including itself. Therefore you will need at least $f(v)$ semesters to complete the course. 

Therefore the maximum number of semesters you need to complete all courses is the maximum over $f(v)$.

## Run time

The run times is $O(\vert V \vert + \vert E \vert)$.

Step 1 takes $O(\vert V \vert + \vert E \vert)$.

Step 2 takes $O(\vert V \vert)$ to check the sizes of the return connected components.

Step 3 takes $O(\vert V \vert)$

Step 4 runs through all vertices. In the process of going through all vertices it looks at all edges once. This step takes $O(\vert V \vert + \vert E \vert)$.

Step 5 takes $O(\vert V \vert)$.

Altogether this takes $2O(\vert V \vert + \vert E \vert) + 3 O(\vert V \vert) = O(\vert V \vert + \vert E \vert)$.

> [!question] Problem 3.22
> Give an efficient algorithm which takes as input a [[Directed graph|directed graph]] $G = (V, E)$, and determines whether or not there is a vertex $s \in V$ from which all other vertices are reachable.

## Algorithm

1. Run [[Depth-first search (DFS)|DFS]] starting at any vertex in $V$.
2. Run [[Depth-first search (DFS)|DFS]] starting at the vertex with the highest post order from the previous run.
3. If the same vertex has the highest post order again - return true. Otherwise return false.

## Correctness

If the algorithm returns true then on the second run of the [[Depth-first search (DFS)|DFS]] algorithm from the vertex we started at we visited every other vertex before finishing at that vertex. Therefore we have the required statement.

If the algorithm returns false. Then we know there is a second source component in the [[Strongly connected component graph (directed graph)|strongly connected component graph]] and by [[Week 9 - Exam Prep#Claim 1|Claim 1]] we have that no such vertex exists.

### Claim 1

>[!important] Claim 1
>A [[Directed graph|directed graph]] has a vertex from which all other vertices are reachable if and only if it has one source vertex in it's [[Strongly connected component graph (directed graph)|strongly connected component graph]].

### Proof of Claim 1

If a vertex $v \in V$ has a path to every other vertex. Then any[[Strongly connected components (directed graphs)|strongly connected component]] not containing $v$ has a path from the [[Strongly connected components (directed graphs)|strongly connected component]] containing $v$. Therefore it is not a source [[Strongly connected components (directed graphs)|strongly connected component]]. As the graph must have a source vertex, it is the one contain $v$.

If [[Strongly connected component graph (directed graph)|strongly connected component graph]] has only one source vertex $S$ then from [[Week 9 - Exam Prep#Claim 2|Claim 2]] there exists a path from $S$ to all other [[Strongly connected components (directed graphs)|strongly connected components]]. Therefore any vertex $v \in S$ has a path to all other vertices.

### Claim 2

>[!important] Claim 2
>If a [[Directed acyclic graph (DAG)]] $G = (V,E)$ has only one source vertex $s \in V$. Then $s$ has a path to every other vertex $v \in V$.

Take any vertex $v \in V$ and set $v_0 := v$.

If $v_i$ is not a source vertex, choose a parent and define $v_{i+1}$ such that $(v_{i+1}, v_i) \in E$. As $G$ is finite there is some $0 \leq k < \vert V \vert$  such that $v_k$ is a source vertex. By our assumption $v_k = s$ and we have a path from $s$ to $v$, namely $(s, v_{k-1}) \ldots (v_1, v)$.

## Run time

Steps 1 and 2 take $O(\vert V \vert + \vert E \vert)$.

Step 3 takes $O(\vert V \vert)$ at worst

Overall this takes $2O(\vert V \vert + \vert E \vert) + O(\vert V \vert) = O(\vert V \vert + \vert E \vert)$. 

> [!question] Problem 3.24
> Give a linear-time algorithm for the following task. 
> Input: A [[Directed acyclic graph (DAG)|directed acyclic graph]] $G$ 
> Question: Does $G$ contain a directed path that touches every vertex exactly once?

## Algorithm

1. Run [[Depth-first search (DFS)|DFS]] starting at any vertex.
2. Run [[Depth-first search (DFS)|DFS]] starting at the vertex of largest post order from the last run.
3. Order the edges $v_i$ with $v_1$ having the smallest post order and $v_n$ having the largest.
4. Check if edges $(v_{i+1}, v_i) \in E$ if not return false.

## Correctness

If it returns true, then $(v_{i+1}, v_i)$ is exactly the path that runs through every vertex exactly once.

If it returns false, then we are missing some edge $(v_{j+1}, v_j)$ this means we have two possible [[Topological sorting (DAG)|topological sorting]] $v_{i + 1} < v_i$ for all $i$ and $v_{i + 1} < v_i$ for all $i \not = j$ and $v_j < v_{j+1}$. Which by [[Week 9 - Exam Prep#Claim 3|Claim 3]] gives that this graph has no such path.  

### Claim 3

> [!important] Claim 3
> A [[Directed acyclic graph (DAG)|dag]] has a path that touches every vertex exactly once if and only if it has a unique [[Topological sorting (DAG)|topological sorting]].

If a [[Directed acyclic graph (DAG)|dag]] has a path $(v_1, v_2) \ldots (v_{n-1}, v_n)$ that touches every vertex exactly once, then $v_i < v_{i+1}$ for $1 \leq i < n$. Fixing the [[Topological sorting (DAG)|topological sorting]].

If the [[Topological sorting (DAG)|topological sorting]] $v_i$ (with $v_i < v_j$ for $i < j$) of the vertices is unique then any switch $v_i$ for $v_{i+1}$ is invalid therefore there must be an edge $(v_i, v_{i+1})$. These edges form this path.   

# [[Breath-first search (BFS)|BFS]] and Shortest path problems

> [!question] Problem 4.1
> Run [[Dijkstra's algorithm]] on the following graph tracking all the intermediate distances and return the path. 

![[ex_4_1]]

| Round | A       | B       | C       | D       | E       | F       | G       | H       |
| ----- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 0     | 0 (-)   | -       | -       | -       | -       | -       | -       | -       |
| 1     | - (0\*) | 1 (A)   | -       | -       | 4 (A)   | 8 (A)   | -       | -       |
| 2     | - (0)   | A (1\*) | 3 (B)   | -       | 4 (A)   | 7 (B)   | 6 (G)   | -       |
| 3     | - (0)   | A (1)   | B (3\*) | 4 (C)   | 4 (A)   | 7 (B)   | 5(C)    | -       |
| 4     | - (0)   | A (1)   | B (3)   | C (4\*) | 4 (A)   | 7 (B)   | 5 (C)   | 8 (D)   |
| 5     | - (0)   | A (1)   | B (3)   | C (4)   | A (4\*) | 7 (b)   | 5 (C)   | 8 (D)   |
| 6     | - (0)   | A (1)   | B (3)   | C (4)   | A (4)   | 6 (G)   | C (5\*) | 6 (G)   |
| 7     | - (0)   | A (1)   | B (3)   | C (4)   | A (4)   | G (6\*) | C (5)   | 6 (G)   |
| 8     | - (0)   | A (1)   | B (3)   | C (4)   | A (4)   | G (6)   | C (5)   | G (6\*) |

![[ex_4_1_tree]]

> [!question] Problem 4.2
> Run [[Bellman-Ford algorithm]] on the following graph tracking all the intermediate distances and return the path.

![[ex_4_2]]

| Iteration | A   | B   | C   | D   | E   | F   | G   | H   | I   | S   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0         | -   | -   | -   | -   | -   | -   | -   | -   | -   | 0   |
| 1         | 7   | -   | 6   | -   | 6   | 5   | -   | -   | -   | 0   |
| 2         | 7   | 11  | 5   | 8   | 6   | 4   | -   | 9   | -   | 0   |
| 3         | 7   | 11  | 5   | 7   | 6   | 4   | 9   | 7   | -   | 0   |
| 4         | 7   | 11  | 5   | 7   | 6   | 4   | 8   | 7   | -   | 0   |
| 5         | 7   | 11  | 5   | 7   | 6   | 4   | 8   | 7   | -   | 0    |

> [!question] Problem 4.3
> Squares. Design and analyze an algorithm that takes as input an undirected graph $G = (V, E)$ and determines whether $G$ contains a simple cycle (that is, a cycle which doesn’t intersect itself) of length four. Its running time should be at most $O(\vert V \vert^3)$. You may assume that the input graph is represented either as an adjacency matrix or with adjacency lists, whichever makes your algorithm simpler.

## Algorithm

We will use a graph in [[Adjacency list format (graph)|adjacency list]] format where for all $v \in V$ we have $U_v \subset V$ being all vertices that are adjacent to $v$. Further more we will assume $U_v$ is ordered for some ordering on $V$ (this only takes $O(\log(\vert V \vert)\vert V \vert^2$ time).

1. For all $u, v \in V$ $u \not = v$
	1. Check $\vert U_u \cap U_v \backslash \{u,v\} \vert > 1$ if so return true
	2. Otherwise continue
2. Return False

## Correctness

For a square to exist it needs 4 vertices $a, b, c, d$ with edges $(a,b)(b,c)(c,d)(d,a)$. Then $b,d \in U_a \cap U_c \backslash \{a,c\}$ making it of size greater than 2. Conversely if $b,d \in U_a \cap U_c \backslash \{a,c\}$ then there exists square $(a,b)(b,c)(c,d)(d,a)$.

## Run time

Step 1 iterates twice over the vertices of $G$ so this is $\vert V \vert^2$ steps. 

Calculating $U_u \cap U_v \backslash \{u,v\}$ with $U_u$ and $U_v$ is order takes $O(\vert V \vert)$ time as we can iterate through both sets incrementing the lesser of the two and taking common elements. So this takes $O(\vert V \vert)$ time.

All together this takes $O(\vert V \vert^3)$ time.

> [!question] Problem 4.8
> Professor F. Lake suggests the following algorithm for finding the shortest path from node $s$ to node $t$ in a directed graph with some negative edges: add a large constant to each edge weight so that all the weights become positive, then run [[Dijkstra's algorithm]] starting at node $s$, and return the shortest path found to node $t$.
> Is this a valid method? Either prove that it works correctly or give a counter example.

It doesn't work. Consider the following counter example with original weights in black and altered weights in red.

![[ex_4_8_cex]]

In the black values the distance from $S$ to $T$ is 0 following the top path. The bottom path takes distance 0.5.

In the altered weights the distance along the top path is 3 whereas on the bottom it is 2.5. Therefore it will pick this path over the top.

> [!question] Problem 4.11
> Give an algorithm that takes as input a directed graph with positive edge lengths, and returns the length of the shortest cycle in the graph (if the graph is acyclic, it should say so). Your algorithm should take time at most $O(\vert V \vert^3)$.

Run [[Floyd-Warshall algorithm]] and return the minimum $D(\vert V \vert,i,i)$ for all $i \in V$.



Problems: 4.12-4.14, 4.20, 4,21.

# [[Minimum Spanning Tree problem (MST)]]

Problems 5.1, 5.2, 5.5, 5.6, 5,7, 5.9, 5.20, 5.22, 5.23.

# Flow problems

Problems 7.18, 7.19, 7.21, 7.22, 7.24(\*), 7.28(\*)