
SNORT is an open-source, rule-based Network Intrusion Detection and Prevention System (NIDS/NIPS). It was developed and still maintained by Martin Roesch, open-source contributors, and the Cisco Talos team.  The official description: "Snort is the foremost Open Source Intrusion Prevention System (IPS) in the world. Snort IPS uses a series of rules that help define malicious network activity and uses those rules to find packets that match against them and generate alerts for users."

|   |   |
|---|---|
|**Parameter**|**Description**|
|**-V / --version**|This parameter provides information about your instance version.|
|**-c**|Identifying the configuration file|
|**-T**|Snort's self-test parameter allows you to test your setup with this parameter.|
|- **q**|Quiet mode prevents Snort from displaying the default banner and initial information about your setup.|
# Sniffer Mode

Like tcpdump, Snort has various flags that allow for viewing different data about the packet it is ingesting.

Sniffer mode parameters are explained in the table below;

|   |   |
|---|---|
|**Parameter**|**Description**|
|**-v**|Verbose. Display the TCP/IP output in the console.|
|**-d**|Display the packet data (payload).|
|**-e**|Display the link-layer (TCP/IP/UDP/ICMP) headers.|
|-**X**|Display the full packet details in HEX.|
|-**i**|This parameter helps define a specific network interface to listen to or sniff. Once you have multiple interfaces, you can choose a specific interface to sniff.|

# Packet Logger Mode

You can use Snort as a sniffer and log the sniffed packets via logger mode. You only need to use the packet logger mode parameters, and Snort does the rest to accomplish this.

Packet logger parameters are explained in the table below;

|   |   |
|---|---|
|**Parameter**|**Description**|
|-l|Logger mode, target **log, and alert** output directory. Default output folder is **/var/log/snort**<br><br>The default action is to dump as tcpdump format in **/var/log/snort**|
|**-K ASCII**|Log packets in ASCII format.|
|-r|Reading option: Review the logged events in Snort.|
|**-n**|Specify the number of packets to be processed or read. Snort will stop after reading the specified number of packets.|

# IDS/IPS Mode


The capabilities of Snort are not limited to sniffing and logging traffic. IDS/IPS mode enables you to manage traffic according to user-defined rules.

| **Parameter** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -c            | Defining the configuration file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -T            | Testing the configuration file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **-N**        | Disable logging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **-D**        | Background mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **-A**        | Alert modes;<br><br>**Full:** Full alert mode, providing all possible information about the alert. This mode is also the default; once you use -A and don't specify a mode, Snort defaults to this mode.<br><br>**Fast mode displays the alert message, timestamp, source and destination IP addresses**, along with port numbers.<br><br>Console: Provides fast style alerts on the console screen.<br><br>**cmg:** CMG style, basic header details with payload in hex and text format.<br><br>**None:** Disabling alerting. |


# PCAP Investigation Mode

Capabilities of Snort are not limited to sniffing, logging and detecting/preventing the threats. PCAP read/investigate mode helps you work with pcap files. Once you have a pcap file and process it with Snort, you will receive default traffic statistics with alerts depending on your ruleset.

| **Parameter**           | **Description**                                   |
| ----------------------- | ------------------------------------------------- |
| **-r / --pcap-single=** | Read a single pcap                                |
| **--pcap-list=""**      | Read pcaps provided in command (space separated). |
| **--pcap-show**         | Show pcap name on console during processing.      |

# Snort Rule Structure

![[Pasted image 20251217143559.png]]

Each rule should have a type of action, a protocol, source and destination IP addresses, source and destination port numbers, and an option. Remember, Snort is in passive mode by default. So most of the time, you will use Snort as an IDS. You will need to start **"inline mode" to turn on IPS mode.** However, before you begin using inline mode, it is essential to be familiar with Snort's features and rules.

|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action**                       | There are several actions for rules. Ensure you understand the functionality and test it thoroughly before creating rules for live systems. The following are the most common actions:<br><br>- alert: Generate an alert and log the packet.<br>- log: Log the packet.<br>- drop: Block and log the packet.<br>- reject: Block the packet, log it, and terminate the packet session.                                                                        |
| **Protocol**                     | The protocol parameter identifies the type of protocol that was filtered for the rule.<br><br>Note that Snort2 supports only four protocol filters in the rules (IP, TCP, UDP, and ICMP). However, you can detect the application flows using port numbers and options. For instance, if you want to detect FTP traffic, you cannot use the FTP keyword in the protocol field; instead, you can filter FTP traffic by investigating TCP traffic on port 21. |
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **IP Filtering**                 | alert icmp 192.168.1.56 any <> any any  (msg: "ICMP Packet From "; sid: 100001; rev:1;)<br><br>This rule will create an alert for each ICMP packet originating from the 192.168.1.56 IP address.                                                                                                                                                                                                                                                            |
| **Filter an IP range**           | alert icmp 192.168.1.0/24 any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each ICMP packet originating from the 192.168.1.0/24 subnet.                                                                                                                                                                                                                                                            |
| **Filter multiple IP ranges**    | alert icmp [192.168.1.0/24, 10.1.1.0/24] any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each ICMP packet originating from the 192.168.1.0/24 and 10.1.1.0/24 subnets.                                                                                                                                                                                                                            |
| **Exclude IP addresses/ranges.** | The "negation operator" is used to exclude specific addresses and ports. The negation operator is indicated with "!".<br><br>alert icmp !192.168.1.0/24 any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each ICMP packet not originating from the 192.168.1.0/24 subnet.                                                                                                                          |
| **Port Filtering**               | alert tcp any any <> any 21  (msg: "FTP Port 21 Command Activity Detected"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet sent to port 21.                                                                                                                                                                                                                                                                                 |
| **Exclude a specific port**      | alert tcp any any <> any !21  (msg: "Traffic Activity Without FTP Port 21 Command Channel"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet not sent to port 21.                                                                                                                                                                                                                                                             |
| **Filter a port range (Type 1)** | alert tcp any any <> any 1:1024   (msg: "TCP 1-1024 System Port Activity"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet sent to ports between 1 and 1024.                                                                                                                                                                                                                                                                 |
| **Filter a port range (Type 2)** | alert tcp any any <> any:1024   (msg: "TCP 0-1024 System Port Activity"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet sent to ports 1 through 1024.                                                                                                                                                                                                                                                                       |
| **Filter a port range (Type 3)** | alert tcp any any <> any 1025: (msg: "TCP Non-System Port Activity"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet sent to a source port that is higher than or equal to 1025.                                                                                                                                                                                                                                             |
| **Filter a port range (Type 4)** | alert tcp any any <> any [21,23] (msg: "FTP and Telnet Port 21-23 Activity Detected"; sid: 100001; rev:1;)<br><br>This rule will create an alert for each TCP packet sent to ports 21 and 23.                                                                                                                                                                                                                                                               |

**Direction**

The direction operator indicates the traffic flow to be filtered by Snort. The left side of the rule shows the source, and the right side shows the destination.

- **->** Source to destination flow.
- **<>** Bidirectional flow

Note that there is no "<-" operator in Snort.


![[Pasted image 20251217143712.png]]