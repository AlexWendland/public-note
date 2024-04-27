---
aliases: 
checked: false
created: 2024-02-19
last_edited: 2024-02-19
publish: true
tags:
  - machine-learning
type: lemma
---
# Statement

> [!important] Lemma
> For a learner with a [[Modelling paradigm|hypothesis space]] $H$ with [[Vapnik-Chervonenkis dimension|VC dimension]] $VC(H)$ then by drawing 
> $$m \geq \frac{1}{\epsilon} \left (8 \ VC(H) \cdot \log_2(\frac{13}{\epsilon}) + 4 \log_2(\frac{2}{\delta}) \right)$$
> [[Independent identically distributed samples|i.i.d.]] samples for [[Training data|training data]] $T$ if there are any hypothesis [[Consistent learner|consistent]] with $T$ then this will be a [[Probably approximately correct learnable (PAC)|PAC learner]] with $\leq \epsilon$ accuracy with probability $1-\delta$.

# Proof
