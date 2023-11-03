---
aliases: 
type: lemma
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - maths
chatgpt: false
---
# Statement

> [!important] Lemma
> [[Independent set of a given size]] is [[NP-Complete|NP-complete]].

# Proof

As [[Independent set of a given size is in NP]] all we need to show is that [[Independent set of a given size]] is [[NP-hard]].

To show this we are going to find a [[Many-one reduction (problem)|many-one reduction]] of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem to [[Independent set of a given size]] problem. (We know [[3-SAT is NP-complete]] so this gives us that [[Independent set of a given size]] is also [[NP-Complete|NP-complete]].) This will involve:

- Taking an instance of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem 

