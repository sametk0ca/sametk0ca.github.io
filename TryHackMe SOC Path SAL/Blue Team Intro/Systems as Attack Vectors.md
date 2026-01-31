Imagine a castle again, but now with a trained gatekeeper who knows how to identify phishing and how to combat deepfakes. However, if the lock on the main gate is fragile and cheap, guardian skills do not matter, as the enemy can just sneak into the castle while no one is watching. In cyber terms, threat actors can attack insecure systems directly, without the users' knowledge.![[678ecc92c80aa206339f0f23-1752596680315.svg]]

## Definition of System

Where do the banks store your cards, or where are your emails stored? The answer - on a system: a physical server, a virtual machine, or a cloud platform like Microsoft 365. Protecting such systems is crucial: if the attackers breach one user's mailbox via phishing, they compromise a single mailbox, but if they breach a mail server, they now control all thousands of mailboxes.

## Supply Chain

Your PC is home to hundreds of apps, including web browsers, messengers, development, and entertainment software. Every app depends on thousands of libraries. If threat actors manage to breach one of the apps or libraries and push an update to all its users, all of them will be compromised. This technique is called a supply chain attack. The most famous examples are the [SolarWinds](https://attack.mitre.org/campaigns/C0024/#:~:text=Victims%20of%20this%20campaign%20included%20government) and [3CX](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise) breaches which affected thousands of companies.

**Emerging Threat of Supply Chain**

It is hard to protect from supply chain attacks since you can't always control all the software present on your laptops, servers, and web apps. Even TryHackMe once [fell victim](https://tryhackme.com/room/supplychainattacks) to a supply chain in Lottie Player, a library used for room animations. As a SOC analyst, you must be ready for such scenarios and know how to respond!

## Software Vulnerabilities

Every piece of software has flaws, but some take years to be discovered. For example, [Shellshock](https://www.invicti.com/blog/web-security/cve-2014-6271-shellshock-bash-vulnerability-scan/), a major Linux vulnerability, existed since 1992 but wasn't found until 2014. In the worst-case scenario, attackers discover the vulnerability before anyone else. This is known as a [zero-day](https://en.wikipedia.org/wiki/Zero-day_vulnerability), and only your SOC skills can determine whether it gets detected in time.

Once a vulnerability is made public, it is assigned a Common Vulnerabilities and Exposures ([CVE](https://www.cvedetails.com/cisa-known-exploited-vulnerabilities/kev-1.html)) number. From that moment, it's a race: attackers develop exploits while defenders rush to update their systems.



## Misconfigurations

On the other hand, a misconfiguration isn't a bug in the software but a mistake in how the system was set up, often by the IT team. These errors happen frequently, usually to make things simpler, like using "1111" instead of typing a long password every time. Let's take a look at some real-world examples.

- How ["123456" password](https://www.bleepingcomputer.com/news/security/123456-password-exposed-chats-for-64-million-mcdonalds-job-chatbot-applications/) exposed chats for 64 million McDonald's job applications
- How a [misconfigured AWS cloud](https://www.bleepingcomputer.com/news/security/capital-one-data-breach-affects-106-million-people-suspect-arrested/#:~:text=intrusion%20occurred%20through%20a%20misconfigured%20web%20application%20firewall) resulted in a breach of 106 million bank customers
- How improperly configured [smart fridges](https://www.sectigo.com/resource-library/when-refrigerators-attack-how-cyber-criminals-infect-appliances-and-how-manufacturers-can-stop-them) are silently used in full-scale botnet attacks

Another common scenario is when the IT department unknowingly introduces new flaws into secure systems. Below is a simple example of how a critical database can be breached because of the insecure configuration:

![[678ecc92c80aa206339f0f23-1754915771066.svg]]