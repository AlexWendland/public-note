---
aliases:
  - CSE6220
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: 2026-01-12
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - OMSCS
  - math
  - programming
term: spring
title: CSE6220 Introduction to High Performance Computing
type: course
year: '2026'
---

This course is a graduate-level introduction to scalable parallel algorithms. "Scale" really refers to two things: efficient as the problem size grows, and efficient as the system size (measured in numbers of cores or compute nodes) grows. To really scale your algorithm in both of these senses, you need to be smart about reducing asymptotic complexity the way you’ve done for sequential algorithms since CS 101; but you also need to think about reducing communication and data movement. This course is about the basic algorithmic techniques you’ll need to do so. The techniques you’ll encounter cover the main algorithm design and analysis ideas for three major classes of machines: for multicore and manycore shared memory machines, via the work-span model; for distributed memory machines like clusters and supercomputers, via network models; and for sequential or parallel machines with deep memory hierarchies (e.g., caches). You will see these techniques applied to fundamental problems, like sorting, search on trees and graphs, and linear algebra, among others. The practical aspect of this course is implementing the algorithms and techniques you’ll learn to run on real parallel and distributed systems, so you can check whether what appears to work well in theory also translates into practice. (Programming models you’ll use include OpenMP, MPI, and possibly others.)

# Links

- [Central](https://www.omscentral.com/courses/high-performance-computing/reviews)
- [OMSCS page](https://omscs.gatech.edu/cse-6220-intro-high-performance-computing)
- [Course textbook](https://github.com/vineethshankar/pagerank/blob/master/Introduction%20to%20Parallel%20Computing%2C%20Second%20Edition-Ananth%20Grama%2C%20Anshul%20Gupta%2C%20George%20Karypis%2C%20Vipin%20Kumar.pdf)
