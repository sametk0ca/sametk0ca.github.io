
Network-based threat intelligence is an essential aspect of modern cyber security defence. Examining IP addresses and domains from a threat intelligence perspective involves investigating beyond network connectivity to understand the malicious intent and capability behind the digital assets in a way that supports quick, safe triage for SOC L1 analysts.

## Why DNS Matters in the SOC

Every time a user clicks a link or a system resolves a hostname, the Domain Name System (DNS) springs into action. DNS is the mechanism that converts human-friendly names like [www.tryhackme.com](https://www.tryhackme.com) into IP addresses that machines understand. Because of its central role in making the internet usable, DNS is also a favourite playground for attackers.

For SOC analysts, DNS is one of the richest early-warning datasets. Suspicious domains will appear in alerts long before a payload hash is known. Adversaries rapidly register, configure, and abandon domains to stay ahead of defences. Our job as analysts is to turn a raw domain into a contextual artefact: who owns it, what IPs it resolves to, how often it changes, and whether it behaves more like a normal content delivery network (CDN) or a throwaway setup.

When you enrich a domain, these are the records that matter most:  


- **A / AAAA Records**: Map the domain to IPv4 and IPv6 addresses. If you see several A records that hop between different networks, raise suspicion of rapid rotation. In practice, copy the A record from [nslookup.io](https://www.nslookup.io) or [dnschecker.org](https://dnschecker.org) and follow with pasting the IP into VirusTotal for a quick read.
- **NS Records**: Identify the nameservers controlling the domain. Unusual or recently changed NS entries can mark fresh set up. As L1 analysts, we should note the provider name rather than chasing low-level details.
- **MX Records**: Define which servers handle email. Attackers may configure MX records to deliver phishing campaigns directly. If the alert relates to web browsing, just record whether MX exists.
- **TXT Records**: Store SPF and DKIM rules or verification tags. Poorly configured or absent SPF can increase risk in mail cases.
- **SOA Record**: Points to the zone's primary authority and often includes contact information. It will be worth noting the primary host and serial, which will support a basic ownership picture.
- **TTL (Time To Live)**: Tells resolvers how long to cache answers. Very low TTLs, seconds or minutes, can point to frequent changes, and should be treated as clues.


## Attack Techniques Using DNS

- **Fast Flux Hosting**: Adversaries rotate many IPs quickly with short cache times to avoid simple blocks. We need to record and escalate when we identify a domain that resolves to changing IPs within a short period and across different providers.
- **CDN Abuse**: Legitimate CDNs like Cloudflare or Akamai change IPs too, but done within their ASN ecosystem. If the A record points to a major CDN and other values are normal, take note and carry reputation and ownership checks,
- **Typosquatting**: Domains like paypa1[.]com or micros0ft[.]net trick users visually. If a name looks like a brand clone, treat it as high risk and escalate it.
- **IDN (Internationalised Domain Names)**: Attackers exploit Unicode, creating look-alike domains. Decode Punycode, for example xn--ppaypal-3ya[.]com, and compare to known brands using simple online decoder.


## IP Enrichment Within the SOC

Most SIEM or EDR alerts contain at least one IP address. An IP address is ambiguous by itself: it could belong to a compromised router in a home office, a shared CDN edge, or a cloud service used by thousands of tenants. Without enrichment, we risk overreacting (blocking legitimate infrastructure) or underreacting (ignoring a real command-and-control server).

**Enrichment** is adding ownership, ASN (Autonomous System Number), geolocation, and service context to an IP so that our decision is evidence-driven. SOC Level 1 analysts must perform this consistently, since IPs are the most common indicators in alert queues.

## The Role of RDAP

The **Registration Data Access Protocol (RDAP)** is the authoritative source for IP ownership. Unlike commercial GeoIP services or provider marketing pages, RDAP data is maintained by Regional Internet Registries (RIRs) such as RIPE NCC, ARIN, and APNIC. It tells us precisely who has been provided with the netblock.

From RDAP, we obtain:

- **NetRange**: The range of addresses delegated.
- **Organisation**: The registered holder (e.g., Amazon, Vodafone, TryHackMe).
- **Remarks**: Often include whether the block is used for hosting, broadband, or mobile.
- **Abuse Contact**: The official mailbox for incident reporting.

## Autonomous Systems and Heuristics

An **Autonomous System (AS)** is a collection of IP prefixes under a single organisation’s control. Each AS is assigned a unique 16 or 32-bit number (ASN), only required for external communications. Looking at the ASN helps analysts assess the likely role of an IP.

- **Hosting ASNs**: Many small netblocks, often with diverse tenants. Suspicious domains are frequently hosted here.
- **Residential ISPs**: These have huge ranges covering millions of users. Alerts on these may indicate compromised home routers or consumer devices.
- **Cloud/CDN ASNs**: Global anycast, dozens of prefixes, shared edges. Blocking whole ranges here causes collateral damage.

## Services and Certificates

Looking at an IP or domain's location data also helps us understand its function. Exposed services provide information on the system's intent and potential blast radius if abused. For example, an IP with RDP exposed on port 3389 may be a target for a brute-force attack.

## Shodan Reconnaissance

[Shodan](https://www.shodan.io/) is a powerful reconnaissance tool for IP address analysis. By indexing internet-connected devices and services, Shodan provides detailed information about open ports, running services, and system configurations. Queries like `org:example[.]com` reveal all systems associated with specific organisations, while searches for specific software versions help identify vulnerable systems.


## TLS Certificate Transparency

We can look at TLS certificate information using tools such as [crt.sh](https://crt.sh) as a gold mine for enrichment. Certificate Transparency logs every publicly trusted certificate. The key fields to look out for include:

- **Issuer**: This field provides details on who signed the certificate. For example, Let's Encrypt is a common but neutral vendor. A self-signed certificate may be a sign of a hastily deployed system.
- **Validity Period**: Short-lived certificates of up to 90 days are normal for usage. Analysts must look for bursts of reissued certificates and investigate suspected phishing infrastructure.
- **Subject Alternative Names**: This provides details on the domains covered by the certificate.

## Censys Search

[Censys.io](https://search.censys.io) can be a good alternative to Shodan for blue teams, as it shows exposed services even on non-standard ports and provides some advanced search capabilities. However, note that some of these features may require an account on the platform. 

## SOC Analyst Workflow

At this stage, our workflow in the SOC could resemble the following, though it may vary depending on established organisational processes and practices.

- **Check Shodan/Censys banners**: Identify exposed services and possible misconfigurations.
- **Review TLS certificates**: Ensure to record issuer, SANs, and validity period.
- **Look for anomalies**: Instances of multiple SANs, brand look-alikes or sudden bursts of issuance.
- **Pivot**: Utilise the certificate or banner artefacts to uncover related infrastructure.
- **Assess blast radius**:
    - RDP/SSH on residential ASN → shows a likelihood of a compromised endpoint.
    - TLS with many unrelated SANs on CDN ASN → shared infrastructure, avoid IP block.
    - Self-signed TLS on small ranges → shows likelihood of attacker panels or proxies.


## Why Reputation and History Matter

By this stage of enrichment, we have uncovered two major intelligence avenues: “_Who owns this IP/domain?”_ and “_What services does it expose?”_ However, we still need to identify more, especially regarding what the infrastructure has been doing over time.

As we know, file hashes are static, while IPs and domains are dynamic assets. Given that a domain may be registered for a phishing campaign today and parked within the week, the IP addresses used may be reassigned to different tenants or pass from malicious to benign use in days.

This makes time context critical when investigating incidents and using threat intelligence to enrich our findings. Reputation services and passive DNS analysis provide us with a way of adding that value.

## Reputation Services

VirusTotal is a primary reputation source that provides information such as detection ratio and indicator relations.

Another resource is Cisco Talos Intelligence, which provides frequently updated web and email reputation scores and category labels.


## Passive DNS

Passive DNS adds time context in domain enrichment, providing a historical record of how domains resolved over time. The key signals to look at include:

- **First Seen/Last Seen**: These tell us if a domain is new or long-lived.
- **Number of IPs in Time Window**: A high churn over days would suggest flux or agile hosting.
- **ASN Spread**: If IPs belong to many unrelated ASNs, this should be marked as suspicious, while those limited to one ASN should be marked as stable or belonging to a CDN mapping.

Beyond using passive DNS to gather domain history, other valuable sources include:

- **Certificate Transparency (CT) Logs**: These logs show certificate issuance history. They are useful for detecting sudden bursts of domains registered under phishing themes.
- **Wayback Machine**: Reveals historical website content. A domain that hosted a blog for years but switched to a phishing kit last week is high-risk.

## SOC Analyst Workflow

In summary, our workflow in the SOC would look as follows. Be mindful that this would vary depending on established organisational processes and practices.

- **Check VirusTotal**: Record detection ratio, First Seen, Last Seen, and any community notes.
- **Check Cisco Talos**: Record reputation score and category, noting any changes in the last 30 days.
- **Check IP2Proxy**: Flag if VPN/proxy/Tor; adjust severity accordingly.
- **Check Passive DNS**: Record First Seen, Last Seen, number of IPs in the last 7 days, and ASN spread.
- **Check CT Logs**: Note certificate bursts, suspicious SANs.
- **Cross-Reference with Wayback**: Identify content shifts (benign → phishing).
- **Decision**: Block, monitor, or close, with expiry tied to observed activity.

## From Data to Decision

We can now follow a simple playbook to make informed decisions when investigating an indicator.

- Verify: Confirm that the indicator appears in our telemetry and is relevant to our environment.
- Enrich: Collect geolocation, ASN, banners, certificates, reputation, and history.
- Score: Apply the confidence matrix and record the rationale.
- Decide: Block, monitor, or allow. Prefer precise controls, add expiry, and document.
- Hunt and notify: Search for related indicators, inform stakeholders, and create follow-up tasks.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
