
SIEM solutions play a vital role in every Security Operations Centre, and any SOC analyst's day-to-day life.  
Let’s take a moment to understand why SIEM is so valuable and explore its key benefits for analysis.

## Centralisation

One of the first things that makes SIEM so helpful for a SOC is **centralisation**. Instead of checking logs in different places, like network devices, cloud services, identity providers, and more, a SIEM allows you to gather all that data in one place. This means an analyst doesn’t have to switch between systems during an investigation. Everything is available in a single solution, making their work much smoother and more efficient.


## Correlation

Another core strength of SIEM is **correlation**, the ability to link separate events and piece them together like pieces of a puzzle to form a complete picture. Let’s walk through a scenario.  
You receive an alert in your SIEM about internal network discovery activity. The only information you have is the IP address of the host performing the scan. Nothing else. The alert comes from your IDS logs.

That’s not much to go on, is it? To make sense of it, you need to enrich the data, find out which device the IP belongs to, and who triggered the activity.

## Historical Events

SIEM also allows you to look at past events, not just current activity. This helps you spot patterns or threats that may have started earlier but weren’t noticed at the time.

For instance, if you get an alert about an unusual login location for a user, you can look back at historical logs to see if he has logged in from that location or IP before. This helps you identify patterns in their behaviour and assess whether the activity is part of a malicious attempt or a legitimate action.  


## Host-Based Log Sources

Host-based log sources come from individual devices within the organisation, such as workstations and servers. Every organisation relies on workstations for employees to perform their duties and servers serving different purposes, such as web servers, SQL servers, DNS servers, and more. Typically, we monitor this type of behaviour from systems.

## Network-Based Log Sources

Network-based log sources collect data from network devices, such as firewalls, routers, IDS and IPS, and other systems. These devices play a critical role in monitoring traffic and connections across the network.

## Web-Based Log Sources

And of course, almost every organisation has its own web application, and logs from it are also sent to the SIEM.  
It’s through web vulnerabilities that attackers often gain access to an organisation’s environment, so careful monitoring of web events is an essential part of every analyst's role in a SOC environment, day by day.

**Time Pitfalls**

One common challenge analysts face when working in a SIEM is time, specifically how time is recorded across different log sources.  
Logs can come from systems in different time zones. Some сan be in UTC, others in local time, and some may not include a timezone at all.

It’s important to understand that your local time can be different from the time set in the SIEM.

Let’s say you’re working in UTC-2, but the logs in Splunk SIEM are normalised to UTC+2.  
If it’s 5 PM for you, those same logs might appear as 1 PM in Splunk.  
That doesn’t mean the logs are ingested four hours late; it’s just a difference in time settings.

So always be aware of which time zones you’re dealing with when analysing events. It can make all the difference in understanding what really happened, and when.

  
**Logs Normalisation**

Different logs come in various formats. Some are in JSON, others in XML, or even plain text. Each system logs events in its own way, using different field names and structures.

That’s where normalisation comes in.

The idea is to convert all these formats into a single, consistent structure, so that logs are easier to work with.  
Analysts can simply view everything in one standard way inside the SIEM. This makes searching, filtering, and linking events much easier. Without normalisation, every log source would feel like solving an entirely different puzzle.


# Windows Logs

When using a SIEM to analyse Windows logs, we usually talk about two main data sources: WinEventLogs and Sysmon. The second one must be installed and configured separately to start receiving logs.

However, combining these two data sources actually provides clear visibility for analysing activity.

![Sysmon vs WinEventLogs](https://tryhackme-images.s3.amazonaws.com/user-uploads/674d9727a22822c1eb46cb31/room-content/674d9727a22822c1eb46cb31-1754989770283.png)


## Sysmon


An additional, and in some cases, even primary log source on Windows is Sysmon. It’s an incredibly powerful place that logs a wide range of activity types, providing a high level of visibility during analysis. Using Sysmon logs, an analyst can observe a variety of activity types that provide deep visibility into system behaviour.  
It helps identify malicious process execution, network connections, possible process injection, registry changes, and file creation, among other activities.

## WinEventLogs

Windows Event Logs include a huge number of unique log files. While you're probably most familiar with the Security, System, and Application logs, in reality, the system contains over 200 different log channels beyond just those three.   
  
**Windows Security Logs**

The most commonly viewed and referenced logs are the Security logs, but why is that the case? Let’s break down why these logs are so important and what makes them essential for investigation. Analysts can detect in Security logs activities such as user authentication attempts, account creation or modification, access to files and registry keys, process execution, system restarts or log clearing, and changes to audit or security policies.

**Windows System Logs**

These logs record events generated by the operating system and its core services. They help detect various events related to services, system-level activity, and potential errors.  
These logs are an excellent place to look for potential persistence or privilege escalation attempts via services. 


# Linux Logs

When you're analysing Linux systems in a SIEM, you'll often start by looking at two key log sources.

First, you’ll see **auth.log**, which tracks authentication-related activity, such as user logins and sudo usage, among other things. These logs are crucial for spotting failed logins, unauthorised access attempts, or privilege escalation.

Next, you'll come across **syslog**, which captures general system-level events. Here, you can monitor service restarts, cron jobs, and background processes - all helpful when building timelines or understanding how the system behaves over time. These tools significantly improve visibility.

## Authentication Logs

Authentication logs are one of the most important sources when analysing Linux systems in a SIEM.  
They help you understand how users interact with the system, especially regarding login attempts and privilege usage.

## System Logs

System logs are another essential source of visibility. They capture events related to service activity, system restarts, and crons, all useful for identifying unusual system behaviour often linked to persistence or privilege escalation attempts.

# Web Application Logs

## Web Log Sources

Almost every organisation has its own website and therefore a web server running it. Logs from these web servers are collected from Apache, Nginx, and other resources.  
The most useful for analysis are the **access logs**, where you can detect requests to website resources. These logs often contain signs of malicious activity, such as scanning, DDoS attempts, various web-based attacks, and web shells. In addition, error logs can provide valuable insight, helping you understand possible failures or issues.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
