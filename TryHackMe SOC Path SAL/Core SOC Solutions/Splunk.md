Splunk is one of the leading SIEM solutions in the market. It allows users to collect, analyze, and correlate network and machine logs in real time.

Splunk has three main components: Forwarder, Indexer, and Search Head. These components work together to help us search and analyze the data.


## Splunk Forwarder

Splunk Forwarder is a lightweight agent installed on the endpoint intended to be monitored, and its main task is to collect the data and send it to the Splunk instance. It does not affect the endpoint's performance as it takes a few resources to process. Some of the key data sources are:

- Web server generating web traffic.
- Windows machine generating Windows Event Logs, PowerShell, and Sysmon data.
- Linux host generating host-centric logs.
- Database generating DB connection requests, responses, and errors.


![[2369fa2efc856b793f1ecbf415681d4d.png]]
The forwarder collects the data from the log sources and sends it to the Splunk Indexer.



## Splunk Indexer

Splunk Indexer plays the main role in processing the data it receives from forwarders. It parses and normalizes the data into field-value pairs, categorizes it, and stores the results as events, making the processed data easy to search and analyze.

![Splunk Indexer](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/e699eaa9af523513e9c6a6ab8aaaa6a2.png)

Now, the data, which is normalized and stored by the indexer, can be searched by the Search Head, as explained below.

## Search Head

Splunk Search Head is the place within the **Search & Reporting App** where users can search the indexed logs, as shown below. The searches are done using the **SPL** (Search Processing Language), a powerful query language for searching indexed data. When the user performs a search, the request is sent to the indexer, and the relevant events are returned as field-value pairs.

![Image showing Splunk Search Head](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/0f7738f88ca807d1edf2ac7d84f6951c.png)

The Search Head also allows you to transform results into presentable tables and visualizations such as pie, bar, and column charts.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
