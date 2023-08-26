---
aliases: []
type: lecture
publish: true
created: 2023-08-26
last_edited: 2023-08-26
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 1
chatgpt: false
---
# Week 1 - Dynamic Programming

[[Dynamic programming]] is a method to speed up [[Recursion|recursion]] especially when the recursive algorithm computes the same step multiple times.

## Example - [[Fibonacci sequence]] by [[Recursion|recursion]] 

Let's calculate the [[Fibonacci sequence]], for the $n^{th}$ step of the [[Fibonacci sequence]] called $Fib(n)$ it is calculated as
$$
Fib(n) = \begin{cases} 0 & \mbox{ if n = 0}\\ 1 & \mbox{ if n = 1}\\ Fib(n-1) + Fib(n-2) & \mbox{ if n > 1}\end{cases} \ .
$$
This can be done recursively as follows:

```python
def fibonacci_1(n: int) -> int:
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
```

If we say $T(n)$ is the [[Run time complexity|run time]] of this algorithm on input $n$, then $T(0) = T(1) = 1$ for the base cases. From this we can [[Induction|inductively]] prove that
$$
Fib(n) \leq T(n) \leq Fib(n) + 1
$$
giving that $T(n) = O(Fib(n)) \approx \frac{\phi^n}{\sqrt{5}}$, where $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$ the [[golden ratio]]. In other other words, this algorithm is exponential in $n$.

This inefficiency is due to computing the same [[Fibonacci sequence|Fibonacci number]] multiple times.

## Example - [[Fibonacci sequence]] by [[Dynamic programming|dynamic programming]]

Instead of starting at the end of the [[Fibonacci sequence|Fibonacci numbers]] this time we will start at the beginning and save past results in an array. 

```python
def fibonacci_2(n:int) -> int:
	fibonacci_numbers = [0, 1]
	for i in range(2,n):
		fibonacci_numbers.append(
			fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
		)
	return fibonacci_numbers[n]
```

This was done [[Iterative algorithms|iteratively]] so the [[Run time complexity|run time]] is easy to compute. The set up step takes $O(1)$ time, then the loop takes $(n-2)O(1) = O(n)$ time giving the run time to be $O(1) + O(n) = O(n)$.

## Dynamic programming

The key features of [[Dynamic programming]] is that there is no [[Recursion|recursion]] in the algorithm it is fully [[Iterative algorithms|iterative]].

There is another method to get around the inefficiencies of [[Recursion|recursion]] called [[Memoization]]. This is where you still use [[Recursion|recursion]] but you use a hash table to store previously computed values.

The benefits to [[Dynamic programming]] over [[Memoization]] are:

- Some people would say the algorithms are more beautiful,
- They are faster as there is less overhead associated to [[Recursion|recursion]], and
- It is much simpler to analyse the [[Run time complexity|run time]] of [[Dynamic programming|dynamic programs]] as they are [[Iterative algorithms|iterative]].

## Longest increasing subsequence

We are provided with a [[sequence]] of $n$ numbers $a_1, a_2, \ldots, a_n$ and the goal is to find the length of the longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] in $\{a_i\}_{i=1}^n$.

### Example

Consider the [[sequence]] 
$$
5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3
$$
here the longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] is
$$-3, 1, 4, 5, 8, 9$$
so has length 6. So the answer to this problem for the example is 6.

> [!Note] We don't need to find the sequence to answer the question.

## [[Dynamic programming]] approach

### Step 1: define subproblem in words

For [[Fibonacci sequence|Fibonacci numbers]] this was simply to calculate $Fib(n)$.

For the longest increasing subsequence (LIS) problem, let $L(i)$ = the LIS on $a_1, \ldots, a_i$ that ends with $a_i$.

>[!warning] It must end with $a_i$
>This definition of $L(i)$ was chosen carefully, so that we can frame the solution of $L(i)$ in terms of previous $L(j)$. If you drop this condition you can't do that.

### Step 2: define recursive relation

For [[Fibonacci sequence|Fibonacci numbers]] this was $Fib(n) = Fib(n-1) + Fib(n-2)$.

For the LIS problem, we calculate $L^{\ast}(i)$ iteratively by using the following formula
$$L(i) = 1 + \max \{0, \ L(j) \ \vert \ 1 \leq j < i \mbox{ and } a_j < a_i \}.$$
i.e. find the longest increasing subsequence that started with a number before your current term such that the end number is less than your current term.

## Back to the example

We do this iteratively

| $a_i$                         | 5   | 7   | 4   | -3  | 9   | 1   | 10  | 4   | 5   | 8   | 9   | 3   |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $L(i)$                 | 1   | 2   | 1   | 1   | 3   | 2   | 4   | 3   | 4   | 5   | 6   | 2   |
| $j$ we got $L(i)$ from | -   | 1   | -   | -   | 2   | 4   | 5   | 6   | 8   | 9   | 10  | 6    |

Therefore we work out that the LIS for this sequence is 6 as that is the maximum value of $L(i)$ and the LIS must end with some number!

So lets write this as an algorithm.

```python
def get_last_best_solution_less_than_current_value(
	past_sequence: list,
	past_solutions:list,
	value: int
) -> int:
	feasible_solutions = []
	for solution, past_value in zip(past_solutions, past_sequence):
		if past_value < value:
			feasible_solutions.append(solution)
	return max(feasible_solutions, default = 0)
	

def length_of_the_longest_increasing_subsequence(sequence: list) -> int:
	lis_solutions = []
	for index, value in enumerate(sequence):
		next_solution = 1 + get_last_best_solution_less_than_current_value(
			sequence[:index],
			lis_solutions,
			value
		)
		lis_solutions.append(next_solution)
	return max(lis_solutions, default = 0)

if __name__ == "__main__":
    lis_solution = length_of_the_longest_increasing_subsequence(
	    [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
	)
	print("The length of the longest increasing subsequence is", lis_solution)
```

### Run time of solution

Now lets break these sub-functions into parts $get\_last\_best\_solution\_less\_than\_current\_value$ goes through all past entries and run some checks, then it takes a max over that set of entries. This takes at most $O(2k)$ operations so, 
$$O(get\_last\_best\_solution\_less\_than\_current\_value(k)) = O(k)$$
Now lets look at $length\_of\_the\_longest\_increasing\_subsequence(n)$ this loops through all $n$ elements running $get\_last\_best\_solution\_less\_than\_current\_value$ on a list of size $k$ where $k$ is the value of the element right now. Lastly it finds the max of a list of length $n$ which is $O(n)$, so:
$$\begin{align*}
O(length\_of\_the\_longest\_increasing\_subsequence(n)) & = \sum_{k=0}^{n-1} O(k) + O(n)\\ 
& = O((n-1)n/2) + O(n)\\
& = O(n^2)\end{align*}$$
giving the run time of this algorithm to be $O(n^2)$.

## Largest common subsequence (LCS)

Given two [[Sequence|sequences]] $X =\{x_i\}_{i=1}^n$ and $Y = \{y_i\}_{i=1}^n$ the goals is to find the length of the longest [[Sequence|sequence]] which is a [[Subsequence|subsequence]] of both $X$ and $Y$.

#### Example

Let
$$X = BCDBCDA, \mbox{ and } Y=ABECBAB.$$
then the largest common subsequence is $BCBA$ of length 4.

>[!Note] This is what the [[Unix]] command diff does to two files.

### Design attempt for this problem

#### Step 1: define subproblem in words

$X\_len(k)$ = the longest common substring with $\{x_i\}_{i=1}^k$ and $Y$ using $x_i$.
$X\_pos(k)$= the last position of the longest common substring with $\{x_i\}_{i=1}^k$ and $Y$ at $Y$.

#### Step 2: define recursive relation

$$X_len(k) = \begin{cases} 0 \mbox{ if } x_k \not \in Y\\ 1 + \max\{0, \}