## Anatomy of a Log Entry

Windows is an interesting OS as it has very powerful logging capabilities but requires a lot of knowledge to read and understand the logs. Your first challenge may be to just open the logs, as they are stored in a binary format inside the `C:\Windows\System32\winevt\Logs` folder:

Every EVTX file corresponds to a specific log category. For example, Application Logs contain events logged by user-mode applications like the IIS web server or MS SQL database, and Security Logs capture events like logon attempts, process activity, and user management.


# EventViewer


1. **Log Sources**: Every EVTX file corresponds to a single item on the left panel
2. **Log List**: Each row you see is a single event that contains a few properties you can sort by:
    - **Keywords**: For some events, indicates if the action was successful or not
    - **Date and Time**: The timestamp when the event occurred (system time, not UTC!)
    - **Event ID**: A unique number for the event name (e.g. a failed login is always 4625)
3. **Log Details**: The actual content of the log, in a plaintext or XML format ("Details" tab)
4. **Filters Menu**: Use the "Filter Current Log" and "Find" buttons to filter the logs

![[Pasted image 20251220154336.png]]

# Authentication

Event ID 4624 == Successful Logon (RDP)
Event ID 4625 == Failed Logon (Brute-force or Password spray)

# User Management

|**Event ID**|**Description**|**Malicious Usage**|
|---|---|---|
|**4720** / **4722** / **4738**|A user account was  <br>created / enabled / changed|Attackers might create a backdoor account or even enable an old one to avoid detection|
|**4725** / **4726**|A user account was  <br>disabled / deleted|In some advanced cases, threat actors may disable privileged SOC accounts to slow down their actions|
|**4723** / **4724**|A user changed their password /  <br>User's password was reset|Given enough permissions, threat actors might reset the password and then access the required user|
|**4732** / **4733**|A user was added to /  <br>removed from a security group|Attackers often add their backdoor accounts to privileged groups like "[Administrators](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#administrators)"|
# Process Monitoring

==**Event ID 4688**==  
**Sysmon ==Event ID 1==
(Security Log: Process Creation)


# Files and Network

|**Event ID**|**Security Log Alternative**|**Event Purpose**|
|---|---|---|
|**11 / 13  <br>**(File Create / Registry Value Set)|**4656** for file changes and **4657** for registry changes, both disabled by default|Detect files dropped by malware or its changes to the registry (e.g. for persistence)|
|**3 / 22  <br>**(Network Connection / DNS Query)|No direct alternative, requires additional firewall and DNS configuration|Detect traffic from untrusted processes or to known malicious destinations|

# Powershell Logging Commands

PowerShell is a powerful tool built into Windows that attackers love to abuse. Mainly because it is both trusted and capable of malware download, system discovery, data exfiltration, and even advanced techniques like process injection. However, you won't capture its commands by just using process creation logs like the Sysmon event ID 1.

## How It Works

Every program has a specific purpose: **firefox.exe** is a web browser, **notepad.exe** is a text editor, and **whoami.exe** simply outputs your username. If you're just browsing the web, you might only create a single Firefox process. However, with every out-of-scope task like RDP access or photo editing, you will have to open new programs and create additional logs.

PowerShell, on the other hand, is a powerful all-in-one tool for managing the system. Once you launch `powershell.exe`, you can run hundreds of different commands within the same terminal session without creating new processes for each action. This is why Sysmon is not very helpful here, and you'll need to find an alternative logging approach.

## PowerShell History File

There are at least five methods to monitor PowerShell, each with its own pros and cons. While you can check out the [Logless Hunt](https://tryhackme.com/room/loglesshunt) room and research AMSI and Transcript Logging topics, in this room, we will focus on a simple but effective way to track PowerShell commands - ==the PowerShell history file:==

