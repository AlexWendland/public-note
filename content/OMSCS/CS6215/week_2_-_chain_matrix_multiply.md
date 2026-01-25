---
aliases: []
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-08-31
date_checked:
draft: false
last_edited: 2023-12-03
tags:
  - OMSCS
title: Week 2 - Chain Matrix Multiply
type: lecture
week: 2
---

The goal is this problem is, given a number of [matrices](../../notes/matrix.md) what is the most efficient way to multiply them together?

Lets say we have [matrices](../../notes/matrix.md) $A$, $B$, $C$ and $D$ and they have different sizes such that we can multiply $A B C D$. Whilst matrix multiplication might be [associative](../../notes/associativity.md) there might be a more efficient way to multiply them together!

# Cost of multiplying two matrices

Lets say with have two [matrices](../../notes/matrix.md) $W$ (of size $a \times b$) and $Y$ (of size $b \times c$) we set their product to be $Z = WY$ (of size $a \times c$). To calculate a single entry in $Z$ we need to multiply a row of $W$ (of size $b$) with a column of $Y$ (of size $b$)
$$ z_{ij} = \sum_{k = 1}^b w_{ik} \ y_{kj}$$
which takes $b$ multiplications and $b-1$ additions. As $Z$ has size $a \times c$ this involves $abc$ multiplications and $a(b-1)c$ additions.

Here the multiplications are the more costly operations so this is what we will focus on for the cost of this single operation.

[Statement](../../notes/chain_multiply_problem.md#statement)

# Dynamic program set up

Let $C(i,j)$ with $1 \leq i \leq j \leq n$ be the minimum cost of multiplying $A_i A_{i+1} \ldots A_j$.

The solution to the problem will be $C(1,n)$.

The base case will be $C(i,i) = 0$.

The [recursion](../../notes/recursion.md) step will be
$$ C(i,j) = \min\{C(i,k) + C(k,j) + m_im_km_j \vert i < k < j\}.$$

To calculate $C(i,j)$ we need to [iteratively](../../notes/iterative_algorithms.md) increase the difference between $j - i$, the base case is $0$ the last case will be $n-1$.

```python
from typing import List


class UpperDiagonalMatrix:
    _matrix_size: int
    _matrix_values: List

    def __init__(self, matrix_size: int):
        self._matrix_size = matrix_size
        self._matrix_values = [0] * int((matrix_size * (matrix_size + 1)) / 2)

    def get(self, row: int, column: int) -> int:
        self._check_row_column(row, column)
        return self._matrix_values[self._get_index(row, column)]

    def set(self, row: int, column: int, value: int) -> None:
        self._check_row_column(row, column)
        self._matrix_values[self._get_index(row, column)] = value

    def _get_index(self, row: int, column: int) -> int:
        return self._get_column_offset(column) + (row - 1)

    def _get_column_offset(self, column: int) -> int:
        return int((column * (column - 1)) / 2)

    def _check_row_column(self, row: int, column: int) -> None:
        if row > column:
            raise ValueError("Row must be less than or equal to column")
        if row < 1:
            raise ValueError("Row must be greater than or equal to 0")
        if column > self._matrix_size:
            raise ValueError("Column must be less than matrix size")


class ChainMultiplySolver:
    _solution_array: UpperDiagonalMatrix
    _sizes: List[int]
    _number_of_matrices: int

    def solve(self, sizes: List[int]) -> int:
        self._setup_problem(sizes)
        self._fill_matrix_diagonally()
        return self._solution_array.get(1, self._number_of_matrices)

    def _setup_problem(self, sizes: List[int]) -> None:
        self._sizes = sizes
        self._number_of_matrices = len(sizes) - 1
        self._solution_array = UpperDiagonalMatrix(self._number_of_matrices)

    def _fill_matrix_diagonally(self) -> None:
        for difference in range(1, self._number_of_matrices):
            for lower_index in range(1, self._number_of_matrices-difference+1):
                upper_index = lower_index + difference
                self._solution_array.set(
                    lower_index,
                    upper_index,
                    self._solve_for_single_value(lower_index, upper_index),
                )

    def _solve_for_single_value(
	    self,
	    lower_index: int,
	    upper_index: int)
	-> int:
        return min(
            [
                self._solution_array.get(lower_index, split_index)
                + self._solution_array.get(split_index + 1, upper_index)
                + self._get_cost_of_multiplying_matrices(
                    lower_index, split_index, upper_index
                )
                for split_index in range(lower_index, upper_index)
            ]
        )

    def _get_cost_of_multiplying_matrices(
        self, left_index: int, middle_index: int, right_index: int
    ) -> int:
        return (
            self._sizes[left_index - 1]
            * self._sizes[middle_index]
            * self._sizes[right_index]
        )


if __name__ == "__main__":
    sizes = [5, 10, 5, 10, 5, 10, 5]
    solver = ChainMultiplySolver()
    print(solver.solve(sizes))
```

Lets look at the run time of this algorithm, let the number of sizes be $n$. First `_setup_problem` takes $O(n^2)$ as we have to fill half a matrix.

Working inside out, `_get_cost_of_multiplying_matrices` takes $O(1)$.  Then `_solve_for_single_value` calls `_get_cost_of_multiplying_matrices` up to $n$ times so takes $O(n)$. Lastly `_fill_matrix_diagonally` has two for loops calling `_solve_for_single_value` up to $n$ times each giving the run time of `_fill_matrix_diagonally` to be $O(n^3)$.

So the cost of running `solve` $O(n^2) + O(n^3) = O(n^3)$.

# Further questions

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 6.20 Optimal BST
>Suppose you are given a list of words $w_1, w_2, \ldots, w_n$ and their frequencies $f_1, f_2, \ldots f_n$. We want to design a [binary search tree](../../notes/binary_search_tree.md) such that at any node with word $w$ on the tree all child nodes to the left of the node have words that are alphabetically lower than $w$ whereas all child nodes to the right of the node have words that are alphabetically greater than it. We want to design such a tree where the average access time with respect to $f_i$ is minimised. i.e. if word $w_i$ has depth $d_i$ we want to minimise
>$$ \sum_{i = 1}^k d_i*f_i.$$
>Write a dynamic program that solves this problem efficiently with the following:
>
>Input: words $w_1, \ldots, w_n$ (in sorted order); frequencies $f_1, \ldots, f_n$.
>Output: The binary search tree of lowest cost.  (Not just the cost!)

>[!question] 6.7 Palindrome subsequence
>Given a sequence $a_1, a_2, \ldots, a_n$ devise an algorithm that returns the length of the longest [palindromic](../../notes/palindrome.md) [subsequence](../../notes/subsequence.md). Its running time should be $O(n^2)$.

>[!question] 6.7 Palindrome *substring* (altered)
>Given a sequence $a_1, a_2, \ldots, a_n$ devise an algorithm that returns the length of the longest [palindromic](../../notes/palindrome.md) [substring](../../notes/substring.md). Its running time should be $O(n)$.

# Tips

- First find a solution using substrings.
- Then consider if substrings was necessary, could you use prefixes?
