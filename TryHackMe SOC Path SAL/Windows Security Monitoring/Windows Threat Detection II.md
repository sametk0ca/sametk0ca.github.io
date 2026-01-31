After breaching a host, threat actors are faced with a choice: quietly establish a backdoor to maintain long-term access or take immediate action to achieve their objectives. This room covers the second approach and continues your Windows threat detection journey by exploring what typically follows the Initial Access, beginning with Discovery and Collection.

![[Pasted image 20251222150243.png]]

## Discovery Commands

The first questions you may have once you wake up from a dream might be "Who am I?" and "Where am I?". The same is true for threat actors that might have sent thousands of phishing attachments to all emails they knew but managed to breach only a couple of systems they saw for the first time. So, they need to find out the victim's details:

|Discovery Purpose|Common CMD / PowerShell Commands|
|---|---|
|**Files and Folders**  <br>(To find out the host purpose, victim's job, or their interests)|`type <file>`, `Get-Content <file>`, `dir <folder>`, `Get-ChildItem <folder>`|
|**Users and Groups**  <br>(To find out who uses the host and with which privileges)|`whoami`, `net user`, `net localgroup`, `query user`, `Get-LocalUser`|
|**System and Apps**  <br>(To find out vulnerabilities or apps to steal data from)|`tasklist /v`, `systeminfo`, `wmic product get name,version`, `Get-Service`|
|**Network Settings**  <br>(To find out if the host belongs to a corporate network)|`ipconfig /all`, `netstat -ano`, `netsh advfirewall show allprofiles`|
|**Active Antivirus**  <br>(To find out how risky it is to continue the attack without being blocked)|`Get-WmiObject -Namespace "root\SecurityCenter2" -Query "SELECT * FROM AntivirusProduct"`|
## Discovery via CMD

Discovery via the command line is the most common and easiest method available for threat actors. This is because it simply uses the existing commands like "whoami" or "ipconfig" that are available on all Windows machines by default; check out [this article](https://thedfirreport.com/2024/08/26/blacksuit-ransomware/#collection:~:text=The%20threat%20actor%20performed%20several%20discovery%20commands) for a real-world attack example. Luckily for the defenders, most of the launched commands are logged as new processes.


## Discovery via GUI

In cases where threat actors log in to the system interactively, like after the RDP breach, they are not limited to console commands (but they often use them anyway as a habit). With access to the graphical interface, nothing prevents attackers from using the same toolkit as you do: Apps & Programs, System Settings, Disk Management, or even Event Viewer. 


## Detecting Discovery

The first task to detect a potential Discovery is to find a Discovery command, or better, a sequence of commands run during a short period of time. You will see them as process creation events tracked by Sysmon event ID 1 or as new rows in the PowerShell history file. There are [lots](https://cheatsheet.haax.fr/windows-systems/local-and-physical/local_recon_enumeration/) of Discovery commands, so be prepared to use the search engine if you are not sure what the command means.

Next, it is important to find out where the commands are coming from. Commands like "ipconfig" are often used by IT departments and legitimate tools, and you don't want to create panic just because your coworker checked their IP.

## Collection Targets

The targets drastically differ depending on the attackers' goals. Some adversaries hunt personal info like images or chat conversations; others look for crypto wallets, gaming, or banking accounts; and advanced groups just use the victim to access the corporate network, hoping for a full-scale ransomware encryption.

Note that while most of the sensitive data is stored as simple files, the secrets can also be hidden in the registry or in process memory. You can review the common Collection targets in the code block below:

```shell
# [Goal: Blackmail Victim] Photos, Chats, Browser History
C:\Users\<user>\AppData\Roaming\Signal\*
C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\History

# [Goal: Steal Money] Web Banking Sessions, Crypto Wallets
C:\Users\<user>\AppData\Roaming\Bitcoin\wallet.dat
C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Cookies

# [Goal: Steal Corporate Data] SSH Credentials, Databases
C:\Users\<user>\.ssh\*
C:\Program Files\Microsoft SQL Server\...\DATA\*


```


## Detecting Collection

Same as with Discovery, threat actors can use both command-line and graphical interface options to review sensitive files. However, in Collection, threat actors don't just check a system configuration but rather look for specific files and folders shown in the previous task. Thus, you can detect access to the files by tracking commands like:

|Command Example|Description|
|---|---|
|`notepad.exe C:\Users\<user>\Desktop\finances-2025.csv`|Threat actors used Notepad to check content of the interesting file|
|CMD: `type debug-logs.txt \| findstr password > C:\Temp\passwords.txt`|Threat actors searched for the "password" keyword in a specific file|
|PowerShell: `Get-ChildItem C:\Users\<user> -Recurse -Filter *.pdf`|Threat actors searched for PDF files in the user's home folder|
|PowerShell: `copy C:\Users\<user>\AppData\Roaming\Signal С:\Temp\`|Threat actors copied Signal chat history to the Temp directory|
|PowerShell: `Compress-Archive С:\Temp\ С:\Temp\stolen_data.zip`|Threat actors archived the stolen data, preparing for exfiltration|
|`7za.exe a -tzip C:\Temp\stolen_data.zip С:\\Temp\\*.*`|Alternatively, threat actors can use the existing archiving software like 7-Zip|

## Ingress Tool Transfer

Recall the previous room explaining how attacks start: not from a fully functional malware, but from a tiny phishing attachment or from an RDP session without any red team tools. Thus, at some attack stages, threat actors may need to download more tools to achieve their goals, for example:

- A script to automate Discovery and find common vulnerabilities like [Seatbelt](https://github.com/GhostPack/Seatbelt)
- A tool to extract saved passwords or OS credentials like [Mimikatz](https://github.com/gentilkiwi/mimikatz)
- A fully functional Remote Access Trojan (RAT) like [Remcos RAT](https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/remcos-malware/)
- Finally, a ransomware binary to encrypt the system after the data is stolen

The process of downloading additional malware to the breached system is mapped to the MITRE [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/) technique, and it is used in the majority of breaches. You have already seen an example where a LNK attachment used PowerShell to download additional malware, but there are many other ways to transfer malware even without PowerShell!

## Common Transfer Methods

Why can't the threat actors just include all they need into a single phishing attachment, you may ask. There can be different reasons, but the common ones are to bypass antivirus by splitting the malware into multiple parts and to minimize exposure of their tools/exploits in case they're caught right in the beginning.

## Detecting Tool Transfer

Since a transfer requires a network connection, your best option would be to track a network connection or a DNS request from the suspicious process. Note, however, that threat actors often try to avoid detection by downloading the tools from legitimate services like GitHub, so make sure to analyze which process is making the connection, the destination domain, and the file being downloaded. 