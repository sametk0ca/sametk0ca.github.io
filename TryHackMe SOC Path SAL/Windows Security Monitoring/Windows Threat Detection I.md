
## Initial Access

Before moving on, let's recap the concept of Initial Access. Imagine the cyber world as a big city filled with skyscrapers and tiny apartments - each one protected by its own front door. Now imagine threat actors as criminals roaming the streets at night. Some of them pick the lock of a specific office for weeks. Others smash at doors with brute force. And some just try every city door until they find one left open by mistake.

No matter what the final goal is, the first step of a threat actor is to get through the front door, and the moment an attacker successfully gets in is known as Initial Access.

## Exposed Services

![Three threat groups are trying to breach the server: the first via an exposed RDP, the second via a mail server, and the third via MS SQL](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1747842641467.svg)

Putting a Windows server directly on the Internet is a common task for IT teams - corporate websites require an open HTTP port to show content, a mail server can't handle emails without an active SMTP port, and IT admins need RDP to manage the machine remotely. However, every exposed service introduces major security risks. Within minutes, your exposed system can be scanned by automated bots looking for open ports, weak passwords, or unpatched vulnerabilities. And if something is not protected enough, threat actors will use their chance, as proven by these MITRE techniques:

- [T1133 / External Remote Services](https://attack.mitre.org/techniques/T1133/): Threat actors will look for exposed RDP/VNC/SSH with weak passwords to get remote access to the machine
- [T1190 / Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/): Threat actors will look for misconfigured or vulnerable websites and applications

## User-Driven Methods

![Threat actor delivering a phishing email and an infected USB to the victim. The victim starts the attack themselves by opening an email or USB](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1748289075632.svg)

But how can the laptop be infected if it is not Internet-exposed? Indeed, unless you help the threat actors yourself, it is very hard to infect your laptop. However, people often help threat actors by clicking on malicious links, launching phishing attachments, using pirated software, picking up unknown USB devices, and so on. And since humans are still the weakest link in cyber security and Windows is the most popular OS for user workstations, you are very likely to handle user-driven Windows Initial Access alerts frequently. The methods are covered by these MITRE techniques:

- [T1566 / Phishing](https://attack.mitre.org/techniques/T1566/): Threat actors employ different phishing techniques, tricking users into launching the malware themselves
- [T1091 / Removable Media](https://attack.mitre.org/techniques/T1091/): Threat actors infect a USB device and hope that users will use the USB on multiple PCs

## Risks of Exposed RDP

As a SOC analyst, you should know that if you expose RDP to the world and set a "12345678" password, your host will be breached within a few days. However, not everyone understands the security risks of an exposed RDP. According to [Censys Search](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.service_name%3A+RDP), there are over 5,000,000 RDP-enabled machines right now, and many of them are already under threat actors' control. The problem is so widespread that defenders often call RDP the **R**ansomware **D**eployment **P**rotocol, emphasizing how often an RDP breach directly results in a ransomware attack.


## Detecting RDP Breach

In our VM scenario, the IT admin exposed RDP on a production server so that it could be accessed from home on weekends. The credentials were set to Administrator:Summer2025. Let's reconstruct what happened next, just in a few hours, and try to detect it in logs by using Event Viewer (**C:\Users\Desktop\Administrator\Practice\RDP Case\RDP-Security.evtx** file):

|#|Step of Attack|Detection Opportunity|
|---|---|---|
|1|**Network Scan**  <br>Botnet scans our IP and detects an exposed RDP port|N/A. Network attacks are out of the room scope|
|2|**RDP Brute Force**  <br>Botnet starts a brute force of common user names  <br>(Administrator, admin, support, etc.)|1. Open Security logs and filter for the failed logins (event ID **4625**)  <br>2. Filter for logon types **3** and **10**, meaning remote logons  <br>3. Filter for logins from external IPs (use "Source IP" field)  <br>4. That's it. You have detected a potential RDP brute force|
|3|**Initial Access via RDP**  <br>After around 100 attempts, the botnet guesses  <br>the correct password and enters the system|1. Continue with the list from the previous step  <br>2. Switch the event ID filter to **4624** (successful logins)  <br>3. Check the account under which the logon was made  <br>4. Now you know which account was used for the Initial Access|
|4|**Further Malicious Actions**  <br>Two hours after the breach, the threat actor  <br>logs in via RDP and reviews the Desktop|1. Continue with the list from the previous step  <br>2. Filter for logon type **10**, indicating interactive RDP login  <br>3. Copy the "Logon ID" field from the logon event  <br>4. Open Sysmon logs and search events with the same "Logon ID"  <br>5. You will see all processes started by the threat actor via RDP|

---
## Current State of Phishing

Phishing attacks are still a major threat as they can't be mitigated as easily as blocking RDP access. If users have access to the Internet, they will eventually bring malware to their laptops, bypassing the firewall entirely. According to the [HoxHunt Phishing Trends Report for 2025](https://hoxhunt.com/guide/phishing-trends-report), phishing attacks have increased 41 times since the release of ChatGPT in 2022. Even more, the success rate of these campaigns remains high, meaning users are still falling for them. In this task, we'll focus on two phishing techniques that lead to Windows breaches: malicious binaries and LNK attachments.


## Binary Attachments

In Windows, there are [lots](https://github.com/michalzobec/Security-Blocked-File-Extensions-Attachments/blob/main/list-of-blocked-file-extensions.txt) of executable extensions, and while most people know not to open untrusted **.exe** files, they are usually less cautious about **.com**, **.scr**, or **.cpl** files. However, all of them can contain the malware inside. For example, users are very likely to open the attached "tryhatme.com" file name assuming it to be a link to a meeting invite, not a malicious binary.

To make it worse, Windows hides known file extensions by default, meaning that the file "program.exe" will be shown to you just as "program". Threat actors [often abuse it](https://attack.mitre.org/techniques/T1036/007/) by naming their viruses like "invoice.pdf.exe" or "cat.png.com" and changing the icons to fit the topic.

## LNK Attachments

To avoid AV detection, threat actors may prefer attaching PowerShell, Visual Basic, or BAT scripts over binaries. A popular way to make the scripts look trustworthy is to hide them behind LNK shortcuts - the same files you have on your Desktop that point to real executables somewhere in the Program Files folder.


---


## Risks of Removable Media

Although some may believe that days of infected USB flash drives are long gone and cloud services have replaced them completely, threat actors will disagree, as proven by [Camaro Dragon](https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/) or [Raspberry Robin](https://redcanary.com/blog/threat-intelligence/raspberry-robin/) attacks. Moreover, Initial Access via an infected USB bypasses firewalls, much like phishing, and can start the attack chain even without Internet access and continue spreading without user interaction.

**USB Delivery Case**

Imagine working for TryHatMe Inc. and receiving a delivery package with a fancy hat and a USB labelled as "A gift from HR". You plug it in, a harmless GIF pops up, and you call HR to thank them for the present. But while the HR figures out what you meant, the malware from the USB has already spread to your laptop. ([Real-World Case](https://hackread.com/fbi-hackers-mail-malicious-usb-drives-ransomware/))

**Print Service Case**

Another common scenario involves third-party entities like a print service. Suppose you visit one and hand over your USB to print a document. Their system, already infected with a worm, passes the malware onto your flash drive. Then, you bring the malware back to your home PC, and the infection chain continues. Now, let's learn how to detect this before it's too late! ([Real-World Story](https://www.malwarebytes.com/blog/news/2025/05/malware-infected-printer-delivered-something-extra-to-windows-users))

## Detecting an Infected USB

Although there are many advanced techniques on how to run the malware from USB automatically as soon as the flash drive is plugged in, the majority of cases occur just because the user launches malware themselves. For example:

- Malware hides all legitimate files on USB and creates a malicious "**RECOVERY.lnk**" file
- Malware creates a "**Photos.exe**" binary and sets its icon to look like a simple folder
- Malware creates double-extension copies of all files, like "**photo_2024_1_12.jpg.exe**"

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
