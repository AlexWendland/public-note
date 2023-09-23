---
aliases: 
type: exercise
publish: false
created: 2023-09-11
last_edited: 2023-09-11
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "3"
chatgpt: false
---
# Week 3 - Homework 2 (unassessed) 

> [!question] From [[Week 3 - Linear-Time Median]]  change 5 in the analysis
> What happens to the run time if we switch out 5 for 3 or 7 in the analysis of this algorithm?

3 leads to $O(n\log(n))$ whereas 7 is still $O(n)$.

>[!question] Smallest missing natural number
>Design an $O(\log(n))$ algorithm to find the smallest missing natural number in a given sorted array. The given array only has natural numbers. For example, the smallest missing natural number from $A = \{3, 4, 5\}$ is $1$ and from $A = \{1, 3, 4, 6\}$ is $2$.

If the first element of $A$ is greater than 1 return 1. If the last element of $A$ is $n$ return $n+1$. This leaves the case where the missing element is in $A$. Then we are in the following subproblem and will run the algorithm to solve that subproblem on the list $A$. 

## Subproblem

Suppose you are given a list $L$ of natural numbers of length $n > 1$ with the first element being $a$ and the last element being $b > a + n - 1$ find the smallest natural number $c$ such that $a < c < b$ is not in the list $L$.

## Algorithm to solve this by D&C

If the list is of length $2$ then we know the answer is $a + 1$. If the list is of length $3$ then we only check the second element. If this element is $a + 1$ we return $a+2$, if it is not we return $a+1$. 

If the list is of length greater than 3. Divide the list $L$ into the first $\lceil \frac{n}{2} \rceil$ elements $A_{left}$ and the rest $A_{right}$.

If the last element of $A_{left}$ is $a + \lceil \frac{n}{2} \rceil - 1$ then run the algorithm on $A_{right}$ if not then run it on $A_{left}$. 

## Run time

Let $T(n)$ represent the running time of this algorithm.

Note if $n=1$ then either $A = [1]$ and we return 2 or we return 1.  If $n = 2$ we check the highest and lowest element to determine if our return is 1, 2 or 3. If $n = 3$ at worst we check all 3 elements to return 1,2,3 or 4,
This takes 1 check so $T(1) = 1$

For the general case, either it takes 2 checks to return or we are solving the subproblem.

If we are solving the subproblem the size of the list $A_{left}$ and $A_{right}$ is at most $n/2$. So we have run time

$T(n) = T(n/2) + 2$

In this case we have $T(n) = O(\log_2(n))$, with $T(n) = \Omega(1)$.

---

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] 4.11 Length of the shortest cycle
> Give an algorithm that takes as input a directed graph with positive edge lengths, and returns the length of the shortest cycle in the graph (if the graph is acyclic, it should say so). Your algorithm should take time at most $O(\vert V \vert^3)$.

Run the [[Floyd-Warshall algorithm]] and return the length of the minimum entry on the diagonal. If they are all infinite then return that it is acyclic.

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction). 
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers. 
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{k−1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits. 
>
>(b) Give an efficient algorithm for detecting the presence of such an anomaly. Use the graph representation you found above.

Define a graph with vertices $V = \{1,\ldots, n\}$  and let the edges be $e_{i,j} = -\log(r_{i,j})$ then run the [[Bellman-Ford algorithm]] on this graph starting at vertex $s$. This will produce the shortest path $p$ to vertex $t$. $P = e_{v_0v_1} \ldots e_{v_kv_{k+1}}$ with $v_0 = s$ and $v_{k+1} = t$. Which has weight
$$- \sum_{i=0}^k \log(r_{v_i,v_{i+1}}) = - \log\left ( \prod_{i=0}^k r_{v_iv_{i+1}} \right )$$

Suppose there was a route $d_0 \ldots d_{w+1}$ such that
$$\prod_{i=0}^k r_{v_iv_{i+1}} < \prod_{i=0}^w r_{d_id_{i+1}} $$
however this would lead to
$$ - \sum_{i=0}^k \log(r_{v_i,v_{i+1}}) > - \sum_{i=0}^w \log(r_{d_i,d_{i+1}})$$
contradicting the output of the algorithm. 

This takes time $O(n^3)$.

>[!question] 2.1 Practice Fast Multiplication
>Use the divide-and-conquer integer multiplication algorithm to multiply the two binary integers 10011011 and 10111010.

$X = 10011011$ and $Y = 10111010$

So

$X_L = 1001$ and $X_R = 1011$.

$Y_L = 1011$ and $Y_R = 1010$.

So Calculate $X_L \cdot Y_L$, $X_R \cdot Y_R$ and $(X_L + X_R) \cdot (Y_L + Y_R) = 10100 \cdot 10101$

Start with $X_L \cdot Y_L$

$10$ and $01$

$10$ and $11$

So calculate $10 \cdot 10 = 100$, $01 \cdot 11 = 11$, $11 \cdot 101$

Start with $0011 \cdot 0101$

$00$, $11$

$01$, $01$

So calculate $00 \cdot 01 = 0$, $11 \cdot 01 = 11$, $11 \cdot 10 = 110$

$0011 \cdot 0101 = 000000 + (110 - 00 - 11) \cdot 100 + 11 = 1100 + 11 = 1111$

So $X_L \cdot Y_L = 1000000 + (1111 - 100 - 11) \cdot 100 + 11 = 1000000 + 100000 + 11 = 1100011$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> a) $T(n) = 2T(n/3) + 1$

By masters theorem the recursion dominates and $T(n) = \theta(n^{\log_3(2)})$

$$\begin{align*} T(n) & = 2T(n/3) + 1\\
& = 2 (2T(n/3^2) + 1) + 1\\
& = 2^2T(n/3^2) + 2 + 1\\
& = 2^2[2T(n/3^3) + 1] + 2 + 1\\
& = 2^3 T(n/3^3) + \sum_{i=0}^2 2^i\\
& = 2^{k} T(n/3^k) + \sum_{i=0}^{k-1} 2^i\\
& = 2^k T(n/3^k) + \frac{1 - 2^{k-1}}{1-2}\\
& = 2^k T(n/3^k) + 2^{k-1} - 1\\
& = 2^{\log_3(n)} T(1) + 2^{\log_3(n) - 1} - 1\\
& = n^{\log_3(2)} T(1) + n^{\log_3(2)} / 2 - 1\\
& = O(n^{\log_3(2)})
\end{align*}$$
> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> b) $T(n) = 5T(n/4) + n$

By masters theorem as $n = O(n)$ and $1 < \log_4(5)$ we have $T(n) = O(n^{\log_4(5)})$

$$\begin{align*} 
T(n) & = 5T(n/4) + n\\
& = 5 [5T(n/4^2) + n/4] + n\\
& = 5^2T(n/4^2) + 5n/4 + n\\
& = 5^2[5T(n/4^3) + n/4^2] + 5n/4 + n\\
& = 5^3 T(n/4^3) + n \sum_{i=0}^2 (5/4)^i\\
& = 5^{k} T(n/4^k) + n \sum_{i=0}^{k-1} (5/4)^i\\
& = 5^k T(n/4^k) + n \frac{1 - (5/4)^{k-1}}{1-(5/4)}\\
& = 5^k T(n/4^k) + n(5/4)^{k-1}/4 - n/4\\
& = 5^{\log_4(n)} T(1) + n (5/4)^{\log_4(n) - 1}/4 - n/4\\
& = n^{\log_4(5)} T(1) + n^{\log_4(5)}/4 - n/4\\
& = O(n^{\log_4(5)})
\end{align*}$$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> c) $T(n) = 7T(n/7) + n$

By masters theorem as $n = O(n)$ and $7/7 = 1$ we should have $O(T(n)) = n\log(n)$.

$$\begin{align*} 
T(n) & = 7T(n/7) + n\\
& = 7 [7T(n/7^2) + n/7] + n\\
& = 7^2T(n/7^2) + 2n\\
& = 7^2[7T(n/7^3) + n/7^2] + 2n\\
& = 7^k T(n/7^k) + kn\\
& = 7^{\log_7(n)} T(1) + n\log_7(n)\\
& = n T(1) + n\log_7(n)\\
& = O(n\log_7(n))
\end{align*}$$
> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> d) $T(n) = 9T(n/3) + n^2$

By masters theorem as $n^2 = O(n^2)$ and $\log_3(9) = 2$ we should have $O(T(n)) = n^2 \log(n)$

$$\begin{align*} 
T(n) & = 9T(n/3) + n^2\\
& = 9 [9T(n/3^2) + n^2/9] + n^2\\
& = 9^2T(n/3^2) + 2n^2\\
& = 9^2[7T(n/3^3) + n^2/9^2] + 2n^2\\
& = 9^k T(n/3^k) + kn^2\\
& = 9^{\log_3(n)} T(1) + n^2\log_3(n)\\
& = n^2 T(1) + n^2\log_3(n)\\
& = O(n^2\log_3(n))
\end{align*}$$
> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> e) $T(n) = 8T(n/2) + n^3$

By masters theorem as $n^3 = O(n^3)$ and $\log_2(8) = 3$ we have $\Theta(T(n)) = n^3\log(n)$.

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> f) $T(n) = 49T(n/25) + n^{3/2}\log(n)$

By masters theorem as $\log_{5^2}(7^2) = \log(7)/\log(5) < 1.5$ then $n^{3/2}\log(n) = \Omega(n^{3/2})$ this gives $T(n) = \Theta(n^{3/2}\log(n))$.

$$\begin{align*} 
T(n) & = 7^2T(n/5^2) + n^{3/2}\log(n)\\
& = 7^2[7^2T(n/5^4) + (n/5^2)^{3/2}\log(n/5^2)] + n^{3/2}\log(n)\\
& = 7^4T(n/5^2) + n^{3/2}\log(n)(7^2/5^3) + n^{3/2}\log(n) - n^{3/2}2\log(5)(7^2/5^3)\\
& = 7^4\left[7^2T(n/5^6) + (n/5^4)^{3/2}\log(n/5^4) \right] + n^{3/2}\log(n)(7^2/5^3) + n^{3/2}\log(n) - n^{3/2}2\log(5)(7^2/5^3)\\
& = 7^6T(n/5^6) + n^{3/2}\log(n)(7^4/5^6) + n^{3/2}\log(n)(7^2/5^3) + n^{3/2}\log(n) - n^{3/2}\log(5)(2^27^4/5^6) - n^{3/2}\log(5)(27^2/5^3)\\
& = 7^{2k}T(n/5^{2k}) + n^{3/2}\log(n)\left ( \sum_{i=0}^{k-1} (49/125)^k \right ) - n^{3/2}\log(5)\left( \sum_{i=1}^{k-1} (98/125)^k \right )\\
& = 7^{2k}T(n/5^{2k}) + n^{3/2}\log(n)\frac{1 - (49/125)^{k-1}}{1 - (49/125)} -  n^{3/2}\log(5)\frac{1 - (98/125)^{k-1}}{1 - (98/125)}\\
& = n^{\log_{25}(49)}T(1) + n^{3/2}\log(n) c + n^{3/2} d
\end{align*}$$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> h) $T(n) = T(n − 1) + 2$

$T(n) = 2n + T(0) = O(n)$.

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> g) $T(n) = T(n − 1) + n^c$ , where $c \geq 1$ is a constant.

$T(n) = T(0) + \sum_{k=1}^n k^c = O(n^{c+1})$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> i) $T(n) = T(n − 1) + c^n$ , where $c > 1$ is a constant.

$T(n) = T(-1) + \sum_{k=0}^n c^k = T(-1) + \frac{c^{n+1} - 1}{c - 1} = O(c^n)$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> j) $T(n) = 2T(n − 1) + 1$.

$T(n) = \sum_{k=0}^{n} 2^k = 2^{n+1} = O(2^n)$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> k) $T(n) = T(\sqrt{n}) + 1$.

$T(n) = k + T(b)$ where $n^{1/2^k} < b$ so $k = \log_2(\log(b))$ therefore $T(n) = O(\log(\log(n)))$. 

## Dynamic Programming (Chapter 6) - filtered

> [!question] 6.5 Pebbling a checkerboard.
> We are given a checkerboard which has $4$ rows and $n$ columns, and has an integer written in each square. We are also given a set of $2n$ pebbles, and we want to place some or all of these on the checkerboard (each pebble can be placed on exactly one square) so as to maximize the sum of the integers in the squares that are covered by pebbles. There is one constraint: for a placement of pebbles to be legal, no two of them can be on horizontally or vertically adjacent squares (diagonal adjacency is fine). 
> 
> (a) Determine the number of legal patterns that can occur in any column (in isolation, ignoring the pebbles in adjacent columns) and describe these patterns. 
> 
> Call two patterns compatible if they can be placed on adjacent columns to form a legal placement. Let us consider subproblems consisting of the first $k$ columns $1 \leq k \leq n$. Each subproblem can be assigned a type, which is the pattern occurring in the last column. 
> 
> (b) Using the notions of compatibility and type, give an $O(n)$-time dynamic programming algorithm for computing an optimal placement.

a) There are 7 legal positions of pebbles. We represent the positions by the row numbers with a pebble, they are $P = \{p_{\emptyset}, p_{0}, p_{1}, p_2, p_3, p_{0,2}, p_{1,3}\}$. Then the legal following positions given the column to the right are

$$P_p = \begin{cases} P & \mbox{if } p = p_{\emptyset}\\ P \backslash \{p_i, p_{i, i\pm2}\} & \mbox{if } p = p_i\\ P \backslash\{p_{i,j}, p_i, p_j\} & \mbox{if } p = p_{i,j}\end{cases}.$$
b) Suppose we have a weight function $\hat{W}: [1, \ldots, n] \times [1,2,3,4] \rightarrow \mathbb{Z}$ which describes the weights, with $w(i,j)$ being the number on the $(i,j)$ checkerboard. Define a function $W: [1, \ldots, n] \times P \rightarrow \mathbb{Z}$ where $W(i,p_S) = \sum_{j \in S} \hat{W}(j)$.

Define $T(i,p)$ with $i \in [1, \ldots, n]$ and $p \in P$ to be a maximum value in the checkerboard using the first $i$ columns with position $p$ in the $i$'th column.

Base case: Set $T(1,p) = W(1,p)$.

Recursion: Set $T(i,p) = \max_{q \in P_p}\{T(i-1,q)\} + W(i,p)$ for $1 < i \leq n$ and $p \in P$.

Solution: $\max_{p \in P} \{T(n,p)\}$  

## Correctness

Prove by induction. 

If $i =1$ then $T(1,p)$ as it has to use $p$ in the first column and that is the only column it is $W(1,p)$.

Suppose it is true for $k-1$ lets prove for $k$.

As $T(k,p)$ must use $p$ in the $k$'th column the solution is going to be $W(k,p)$ with a solution to the $k-1$'th problem.

The only valid possibilities for the $k-1$'th column are $P_p$ therefore it must use a maximal solution to $k-1$'th problem with one of the $q \in P_p$ in that column. These are exactly $T(i-1,q)$ by the induction hypothesis. 

So
$$T(k,p) = \max_{q \in P_p}\{T(i-1,q)\} + W(i,p)$$
giving the correctness of our solution at the $k$'th column.

By induction $T(i,p)$ is correct for all columns.

The correct solution to the problem must use one of $p \in P$ for the $n$'th column. Which would mean it would be a maximal solution for the $k$'th problem.

Therefore this is one of $T(n,p)$ by the correctness of $T$ giving our algorithm is correct on the whole problem.

## Pseudocode

```pseudocode
Checkerboard solver
Input: Function W: [1..n] x [1..4] -> Z.
Output: The maximum value putting the stones on the board.
	Define P to be the set of valid position
	Define P_p to be the set of compatible positions for an adjacent column 
		when it is next to a column with p in P in it.
	Set up T as a map from [1..n], P into Z.
	Set T[1,p] = sum_(i in p) W(1,i)
	for i = 2 -> n
		for p in P
			T[i, p] = sum_(j in p) W(i,j) + max_q in P_p T[i-1,q]
	return max_p in P T[n,p]
```

Lets analyse the run time of this algorithm.

Making the sets $P$ and $P_p$ take $O(1)$ time as they are the same for every run.

Defining $T[1,p]$ for each $p$ takes at most 2 looks ups and this is carried out $7$ times so takes $O(1)$ time.

We loop over $i$ being $2$ to $n$ which is $n-1$ steps. We loop over $p \in P$ which is 7 steps. We calculate the sum of elements in $p$ which takes at most 2 loops ups. Then we calculate the max over $P_p$ which takes at most $7$ look ups.

In total this loop is at most $(n-1) \cdot 7 \cdot (2 + 7)$ look ups which is $O(n)$.

Returning the solution involves $7$ look ups which is $O(1)$.

The run time of this algorithm is $O(1) + O(1) + O(n) + O(1) = O(n)$.

> [!question] 6.6 Multiplication operation
> Let us define a multiplication operation on three symbols $a, b, c$ according to the following table; thus $ab = b,\ ba = c$, and so on. Notice that the multiplication operation defined by the table is neither associative nor commutative.
> $$\begin{tabular}{c|ccc} & a & b & c\\\hline a & b & b & a\\ b & c & b & a\\ c & a & c & c \end{tabular}$$
> 
 
**6.6** (this problem is like the Matrix Multiplication! A Y/N table should do it, but it may help to add a third dimension accounting for the symbol you wish to reduce to).

6.7, 6.9, 6.22 (hint included in the problem).

**6.25-6.30** Note: These are a bit harder, but definitely nice problems.

## Divide and Conquer (Chapter 2)

2.4 (recurrences), 2.10 (FFT), 2.12 (recurrences), 2.15 (strange ... skip?), 2.16 (hw 2), 2.17 (D&C) 2.18(theory), 2.19 (merge d&c), 2.20(Sorting algorithm)

- Look into sorting algorithms more generally.

2.22 (you should come up with two solutions: a straightforward Median of medians application and a "merging" approach.)

2.23 (part (a) should follow using a D&C standard, part (b) is more demanding)

2.27-2.28 (if you are curious about further extensions of the Fast Multiplication Algorithm)

2.32 (a very nice application of D&C in a geometric setting, this problem is harder and its runtime analysis is above what we had covered in class so far)