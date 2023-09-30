---
aliases: []
type: lecture
publish: false
created: 2023-09-30
last_edited: 2023-09-30
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: int
chatgpt: false
---
# Week 6 - 2-Satisfiability

This week we will look at

![[Satisfiability problem (SAT problem)#Statement]]

> [!note] Notation
> We use the following logical operators
> - $\overline{x}$ to represent not $x$,
> - $\lor$ to represent or, and
> - $\land$ to represent and.

> [!example] Example
> Let 
> $$f = (\overline{x_1} \lor \overline{x_2} \lor x_3) \land (x_2 \lor x_3) \land (\overline{x_3} \lor \overline{x_1}) \land (\overline{x_3})$$
> Is there an assignment to $x_1$, $x_2$ and $x_3$ that satisfies $f$?
> 

This problem is generally quite hard so we look at the limited problem.

![[k-satisfiability problem (k-SAT problem)#Statement]]

![[k-satisfiability problem (k-SAT problem)#Theory]]

## Solving [[k-satisfiability problem (k-SAT problem)|2-SAT]] problem

>[!example] [[k-satisfiability problem (k-SAT problem)|2-SAT]] example
>Consider
>$$(x_3 \lor \overline{x_2}) \land (\overline{x_1}) \land (x_1 \lor x_4) \land (\overline{x_4} \lor x_2) \land (\overline{x_3} \lor x_4).$$

### Simplifying the problem

First we simplify the input by getting rid of forced decisions. We do this by repeatedly looking for unit clauses with 1 literal and reducing the problem by removing this variable.

1. Take a unit clause, say literal $a_i$,
2. If the unit clause $\overline{a_i}$ exists output then no solution exists,
3. Satisfy it, set $a_i = T$,
	1. If a_i = x, then x = T, or
	2. If a_i = \overline{x} then x = F.
4. Remove clauses containing $a_i$ and drop $\overline{a_i}$ from clauses.
5. Let $f'$ be the resulting formula.

We can repeat this until either: 
- we find an issue, 
- the formula becomes empty and we have an assignment, or
- the output formula only has clauses with 2 variable.

>[!note] Observation
>$f$ is satisfiable if and only if $f'$ is satisfiable. Therefore this is a proper reduction.

### Forming a graph





