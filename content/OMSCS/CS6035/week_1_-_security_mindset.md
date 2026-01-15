---
aliases:
checked: false
course_code: CS6035 O01
course_name: Introduction to Information Security
created: '2026-01-12'
draft: true
last_edited: '2026-01-12'
tags:
  - OMSCS
title: Week 1 - Security Mindset
type: lecture
week: 1
---

We need security when two things are met:

- We have something of value, and 

- We have a threat to that thing.


# Things of value

In the context of cyber security usually the thing of value is information.
However, there are examples of using cyber attacks to attack things in the physical world such as the Stuxnet attack on Iran's nuclear facility or digital attacks on electric grids.

# Threat sources

There are 3 major groups of threats when it comes to cyber security:

- *Cyber criminals*: Professional criminals looking to profit from stealing money.

- *Hacktivists*: Activists who are looking to make a statement by hacking particular companies.

- *Nation states*: Countries who are looking to compromise one another for their own gain, either political gain or espionage.

# Vulnerabilities

Once we have something of value and someone willing to act on that we need to talk about what leads to attacks.

- *Threat actors*: Are looking to exploit vulnerabilities and to launch attacks.

- *Vulnerabilities*: Are weaknesses in the system that can be exploited, these happen with software, networks, and humans!

- *Attacks*: Are the actions taken by the threat actors to exploit the vulnerabilities.

> [!example] Target store breach (2013)
> In this attack the criminals were looking for credit card data.
> The vulnerability was within a contractor they were using.
> The attack was a phishing email sent to them.

![Vulnerabilities](../../../static/images/vulnerabilities.png)

# What can we do about this?

Some steps we can take are detailed below:

- Make threats go away (crime should not pay): This has largely been unsuccessful.

- Reduce vulnerabilities: Consistently audit and check systems.
However, it is a fact of life that any sufficiently large and complex system will have bugs.

- Strive to meet security requirements (CIA):

  - Confidentiality: Only people who are permitted to access data should be able to view it.

  - Integrity: Data should not be modified without permission.

  - Availability: Data should be available to be viewed.

All these functionally break down into the following categories.

- Prevention: Stop the threat actors from doing what they are doing.

- Detection: Know when your systems have been compromised.

- Response: Take action to stop the attack.

- Recovery and remediation: Bring systems back up and fix any vulnerabilities.

There are normally two parts to both of these.
The *policy* of what should happen and the *mechanism* of how that does happen.
This practically can come from following some standard design principles for secure systems:

- *Reduce complexity*: Complex systems have more bugs, which means more vulnerabilities.
Therefore, keeping your code simple reduces the chances of something getting missed.

- *Fail-safe defaults*: If a system fails it should have a default that is safe, such as denying access.

- *Complete mediation*: Someone should never be able to bypass the monitor, so all actions are observed.

- *Open design*: More people being able to review the design of your system means that it is more likely people spot issues and if they are using it fix them.
A lot of people believe in 'security through obscurity' but closed source solutions can be reverse engineered without the benefit of the users checking the source.

- *Least privilege*: Only give people the minimum access they need to do their job.

- *Psychological acceptability*: Do not ask people to do things that do not come 'naturally' to them as they will not do it.
