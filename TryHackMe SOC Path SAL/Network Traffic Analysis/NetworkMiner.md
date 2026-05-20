
NetworkMiner is an open-source traffic sniffer, PCAP handler and protocol analyser. Developed and still maintained by Netresec.

## Operating Modes

There are two main operating modes:

- **Sniffer Mode**: Although it has a sniffing feature, it is not intended to use as a sniffer. The sniffier feature is available only on Windows. However, the rest of the features are available in Windows and Linux OS. Based on experience, the sniffing feature is not as reliable as other features. Therefore we suggest not using this tool as a primary sniffer. Even the official description of the tool mentions that this tool is a "Network Forensics Analysis Tool", but it can be used as a "sniffer". In other words, it is a Network Forensic Analysis Tool with but has a sniffer feature, but it is not a dedicated sniffer like Wireshark and tcpdump.


-  **Packet Parsing/Processing**: NetworkMiner can parse traffic captures to have a quick overview and information on the investigated capture. This operation mode is mainly suggested to grab the "low hanging fruit" before diving into a deeper investigation.


| **Feature**                 | **NetworkMiner**                                     | **Wireshark**     |
| --------------------------- | ---------------------------------------------------- | ----------------- |
| Purpose                     | Quick overview, traffic mapping, and data extraction | In-Depth analysis |
| GUI                         | ✅                                                    | ✅                 |
| Sniffing                    | ✅                                                    | ✅                 |
| Handling PCAPS              | ✅                                                    | ✅                 |
| OS Fingerprinting           | ✅                                                    | ❌                 |
| Parameter/Keyword Discovery | ✅                                                    | Manual            |
| Credential Discovery        | ✅                                                    | ✅                 |
| File Extraction             | ✅                                                    | ✅                 |
| Filtering Options           | Limited                                              | ✅                 |
| Packet Decoding             | Limited                                              | ✅                 |
| Protocol Analysis           | ❌                                                    | ✅                 |
| Payload Analysis            | ❌                                                    | ✅                 |
| Statistical Analysis        | ❌                                                    | ✅                 |
| Cross-Platform Support      | ✅                                                    | ✅                 |
| Host Categorisation         | ✅                                                    | ❌                 |
| Ease of Management          | ✅                                                    | ✅                 |

Versiyon 1.6 ve 2.7'de farklılıklar var !!

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
