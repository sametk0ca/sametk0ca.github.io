
Linux has long been a leader in servers and embedded systems, and now its use is even more widespread with the growth of cloud adoption. As a SOC analyst, you are now very likely to investigate Linux alerts and incidents, either from traditional on-premises servers or from cloud-native containerized workloads. 


## Log Format

Contrary to a common belief, Linux-based systems are ==not immune to malware==. Moreover, Linux-targeted intrusions are a growing problem. Thus, as a SOC analyst, you will often need to investigate Linux alerts, and for this, you need to understand how its logging works. Now, let's clarify a couple of things and move on!


## Working With Logs

Unlike in Windows, Linux logs most events into ==plain text files==. This means you can read the logs via any text editor without the need for specialized tools like Event Viewer. On the other hand, default Linux logs are less structured as there are ==no event codes and strict log formatting rules.== Most Linux logs are located in the `/var/log` folder.

## Authentication Logs

The first and often the most useful log file you want to monitor is `/var/log/auth.log` (or `/var/log/secure` on RHEL-based systems). Although its name suggests it contains authentication events, it can also store user management events, launched sudo commands, and much more! Let's start with the log file format:

![[Pasted image 20251225142153.png]]

## Login and Logout Events

There are many ways users authenticate into a Linux machine: locally, via SSH, using "sudo" or "su" commands, or automatically to run a cron job. Each successful logon and logoff is logged, and you can see them by filtering the events containing the =="session opened" or "session closed"== keywords.

## Bash History

Another valuable log source is Bash history - a feature that records each command you run after pressing Enter. By default, commands are first stored in memory during your session, and then written to the per-user `~/.bash_history` file when you log out. You can open the `~/.bash_history` file to review commands from previous sessions or use the `history` command to view commands from both your current and past sessions:

## Runtime Monitoring

Up to this point, you have explored various Linux log sources, but none can reliably answer questions like "Which programs did Bob launch today?" or "Who deleted my home folder, and when?". That's because, by default, Linux doesn't log process creation, file changes, or network-related events, collectively known as **==runtime==** events. Interestingly, Windows faces the same limitation, which is why in the [Windows Logging for SOC](https://tryhackme.com/room/windowsloggingforsoc) room we had to use an additional tool: Sysmon. In Linux, we'll take a similar approach.

![[Pasted image 20251225144409.png]]

## System Calls

Before moving on, let's explore a core OS concept that might help you understand many other topics: system calls. In short, whenever you need to open a file, create a process, access the camera, or request any other OS service, you make a specific system call. There are [over 300](https://man7.org/linux/man-pages/man2/syscalls.2.html) system calls in Linux, like `execve` to execute a program. Below is a high-level flowchart of how it works:

![A flowchart of a Linux system call: you start a program, the "execve" system call is passed to the kernel, the kernel uses hardware resources, and returns the results.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1757002115631.svg)

Why do you need to know about system calls? Well, all modern EDRs and logging tools rely on them - they monitor the main system calls and log the details in a human-readable format. Since there is nearly no way for attackers to bypass system calls, all you have to do is choose the system calls you'd like to log and monitor. In the next task, you will try it in practice using auditd.

## Using Auditd

You can view the generated logs in real time in `/var/log/audit/audit.log`, but it is easier to use the `ausearch` command, as it formats the output for better readability and supports filtering options.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
