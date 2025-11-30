---
aliases: null
checked: false
created: 2023-09-07
last_edited: 2023-11-11
draft: true
tags:
  - maths
type: lemma
---
>[!important] Masters theorem
>Given a $T$ a recurrence relation of the form
>$$T(n) = a T(\frac{n}{b}) + f(n), \mbox{ with } T(1) = d$$
>for constants $a \geq 1$, $b > 1$, and $d > 0$. Let $c_{crit} = \log_b(a)$ with $f$ asymptotically positive. Then the following statements are true:
> - **Case 1**: If $f(n) = O(n^{c})$ for some $c < c_{crit}$, then $T(n) = \Theta(n^{\log_b(a)})$.
> - **Case 2**: If $f(n) = \Theta(n^{c_{crit}}\log^k(n))$
> 	- **Case 2a**: for $k > -1$, then $T(n) = \Theta(n^{c_{crit}}\log^{k+1}(n))$.
> 	- **Case 2b**: for $k = -1$, then $T(n) = \Theta(n^{c_{crit}}\log(\log(n)))$.
> 	- **Case 2c**: for $k < -1$, then $T(n) = \Theta(n^{c_{crit}})$.
> - **Case 3**: If $f(n) = \Omega(n^{c})$ for some $c > c_{crit}$ then $T(n) = \Theta(f(n))$.

> [!warning] NEED TO REVIEW THIS!


## Links

- [Brilliant](https://brilliant.org/wiki/master-theorem/)
- [Wikipedia](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
