---
aliases:
checked: false
course_code: CS6210
course_name: Advanced Operating Systems
created: '2025-12-01'
draft: true
last_edited: '2025-12-01'
tags:
  - OMSCS
title: Week 11 - Security
type: lecture
week: 11
---
# Principles of information security

Information security is a large part of the developer industry.
This field has whole masters courses dedicated to its study.
However, lots of the modern terminology was invented by visionaries in the early years of computer history.

The notes in this section are based on the following paper:

> Protection and the Control of Information in Computer Systems

## Terminology

First we make a clear distinction between privacy and security:

> [!define] Privacy
> Privacy is about controlling who is allowed to access, observe, or use information about you.
> It concerns people, preferences, context, and expectations.
> Example: Deciding who may see your photos or email address.

> [!define] Security
> Security is about the technical and organizational measures used to enforce desired privacy (and other protections such as integrity and availability).
> It covers authentication, encryption, access control, safe storage, etc.
> Example: The system verifying your password before allowing access to your data.

Privacy is a user-centric concept whereas security is a system-centric concept.

Some concerns related to this are:

- Unauthorized information release.

- Unauthorized information modification.

- Unauthorized denial of use (denial of service).

A goal of a good system should prevent all the above.
However, this statement is hard to prove as it is a negative statement such as 'there are no bugs in my code'.
Instead we want a positive definition of things we can check.

## Levels of protection

We can broadly group protection into levels.

- Unprotected: No protection at all.

- All or nothing: You either have access to the whole system or you don't.

- Controlled sharing: You can provide access control lists (ACLs) for files.

- User programmed sharing controls: You can differentiate users into different groups and those groups have different access levels for files.
For example unix styled creator, group, and other permissions.

- Strings on into: You can put particular requirements on each file.
For example, in the civil service documents will have a string relaying the security clearance you need to view different information.

These are very general and you should specialise these to fit your use case.
We also need to be able to dynamically change these.

## Design principles

There are some guiding principles for protection:

- Economy of mechanisms: It should be easy to verify that mechanisms of security are working correctly.

- Fail-safe defaults: Explicitly allow access to everything by default.

- Complete mediation: When it comes to security we need to not take short cuts for efficiency such as caching passwords - as this compromises on the security.

- Open design: The design should be published so others can review it but you should protect the keys.

- Separation of privilege: The system should be designed so no one person has privileged access to everything.

- Least privilege: The privileges to do something should be as limited as possible.

- Least common mechanism: The mechanism used to implement the control should have the least privileges possible, so if it fails it limits the damage attackers can do.

- Physiological acceptability: Users should know clearly what they are doing when they do it.
This means a good UI is critical and warnings clearly stating what changes will mean.

There are two very high level takeaways from all these principles:

- Difficult to crack the protection boundary.

- Detection rather than prevention: Prevention is incredibly hard, whereas detection is relatively easier.
