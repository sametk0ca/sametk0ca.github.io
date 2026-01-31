## What is a Web Shell?

To effectively detect web shells, it is important to understand what they are, how attackers deploy them, and the vulnerabilities that they exploit.

A web shell is a malicious program uploaded to a target web server, enabling adversaries to execute commands remotely. Web shells often serve as both an [initial access](https://attack.mitre.org/techniques/T1190/) method (via file upload vulnerabilities) and a [persistence](https://attack.mitre.org/techniques/T1505/003/) mechanism.

Once access has been gained on a compromised server, attackers can use a web shell to move through the kill chain, performing [reconnaissance](https://attack.mitre.org/tactics/TA0043/), [escalating privileges](https://attack.mitre.org/tactics/TA0004/), [moving laterally](https://attack.mitre.org/tactics/TA0008/), and [exfiltrating data](https://attack.mitre.org/tactics/TA0010/).

## Web Shell Deployment

For an attacker to upload and execute a web shell, a file upload vulnerability, misconfiguration, or prior access to the system is required. These vulnerabilities arise when an application fails to validate file type, extension, content, or destination. While web shells are used as an initial access vector, they can also serve as a persistence mechanism if the attacker has already compromised the system and wants to maintain long-term access.

Imagine a simple website that allows you to upload your pet photos. The website is intended for storing images. However, if developed insecurely, an attacker may upload a web shell like `shell.php` or `mydog.aspx` and gain command execution on the server.


## Auditd

A native Linux utility that tracks and records events, creating an audit trail. Rules can be created for `auditd`, which determine what is logged in the `audit.log`. Rules can be highly configured to match specific conditions, such as when certain programs are run or files are modified in a particular directory. In the example below, `ausearch` is used to search for any logs matching the `web_shell` rule.

   `user@tryhackme$ ausearch -k web_shell time->Wed Jul 23 06:20:36 2025  // A log matching the web_shell rule 
   `"name = /uploads/webshell.php"` 
   `"OGID = www-data"

## Web Server Logs

Web shells rely on the abuse of web servers, so web server logs are a natural place to start our hunt for evidence. We will explore what to look for in popular web servers like Apache & Nginx. Understanding the difference between normal and suspicious behavior can help uncover malicious activity.

While the format of web server logs varies depending on the service, **access logs** generally follow a similar structure and include the following information.

The remote log name field is typically represented by a hyphen (-), as it is a legacy field that is rarely used today. However, it still appears in access logs for compatibility. Similarly, the authenticated user field is usually shown as a hyphen as well, unless the server required prior authentication, in which case it may contain the actual username.

![[Pasted image 20251218141059.png]]

## File System Analysis

An attacker's web shell must be stored somewhere. Analyzing web server files is crucial in identifying uploaded web shells or locating files modified to include a web shell payload.  
It should be noted that some platforms like WordPress and Django store page content in a database rather than a file system, so malicious code may be injected into posts, themes, or settings and won't appear in normal file system searches.

## Network Traffic Analysis

Network traffic analysis allows analysts to go beyond logs by examining the data exchanged between a client and a server. By inspecting packet payloads, it becomes possible to observe attacker behavior on a more detailed level.

Many of the indicators that analysts need to be on the lookout for in log analysis can be applied to network traffic analysis as well.

- Unusual HTTP Methods & Request Patterns
- Suspicious User-Agents & IP Addresses
- Encoded Payloads
- Malicious Code or Commands in Request Bodies
- Unexpected Protocols or Ports
- Unexpected Resource Usage
- Web Server Processes Spawning Command Line Tools