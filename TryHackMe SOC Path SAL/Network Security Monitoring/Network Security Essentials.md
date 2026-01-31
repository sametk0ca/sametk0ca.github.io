
## Network Components - Building Blocks of a Network

A computer network is not just a random collection of devices; it is an organized structure where network assets connect to enable communication, resource sharing, and connectivity with each other and the world.


## Small Enterprise Network

From a security perspective, knowing what these devices do and why they’re important helps quickly identify suspicious activity. Let's take an example of a small enterprise network, and understand its key components, usage, and their importance from a security perspective:

### User Workstations (Endpoints)

Employees do their daily work at workstations (PCs, laptops). However, they are also the most common entry point for attackers, ==often via phishing emails or malicious downloads.== 

- Example: A phishing email drops malware on a finance user’s PC.
- Why it matters: Endpoints are often less monitored, but a compromise here can give attackers a foothold to move laterally.

**Importance**

Endpoint logs can reveal malicious processes, but network logs may first show C2 (Command & Control) connections.

### File & Database Servers

These servers store the business's most important asset, its data. File servers provide centralized access to shared documents, while database servers manage structured data like customer records, HR information, or financial data.

**Importance**

Attackers usually target these servers because compromising them means access to valuable or sensitive data. ==Ransomware== operators, in particular, target file servers to maximize their impact. Data exfiltration campaigns often involve stealthily moving data from these servers out of the network.

### Application Servers (Web, Email, VPN, etc.)

These servers provide services that employees and customers rely on daily.

- Web Servers: Host company websites and web applications.
- Email Servers: Handle corporate communications.
- VPN Gateways: Allow secure remote access to internal resources.

**Importance**

Because they are ==externally facing==, application servers are high-value targets. Attackers scan them constantly for ==software vulnerabilities or weak configurations==. Exploiting one often provides a foothold into the internal network.

From a security perspective, we need to monitor application logs, firewall alerts, and IDS signatures to identify:

- Exploit attempts (e.g., SQL injection on a web app).
- Brute-force login attempts on email or VPN services.
- Suspicious external IPs interacting with sensitive applications.


### Active Directory (AD) / Authentication Servers

Active Directory is the identity backbone of most enterprise networks. It manages users, groups, computers, and their access rights. Employees use their AD credentials to log into their computers, access email, file servers, and internal applications.

**Importance**

- AD is the main component that controls all user accounts and systems within the network.
- Attackers commonly target AD for privilege escalation, persistence, and lateral movement.
- A single compromised ==domain admin account== can bring down the entire enterprise.

From a security perspective, we need to monitor ==authentication== logs for suspicious behavior such as:

- Multiple failed login attempts (password spraying).
- Unusual logins from external IPs or at odd hours.
- Accounts accessing systems they normally shouldn’t.


### Routers & Switches (Network Infrastructure)

Routers connect different networks, most importantly ==linking== the enterprise LAN to the Internet. Switches ==connect== devices within the same network, ensuring employees’ PCs, printers, and servers communicate seamlessly. These devices are the circulatory system of the enterprise.

**Importance**  
While routers and switches are not directly exposed in most enterprise setups, if compromised, they provide attackers with the ability to:

- Intercept and manipulate traffic (Man-in-the-Middle attacks).
- Create backdoors by rerouting traffic.
- Open hidden channels to the Internet.


### Firewalls / Perimeter Devices

A firewall is the primary security gateway that ==controls traffic== between the trusted internal network and the untrusted Internet. It inspects incoming and outgoing packets and decides whether to ==allow or block== them based on defined security rules. Modern firewalls also perform deep inspection of applications, intrusion prevention, and even malware detection.

**Importance:**

- Protects the enterprise from direct exposure to the Internet.
- Prevents unauthorized access to internal services (e.g., database or RDP).
- Logs every connection attempt, successful or blocked. These logs are often the earliest indicators of attacks such as port scans, brute-force attempts, or exploitation attempts.



Network visibility is essential in cyber security. It's the ability to monitor and understand what's happening across your network. It's a core principle for security analysts: ==you can't defend what you can't see==. Effective visibility enables threat detection, incident investigation, and a strong security posture. It’s not about tracking every packet but having the tools to build a clear picture. Without it, you're blind to potential threats.

The network visibility comes from two primary sources of logs. You must understand the difference between them to piece together an attack timeline effectively.


## Host-Centric Logs

![Image showing a host machine](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/5e8dd9a4a45e18443162feab-1758767657414.png)

Host-centric logs are generated by ==individual devices (hosts)== on the network, such as servers, workstations, and laptops. These logs give us a detailed, ground-level view of what's happening on a specific machine. They are essential for understanding the direct impact of an attack on a system.

### Key Host-Centric Log Sources

- **Operating System Logs:** Windows Event Logs, Linux `syslog`, macOS logs. These record events like user logons, process creation, service startups, and failed login attempts.
- **Application Logs:** Logs from software running on the host, such as web servers (Apache, Nginx), databases (MySQL, MSSQL), and other applications.
- **Security Tool Logs:** Logs from antivirus software, Endpoint Detection and Response (EDR) agents, and host-based intrusion detection systems (HIDS).


## Network-Centric Logs

![Image showing a host machine emitting network connections](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/5e8dd9a4a45e18443162feab-1758767252683.png)

While host logs tell us what's happening on a device, network-centric logs tell us what's happening ==between devices==. These are generated by network appliances that sit on the network and monitor the traffic flowing through them.

- **What they show:** Source and destination IPs, ports, protocols, and the action taken (e.g, allowed or blocked).
- **Why they are important:** They give you the crucial "when," "where," and "how." They can reveal an attacker's initial reconnaissance attempts, lateral movement between systems, or attempts to exfiltrate data.

To get a complete picture, you need to correlate both. Think of it this way: Host-centric logs tell you what happened inside a room, while network-centric logs tell you who entered and left the building.

## Key Network-Centric Log Sources

- **Firewalls:** The firewall logs provide a record of every connection allowed or denied based on pre-defined security rules. Firewall logs are the first place to look for unauthorized connection attempts from the internet.
- **Intrusion Detection/Prevention Systems (IDS/IPS):** They monitor network traffic for patterns that match known malicious attacks (signatures) or for unusual behavior (anomalies). Their logs are critical for detecting active attacks in real time.
- **Routers and Switches:** While not logging in the traditional sense, devices like routers can generate flow data. This data summarizes traffic conversations, telling who talked to whom, for how long, and how much data was sent. It’s excellent for getting a high-level overview of network activity.
- **Web Proxies:** These logs are a goldmine for organizations that route their web traffic through proxies. They record every website user's visit, providing visibility into web-based threats, policy violations, or data exfiltration attempts.
- **VPN:** These devices manage remote access for employees. Their logs track who is connecting to the corporate network, from where, and at what time, which is essential for monitoring the security of remote connections.


# Network Perimeter


The network perimeter is the boundary that separates an organization's internal network (trusted zone, like employees, servers, business applications) from the external Internet (untrusted zone). It’s the point where data enters or leaves the network. Think of it as the main gate or front door of a secure building. All traffic coming from the Internet must pass through this point to enter your network, and all internal traffic must pass through it to exit the Internet. The network perimeter is your first and most critical line of defense.

- The internal network is where business-critical systems live.
- The external Internet is full of potential threats.
- The perimeter is the controlled entry point through which all traffic passes.