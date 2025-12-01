---
aliases:
checked: false
created: 2023-10-01
draft: false
last_edited: 2023-11-12
tags:
  - programming
type: algorithm
---
# 2-SAT algorithm using SCC

```pseudocode
2SAT(f):
    Input: 2-SAT problem on n variables with m clauses.
    Output: Assignment from n variables satisfying f or stating no assignment is possible.
1. Find all the unit clauses u_i in f.
2. Create a dummy variable Y. Set f' = f
    1. Replace the unit clauses in f' with u_i \lor Y.
    2. Add new clauses to f' of u_i \lor \overline{Y}.
3. Construct graph G for f'.
4. Run the SCC algorithm on G.
5. If any variable and its complement are in the same SCC, return no assignment possible.
6. While there are still SCCs left:
    1. Take sink SCC S.
    2. Set the clauses in S to true (and their complements to false).
    3. Remove S & \overline{S}.
7. Return the assignment, excluding the value for Y.
```

# Correctness

See [[Week 6 - 2-Satisfiability]] for the correctness of this algorithm.

# Run time

This has run time $O(n + m)$.

The simplification step takes $O(m)$ time and produces a problem with $n+1$ variables and at most $2m$ clauses.The latter half of the algorithm solves in $O(n+1 + 2m) = O(n + m)$. This results in an overall runtime of $O(n + m)$.
