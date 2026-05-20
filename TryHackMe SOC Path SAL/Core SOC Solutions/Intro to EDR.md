Endpoint Detection and Response (EDR) is a security solution designed to monitor, detect, and respond to advanced threats at the endpoint level. As a SOC analyst, it is essential for you to understand how the EDR works since it is a widely adopted solution in organizations to protect their endpoints.

The increase in the use of digital devices is undeniable. Most of the business's core functions rely on the use of these digital devices. Cyber threats, on the other hand, are also increasing day by day. To protect these devices, organizations implement several security measures, most of which are to protect the network on which they operate these digital devices. However, the fast adoption of Remote Work has exposed these devices as they are out of the perimeter protection deployed on the organization's network. 

To ensure these endpoint devices are protected even out of the network, we need a security solution that guards all devices in different areas and is capable of fighting advanced threats. Endpoint Detection and Response (EDR) is a security solution that offers deep-level protection for endpoints. No matter where the endpoints are, the EDR will make sure they are monitored constantly and threats are detected.

## Features of EDR

There are three main features of an EDR, which can also be referred to as the three pillars of an EDR solution.

![[6645aa8c024f7893371eb7ac-1754897179751.png]]



# Visibility

A good analysis often depends on the available level of visibility of the activity. This is one of the features of **EDR** that makes it unique from other endpoint security solutions. The level of visibility EDR provides is impressive. ==It collects detailed data from the endpoints==, which includes process modifications, registry modifications, file and folder modifications, user actions, and much more. It then presents this information in a very structured format to the analyst. The analyst can see the whole process tree with a complete activity timeline of the sequence of actions. The analyst can also access the historical data of any endpoint for threat hunting or any other purpose. Any detections in the EDR land with a whole context.

![[6645aa8c024f7893371eb7ac-1755242793089.png]]

# Detection 

The detection feature of EDR wins over traditional detection capabilities. It incorporates signature-based detections as well as behavior-based detections, such as unexpected user activities. With modern machine learning capabilities, it identifies any deviation from the baseline behavior and instantly flags it. It can also detect fileless malware that resides in memory. It also allows us to feed custom IOCs for threat detections.


# Response 

EDR also empowers analysts to take action on detected threats. These actions can be taken at any endpoint within the central EDR console. Imagine getting a detection on the EDR with full-fledged details on when, where, and what happened, and you have to opt for the best possible action for that detection. As an analyst, you may decide to isolate a complete endpoint, terminate a process, or quarantine some files. You can also connect to the host remotely and execute actions independently. ==You can do this all from within the EDR console.==


## ==Why do we need an EDR when we already have an Antivirus (AV) on the endpoints?==


Both of these security solutions have the same motive of protecting the endpoint on which they are installed. However, both differ in the level of protection they provide. Let's assume an airport is an endpoint that needs protection. One layer of protection is to check the passports of people when they pass through immigration. The immigration check (AV) monitors incoming people and matches their passports with a list of known criminals in its database. If there is a match, the entry is blocked and caught. 

Sounds like a smart protection, right?

But, what happens if somebody who has never been identified as a criminal in the past and has an innocent personality tries to come in? The immigration check will let them in. Now, what if this innocent person were a professional thief trained to evade basic security? The airport has an undetected threat inside!

This is where an EDR comes in.

An EDR in this analogy would be the security officers stationed inside the airport (endpoint). These security officers ==would constantly monitor the security cameras and motion sensors== in the airport (endpoint). Compared to the immigration check (AV), the security officers (EDR) enhance the protection of the airport (endpoint) through CCTV monitoring and motion sensors. Even if somebody manages to evade the immigration check, the security officers will constantly be monitoring their actions, such as:

- Are they roaming close to restricted areas?
- Is their behaviour suspicious?
- Are they leaving their bags somewhere unattended?

The security officers can also take action if something does not feel right to them or alert the airport management with complete details of what happened.

The Antivirus (AV) may detect some basic threats, but to detect advanced threats that evade normal detections, we need an EDR. Unlike antivirus software's basic signature-based detection, it monitors and records the behaviors of the endpoint. An EDR also provides organization-wide visibility of any activity. For example, if a suspicious file is detected on one endpoint, the EDR will also check it across all the other endpoints.

# ==How an EDR Works?==

- How does an EDR manage to provide this much visibility of the endpoints?
- How can it detect advanced threats?
- How can a few clicks eradicate the threat from an endpoint?
## Agents

We can integrate multiple endpoints with our EDR and manage them through a centralized console. There are EDR agents that we have to deploy inside those endpoints. These agents are also sometimes referred to as sensors. They are the eyes and ears of the EDR. Their job is to sit at the endpoint and monitor all the activities. The information about these activities is sent in detail to the EDR central console in real time. The EDR agents can do some basic signature-based and behavior-based detections by themselves and send them to the EDR console, which triggers alerts.

![[6645aa8c024f7893371eb7ac-1752910180686.png]]

## EDR Console

All the detailed data sent by the EDR agents is correlated and analyzed through complex logic and machine learning algorithms. The threat intelligence information is matched with the collected data. The EDR is just like the brain connecting all the dots. These dots connect to form a detection, often called an alert. 

The following screenshot shows the dashboard of an EDR console. All the data from the endpoint agents is coming into this console, and the detections are happening here. This dashboard gives a holistic view of the current status of detections in all the endpoints.

## What happens after Detection?

When a detection comes, it's a SOC analyst's responsibility to acknowledge the alert and prioritize it. The prioritization is made easy by the EDR itself. It gives severities to all the alerts (Critical, High, Medium, Low, Informational). The alert with the highest severity is investigated as a priority. For the investigation, once the alert is clicked, the analyst can see all the details of the detection. This includes any files executed, processes executed, network connection attempts, registry modifications, and much more. Based on the available data, the analyst's job is first to use their expertise to determine if the alert is a false positive or a true positive. In case of a true positive, the analyst can take actions from within the EDR console.

## What is Telemetry?

In the previous task, we learned about EDR agents, which collect different data from their endpoints and push it to the EDR console. This data is known as Telemetry. Telemetry is the black box of an endpoint with everything necessary for detection and investigation.

## Collected Telemetry

Usually, many activities are going on in the endpoints, most of which are legitimate. It is often difficult to differentiate between regular and malicious activity. The more data is collected, the better judgments can be made. EDR collects detailed telemetry from the endpoints. Let's take a brief look at some of the telemetry that it collects:

- **Process Executions and Terminations**  
    It keeps track of all the running and idle processes, which helps to identify suspicious child-parent process relationships, suspicious executables initiating a process, malware payload, etc.
- **Network Connections**  
    All the endpoints' network connections are monitored, which helps identify any connection to a C2 server, unusual port usage, data exfiltration, or lateral movement within the network.
- **Command Line Activity**  
    It captures all the commands executed on the endpoints in CMD, PowerShell, etc., which helps to identify malicious command execution, obfuscated PowerShell script executions, which are often missed by a traditional antivirus.
- **Files and Folders Modifications**  
    Threat actors modify different files and folders during data staging, ransomware executions, and malicious file dropping. The EDR tracks this.
- **Registry Modifications**  
    The registry is a goldmine of information about the configurations in a Windows system. There are many registry modifications that occur during a malicious activity, and most of these are monitored by the EDR.


## Detection

Based on the telemetry received from the endpoints, some advanced detection techniques are applied to this data. Some of these techniques include:

- **Behavioral Detection**  
    Instead of just matching the signatures with known threats, it observes the complete behavior of a file. Advanced threats craft their malware to look clean and use legitimate processes to carry out their attack. EDR catches this behavior.  
    **Example:** A process winword.exe spawning PowerShell.exe will be flagged by the EDR due to the behavior. A Word document spawning a PowerShell is an unusual parent-child relationship.
- **Anomaly Detection**  
    With time, EDR understands the baseline behavior of the endpoints. Any activity that deviates from this behavior will be flagged. During any malicious activity, the endpoint's behavior deviates from normal. EDR picks it up. Sometimes, this can generate false positives as well. However, with the full context it gives, the analyst can identify its legitimacy.  
    **Example:** On one of the endpoints, a process modifies an auto-start registry key, which is not a common behavior on the endpoint.
- **IOC matching**  
    EDRs have some strong threat intelligence field integrations. Except for zero-day attacks, most of the attacks have indicators published in the threat intelligence feeds. EDR flags any activity that matches any known IOC.  **Example:** A user downloads a file that drops an executable. The executable is often used in a specific attack. The hash of this executable will get matched with the threat intelligence feed and instantly flagged by the EDR.
- **MITRE ATT&CK Mapping**  
    Any activity flagged by the EDR is not only marked as malicious or suspicious but also mapped with the MITRE Tactic and Technique (attack stage) that the particular activity was on. This proves to be very helpful for the analysts.  
    **Example:** If the EDR flags the creation of a scheduled task for any reason, it will likely map this activity to the following:
    - Tactic: Persistence
    - Technique: Scheduled Task/Job

- **Machine Learning Algorithms**  
    Advanced threat actors try to evade defenses as much as possible, and their activities may sometimes bypass advanced detection techniques. Modern EDRs have machine learning models trained by a large dataset of normal and malicious behaviors. This can detect complex patterns of an attack.  
    **Example:** Attacks in which the individual actions are not inherently malicious, but the ML algorithm identifies the whole chain of activities as malicious. Fileless attacks and multi-staged intrusions are often detected through this.

## Response

The next step after any detection is the response. EDR offers both automated and manual responses. You can make policies to block known malicious behaviors automatically. However, manual response gives you a wide range of response capabilities. Let's discuss some of them.

- **Isolate Host**  
    During any malicious activity on an endpoint, you can isolate that endpoint from the network through EDR. This is a very effective function for containing malicious activity. Most attacks start from a single endpoint and move laterally to other endpoints to compromise the whole network. Isolating the infected endpoint on time can stop this from happening.
- **Terminate Process**  
    Not every malicious activity requires host isolation. Some hosts run the core business operations, and isolating them can cause more loss than the malicious activity. In such cases, terminating a process is enough to neutralize the malicious activity. The analysts get this option in the EDR. They can terminate any process at any time. This action should be taken consciously since terminating a legitimate process can disrupt the endpoint.
- **Quarantine**  
    If a malicious file comes into the endpoint, it can be quarantined. Quarantine ensures that the file is moved to an isolated location where it can not be executed. The analysts can then review the file to restore or permanently remove it. 
- **Remote Access**  
    Analysts can also remotely access the shell of any endpoint. This is often done when the EDR's built-in response is not enough to take action on a specific activity. Through remote access, analysts can gain deeper visibility into the system or take custom actions within the endpoints. The analysts can also run scripts or collect their desired data from the host through remote access.  
    Below is an example of CrowdStrike Falcon EDR's RTR (Real Time Response) console, which allows analysts to remotely access the shell of any endpoint and run commands and scripts.
- **Artefacts Collection**  
    Sometimes, the analysts may need to extract some data from the endpoints for detailed forensic investigation or reporting for legal actions. Analysts can extract important artefacts from the endpoints without physically accessing the device. The most commonly extracted artefacts include:
    - Memory Dump
    - Event Logs
    - Specific Folder Contents
    - Registry Hives

The Detection and Response capabilities of EDR solutions differ from those of traditional endpoint protection solutions. Modern EDRs are introducing more advanced detection techniques.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
