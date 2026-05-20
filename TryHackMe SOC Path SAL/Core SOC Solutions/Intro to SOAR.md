
To defend against attacks, a SOC team relies on various security solutions, such as SIEM, EDR, firewalls, and threat intelligence platforms. They also communicate with IT and management teams as part of their processes. However, as threats grow more complex and advanced, SOC teams face challenges like alert fatigue, manual processes, too many disconnected tools, and difficulties in communication across teams.

## What is SOAR?

Security Orchestration, Automation, and Response (SOAR) is a tool that unifies all the security tools used in a SOC. With SOAR, SOC analysts do not need to switch between SIEM, EDR, Firewall, and other security tools for their investigations. They can operate all these tools within a single SOAR interface. Along with unifying the security tools, it also provides ticketing and case management features to the analysts, through which they can document, track, and resolve their incidents in a structured way.

![[6645aa8c024f7893371eb7ac-1759484710562.png]]


The core strength of a SOAR tool comes from the following three main capabilities:

## 1. Orchestration

Traditionally, while investigating an alert, a SOC analyst has to switch between multiple security tools for the analysis. For example, during a VPN brute force, the analyst typically switches between the following tools:

1. **SIEM** to check if the user usually uses the subject IP for logging
2. **Threat Intelligence (TI) platforms** to verify the IP's reputation
3. **IAM tool** to disable the user if there was any successful attempt
4. **Ticketing system** to open and track the incident

This manual switching between different tools slows down the process. Orchestration solves this problem by coordinating all these tools together inside the SOAR. It connects different tools from various vendors within the unified SOAR interface. It defines workflows for investigating various types of alerts, known as **Playbooks**. These playbooks are predefined steps that tell the SOAR how to investigate an alert.

## 2. Automation

The art of coordinating with multiple tools through predefined actions (Playbooks), which we studied in Orchestration, can be automated. Automation means no more manual clicks needed from SOC analysts. SOAR will itself follow the playbooks. Let's resume the playbook for VPN brute force alert combined with the Automation.

1. SOAR receives the alert from SIEM
2. It automatically queries the SIEM for the user's historical logins
3. It automatically verifies the IP's reputation through TI platforms
4. If the IP is malicious, it automatically disables the user from the IAM
5. Lastly, it automatically opens a ticket in the ticketing system with all the details to initiate an investigation

This saves a tremendous amount of time for SOC analysts. They can handle hundreds of alerts without burning out.


## 3. Response

SOAR gives the ability to take actions using different tools from one unified interface. It also automates the response, as we saw earlier while looking at its Automation capability. For example, SOAR can follow the playbook of VPN Brute force and block the IP on the firewall, disable the user in the IAM, and open a ticket with all the details. 

The Orchestration, Automation, and Response capabilities of SOAR solve the major challenges a SOC team faces. With SOAR, there is no more alert fatigue, most of the processes are automated, and all the different tools are connected for coordination.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
