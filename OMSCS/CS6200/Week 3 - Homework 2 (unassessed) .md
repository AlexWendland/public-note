---
aliases: null
chatgpt: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-09-11
last_edited: 2023-09-11
publish: false
tags:
  - OMSCS
type: exercise
week: '3'
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
> Give an algorithm that takes as input a directed graph with positive edge lengths, and returns the length of the shortest cycle in the graph (if the graph is acyclic, it should say so). Your algorithm should take time at mostÂ $O(\vert V \vert^3)$.

Run the [[Floyd-Warshall algorithm]] and return the length of the minimum entry on the diagonal. If they are all infinite then return that it is acyclic.

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction).
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers.
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{kâˆ’1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits.
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

$$\begin{align*}Â T(n) & = 2T(n/3) + 1\\
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

$$\begin{align*}Â
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

$$\begin{align*}Â
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

$$\begin{align*}Â
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

$$\begin{align*}Â
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
> h) $T(n) = T(n âˆ’ 1) + 2$

$T(n) = 2n + T(0) = O(n)$.

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> g) $T(n) = T(n âˆ’ 1) + n^c$ , where $c \geq 1$ is a constant.

$T(n) = T(0) + \sum_{k=1}^n k^c = O(n^{c+1})$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> i) $T(n) = T(n âˆ’ 1) + c^n$ , where $c > 1$ is a constant.

$T(n) = T(-1) + \sum_{k=0}^n c^k = T(-1) + \frac{c^{n+1} - 1}{c - 1} = O(c^n)$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> j) $T(n) = 2T(n âˆ’ 1) + 1$.

$T(n) = \sum_{k=0}^{n} 2^k = 2^{n+1} = O(2^n)$

> [!question] 2.5 Solving recurrence
> Solve the following recurrence relations and give a $\Theta$ bound for each of them.
> k) $T(n) = T(\sqrt{n}) + 1$.

$T(n) = k + T(b)$ where $n^{1/2^k} < b$ so $k = \log_2(\log(b))$ therefore $T(n) = O(\log(\log(n)))$.

> [!question] 2.17 Index matching
> Given a sorted array of distinct integers $A[1, \ldots , n]$, you want to find out whether there is an index $i$ for which $A[i] = i$. Give a divide-and-conquer algorithm that runs in time $O(\log(n))$.

First lest examine a subproblem.

## Subproblem

Given an array $B[1, \ldots, k]$ with $k \geq 2$ and a value $a$ where $B[1] \leq a$ and $B[k] > a+k$ is there an index $i$ such that $a + i = B[i]$. If not return False, if there is return $a+k$.

## Algorithm

Define this algorithm as $Sub(B,a)$.

If $k = 2$ return False. If $k = 3$ return $a + 2$ if $B[2] = a + 2$ otherwise return False.

Examine the middle element $m = \lceil \frac{k}{2} \rceil$ if $B[m] = a + m$ return $a + m$.

If $B[m] < a + m$ return $Sub(B[m, \ldots, k], a + m - 1)$ else return $Sub(B[1, \ldots, m], a)$.

## Overall Algorithm

If $A[1]$ is greater than $1$, return False. If it is equal to 1 return 1.

If $A[n]$ is less than $n$, return False. If it is equal to $n$ return $n$.

Otherwise return $Sub(A, 0)$.

## Correctness

First prove a sublemma

> [!important] Lemma
> If $A[i] = i$ then for all $k > 1$ we have $A[i + k] \geq i + k$ and $A[i - k] \leq i - k$.

As $A$ is sorted and contains distinct integers we have that $A[j+1] \geq A[j] + 1$ which can be expanded to $A[j + k] \geq A[j] + k$ similarly $A[j - k] \leq A[k] - k$ for $k \geq 1$.

Therefore as $A[i] = i$ we get $A[i + k] \geq A[i] + k = i + k$ similarly $A[i - k] \leq A[i] - k = i - k$. Giving the desired result.

$\square$

### Sub problem

First lets prove $Sub(B,a)$ is correct. We prove this by induction on $k$.

If $k = 2$ as $B[1] \leq a$ and $B[2] > a + 2$ then neither element satisfies $B[i] = a + i$. So it is correct to return False.

If $k = 3$ by the argument of $k=2$ the only element that can satisfy $B[i] = a+i$ is $i=2$ which it checks. So it returns the correct result in this case.

Suppose it is true for all $k < t$.

Let $B$ have size $t > 3$.

If the $m$'th element satisfies $B[m] = i + m$ then we need to return it which we do.

Suppose $B[m] < i + m$.

If $B[i] = i + a$ for $1 \leq i < m$ then $B[m] \geq i + m$ by the lemma. Therefore $B[i] \not = i + a$ for $1 \leq i <m$. So we are safe to discount these elements and only look at $B[m, \ldots, k]$.

Note that $B[m, \ldots, k]$ now satisfies the requirements of the sub problem with $a + m - 1$.
1. $B[k] > a + k = (a + m - 1) + (k - m + 1)$,
2. $B[m] \leq a + m - 1$,
3. $k - m + 1 \geq k/2 + 1 \geq 2$ as $k \geq 4$.
So by the induction hypothesis the solution to $Sub(B[m, \ldots, k], a + m - 1)$ is the solution we desire.

Suppose $B[m] > i + m$.

We can now discount the elements $B[m, \ldots, k]$ similarly to the logic above.

Note the $B[1, \ldots, m]$ now satisfies the requirements of the sub problem with $a$.
1. $B[1] \leq a$ from before,
2. $B[m] > i + m$,
3. m \geq k/2 \geq 2$ as $k \geq 4$.
So by the induction hypothesis the solution to $Sub(B[1, \ldots, m], a)$ is the required solution.

Therefore we have the correct solution on $B$ of size $t$ and from induction it $Sub$ correctly solves the subproblem.

### Full algorithm

Note from the lemma if $A[1] > 1$ or $A[n] < n$ then there is no correct solution.

If $k = 1$ or $k = 2$ we have checked both elements of being the correct form, so we have solved the problem. Therefore we will terminate here in this case.

Note $A$ with 0 now satisfies the subproblem as
1. $A[1] \leq 0$
2. $A[n] > n$,
3. $k > 2$
So $Sub(A,0)$ returns the correct result.

## Run time analysis

Let $T(n)$ be the run time of this algorithm. For $T(1)$ and $T(2)$ it takes 2 checks so $T(1) = T(2) = 2$.

For larger $n$ either it takes $2$ check and we terminate immediately or we run $Sub$.

Functionally $Sub$ is just binary search so $Sub$ takes $O(\log(n))$ time.

This gives $T(n) = O(\log(n))$.

# UNSOLVED QUESTIONS

## Divide and Conquer (Chapter 2)

2.4 (recurrences), 2.10 (FFT), 2.12 (recurrences), 2.15 (strange ... skip?), 2.18(theory), 2.19 (merge d&c), 2.20(Sorting algorithm)

- Look into sorting algorithms more generally.

2.22 (you should come up with two solutions: a straightforward Median of medians application and a "merging" approach.)

2.23 (part (a) should follow using a D&C standard, part (b) is more demanding)

2.27-2.28 (if you are curious about further extensions of the Fast Multiplication Algorithm)

2.32 (a very nice application of D&C in a geometric setting, this problem is harder and its runtime analysis is above what we had covered in class so far)
