---
aliases:
  - dual linear programme
checked: false
created: 2023-11-09
last_edited: 2023-11-09
publish: true
tags:
  - programming
type: definition
---
>[!tldr] Dual linear programme
>Suppose we have a [[Linear programme standard form|linear programme in standard form]] given by $A \in M_{m,n}(\mathbb{R})$, $b \in M_{m,1}(\mathbb{R})$ and $c \in M_{n,1}(\mathbb{R})$. Define the *dual linear programme* to be defined by $-A^T \in M_{n,m}$, $-c \in M_{n,1}(\mathbb{R})$ and $-b \in M_{m,1}(\mathbb{R})$. Where we want to solve for some $y \in M_{m,1}$ where we
>$$ \max_y -b y^T \mbox{ such that } -A^Ty \leq -c.$$
>Note we have added the minus signs to keep it in [[Linear programme standard form|standard form]].



