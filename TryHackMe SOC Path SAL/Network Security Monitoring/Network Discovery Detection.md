
## Attackers and Network Discovery

As discussed in the previous task, attackers start their attack by trying to discover an organisation's assets that are open to the publicly accessible internet (called the ==attack surface==). During this discovery phase, the attacker attempts to ascertain some of the following information:

- What assets can be accessed by the attacker? 
- What are the IP addresses, ports, OS, and services running on these assets?
- What versions of services are running? Does any service have a vulnerability that can be exploited?

In short, the attacker is trying to find an opening that will allow them to exploit the network.

## Defenders and Network Discovery

On the other hand, defenders also sometimes run software that performs network discovery activity. During this activity, defenders want to achieve the following goals:

- Inventory the organisation's assets and ensure all assets are documented.
- Ensure no unnecessary IP, port, or service is open, and whatever is running is necessary.
- Ensure vulnerabilities are patched, or at least the exploitable vulnerabilities are patched.

In short, defenders attempt to reduce the attack surface as much as possible.


Eğer scanning olayı dış IP'den geliyorsa (private network içerisinde olmayan IP ) saldırı henüz ==Recon== aşamasındadır.

Eğer içeriden geliyorsa (10.x.x.x gibi private IP'ler) o zaman çoktan ağa sızılmış ve ==Discovery== aşamasındadır.


## Horizontal Scanning

Sometimes, an attacker will scan for the same port across ==multiple destination IP addresses.== This type of scan is called a horizontal scan. Horizontal scans are performed to identify which hosts expose a particular port. An attacker might perform this scan if they intend to exploit that specific port. An example can be the WannaCry ransomware, which spread through the network using an SMBv1 vulnerability and scanned for machines with port 445 (which is used for SMB) open.

## Vertical Scanning

Vertical scanning occurs when a single host IP address is scanned across multiple ports. Attackers perform vertical scanning to footprint a host and identify its exposed services. This activity might be performed when an attacker is focused on identifying a vulnerability on a single machine because they consider it a valuable target based on their objectives. For example, if an organisation exposes only a single server to the internet, any attacker who wants to breach that organisation would first perform a vertical scan on that server to identify open ports and understand the services running on the machine.


