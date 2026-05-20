The term **kill chain** is a military concept related to the structure of an attack. It consists of target identification, decision and order to attack the target, and finally the target destruction.

### Reconnaissance

**Reconnaissance** is the research and planning phase of an attack against a system or victim. Adversaries use this phase to gather information about their target to inform their next steps. This information can include infrastructure details, employee data, business processes, and exposed technologies. Reconnaissance is often passive and undetected.

**Email harvesting** is the process of obtaining email addresses from public, paid, or free services. An attacker can use email-address harvesting for a phishing attack (a type of social-engineering attack used to steal sensitive data, including login credentials and credit card numbers). The attacker will have a big arsenal of tools available for reconnaissance purposes.

### Weaponization

Creating payload phase.

**Malware** is a program or software that is designed to damage, disrupt, or gain unauthorized access to a computer.

**Exploits** are programs or code that take advantage of the vulnerability or flaw in the application or system.

A **payload** is a malicious code that the attacker runs on the system.

### Delivery

Method for transmitting payload.

### Exploitation

Exploitation is the moment the attacker's code executes on the target, taking advantage of a known vulnerability. 

Signs of exploitation to look out for include:

- Unexpected process spawns.
- Registry changes or new services created.
- Suspicious command-line arguments found in system logs.

### Installation

As you have learned from the Weaponization phase, the backdoor lets an attacker bypass security measures and hide the access. A backdoor is also known as an access point.

Once the attacker gets access to the system, he would want to reconnect back to the system if he loses the connection to it or if he got detected and got the initial access removed. Or if the system is later patched, they will no longer have access to it. That is when the attacker needs to install a **[persistent backdoor](https://www.offensive-security.com/metasploit-unleashed/persistent-backdoors/).** A persistent backdoor will let the attacker access the system he compromised in the past.

### Command & Control (C2)

Communication between victim host and hacker.

### Action

Hacker can do whatever he wants to.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
