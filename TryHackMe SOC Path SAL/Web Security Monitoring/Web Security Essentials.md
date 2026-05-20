
The shift from desktop to web-based applications has been ongoing for decades. In the 1990s, desktop applications were the norm because of speed and connectivity limitations. As web technology advanced, the 2000s gave way to much more widely used dynamic web applications for email, social media, and banking. In the 2010s, there was a [massive rise](https://www.techrepublic.com/article/the-most-important-cloud-advances-of-the-decade/) in cloud computing and software as a service (SaaS), and today, nearly everything can be done in a browser.

![A graphic showing the shift from desktop applications to web applications. The left side shows an old desktop where users would access their favorite apps. On the right is a modern, sleek web application emphasizing ease of use and availability.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1755698728579.svg)

The shift to web apps brings some amazing advantages, including increased accessibility, faster updates, better compatibility, and reduced resource usage on the user's end. Think of it, you can browse online marketplaces and social networks, play games, edit images and video, and even run virtual machines all through your browser. However, these benefits come with tradeoffs in terms of security. The more powerful and widespread the web becomes, the more opportunities it introduces for attackers.

Web applications are among the most common entry points for attackers because they are always available and exposed. They often connect to back-end systems like databases and other infrastructure, offering attackers high-impact opportunities. A vulnerable web application is often the first stage in a larger attack sequence.


## Components of a Web Service

For example, any web service, like [tryhackme.com](https://tryhackme.com/), requires three main components to function.

- **Application**: The code, images, styles, and icons that dictate how the website looks and functions.
- **Web Server**: This component hosts the application. It listens for requests and returns a response to the user.
- **Host Machine**: The underlying operating system, Linux or Windows, that runs the web server and the application.

![[Pasted image 20251218114830.png]]


## ==Best Practices==

Various security measures are available when securing websites and web applications. Some solutions provide visibility, while others can actively stop or limit an attack, commonly known as mitigation. Referencing Task 3, where we discussed the three essential components of any web service: the **application**, the **web server**, and the **host machine**, let's now examine the protections available for each of these components.

**Protecting the Application**

- Secure Coding: Avoid insecure functions, ensure proper handling of errors, and remove sensitive information.
- Input Validation & Sanitization: Validate and sanitize user input to prevent injection attacks.
- Access Control: Restrict access based on user roles.

**Protecting the Web Server**

- Logging: Keep a detailed record of all web requests with access logs.
- Web Application Firewall (WAF): Filter and block harmful traffic based on defined rules.
- Content Delivery Network (CDN): Reduce direct exposure to your server and use integrated WAFs.

**Protecting the Host Machine**

- Least Privilege: Use low-privilege users for services.
- System Hardening: Disable unnecessary services and close unused ports.
- Antivirus: Add endpoint-level protection that blocks known malware.

**Security Tips for All Three Components**

- Strong Authentication: Don't just let anyone access your code, admin panels, or host machine.
- Patch Management: Ensure your app dependencies, web server, and host machine are up to date.


## Web Application Firewall (WAF)

**WAFs** are a powerful tool that can be integrated as another layer of protection for websites and web applications. They inspect incoming HTTP traffic and block or log potentially harmful requests based on security rules. Think of the analogy of a bouncer at a bar or club. Every person (web request) that wants to enter must be checked by the bouncer (firewall). Anyone (any request) that doesn't meet the standard requirement will be rejected.

Let's take a closer look at the types of WAFs available to us as defenders, then dive deeper into their functionality.

- Cloud-based (Reverse Proxy): Sits in front of the web server. These WAFs are easy to deploy and have great scalability.
- Host-based: Software deployed directly on the web server and offers control for each application.
- Network-based: A physical or virtual appliance situated on the network perimeter. More suited for enterprise environments.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
