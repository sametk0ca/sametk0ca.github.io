
# Client Side Attacks

**Client-side** attacks rely on abusing weaknesses in user behavior or on the user's device. These attacks often exploit vulnerabilities in browsers or trick the user into performing unsafe actions to gain access to accounts and steal sensitive information. Valuable data can be stored on a user's device, so a successful client-side attack can result in data loss. With the demand for dynamic and versatile web applications rising, companies are integrating more third-party plugins, broadening the attack surface in browsers, and opening more opportunities for client-side attacks.

## SOC Limitations

The tools available to an analyst, such as server-side logs and network traffic captures, offer little to no visibility into what occurs inside a user's browser. As discussed above, client-side attacks occur on the user's system, meaning they can execute malicious code, steal information, or manipulate the environment without generating suspicious HTTP requests or network traffic that the SOC can see. As a result, detecting these attacks from a SOC perspective is often difficult or even impossible without additional browser-side security controls or endpoint monitoring.

![[Pasted image 20251218125839.png]]

# Server Side Attacks

**Server-side** attacks rely on exploiting vulnerabilities within a web server, the application's code, or the backend that supports a website or a web application. While client-side attacks manipulate users' interaction with a site, server-side attacks focus on taking advantage of the systems themselves. By exploiting flaws and vulnerabilities, server logic, misconfigurations, or input handling, attackers can gain access, steal information, and cause damage to running services.

## Catching Server-Side Attacks

One advantage for defenders when dealing with server-side attacks is that they leave a trail of evidence, if you know where to look. Every web request sent to an application is processed by the server and is recorded in logs or other monitoring systems. These requests also travel across the network, meaning network traffic can reveal suspicious behavior. In the upcoming tasks, we will identify server-side attacks in both logs and network traffic.

![An attacker sending a suspicious request to a web server. The request leaves behind a trail of evidence in the form of network traffic and a log file.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1756209970986.svg)


**Challenge-Response Mechanisms**

WAFs don't always need to block suspicious requests outright. For example, they can challenge requests with CAPTCHA to verify whether they come from a real user rather than a bot. This capability is extremely valuable considering that malicious bot traffic [makes up 37%](https://www.thalesgroup.com/en/worldwide/defence-and-security/press_release/artificial-intelligence-fuels-rise-hard-detect-bots) of global web traffic. This approach is beneficial for firewall rules with a higher chance of blocking legitimate web traffic.

![[Pasted image 20251218134317.png]]

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
