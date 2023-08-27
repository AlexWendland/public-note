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

> [!example] [[Fibonacci sequence]] by [[Recursion|recursion]] 
>
>Let's calculate the [[Fibonacci sequence]], for the $n^{th}$ step of the [[Fibonacci sequence]] called $Fib(n)$ it is calculated as
>$$Fib(n) = \begin{cases} 0 & \mbox{ if n = 0}\\ 1 & \mbox{ if n = 1}\\ Fib(n-1) + Fib(n-2) & \mbox{ if n > 1}\end{cases} \ .$$
>This can be done recursively as follows:
>
>```python
>def fibonacci_1(n: int) -> int:
>	if n <= 0:
>		return 0
>	if n == 1:
>		return 1
>	return fibonacci(n-1) + fibonacci(n-2)
>```
>
>If we say $T(n)$ is the [[Run time complexity|run time]] of this algorithm on input $n$, then $T(0) = T(1) = 1$ for the base cases. From this we can [[Induction|inductively]] prove that
>$$Fib(n) \leq T(n) \leq Fib(n) + 1$$
>giving that $T(n) = O(Fib(n)) \approx \frac{\phi^n}{\sqrt{5}}$, where $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$ the [[golden ratio]]. In other other words, this algorithm is exponential in $n$.
>
>This inefficiency is due to computing the same [[Fibonacci sequence|Fibonacci number]] multiple times.

Lets try to do this [[Iterative algorithms|iteratively]] instead of [[Recursion|recursively]].

> [!Example] [[Fibonacci sequence]] by [[Dynamic programming|dynamic programming]]
>
>Instead of starting at the end of the [[Fibonacci sequence|Fibonacci numbers]] this time we will start at the beginning and save past results in an array. 
> ```python
>def fibonacci_2(n:int) -> int:
>	fibonacci_numbers = [0, 1]
>	for i in range(2,n):
>		fibonacci_numbers.append(
>			fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
>		)
>	return fibonacci_numbers[n]
>```
>
>This was done [[Iterative algorithms|iteratively]] so the [[Run time complexity|run time]] is easy to compute. The set up step takes $O(1)$ time, then the loop takes $(n-2)O(1) = O(n)$ time giving the run time to be $O(1) + O(n) = O(n)$.

## Dynamic programming

The key features of [[Dynamic programming]] is that there is no [[Recursion|recursion]] in the algorithm it is fully [[Iterative algorithms|iterative]].

There is another method to get around the inefficiencies of [[Recursion|recursion]] called [[Memoization]]. This is where you still use [[Recursion|recursion]] but you use a hash table to store previously computed values.

The benefits to [[Dynamic programming]] over [[Memoization]] are:

- Some people would say the algorithms are more beautiful,
- They are faster as there is less overhead associated to [[Recursion|recursion]], and
- It is much simpler to analyse the [[Run time complexity|run time]] of [[Dynamic programming|dynamic programs]] as they are [[Iterative algorithms|iterative]].

## Longest increasing subsequence

We are provided with a [[sequence]] of $n$ numbers $a_1, a_2, \ldots, a_n$ and the goal is to find the length of the longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] in $\{a_i\}_{i=1}^n$.

> [!example] Longest increasing subsequence
>Consider the [[sequence]] 
> $$5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3$$
>here the longest [[Increasing sequence|increasing]] [[Subsequence|subsequence]] is
>$$-3, 1, 4, 5, 8, 9$$
>so has length 6. So the answer to this problem for the example is 6.
>
>**We don't need to find the sequence to answer the question.**

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

> [!example] Back to the example: Longest increasing subsequence
>
>We do this iteratively
>
>| $a_i$                         | 5   | 7   | 4   | -3  | 9   | 1   | 10  | 4   | 5   | 8   | 9   | 3   |
>| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
>| $L(i)$                 | 1   | 2   | 1   | 1   | 3   | 2   | 4   | 3   | 4   | 5   | 6   | 2   |
>| $j$ we got $L(i)$ from | -   | 1   | -   | -   | 2   | 4   | 5   | 6   | 8   | 9   | 10  | 6    |
>
Therefore we work out that the LIS for this sequence is 6 as that is the maximum value of $L(i)$ and the LIS must end with some number!
>
>So lets write this as an algorithm.
>
>```python
>def get_last_best_solution_less_than_current_value(
>	past_sequence: list,
>	past_solutions:list,
>	value: int
>) -> int:
>	feasible_solutions = []
>	for solution, past_value in zip(past_solutions, past_sequence):
>		if past_value < value:
>			feasible_solutions.append(solution)
>	return max(feasible_solutions, default = 0)
>	
>
>def length_of_the_longest_increasing_subsequence(sequence: list) -> int:
>	lis_solutions = []
>	for index, value in enumerate(sequence):
>		next_solution = 1 + get_last_best_solution_less_than_current_value(
>			sequence[:index],
>			lis_solutions,
>			value
>		)
>		lis_solutions.append(next_solution)
>	return max(lis_solutions, default = 0)
>
>if __name__ == "__main__":
 >   lis_solution = length_of_the_longest_increasing_subsequence(
>	    [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
>	)
>	print("The length of the longest increasing subsequence is", lis_solution)
>```
>
>To calculate the Run time of solution lets break these sub-functions into parts $get\_last\_best\_solution\_less\_than\_current\_value$ goes through all past entries and run some checks, then it takes a max over that set of entries. This takes at most $O(2k)$ operations so, 
>$$O(get\_last\_best\_solution\_less\_than\_current\_value(k)) = O(k)$$
>Now lets look at $length\_of\_the\_longest\_increasing\_subsequence(n)$ this loops through all $n$ elements running $get\_last\_best\_solution\_less\_than\_current\_value$ on a list of size $k$ where $k$ is the value of the element right now. Lastly it finds the max of a list of length $n$ which is $O(n)$, so:
>$$\begin{align*}
>O(length\_of\_the\_longest\_increasing\_subsequence(n)) & = \sum_{k=0}^{n-1} O(k) + O(n)\\ 
>& = O((n-1)n/2) + O(n)\\
>& = O(n^2)\end{align*}$$
>giving the run time of this algorithm to be $O(n^2)$.

## Largest common subsequence (LCS)

Given two [[Sequence|sequences]] $X =\{x_i\}_{i=1}^n$ and $Y = \{y_i\}_{i=1}^n$ the goals is to find the length of the longest [[Sequence|sequence]] which is a [[Subsequence|subsequence]] of both $X$ and $Y$.

> [!Example] Largest common subsequence
>
>Let
>$$X = BCDBCDA, \mbox{ and } Y=ABECBAB.$$
>then the largest common subsequence is $BCBA$ of length 4.

>[!Note] This is what the [[Unix]] command diff does to two files.

### Design attempt for this problem (my solution)

#### Step 1: define subproblem in words

$X\_len(k)$ = the longest common substring with $\{x_i\}_{i=1}^k$ and $Y$ using $x_i$.
$X\_pos(k)$= the last position of the longest common substring with $\{x_i\}_{i=1}^k$ and $Y$ at $Y$.

#### Step 2: define recursive relation

$$X\_len(k) = \begin{cases} 0 & \mbox{if } x_k \not \in Y\\ 1 + \max\{0, X\_len(j) \ \vert \ 1 \leq j \leq k \mbox{ and } x_k \in Y[X\_pos(j)+1:] \ \} & \mbox{otherwise} \end{cases}$$
$$ X\_pos(k) = \begin{cases} 0 & \mbox{if } x_k \not \in Y\\ \min\{j \ \vert \ y_j = x_k\} & \mbox{if } X\_len(k) = 1\\ \min \left \{ j \ \vert \substack{ \ y_j = x_k \mbox{ and } \exists \ r \mbox{ where }  \\ X\_len(k) = X\_len(r) + 1 \mbox{ and } j > X\_pos(r)} \right \} & \mbox{otherwise} \end{cases}$$

>[!warning] I think this would work but the lecturers solution is way better!

### Design attempt for this problem (lecturers)

#### Step 1: define subproblem in words

Let $L(a,b)$ = the longest common substring with $\{x_i\}_{i=1}^{a}$ and $\{y_j\}_{j=1}^{b}$ 

#### Step 2: define recursive relation

Set $L(i,0) = L(0,i) = 0$ for all $1 \leq i \leq n$.

Then set
$$L(i,j) = \begin{cases} 1 + L(i-1, j-1) & \mbox{if } x_i = y_j\\ \max\{L(i,j-1), L(i-1, j)\} & \mbox{otherwise} \end{cases}$$
>[!Note] Why does this work?
> If $x_i = y_j$ you can always just add the $x_i$/$y_j$ string to the longest common subproblem found in $L(i-1, j-1)$. Note that if a larger one existed for $L(i,j)$ not using both $x_i$ and $y_j$ it must at least use one of them. However if this was the case we could switch to using both $x_i$ and $y_j$ and we have found a larger common substring for $L(i-1,j-1)$.
> 
> If $x_i \not = y_j$ then the largest common substring must use at most one of $x_i$ or $y_j$. Therefore the solution can be found in $L(i-1,j)$ or $L(i,j-1)$.

Then lets turn this into code. 

```python
from typing import List, Any

def _get_solution(
	first_value: int, 
	second_value: int, 
	left_solution: int, 
	above_solution: int, 
	diagonal_solution: int
) -> int:
	"""
	Implements fill logic as described by L(i,j) above.
	"""
	if first_value == second_value:
		return 1 + diagonal_solution
	return max(left_solution, above_solution)

def common_longest_subsequence(
	first_sequence: List[Any], 
	second_sequence: List[Any]
) -> int:
	# Set the (n+1, m+1) matrix to all 0's first. (Some strang)
	[
		[0 for _ in range(len(second_sequence)+1)] 
		for _ in range(len(first_sequence)+1)
	]
	# This is used to track the max
	max_value = 0
	for first_index in range(len(first_sequence)):
		for second_index in range(len(second_sequence)):
			solutions[first_index+1][second_index+1] = _get_solution(
				first_sequence[first_index],
				second_sequence[second_index],
				solutions[first_index][second_index+1],
				solutions[first_index+1][second_index],
				solutions[first_index][second_index]
			)
			max_value = max(
				max_value, 
				solutions[first_index+1][second_index+1]
			)
	return max_value

if __name__ == "__main__":
	first_sequence = "BCDBCDA"
	second_sequence = "ABECBAB"
	solution = common_longest_subsequence(first_sequence, second_sequence)
	print(
		f"The length of longest common subsequence of {first_sequence} "
		f"and {second_sequence} is {solution}."
	)
```

The [[Run time complexity|runtime]] of my algorithm can be broken down into 2 main steps. (For this I assume the [[Sequence|sequences]] are of the same length $n$). Setting up the matrix which is $n^2$ operations and running the main for loop which has $n^2$ steps and uses $O(1)$ operations in each step. Giving the [[Run time complexity|run time]] to be $O(n^2) + O(n^2) = O(n^2)$. 

## Further practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 6.1 Contiguous Subsequence
>A contiguous subsequence of a list $S$ is a subsequence made up of consecutive elements of $S$. 
>
>For instance, if $S$ is 
>$$5, 15, −30, 10, −5, 40, 10,$$ 
>then 15, −30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a linear-time algorithm for the following task: 
>
>Input: A list of numbers, $a_1, a_2, \ldots , a_n$. 
>
>Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero). 
>
>For the preceding example, the answer would be 10, −5, 40, 10, with a sum of 55.
>
>(Hint: For each $j \in \{1, 2, \ldots , n\}$, consider contiguous subsequence's ending exactly at position $j$.)

>[!question] 6.2 hotel stops
>You are going on a long trip. You start on the road at mile post 0. Along the way there are $n$ hotels, at mile posts $a_1 < a_2 < \ldots < a_n$, where each $a_i$ is measured from the starting point. The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at. You must stop at the final hotel (at distance $a_n$), which is your destination. 
>
>You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels). If you travel $x$ miles during a day, the penalty for that day is $(200 − x)^2$. You want to plan your trip so as to minimize the total penalty —that is, the sum, over all travel days, of the daily penalties. 
>
>Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.

> [!question] 6.3 Yuckdonald's
> Yuckdonald’s is considering opening a series of restaurants along Quaint Valley Highway (QVH). The n possible locations are along a straight line, and the distances of these locations from the start of QVH are, in miles and in increasing order, m1, m2, . . . , mn. The constraints are as follows: 
> 
> - At each location, Yuckdonald’s may open at most one restaurant. The expected profit from opening a restaurant at location i is pi , where pi > 0 and i = 1, 2, . . . , n.
> - Any two restaurants should be at least k miles apart, where k is a positive integer.
> 
> Give an efficient algorithm to compute the maximum expected total profit subject to the given constraints.

> [!question] 6.4 String of words
> You are given a string of n characters s[1 . . . n], which you believe to be a corrupted text document in which all punctuation has vanished (so that it looks something like “itwasthebestoftimes...”). You wish to reconstruct the document using a dictionary, which is available in the form of a Boolean function dict(·): for any string w,
> $$dict(w) = \begin{cases} true & \mbox{if w is a valid word}\\ false & \mbox{otherwise}\end{cases}.$$ 
> 1. Give a dynamic programming algorithm that determines whether the string s[·] can be reconstituted as a sequence of valid words. The running time should be at most O(n 2 ), assuming calls to dict take unit time.
> 2. In the event that the string is valid, make your algorithm output the corresponding sequence of words.

>[!question] 6.11 Longest common **substring**) - altered
>Given two strings x = x1x2 · · · xn and y = y1y2 · · · ym, we wish to find the length of their longest common **substring**, that is, the largest k for which there are indices i and j with xi xi+1 · · · xi+k-1 = yj yj+1 · · · yj+k-1. Show how to do this, what is the time complexity of this?

## Summary

To approach [[Dynamic programming]] problems follow these steps

1. Define a subproblem in words.
	1. Set up an array to fill in with a clearly defined meaning. 
2. Define recurrence relation.
	1. This is where you define solving a higher case in terms of the smaller cases.
3. Define how you get the overall solution from the subproblem you have defined.
	1. You may need to take a max or just look at the last element.

Note that sometimes you may need to increase the strength of the subproblem or increase it size. 