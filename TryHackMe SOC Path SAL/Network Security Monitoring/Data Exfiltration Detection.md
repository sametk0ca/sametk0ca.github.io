
Data exfiltration is the unauthorized transfer of sensitive data from a computer or other device. It's a primary objective for attackers who have breached a network. As a SOC analyst, our job is to detect and stop this before sensitive information walks out the door. This room will cover the common techniques attackers use to steal data and, more importantly, how we can catch them in the act.

### Common phases related to exfiltration

- **Discovery / Collection**: attacker locates sensitive files. 
- **Staging / Compression**: attacker aggregates, compresses, encrypts, or encodes files (ZIP, RAR, 7z, tar, base64, steganography).
- **Exfiltration transport**: transfer over network, removable media, cloud, or covert channels.
- **Command & Control (C2) coordination**: orchestrates transfer and confirms receipt.


## Techniques and Indicators

|Techniques|Examples|Indicator of Attack & where to look|
|---|---|---|
|**Network-based**|HTTP/HTTPS uploads to S3/Azure Blob/webmail, FTP/SFTP/SCP, DNS tunnelling, ICMP/covert protocols, custom TCP/UDP.|Proxy/web gateway logs (large POSTs, uploads to cloud endpoints), firewall/NGFW flows (high bytes to single IP/ASN), netflow (spikes/outbound flows), DNS logs (long hostnames, TXT queries).|
|**Host-based**|Powershell/Invoke-WebRequest, rclone, awscli, curl/wget, archive creation (zip/rar), use of removable USBs, ADS/hidden streams.|Sysmon/EDR (Process Create, Network Connect, File Create events), Windows Security (4663/4656 object access), auditd/shell history on Linux, and removable-media events.|
|**Cloud exfiltration**|S3 PutObject / multipart upload, Azure Blob uploads, Google Cloud Storage objects. Insert, Drive/SharePoint external sharing.|CloudTrail / Azure Activity / GCP Audit, cloud storage access logs, unusual service-account or IP activity.|
|**Covert & encoding**|DNS tunnelling, base64 or chunked encoding, steganography into images/audio, splitting files into many small requests (low-and-slow).|DNS logs, proxy logs with many small POSTs, correlation of intermittent uploads + suspicious process activity.|
|**Insider & collaboration tools**|Slack/Teams/Dropbox/Google Drive/Box uploads or sharing to external users; compromised employee accounts.|Audit logs (share events, file downloads), and mail logs.|
|**General IoAs & triage signals**|A large outbound volume to external IPs/domains, unknown destination domains, suspicious processes/command lines, many file read events followed by an outbound connection, and multipart/streamed uploads.|Correlate: Proxy/Firewall/Netflow, DNS, Sysmon/EDR (EventID 1/3/11), mail server logs.|



| Techniques                        | Examples                                                                                                                                                                                                    | Indicator of Attack & where to look                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Network-based**                 | HTTP/HTTPS uploads to S3/Azure Blob/webmail, FTP/SFTP/SCP, DNS tunnelling, ICMP/covert protocols, custom TCP/UDP.                                                                                           | Proxy/web gateway logs (large POSTs, uploads to cloud endpoints), firewall/NGFW flows (high bytes to single IP/ASN), netflow (spikes/outbound flows), DNS logs (long hostnames, TXT queries). |
| **Host-based**                    | Powershell/Invoke-WebRequest, rclone, awscli, curl/wget, archive creation (zip/rar), use of removable USBs, ADS/hidden streams.                                                                             | Sysmon/EDR (Process Create, Network Connect, File Create events), Windows Security (4663/4656 object access), auditd/shell history on Linux, and removable-media events.                      |
| **Cloud exfiltration**            | S3 PutObject / multipart upload, Azure Blob uploads, Google Cloud Storage objects. Insert, Drive/SharePoint external sharing.                                                                               | CloudTrail / Azure Activity / GCP Audit, cloud storage access logs, unusual service-account or IP activity.                                                                                   |
| **Covert & encoding**             | DNS tunnelling, base64 or chunked encoding, steganography into images/audio, splitting files into many small requests (low-and-slow).                                                                       | DNS logs, proxy logs with many small POSTs, correlation of intermittent uploads + suspicious process activity.                                                                                |
| **Insider & collaboration tools** | Slack/Teams/Dropbox/Google Drive/Box uploads or sharing to external users; compromised employee accounts.                                                                                                   | Audit logs (share events, file downloads), and mail logs.                                                                                                                                     |
| **General IoAs & triage signals** | A large outbound volume to external IPs/domains, unknown destination domains, suspicious processes/command lines, many file read events followed by an outbound connection, and multipart/streamed uploads. | Correlate: Proxy/Firewall/Netflow, DNS, Sysmon/EDR (EventID 1/3/11), mail server logs.                                                                                                        |

# Data Exfil through DNS Tunnelling

DNS exfiltration abuses the Domain Name System, a protocol normally allowed through networks, to smuggle bytes encoded inside DNS queries/responses so firewalls and web proxies don't notice. Because DNS is typically allowed and often unfiltered or forwarded to public resolvers, it's attractive for covert channels.

## DNS Tunneling

DNS (Domain Name System) translates human-friendly domain names (e.g., `example.com`) into IP addresses and provides other record types (A, AAAA, TXT, MX, CNAME, etc.). Key points:

- DNS queries are ubiquitous: almost every host performs DNS lookups.
- DNS is normally allowed through firewalls and gateways, making it an attractive covert channel.
- DNS uses UDP (mostly) on port 53 for queries and responses; TCP is used for zone transfers or large responses.

Why attackers use DNS for exfiltration:

- Always-on service: DNS lookups are routine and often allowed outbound.
- High cover: queries look like normal requests unless inspected closely.
- Flexible payload: data can be encoded into the subdomain labels or TXT responses.

## Indicators of attack 

When analysing DNS traffic for possible indicators of data exfiltration, we should look for:

- Many DNS queries are sent to a single external domain, especially with very high counts compared to the baseline.
- ==Long subdomain labels or unusually long full query names (> 60–100 characters).==
- High entropy or Base32/Base64-like patterns in the query name (lots of mixed case letters, digits, `-`, `=` signs for base64).
- Rare record types (TXT, NULL) or many large TXT responses.
- Unusual response behavior: frequent NXDOMAIN (if attacker uses exfil-by-query without answering), or TCP/large UDP fragments for DNS.
- Queries at regular intervals (beaconing behaviour).

# Data Exfil through FTP


FTP (File Transfer Protocol) is one of the oldest protocols for transferring files between a client and server over a TCP/IP network. Attackers use it to move large amounts of data off a network, sometimes via compromised credentials, misconfigured servers, or ephemeral accounts. Detection relies on a mix of packet inspection (FTP only), server logs, SSH session metadata, and network flow/size/pattern analysis.

## How adversaries use FTP for exfiltration

- Use **legitimate FTP servers** (public or misconfigured internal servers) to stage/transfer data.
- Use **compromised credentials** (service accounts, user creds).
- Use **non-standard ports** or tunneling to blend with other traffic.

## Indicators of attack

What to look for:

- ==`USER` and `PASS` commands (cleartext credentials).==
- `STOR` (upload) and `RETR` (download) commands: repeated or large transfers.
- Large data connections to unusual external IPs, especially outside business hours.
- Data channel openings on ephemeral ports (PASV) paired with large payloads.

# Data Exfil through HTTP

**Data exfiltration via HTTP** is when an attacker moves sensitive data out of a target network using HTTP as the transport. HTTP is commonly abused because it blends with normal web traffic, can traverse firewalls and proxies, and can be obfuscated (encoding, encryption, tunneling).

## How adversaries use HTTP for data exfiltration

- **POST uploads to external servers**: Bulk data is sent to attacker-controlled hosts or cloud storage in POST request bodies.
- **GET requests with encoded data**: Attacker squeezes small chunks into query strings or path segments (useful for low-and-slow exfiltration).
- **Use of common services / CDN**: Exfiltration disguised as uploads to popular services or attacker-controlled subdomains under reputable domains.
- **Custom headers**: Data placed in headers (e.g., `X-Data: <base64>`) may bypass some string-based DLP.
- **Chunked transfer / multipart**: Large payloads split into multiple requests to avoid size thresholds.
- **HTTPS/TLS tunneling**: The encrypted channel hides the payload; detection requires TLS inspection, SNI analysis, or metadata-based detection.
- **Staging via cloud services**: The attacker uploads to Dropbox/GitHub/Gist and then fetches externally.
## Indicators of Attack (IoAs) 

### Common network indicators

- Unusually large HTTP POST requests to external/unexpected hosts.
- HTTP requests to domains with low reputation / rarely seen in baseline traffic.
- Frequent small requests (beaconing) to the same host, followed by large uploads.
- Chunked or multipart transfers where multiple requests compose a larger file.


# Data Exfil through ICMP


## How adversaries use ICMP for exfiltration

Common techniques:

- ICMP echo (type 8) / reply (type 0) tunneling: attackers place encoded (base64, hex) chunks of files inside ICMP payloads. The remote server collects and decodes them.
- Custom ICMP types/codes: using uncommon ICMP types or non-zero codes to avoid signature-based detections.
- Fragmentation and reassembly: large payloads are split across multiple packets.
- Encryption/obfuscation: Encrypting or encrypting payloads (base64 is common) to look like random data.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
