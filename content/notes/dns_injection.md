---
aliases:
created: 2024-07-22
date_checked:
draft: false
last_edited: 2024-07-22
tags:
  - networks
title: DNS injection
type: definition
---
>[!tldr] DNS injection
>This is a form of [DNS censorship](dns_censorship.md). It uses a ruleset for which [DNS](domain_name_system_(dns).md) entries are unacceptable and fakes the replies from a [DNS](domain_name_system_(dns).md) lookup so the requester can not resolve the [IP address](internet_protocol_(ip).md). The works in the following way:
>1. DNS probe is sent to the open DNS resolvers
>2. The probe is checked against the blocklist of domains and keywords
>3. For domain-level blocking, a fake [DNS A record](dns_records.md) response is sent back. There are two levels of blocking domains: the first one is by directly blocking the domain, and the second one is by blocking it based on keywords present in the domain

