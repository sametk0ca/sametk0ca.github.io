The main focus of the SOC team is to keep ==**Detection**== and ==**Response**== intact.

# **Detection**

- **Detect vulnerabilities**: A vulnerability is a weakness that an attacker can exploit to carry out things beyond their permission level. A vulnerability might be discovered in any device’s software (operating system and programs), such as a server or computer. For instance, the SOC might discover a set of MS Windows computers that must be patched against a specific published vulnerability. Strictly speaking, vulnerabilities are not necessarily the SOC’s responsibility; however, unfixed vulnerabilities affect the security level of the entire company.
- **Detect unauthorized activity**: Consider the case where an attacker discovered the username and password of one of the employees and used them to log in to the company system. It is crucial to detect this kind of unauthorized activity quickly before it causes any damage. Many clues, such as geographic location, can help us detect this.
- **Detect policy violations**: A security policy is a set of rules and procedures created to help protect a company against security threats and ensure compliance. What is considered a violation would vary from company to company; examples include downloading pirated media files and sending confidential company files insecurely.
- **Detect intrusions**: Intrusions refer to unauthorized access to systems and networks. One scenario would be an attacker successfully exploiting our web application. Another would be a user visiting a malicious site and getting their computer infected.

# **Response**

- **Support with the incident response**: Once an incident is detected, certain steps are taken to respond to it. This response includes minimizing its impact and performing the root cause analysis of the incident. The SOC team also helps the incident response team carry out these steps.


There are three pillars of a SOC. With all these pillars, a SOC team becomes mature and efficiently detects and responds to different incidents. These pillars are **People**, **Process**, and **Technology**.



# **People**

Regardless of the evolution of automating the majority of security tasks, the **People** in a SOC will always be important. A security solution can generate numerous red flags in a SOC environment, which can cause huge noise.

Imagine you are part of a fire brigade team and have centralized software where all the city’s fire alarms are integrated. Suppose you get many fire notifications at once, all for different places. When you get into those locations, your team finds out most of those were only triggered by excessive smoke from cooking. Eventually, all the efforts will be a waste of time and resources.

In a SOC, with security solutions in place without human intervention, you'll end up focusing on more irrelevant issues. There are always the **People** who help the security solution to identify truly harmful activities and enable a prompt response.

The **People** are known as the SOC team. This team has the following roles and responsibilities.

![[6645aa8c024f7893371eb7ac-1718872774537.png]]

- **SOC Analyst (Level 1):** Anything detected by the security solution would pass through these analysts first. These are the first responders to any detection. SOC Level 1 Analysts perform basic alert triage to determine if a specific detection is harmful. They also report these detections through proper channels.
- ****SOC Analyst (Level 2)**:** While Level 1 does the first-level analysis, some detections may require deeper investigation. Level 2 Analysts help them dive deeper into the investigations and correlate the data from multiple data sources to perform a proper analysis.
- ****SOC Analyst (Level 3)**:** Level 3 Analysts are experienced professionals who proactively look for any threat indicators and support in the incident response activities. The critical severity detection reported by Level 1 and Level 2 Analysts are often security incidents that need detailed responses, including containment, eradication, and recovery. This is where Level 3 analysts’ experience comes in handy.
- **Security Engineer:** All analysts work on security solutions. These solutions need deployment and configuration. Security Engineers deploy and configure these security solutions to ensure their smooth operation.
- **Detection Engineer:** Security rules are the logic built behind security solutions to detect harmful activities. Level 2 and 3 Analysts often create these rules, while the SOC team can sometimes also utilize the detection engineer role independently for this responsibility.
- **SOC Manager:** The SOC Manager manages the processes the SOC team follows and provides support. The SOC Manager also remains in contact with the organization’s CISO (Chief Information Security Officer) to provide him with updates on the SOC team’s current security posture and efforts.

**Note:** The roles in the SOC team can increase or decrease depending on the size and criticality of the organizations.

# **Process**

## Alert Triage

The alert triage is the basis of the SOC team. The first response to any alert is to perform the triage. The triage is focused on analyzing the specific alert. This determines the severity of the alert and helps us prioritize it. The alert triage is all about answering the ==5 Ws==. What are these 5 Ws?


![[6645aa8c024f7893371eb7ac-1718872960352.png]]![[Pasted image 20251105135945.png]]

## Reporting

The detected harmful alerts need to be escalated to higher-level analysts for a timely response and resolution. These alerts are escalated as tickets and assigned to the relevant people. The report should discuss all the 5 Ws along with a thorough analysis, and screenshots should be used as evidence of the activity.



# **Technology**

An organization’s network consists of many devices and applications. As a security team, individually detecting and responding to threats in each device or application would require significant effort and resources. Security solutions centralize all the information of the devices or applications present in the network and automate the detection and response capabilities.

Let's get a brief understanding of some of these security solutions:

- **==SIEM==:** Security Information and Event Management (SIEM) is a popular tool used in almost every SOC environment. This tool collects logs from various network devices, referred to as log sources. Detection rules are configured in the SIEM solution, which contains logic to identify suspicious activity. The SIEM solution provides us with the detections after correlating them with multiple log sources and alerts us in case of a match with any of the rules. Modern SIEM solutions surpass this rule based detection analysis, providing us with user behavior analytics and threat intelligence capability. Machine learning algorithms support this to enhance the detection capabilities.

**Note:** The SIEM solution only provides the **Detection** capabilities in a SOC environment.

- ==**EDR==:** Endpoint Detection and Response (EDR) provides the SOC team with detailed real-time and historical visibility of the devices’ activities. It operates on the endpoint level and can carry out automated responses. EDR has extensive detection capabilities for endpoints, allowing you to investigate them in detail and respond with a few clicks.
- **==Firewall==:** A firewall functions purely for network security and acts as a barrier between your internal and external networks (such as the Internet). It monitors incoming and outgoing network traffic and filters any unauthorized traffic. The firewall also has some detection rules deployed, which help us identify and block suspicious traffic before it reaches the internal network.

Several other security solutions play unique roles in a SOC environment, such as Antivirus, EPP, IDS/IPS, XDR, SOAR, and more. The decision on what Technology to deploy in the SOC comes after careful consideration of the threat surface and the available resources in the organization.

# **Security Hierarchy**


![[678ecc92c80aa206339f0f23-1756329066210.png]]

In tiny companies, the IT department takes the role of securing the company. Small to medium-sized companies may have a generic "Information Security" team that does all sorts of tasks. For this room, we will focus on bigger companies with a CISO overseeing multiple security teams, each handling a specific task. For example:

- **Red Team**: Offensive security experts, pentesters, or ethical hackers who look for security issues
- **GRC Team**: Specialists managing policies and ensuring compliance with regulations like [PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)
- **Blue Team**: Defensive security experts like SOC analysts, engineers, or incident responders



# **Meet the Blue Team**

## Security Operations Center (SOC)

SOC is the central hub for an organization's cyber security - they are the first line of defense, work with various alerts, and handle most attacks. You can read more about SOC structure in [this room](https://tryhackme.com/room/socfundamentals), but an efficient SOC is usually composed of the following roles:

- **L1 Analysts**: Junior members who triage alerts and pass complex cases to L2
- **L2 Analysts:** Experienced members who investigate more advanced attacks
- **Engineers**: Experts in configuring security tools like EDR or SIEM
- **Manager**: A person who manages the whole SOC team


![[678ecc92c80aa206339f0f23-1756425129235.svg]]
## Cyber Incident Response Team (CIRT)

If SOC expertise is not enough or the incident goes out of control, you urgently call the "==firefighters==" - CIRT, also called CSIRT or CERT. The members should have a broad knowledge of cyber threats and handle breaches without depending on tools like EDR or SIEM. A CIRT job is stressful and responsible, but also rewarding.

![[678ecc92c80aa206339f0f23-1756425129228.svg]]



## Internal SOC vs MSSP

Not every organization has the expertise to operate a SOC on its own and relies on a Managed Security Services Provider (MSSP), a company that delivers outsourced security services, most commonly SOC, to its clients. Working at MSSP is typically high-pressure, but it is also a good option to quickstart your career. While we recommend applying for any open SOC position as your first job, it's also important to understand the differences

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
