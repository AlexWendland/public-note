---
aliases: null
checked: false
created: 2023-11-12
last_edited: 2023-11-12
draft: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Max-Satisfiability Problem|Max-SAT]] is [[NP-hard]]

# Proof

There is a [[Many-one reduction (problem)|many-one reduction]] from the [[Satisfiability problem (SAT problem)|SAT problem]] to [[Max-Satisfiability Problem|max-SAT]].

If we have an instance of the [[Satisfiability problem (SAT problem)|SAT problem]] plug it into [[Max-Satisfiability Problem|max-SAT]] and if we get an assignment the satisfies all clauses return that, otherwise say no.

As [[SAT is NP-complete]] this gives that [[Max-Satisfiability Problem|max-SAT]] is [[NP-hard]].
