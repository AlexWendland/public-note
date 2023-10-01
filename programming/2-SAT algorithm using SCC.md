---
aliases: 
type: algorithm
publish: true
created: 2023-10-01
last_edited: 2023-10-01
tags:
  - programming
chatgpt: false
---
# 2-SAT algorithm using SCC

```pseudocode
2SAT(f):
	Input: 2-SAT problem on n variables with m clauses.
	Output: Assignment from n variables to m clauses satisfying f of no
		assignment possible.
1. Set f' = f
2. While f' has a unit clauses:
	1. Find a unit clause c.
	2. Assign c to True.
	3. If \overline{c} is a unity clause return no assignment possible.
	4. Remove clauses with c in and remove occurances of \overline{c}.
	5. Set this new statement to f'.
3. Construct graph G for f'.
4. Run SCC algorithm on S.
5. If any variable and its complement are in the same SCC return no assignment possible.
6. While still SCC left.
	1. Take sink SCC S,
	2. Set the variables in S to true (and thier complements to false)
	3. Remove S & S
7. Return assignment.
```

# Correctness

See [[Week 6 - 2-Satisfiability]] for the correctness of this algorithm.

# Run time

The run time of this algorithm is $O(nm)$ to simplify the clause with the algorithm on $G$ running in $O(n + m)$ time. 