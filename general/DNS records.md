---
aliases:
  - DNS A record
  - CNAME
  - NS record
  - MX record
checked: false
created: 2024-07-22
last_edited: 2024-07-22
publish: true
tags:
  - networks
type: definition
---
>[!tldr] DNS records
>This is the response from a [[Domain Name System (DNS)|DNS]] server. This comes in a question/answer format as bellow. Typically these 4 vales:
>- Domain name: The name of the domain requested.
>- [[Time to live (TTL)|TTL]]: How long the response should be cached for by other DNS servers.
>- Type: The type of record being returned.
>- Value: What is associated to the Domain name.
>This is given in the following format
>![[dns_message_format.png]]
>The flags provide information such as the type of query iterative or recursive. 
>There are different types of responses you can get from a [[Domain Name System (DNS)|DNS]] resolver. 
>1. **A (Address) Record**: Maps a domain name to an [[Internet Protocol (IPv4)|IPv4]] address.
>2. **AAAA (Quad-A) Record**: Maps a domain name to an [[Internet Protocol (IPv6)|IPv6]] address.
>3. **CNAME (Canonical Name) Record**: Alias of one domain name to another. The DNS lookup will continue by retrying the lookup with the new name.
>4. **NS (Name Server) Record**: Indicates the authoritative DNS servers for a domain.
>5. **MX (Mail Exchange) Record**: Specifies the mail server responsible for receiving email messages on behalf of a domain.
>6. **TXT (Text) Record**: Holds text information. Commonly used for SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and other verification purposes.
>7. **SOA (Start of Authority) Record**: Provides information about the DNS zone, such as the primary name server, the email of the domain administrator, the domain serial number, and various timers.
>8. **PTR (Pointer) Record**: Maps an IP address to a domain name (reverse DNS lookup).
>9. **SRV (Service) Record**: Defines the location (hostname and port) of servers for specified services.
>10. **CAA (Certification Authority Authorization) Record**: Specifies which [[Certificate authorities (CA)|certificate authorities]] are allowed to issue certificates for the domain.
>11. **DS (Delegation Signer) Record**: Used in DNSSEC to delegate a subzone.
>12. **DNSKEY Record**: Contains a public signing key used in DNSSEC.
>13. **NSEC (Next Secure) Record**: Used in DNSSEC to prove the non-existence of a DNS record.
>14. **NSEC3 (Next Secure3) Record**: A more secure version of the NSEC record used in DNSSEC.
>15. **RRSIG (Resource Record Signature)**: Contains a digital signature of a DNSSEC-protected record set.
>16. **TLSA (Transport Layer Security Authentication) Record**: Associates a TLS server certificate or public key with the domain name to enable DANE (DNS-based Authentication of Named Entities).

