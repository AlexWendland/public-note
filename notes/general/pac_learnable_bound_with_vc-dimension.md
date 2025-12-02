---
aliases:
checked: false
created: 2024-02-19
draft: false
last_edited: 2024-02-19
title: PAC learnable bound with VC-dimension
tags:
  - machine-learning
type: lemma
---
# Statement

> [!important] Lemma
> For a learner with a [hypothesis space](modelling_paradigm.md) $H$ with [VC dimension](vapnik-chervonenkis_dimension.md) $VC(H)$ then by drawing
> $$m \geq \frac{1}{\epsilon} \left (8 \ VC(H) \cdot \log_2(\frac{13}{\epsilon}) + 4 \log_2(\frac{2}{\delta}) \right)$$
> [i.i.d.](independent_identically_distributed_samples.md) samples for [training data](training_data.md) $T$ if there are any hypothesis [consistent](consistent_learner.md) with $T$ then this will be a [PAC learner](probably_approximately_correct_learnable_(pac).md) with $\leq \epsilon$ accuracy with probability $1-\delta$.

# Proof
