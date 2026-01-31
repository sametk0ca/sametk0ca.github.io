
Network Traffic Analysis (NTA) is a process that encompasses capturing, inspecting, and analyzing data as it flows in a network. Its goal is to have complete visibility and understand what is communicated inside and outside the network. It is important to stress that NTA is not a synonym for the tool Wireshark. It is more than that: It is a combination of correlating several logs, deep packet inspection, and network flow statistics with specific outlined goals (which we will discuss later on).

Knowing how to analyze network traffic is an essential skill, not only for an aspiring SOC L1 analyst but also for many other blue and red team roles. As an L1 analyst, you need to be able to navigate through the sea of network information and understand what is normal and what deviates from the baseline.

In this room, we will focus on defining network traffic analysis, why you need it, what and how you can observe network traffic, and some of the sources and flows of network traffic you need to be aware of.


## Why should we analyse network traffic?

Generally, we will use network traffic analysis to:

- Monitor network performance
- Check for abnormalities in the network. E.g., sudden performance peaks, slow network, etc
- Inspect the content of suspicious communication internally and externally. E.g., exfiltration via DNS, download of a malicious ZIP file over HTTP, lateral movement, etc

From a SOC perspective, network traffic analysis helps:

- Detecting suspicious or malicious activity
- Reconstructing attacks during incident response
- Verifying and validating alerts



# What Network Traffic Can We Observe?


The best way to showcase the traffic we can observe in the network is by using the architecture implemented in nearly every device with a network interface: the ==TCP/IP stack==. The image below shows the different layers of the TCP/IP model. Each layer describes the required information (headers) to pass the data to the next layer. The information included in each header, together with the application data, is precisely what we want to observe. Logs often include bits and pieces of these headers, but never the full packet details. This is why we need to do network traffic analysis.

![[66c44fd9733427ea1181ad58-1760351911672.png]]


**Application**  
On the application layer, we can find two important information structures: the application header information and the application data itself (==payload==). This information will change depending on which application layer protocol is used.


**Transport**  
The application data and header are segmented and encapsulated at the transport layer into smaller pieces. Each piece includes a transport header, in most cases TCP or UDP. 

==Firewall logs often include the source and destination ports and the flags==, but all the other fields are often not included. However, they are valuable for detecting certain types of attacks, such as session hijacking. **Session hijacking** can be detected by analyzing the **sequence numbers** included in the header. If the sequence numbers are suddenly far apart, further investigation is warranted. 


**Internet**  
When the transport layer sends down a segment, the internet layer also adds its header. If the segment is larger than the ==Maximum Transmission Unit (MTU==), it will be divided into ==fragments==, and a header will be added to each of them. The fields that are most often logged are the source and destination IP and TTL. This is sufficient for most use cases. But, if we want to, for example, detect fragmentation attacks, we will need to inspect the fragment offset and total length fields as well. There are different variations of a fragmentation attack. For example, an attacker can create tiny fragments to evade the IDS or mess up the reassembly of fragments by using ==overlapping== byte ranges. The example below shows overlapping byte ranges. The ==offset== in line 3 (highlighted in yellow) overlaps with the one in line 2. This means that the complete packet can be reassembled one way or another. Attackers can use this technique to bypass an IDS. For example : Fragmentation Attack

Buradaki mantığı sana basitçe, adım adım açıklayayım:

### 1. Normal Süreç: MTU ve Parçalama Nedir?

İnternette veriler taşınırken belirli bir boyut sınırı vardır. Buna **MTU (Maximum Transmission Unit)** denir. Genellikle bu sınır 1500 byte'tır.

- Eğer göndermek istediğin veri bu sınırdan büyükse, sistem bu veriyi daha küçük parçalara (**fragment**) böler.
    
- Her parçaya bir "etiket" yapıştırır: "Bu parça 1. sıradadır", "Bu parça 1480. byte'tan başlar" gibi. Buna **Offset** denir.
    
- Alıcı bilgisayar bu etiketlere (offset) bakarak parçaları doğru sırayla birleştirir ve orijinal veriyi oluşturur.
    

### 2. Saldırı Mantığı: Örtüşen Parçalar (Overlapping)

Görseldeki metin, saldırganların bu sistemi nasıl kandırdığını anlatıyor.

- Saldırgan, güvenlik duvarını (IDS) atlatmak için bilerek hatalı veya karmaşık parçalar gönderir.
    
- **"Overlapping Byte Ranges" (Örtüşen Byte Aralıkları):** Saldırgan, aynı yere aitmiş gibi görünen iki farklı parça gönderir.
    
- IDS (Güvenlik sistemi), bu parçaları birleştirmeye çalışırken kafası karışır. Hangi parçayı kabul edeceğini bilemez ve bazen zararlı olan paketi içeri alarak saldırının gerçekleşmesine izin verir.
    

### 3. Görseldeki Tablonun (Logların) Analizi

Görselin altındaki siyah ekrandaki loglar (Wireshark görüntüsü), bu saldırının kanıtıdır. Buraya dikkat et:

- **1. Satır:** Birinci parça gönderilmiş. (Offset=0, Uzunluk=1480). Yani 0 ile 1480 arasını doldurdu.
    
- **2. Satır:** İkinci parça gelmiş. **Offset=1480** diyor. Yani "Ben 1480. sıradan başlıyorum" diyor. Buraya kadar her şey normal.
    
- **3. Satır (SARI İLE İŞARETLİ):** Burası kritik nokta. Bu paket de **Offset=1480** diyor.
    
    - **Sorun şu:** 2. satırdaki paket zaten 1480. sıraya oturmuştu. 3. satırdaki paket de "Hayır, 1480. sıraya ben oturacağım" diyor.
        
    - Bu duruma **Overlap (Örtüşme)** denir.
        

### Özetle

Saldırgan, bilgisayara "Al sana yapbozun parçaları" diyor ama aynı boşluğa uyan iki farklı parça veriyor. Biri masum bir resim parçası, diğeri ise virüslü bir parça olabilir. Güvenlik sistemi (IDS) hangisini seçeceğini şaşırırsa, saldırgan içeri sızmış olur.


# Network Traffic Sources and Flows

In the previous task, we discussed what we can observe theoretically based on the TCP/IP stack. Practically, it is more helpful to focus on specific sources and flows. A corporate network typically has some predetermined network flows and sources. We can group the sources into two categories:

- Intermediary
- Endpoint

The flows we can also group into two categories:

- North-South: Traffic that exits or enters the LAN and passes the firewall
- East-West: Traffic that stays within the LAN (including LAN that extends to the cloud)


## Sources

As mentioned, two network traffic sources exist: endpoint and intermediary devices. These devices can be found within the LAN and WAN.

**Intermediary Sources**  
These are devices through which traffic mostly passes. While they generate some traffic, it is significantly lower than what endpoint devices generate. ==Under this category, we can find firewalls, switches, web proxies, IDS, IPS, routers, access points, wireless LAN controllers, and many more.== Maybe less relevant for us, but all the infrastructure of Internet Service Providers is also considered part of this category.

The traffic that originates from these devices comes from services like routing protocols (EIGRP, OSPF, BGP), management protocols (SNMP, PING), logging protocols (SYSLOG), and other supporting protocols (ARP, STP, DHCP).

**Endpoint Sources**  
These are devices where traffic originates and ends. Endpoint devices take the bulk of the network bandwidth. ==Devices that fall under this category are servers, hosts, IoT devices, printers, virtual machines, cloud resources, mobile phones, tablets, and many more.==


## Flows

A network traffic flow is typically determined by the services available in the network, such as Active Directory, SMB, HTTPS, and so on. In a typical corporate network, we can group these flows into ==North-South and East-West traffic.==

**North-South Traffic**  
NS traffic is often monitored closely as it flows from the LAN to the WAN and vice versa. The most well-known services in this category are client-server protocols like HTTPS, DNS, SSH, VPN, SMTP, RDP, and many more. Each of these protocols has two streams: ingress (inbound) and egress (outbound). All of this traffic passes the firewall in one way or another. ==Configuring firewall rules and logging properly are key to visibility.==

**East-West Traffic**  
EW traffic stays within the corporate LAN, so it is often monitored less. However, it is important to keep track of these flows. When the network is compromised, an attacker will often exploit different services ==internally to move laterally within the network==. As we see below, there are many services within this category. Click on each category to see which services it contains.

Directory, Authentication & Identity Services

File shares & print services

Router, switching, and infrastructure services

Application Communication

Backup & Replication

Monitoring & Management

Now that we have covered what we can and should observe in a network, let's examine how. As mentioned in the introduction, network traffic analysis focuses on combining multiple sources of information, analyzing them, finding patterns, and using the results to inform actions.

We can obtain these sources of information in multiple ways:

- Logs
- Full Packet Capture
- Network Statistics

## Logs

Logs are our first entry into acquiring information about what is going on in the network. Each system and protocol in the network includes a way of logging information. It is essential to know that there is no universal standard for implementing logging on each system and protocol. Each vendor chooses how to implement logging for themselves. For example, Microsoft implements Windows Event Logs. Also, the data that is logged is up to the vendor. Most vendors will not log a full packet as it enters or exits the system. They will log some fields that they deem useful, such as a source IP address and a destination IP address. On the terminal below, we see some example logs of authentication on a Linux host using the Syslog format and an Apache web server access log that uses the CLF standard.


When the logs don't provide enough information, we must dig deeper. To do so, we need to correlate logs, inspect full packet captures, and check network statistics.


## Full Packet Capture

In task three, we discussed what a full packet looks like. Now, we want to know how to capture and inspect those packets. To do this, we have two options:

- Install a physical network tap
- Configure port mirroring

**Network Tap**  
A network tap is a physical device you place inline in your network. These devices create a copy of all the network traffic that passes without affecting performance. That copied data is then forwarded to a packet capture box, IDS, or other system using the dedicated monitoring port. It is interesting to know that a TAP operates only on the link layer of the TCP-IP model; it does not need a MAC or IP address, because it copies the electrical/light signals and sends them to its monitoring port. This way, there is no added delay to the network. 


**Port Mirroring**  
Port mirroring is a software approach to copying packets from one port on an intermediary device to another that is attached to, for example, an IDS, packet capture box, or other systems. Each vendor has its own name. Cisco, for example, calls it SPAN. On the terminal below, we can see how to configure SPAN on a Cisco device.

![[66c44fd9733427ea1181ad58-1760354092835.png]]