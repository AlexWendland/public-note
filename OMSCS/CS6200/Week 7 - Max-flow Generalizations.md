---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-10-07
last_edited: 2023-11-11
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Max-flow Generalizations

>[!tldr] [[Max flow problem|Max flow]] with demands
>Let $(G=(V,E), c, s, t)$ be a [[Flow network|flow network]] and assume we are provided with demands $d(e) \geq 0$ for $e \in E$. A flow $f$ is called feasible if
>$$d(e) \leq f(e) \leq c(e).$$
>Is there a feasible flow? If so what is the maximum feasible flow?

We would like to turn the [[Flow network|flow network]] with demands into a problem of just the [[Max flow problem|max flow]].

The intuition guiding this is we want to let the edges of $G$ just present the spare capacity after you subtracted off the demand. Then we want to use exterior vertices $s'$ and $t'$ to represent the demands on the network.

We will define a new [[Flow network|flow network]] $(G' = (V',E'), c', s', t')$ to do this. First lets define the graph $G'$ with $V' = V \cup \{s', t'\}$ and
$$E' = \left \{ \begin{array} \ e \\ (s', v)\\ (v, t')\\ (t,s) \end{array} \Bigg \vert \begin{array} \ \\ \ e \in E\\ v \in V \\ \ \end{array} \right \}.$$
These have capacity
$$c'(e) = \begin{cases} c(e) - d(e) & \mbox{if } e \in E\\ \sum_{(u,v) \in E} d(u,v) & \mbox{if } e = (s',v)\\ \sum_{(v,u) \in E} d(v,u) & \mbox{if } e = (v,t')\\ \infty & \mbox{if } e = (t,s) \end{cases}.$$
Then a [[Flow|flow]] $f'$ on $(G', c', s', t')$ will be converted into a flow on $(G,c,s,t)$ by defining $f(e) = f'(e) + d(e)$ for $e \in E$.

However, this will only be a valid [[Flow|flow]] on $(G,c,s,t)$ if the value of $capacity(f') = \sum_{e \in E} d(e)$ (the maximum capacity on $(G', c', s', t')$ ). Such a [[Flow|flow]] $f'$ will be called a saturating [[Flow|flow]].

>[!important] Lemma
>$G$ has a feasible flow $f$ if and only if $G'$ has a saturating flow $f'$.

### $\Leftarrow$

Define $f(e) = f'(e) + d(e)$ for $e \in E$ as above.

Note $f(e) = f'(e) + d(e) \geq d(e)$ so this flow is feasible.

We have to show $f$ is valid, so for any $v \in V \backslash \{s,t\}$
$$ \sum_{(u,v) \in E} f(u,v) = \sum_{(v,w) \in E} f(v,w).$$
We have that $f'$ is valid, so for any $v \in V$
$$\sum_{(u,v) \in E'} f'(u,v) = \sum_{(v,w) \in E'} f'(v,w).$$
Lets break this edge set down for $v \in V \backslash \{s, t \}$
$$\begin{align*}
\sum_{(u,v) \in E'} f'(u,v) & = \left ( \sum_{(u,v) \in E} f'(u,v) \right ) + \left ( \sum_{(s',v) \in E} f'(s',v) \right )\\
& = \left ( \sum_{(u,v) \in E} f'(u,v) \right ) + \left ( \sum_{(u,v) \in E} d(u,v) \right )\\
& =  \sum_{(u,v) \in E} f'(u,v) + d(u,v)\\
& = \sum_{(u,v) \in E} f(u,v)
\end{align*}$$
which similarly we get
$$\sum_{(v,w) \in E'} f'(v,w) = \sum_{(v,w) \in E} f(v,w).$$
This gives us validity of $f$ from the validity of $f'$.

### $\Rightarrow$

Define
$$f'(e) = \begin{cases}
f(e) - d(e) & \mbox{if } e \in E\\
\sum_{(u,v) \in E} d(u,v) & \mbox{if } e = (s', v)\\
\sum_{(v,w) \in E} d(v,w) & \mbox{if } e = (v, t')\\
capacity(f) & \mbox{if } e = (t', s')
\end{cases}$$
Note the similarity to $c'(e)$ in fact as $f(e) \leq c(e)$ we get $f'(e) \leq c(e)$. For the edges $(s',v)$ and $(v,t')$ we have $f'(e) = c'(e)$.

As $f$ is a feasible flow we have $f'(e) \geq 0$ for all $e \in E'$.

The main thing to show is that $f'$ is a valid flow.

For $v \in V \backslash \{s, t\}$ calculate
$$\begin{align*} \sum_{(u,v) \in E'} f'(u,v) & = \left ( \sum_{(u,v) \in E} f(u,v) - d(u,v) \right ) + \sum_{(u,v) \in E} d(u,v)\\
& = \sum_{(u,v) \in E} f(u,v)\\
& = \sum_{(v,w) \in E} f(v,w)\\
& = \left ( \sum_{(v,w) \in E} f(v,w) - d(v,w) \right ) + \sum_{(v,w) \in E} d(v,w) \\
& = \sum_{(v,w) \in E'} f'(v,w)\end{align*}$$
giving it is valid here. Whereas for $s$ we have
$$\begin{align*} \sum_{(u,s) \in E'} f'(u,s) & = \sum_{(s,w) \in E} f(s,w) & \mbox{from } f'(t',s')\\
& = \left ( \sum_{(s,w) \in E} f(s,w) - d(s,w) \right ) + \sum_{(s,w) \in E} d(s,w) \\
& = \sum_{(s,w) \in E'} f'(s,w)\end{align*}$$
similarly for $t$
$$\begin{align*} \sum_{(t,w) \in E'} f'(t,w) & = \sum_{(u,t) \in E} f(u,t) & \mbox{from } f'(s',t')\\
& = \left ( \sum_{(u,t) \in E} f(u,t) - d(u,t) \right ) + \sum_{(u,t) \in E} d(u,t) \\
& = \sum_{(u,t) \in E'} f'(u,t)\end{align*}$$
giving us validity.

$\square$

## Max feasible flow

Now we have a feasible flow $f$ if one exists, how do we maximises it?

We run [[Ford-Fulkerson Algorithm]] or [[Edmonds-Karp algorithm]] but instead of starting from a zero flow we instead start from $f$.

Also instead of defining the usual [[Residual Network (flow)|residual network]] instead we define a limited version
$$c^f(v,w) = \begin{cases} c(v,w) - f(v,w) & \mbox{if } (v,w) \in E \mbox{ and } f(v,w) < c(v,w)\\ f(w,v) - d(w,v) & \mbox{if } (w,v) \in E \mbox{ and } f(w,v) > d(w,v)\\ 0 & \mbox{otherwise} \end{cases}.$$
this accounts for the restriction.
