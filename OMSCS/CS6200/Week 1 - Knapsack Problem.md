---
aliases: []
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-08-29
last_edited: 2023-11-11
publish: true
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - [[Knapsack Problem]]

![[Knapsack Problem#Statement]]

There are different versions of this problem:
- Where you can have at most one version of each object,
- Where you can have at most a given number of each object, and
- Where you can have an infinite amount of each object.

We will focus on the first problem for the next sections.

## Greedy solution

> [!example] Greed's downfall
> Suppose we have the following objects $o_i = (w_i, v_i)$
> $$O = \{(15,15), (12,10), (10,8), (5,1)\},$$
> with a max capacity of $B=22$.

Here a greedy algorithm would notice that the first object $(15,15)$ has the best value to weight ratio, so would fit one of those in the bag first. With 7 (=22-15) capacity left it would fit a single copy of the 4th object $(5,1)$ making the bag full.

This solution has a value of 16.

However, consider the solution using objects 2 and 3. This has weight 22, so in capacity but has value 18. This is 2 value higher than the greedy solution.

In summary greedy algorithm will not work for this problem.

## Dynamic programming approach (single version)

Lets define a [[Dynamic programming|dynamic program]] for the single copy Knapsack problem.

Let $K(i, b)$ be the max value using the first $0 \leq i \leq n$ objects with a bag of capacity $0 \leq b \leq B$.

The solution to the knapsack problem will then be $K(n,B)$.

To define the [[Recursion|recursion]] for this problem first set the base case $K(0,b) = K(i,0) = 0$. More generically define,
$$K(i,b) = \begin{cases} K(i-1,b) & \mbox{if } w_i > b\\ \max\{v_i + K(i-1,b-w_i), K(i-1,b)\} & \mbox{otherwise.} \end{cases}$$
The code for this program would look as follows.

```python
from typing import List
from dataclasses import dataclass


@dataclass
class KnapsackItem:
    weight: int
    value: int


class KnapsackSolver:
    solution_array: List[List[int]]
    items: List[KnapsackItem]
    capacity: int

    def solve(self, items: List[KnapsackItem], capacity: int) -> int:
        self._setup_problem(items, capacity)
        self._setup_solution_array()
		self._fill_array()
        return self.solution_array[-1][-1]

	def _fill_array() -> None:
		for item_number in range(1, len(self.items) + 1):
            for capacity_limit in range(1, self.capacity + 1):
                self.solution_array[item_number][
                    capacity_limit
                ] = self._solve_for_single_value(item_number, capacity_limit)

    def _setup_problem(self, items: List[KnapsackItem], capacity: int) -> None:
        self.items = items
        self.capacity = capacity

    def _setup_solution_array(self) -> None:
        self.solution_array = [
            [0 for _ in range(self.capacity + 1)]
            for _ in range(len(self.items) + 1)
        ]

    def _solve_for_single_value(
	    self,
	    item_number: int,
	    capacity_limit: int)
	-> int:
        current_item = self.items[item_number - 1]  # 0-indexed
        previous_solution = self.solution_array[item_number - 1][
	        capacity_limit
        ]
        if current_item.weight > capacity_limit:
            return previous_solution
        else:
            return max(
                [
                    previous_solution,
                    self.solution_array[item_number - 1][
                        capacity_limit - current_item.weight
                    ]
                    + current_item.value,
                ]
            )


if __name__ == "__main__":
    items = [
        KnapsackItem(weight=15, value=15),
        KnapsackItem(weight=12, value=10),
        KnapsackItem(weight=10, value=8),
        KnapsackItem(weight=5, value=1),
    ]
    capacity = 22
    solver = KnapsackSolver()
    print(solver.solve(items, capacity))
```

Lets look at the run time of each part of this algorithm. Let $n$ be the number of coins and $B$ be the total capacity.

First `_setup_problem` is $O(1)$ as it is just setting variables.

Whereas `_setup_solution_array` fills an $(n+1) \times (B+1)$ array that takes $O(nB)$ time.

The function `_solve_for_single_value` does 1 check and the at worst takes the max of 2 values so is $O(1)$. This is ran $nB$ times in `_fill_array` giving this a run time of $O(nB)$.

Combining these we have `solve` has run time $O(1) + O(nB) + O(nB) = O(nB)$.

## This is not polynomial in the input size

Even though $O(nB)$ is polynomial in $n$ and $B$ - the space it takes to represent $B$ is $\log_2(B)$. If we set $\overline{B} = \log_2(B)$ then the input size is $n, \overline{B}$ and the run time of this algorithm is $O(n 2^{\overline{B}})$ which is exponential.

The Knapsack is [[Nondeterministic Polynomial time (NP)]], meaning there is no polynomial algorithm for the knapsack problem.

## Dynamic programming approach (multi version)

### Attempt 1

We can modify what we did for the last problem to solve this problem.

Let $K(i, b)$ be the max value using the first $0 \leq i \leq n$ objects as many times as you would like with a bag of capacity $0 \leq b \leq B$.

The solution to the knapsack problem will then be $K(n,B)$.

To define the [[Recursion|recursion]] for this problem first set the base case $K(0,b) = K(i,0) = 0$. More generically define,
$$K(i,b) = \begin{cases} K(i-1,b) & \mbox{if } w_i > b\\ \max\{v_i + K(i,b-w_i), K(i-1,b)\} & \mbox{otherwise.} \end{cases}$$
>[!Note] Change in $K$'s parameters
>Notice that we either use the amount we had for not using the coin $i$ or we add $v_i$ to the max amount we could get *using* coin $i$ but with weight $b-w_i$.

This is a very small change and will have the same psudo-code and run time as the previous algorithm. Though there is a way to get rid of the $i$ parameter from our array.

### Attempt 2

As we can now use as many copies of which ever coin we would like we no longer need to track the coins at all.

Let $K(b)$ be the max value using all coins for a bag with capacity $0 \leq b \leq B$.

The solution to the knapsack problem will then be $K(B)$.

To define the [[Recursion|recursion]] for this problem we set
$$ K(b) = \max \{0, v_i + K(b - w_i) \vert 1 \leq i \leq n \mbox{ and } w_i \geq b \}$$
This has very simple psudo code

```pseudocode
Knapsack Repeat (w_1, ..., w_n, v_1, ..., v_n, B)
for b = 0 -> B
	k(b) = 0
	for i = 1 -> n
		if w_i <= b
			k(b) = max(k(b), v_i + k(b-w_i))
return k(B)
```

The run time of the algorithm is still $O(nb)$ but it's [[Spacial complexity|spacial complexity]] has reduced.

## Tracing the solution

You can alter the algorithm to store a second array $S$ which tracks the coin that was added to the solution to get the new optimum. Then by back tracking and subtracting the weight you will rebuild the set of coins.

## Further question

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 6.17 Making change I
>Given an unlimited supply of coins of denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$; that is, we wish to find a set of coins whose total value is $v$. This might not be possible: for instance, if the denominations are $5$ and $10$ then we can make change for $15$ but not for $12$. Give an $O(nv)$ dynamic-programming algorithm for the following problem.
>
>Input: $x_1, \ldots , x_n; v$.
>Question: Is it possible to make change for $v$ using coins of denominations $x_1, \ldots , x_n$?

>[!question] 6.18 Making change II
>Consider the following variation on the change-making problem (Exercise 6.17). Given coin denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$ but you are only allowed to use each denomination *at most once*. For instance, if the denominations are 1, 5, 10, 20, then you can make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 but not for 40 (because you can’t use 20 twice).
>
>Input: $x_1, \ldots , x_n; v$.
>Question: Is it possible to make change for $v$ using coins of denominations $x_1, \ldots , x_n$ only once?
>
>Show how to solve this problem in time O(nv).

>[!question] 6.19 Making change III
>Consider the following variation on the change-making problem (Exercise 6.17). Given coin denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$ but you can only use a *at most $k$ coins* (with repeats). For instance, if the denominations are $5$, $10$ with $k=6$ then you can make change for 55 with $5 \times 10 + 1 \times 5$ but not $65$.
>
>Input: $x_1, \ldots , x_n; k; v$.
>Question: Is it possible to make change for $v$ using at most $k$ coins of denominations $x_1, \ldots , x_n$?
