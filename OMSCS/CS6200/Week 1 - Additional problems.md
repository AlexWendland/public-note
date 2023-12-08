---
aliases: []
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-08-27
last_edited: 2023-12-03
publish: false
tags:
  - OMSCS
type: exercises
week: 1
---
# Substring with max sum

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
>(Hint: For each $j \in \{1, 2, \ldots , n\}$, consider contiguous subsequences ending exactly at position $j$.)

Subproblem:
Let $L(i)$ = the largest positive contiguous subsequence end with $a_i$ (if non-empty).

Solution:
The max of $L(i)$.

Recursion:
$L(i) = \max\{0, L(i-1) + a_i\}$
where $L(0) = 0$.

This runs in $O(n)$ time.

>[!question] 6.2 hotel stops
>You are going on a long trip. You start on the road at mile post 0. Along the way there are $n$ hotels, at mile posts $a_1 < a_2 < \ldots < a_n$, where each $a_i$ is measured from the starting point. The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at. You must stop at the final hotel (at distance $a_n$), which is your destination.
>
>You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels). If you travel $x$ miles during a day, the penalty for that day is $(200 − x)^2$. You want to plan your trip so as to minimize the total penalty —that is, the sum, over all travel days, of the daily penalties.
>
>Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.

Subproblem:
Let $L(i)$ = minimum penalty stopping at hotel $a_i$.

Solution:
$L(n)$.

Recursion:
$L(k) = \min \{ L(i) + (200 - (a_k-a_i))^2 \vert 1 \leq i \leq k \}$

This runs in $O(n^2)$ time.

```python
from typing import List


def minimum_hotel_cost(sequence: List[int]) -> int:
    solutions = []

    for index, value in enumerate(sequence):
        best_solution = sequence[-1]**2
        for i in range(index):
            this_solution = 0
            this_solution += solutions[i]
            this_solution += (200 - (value - sequence[i])) ** 2
            best_solution = min(best_solution, this_solution)
        if index == 0:
            best_solution = 0
        solutions.append(best_solution)

    return solutions[-1]


if __name__ == "__main__":
    sequence = [0, 200, 300, 400, 500, 600]
    solution = minimum_hotel_cost(sequence)
    print(f"The minimum cost of the hotel is {solution}.")
```

> [!question] 6.3 Yuckdonald's
> Yuckdonald’s is considering opening a series of restaurants along Quaint Valley Highway (QVH). The $n$ possible locations are along a straight line, and the distances of these locations from the start of QVH are, in miles and in increasing order, $m_1 < m_2 \ldots  m_n$. The constraints are as follows:
>
> - At each location, Yuckdonald’s may open at most one restaurant. The expected profit from opening a restaurant at location $i$ is $p_i$ , where $p_i > 0$ and $i = 1, 2, . . . , n$.
> - Any two restaurants should be at least $k$ miles apart, where $k$ is a positive integer.
>
> Give an efficient algorithm to compute the maximum expected total profit subject to the given constraints.

Subproblem:
Let $L(k)$ = the maximum profit from opening restaurants in the first $k$ locations including opening one at $m_k$.

Solution:
The maximum of $L(k)$.

Recursion:
$L(a) = \max\{p_a, L(i) + p_a | 1 \leq i < a \mbox{ if } m_a - m_i > k \}$

This runs in $O(n^2)$ time.

```python
from typing import List


def solve_the_yuck_problem(distances: List[int], profits: List[int], space: int) -> int:
    """
    This function solves the yuck problem using dynamic programming.
    """
    solutions = []
    for index, (distance, profit) in enumerate(zip(distances, profits)):
        solutions.append(
            max(
                [
                    solutions[i] + profit
                    for i in range(index)
                    if distance - distances[i] >= space
                ]
                + [profit]
            )
        )
    print(solutions)
    return max(solutions)


if __name__ == "__main__":
    distances = [0, 1, 2, 3, 4, 5, 6]
    profits = [1, 1, 1, 1, 1, 1, 1]
    space = 2
    solution = solve_the_yuck_problem(distances, profits, space)
    print(f"The maximum profit is {solution}.")
```

> [!question] 6.4 String of words
> You are given a string of $n$ characters $s[1 \ldots n]$, which you believe to be a corrupted text document in which all punctuation has vanished (so that it looks something like “itwasthebestoftimes...�). You wish to reconstruct the document using a dictionary, which is available in the form of a Boolean function $dict( \cdot )$ for any string $w$,
> $$dict(w) = \begin{cases} true & \mbox{if w is a valid word}\\ false & \mbox{otherwise}\end{cases}.$$
> 1. Give a dynamic programming algorithm that determines whether the string $s[\cdot]$ can be reconstituted as a sequence of valid words. The running time should be at most $O(n^2)$, assuming calls to $dict$ take unit time.
> 2. In the event that the string is valid, make your algorithm output the corresponding sequence of words.

Question 1)

Subproblem:
Let $L(k)$ = whether the subword $s[1\ldots k]$ can be split into words.

Solution:
$L(n)$.

Recursion:
$L(k) = \bigwedge_{i=0}^{k-1} L(i) \land dict(s[i+1\ldots k])$
where $L(0)$ is true.

```python
from typing import List


def string_of_words(word_dictionary: List, string: str) -> bool:
    solution = []

    for index in range(len(string)):
        potenial_solutions = [
            solution[i] and (string[i + 1 : index + 1] in word_dictionary)
            for i in range(index)
        ] + [string[: index + 1] in word_dictionary]

        solution.append(any(potenial_solutions))

    return solution[-1]


if __name__ == "__main__":
    word_dictionary = ["aba", "aa"]

    print(string_of_words(word_dictionary, "abaabaaaba")) # False
```

Question 2)

```python
from typing import List, Optional


def string_of_words(word_dictionary: List, string: str) -> Optional[str]:
    solutions = []

    for index in range(len(string)):
        if string[: index + 1] in word_dictionary:
            solutions.append([string[: index + 1]])
        else:
            solution = []
            for i in range(index):
                if (
	                solutions[i]
	                and (string[i + 1 : index + 1] in word_dictionary)
	            ):
                    solution = solutions[i] + [string[i + 1 : index + 1]]
                    break
            solutions.append(solution)

    return solutions[-1]


if __name__ == "__main__":
    word_dictionary = ["aba", "abaa"]

    print(string_of_words(word_dictionary, "abaaaba"))
```

>[!question] 6.11 Longest common **substring** - altered
>Given two strings $x = x_1x_2 \ldots x_n$ and $y = y_1y_2 \ldots y_m$, we wish to find the length of their longest common **substring**, that is, the largest $k$ for which there are integers $i$ and $j$ with $x_{i+1} x_{i+2} \ldots x_{i+k} = y_{j+1} y_{j+2} \ldots y_{j+k}$. Show how to do this, what is the time complexity of this?

Subproblem:
Let $L(i,j)$ = the longest similar suffix of $x_1x_2 \ldots x_i$ and $y_1y_2 \ldots y_j$.

Solution:
$\max\{L(i,j) \vert 1 \leq i \leq n, \ 1 \leq j \leq m\}$

Recursion:
Let $L(i,0) = L(0,j) = 0$ then
$$L(i,j) = \begin{cases} 0 & \mbox{if } x_i \not = y_j\\ 1 + L(i-1,j-1) & \mbox{otherwise}\end{cases}.$$
```python
from typing import List, Any


def common_longest_subsequence(
    first_sequence: List[Any], second_sequence: List[Any]
) -> int:
    # Set the (n+1, m+1) matrix to all 0's first.
    solutions = [
        [0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)
    ]
    # This is used to track the max
    max_value = 0
    for first_index, first_value in enumerate(first_sequence):
        for second_index, second_value in enumerate(second_sequence):
            if first_value == second_value:
                solution = 1 + solutions[first_index][second_index]
                solutions[first_index + 1][second_index + 1] = solution
                max_value = max(max_value, solution)
    return max_value


if __name__ == "__main__":
    first_sequence = "BCDBABCDA"
    second_sequence = "ABECBAB"
    solution = common_longest_subsequence(first_sequence, second_sequence)
    print(
        f"The length of longest common substring of {first_sequence} "
        f"and {second_sequence} is {solution}."
    )
```
