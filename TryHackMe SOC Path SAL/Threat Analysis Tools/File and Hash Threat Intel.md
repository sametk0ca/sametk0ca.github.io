
Security Operations teams live inside alert queues and triaging. Every entry follows three essential steps: **verify**, **enrich**, and **decide**. File and hash intelligence sits squarely in the _enrich_ phase, transforming a lone path or hash value into contextual knowledge within your organisation about malicious artefacts that would be identified.

## Filepath Analysis

File paths and names are like crime scene clues, revealing attacker behaviour. Attackers may use different disk locations to hide their actions and reduce visibility. For example:

- `C:\` (System drive) can be a common target for persistence mechanisms.
- `C:\Users\Public` profile can enable cross-user access of detonated adversary tools.
- `C:\Users\Public\Public Downloads` provides a high-traffic directory that would often evade strict monitoring.

Additionally, adversaries may utilise other malware staging patterns such as:

- Utilising temporary directories such as `C:\Windows\Temp\` for ephemeral payloads.
- Placing payloads in writable system paths, such as `C:\ProgramData\` for stealth persistence.

## Filename Heuristic Indicators

Attackers are also known to modify filenames to escape detection through implementing various types of heuristic indicators, including:

- Double extensions - An example of this would be `invoice.pdf.exe`, which leverages default Windows settings that hide file extensions.
    
- System binary impersonation - A filename such as `scvhost.exe` abuses the user's familiarity with core system processes. Defenders should include legitimate locations for system processes in an allowlist, rather than standalone filenames.
    
- High-entropy Strings – A filename such as `jh8F21.exe` suggests automated packing or polymorphic generation, which is commonly used in a high-churn phishing operation.
    
- Masquerading - Filenames such as `backup-2300.exe` can blend with routine files, thus leveraging on reduced suspicion. Another example is a single character substitution, which can bypass detection while looking visually legitimate to an unsuspecting employee.
    

SOC analysts should become aware of these heuristic techniques and always flag and investigate alerts with these characteristics.

We've identified suspicious heuristics from the sample files through path and name analysis. The analysis is not conclusive, as attackers constantly rename files. We can tie the names back to the same binary through cryptographic fingerprinting through its file hash, especially SHA256 and MD5 hashes. File hashes uniquely identify files and malware, regardless of name changes. Attackers constantly rename their malware; hashes always provide an immutable and actionable way to identify it.

It is advisable to work with potentially malicious binaries in a separate, isolated environment.

We can generate and verify our file hash using the following commands:

Windows Commands

      `Command prompt: certutil -hashfile bl0gger.exe SHA256      PowerShell: Get-Filehash -Algorithm SHA256 bl0gger.exe`
    

Linux Commands

      `ubuntu@tryhackme$ sha256sum bl0gger.exe`


## Dynamic Analysis for SOC

Static properties such as hashes, strings, and sections tell you identity. To understand the impact of malicious files, you need to execute them safely in a controlled environment. Sandboxes provide a disposable VM instrumented to capture every process, registry write, and network packet associated with the malware being investigated.

Security analysts will use sandboxes to do three things:

- Confirm execution - if nothing happens, your alert might be a decoy.
- Extract runtime IOCs - domains, mutexes, dropped payloads, feed hunts and detections.
- Map to ATT&CK - most sandboxes auto‑label behaviour with technique IDs, fast‑tracking your report.

As an L1 analyst, you would use the sandboxes' lookup features to quickly identify information about an obtained hash, while senior analysts would perform the other sophisticated tasks.

## Sandboxing Tools

The most widely used tools for detonating wild malware are **Hybrid Analysis** and **Joe Sandbox**, each with its distinct application:

- Hybrid Analysis (HA) focuses on behaviour trees and a clean MITRE ATT&CK heatmap. It is suitable for a fast executive summary.
- Joe Sandbox (JS): goes deep, covering system calls, strings, and memory dumps. Great for reverse engineers and detection engineers.

## Sandboxing Limitations

While sandboxing is a powerful tool for malware analysis, it has critical limitations that SOC analysts must account for when performing threat intelligence. Blindly trusting sandbox results can lead to false negatives, missed detections, or incorrect conclusions.

These limitations include, but are not limited to, the following:

1. **Sandbox Evasion Techniques**
    
    Threat actors would design their payloads to detect and evade sandboxes, leading to false negatives. Some of the common evasion tactics used include:
    
    - Environment Awareness Checks: Malware checks for signs of virtualised/sandboxed environments
    - Anti-Debugging & Anti-Sandboxing Tricks: Malware conducts debugger detection and checks for unique hardware IDs.
2. **Limited Execution Time & Coverage**
    
    Most sandboxes terminate analysis after 2-5 minutes, which means multi-stage malware may not fully execute. Additionally, time-delayed attacks will evade detection. As previously covered, this would mean cross-referencing other threat intelligence resources.
    
3. **Encrypted & Obfuscated Traffic**
    
    Many sandboxes cannot decrypt SSL/TLS traffic, leading to blind spots. This may result in HTTPS C2 Traffic appearing with no payload visibility or the malware utilising DNS tunnelling to hide data in DNS queries
    
4. **Fileless & Living-off-the-Land (LotL) Malware**
    
    Some threats never touch disk, bypassing traditional sandbox analysis by employing PowerShell Attacks and WMI Persistence.