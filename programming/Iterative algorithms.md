---
aliases: [iterative algorithms, iterative]
type: algorithm
publish: true
created: 2023-08-26
last_edited: 2023-08-26
tags: programming
chatgpt: true
---
# Iterative algorithms

An iterative algorithm is a computational procedure that solves a problem by repeating a set of steps until a specific condition is met, without making [[Recursion|recursive]] calls. In other words, it uses loops (like `for`, `while`, etc.) to repeatedly execute code blocks, updating the state variables as it progresses, until it reaches an exit condition that signifies the problem has been solved.

Here are some key characteristics of iterative algorithms:

1. **State Variables**: Iterative algorithms often employ one or more variables to maintain the state of the computation. These variables are updated throughout the loop's iterations.
    
2. **Exit Condition**: Every iterative algorithm has an exit condition that determines when the loop will terminate. This condition is evaluated at the end or beginning of each iteration.
    
3. **Looping Construct**: Iterative algorithms use looping constructs (`for`, `while`, etc.) to manage the repetition of a set of steps.
    
4. **In-Place Update**: They often update variables or data structures in-place, which can be more memory-efficient.
    
5. **Deterministic**: The number of steps or iterations can often be determined beforehand or are evident based on the exit condition.