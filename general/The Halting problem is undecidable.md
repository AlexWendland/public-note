---
aliases: 
checked: false
created: 2023-11-13
last_edited: 2023-11-13
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> The [[Halting problem]] is [[Undecidable problem|undecidable]].

# Proof

Suppose we have an algorithm that solves the [[Halting problem]] on every input. Call this $terminator(P,I)$ which returns true or false based on if $P(I)$ terminates.

Define the following programme $Harmful$.

```pseudocode
Harmful(J):
	Input: Some problem J
	Output: Null
1. If Terminator(J,J)
	1.1. Then goto 1
	1.2. else reutrn
```

What is $terminator(Harmful, Harmful)$?

If $terminator(Harmful, Harmful) = true$ then $Harmful(Harmful)$ by definition is an infinite loop - contradicting $terminator(Harmful, Harmful) = true$.

If $terminator(Harmful, Harmful) = false$ then $Harmful(Harmful)$ by definition terminates after 1 step - contradicting $terminator(Harmful, Harmful) = false$.

Therefore no such programme $terminator$ can exist and we have the [[Halting problem]] is [[Undecidable problem|undecidable]].

