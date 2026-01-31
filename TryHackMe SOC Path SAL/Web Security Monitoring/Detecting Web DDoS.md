
At their core, **Denial-of-Service (DoS)** attacks are meant to overwhelm a website or app so that people can’t use it. When this happens, customers can’t log in, shop, or access services, and businesses lose money and trust.

At their core, **Denial-of-Service (DoS)** attacks are meant to overwhelm a website or app so that people can’t use it. When this happens, customers can’t log in, shop, or access services, and businesses lose money and trust.


To scale up, attackers turn to **Distributed Denial-of-Service (DDoS)** attacks and utilize ==botnets==, an army of compromised devices under their control. The computers, IoT devices, and even servers are often infected with malware and secretly controlled by the attacker. When instructed, the bots flood the target website or web application with traffic, overwhelming it much more effectively than a single machine could.

## Targeted Resources

If an attacker aims to disrupt a web service like we've discussed, they will likely focus on endpoints that consume the most server resources per request or are most critical to maintain site functionality. Pages like `/login` or search forms are prime targets because each request forces the server to query a database, validate input, and return results. This makes the requests far more expensive to process than static content like product pages or images.

Commonly targeted endpoints and reasoning: 

- `/login` - involves authentication processes 
- `/search` - requires complex database queries
- `/api` endpoints - critical for dynamic content delivery
- `/register` or `/signup` - requires database writes and validation
- `/contact` or `/feedback` - requires database entries and can trigger email notifications
- `/cart` or `/checkout` - requires session management, inventory checks, and payment processing

# Indicators

|Indicator|Example|Description|
|---|---|---|
|High Request Rate|`10.10.10.100` → 1000 `GET /login`|A resource-heavy page like `/login` is flooded with requests to overwhelm authentication processes. Login pages are common targets since each request may trigger password checks and database queries|
|Odd User-Agents|`curl/7.6.88` → `/index` repeatedly|Attackers spoof outdated or unusual User-Agents to blend in or bypass filters. Spotting traffic with tools like `curl` or `Python-urllib/3.x`, for example, can be a red flag for automated attacks|
|Geographic Anomalies|IP address origins dotted around the world|Legitimate traffic typically comes from a few regions where real users are located. A globally distributed botnet may utilize IP addresses from around the world|
|Burst Timestamps|50 requests in 1 second → `/search`|A sudden spike of requests packed into the same second creates an unnatural traffic pattern that points to automation|
|Server Errors ([5xx](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#server_error_responses))|A significant spike of `503 Service Unavailable` errors|A sudden surge of server error responses (`500` - `511`) indicates resources are maxed out and the service is struggling under attack traffic|
|Logic Abuse|`GET /products?limit=999999`|Attackers craft queries that overload the server, forcing it to load huge amounts of information and slowing it down for everyone|
# Defense

## Application Level Defense

**Secure Development Practices  


A secure site starts with secure code. Search fields and forms must validate input so they can’t be abused. Think of a search form like a librarian who looks up books on request. If the librarian has clear rules, like “only search for titles under 50 characters”, they can respond quickly. Without rules in place, someone could ask the librarian to search for an overly long or strange title with special characters, slowing them down and delaying everyone else's requests. In the same way, web applications need input validation to stop attackers from submitting specialized queries aimed at overloading the system.

**Challenges**

One way to stop automated traffic is to require a challenge before granting access. This could be a CAPTCHA, where the user solves a puzzle, like clicking images or checking a box. For humans, it’s a small step, but for bots, it can block or slow down an attack.

Websites can also use JavaScript challenges, which run quietly in the background to confirm if a visitor is a real user or automated traffic. Legitimate users usually don’t notice them, but automated tools and botnets often fail, making these challenges an effective filter against malicious traffic.

## Network and Infrastructure Defenses

**Content Delivery Network (CDN)**

CDNs help manage server load by caching and serving content from edge servers closest to users. This reduces latency and allows the origin server to handle only a fraction of requests, while the CDN serves the majority. As a result, CDNs take on much of the burden of mitigating DDoS attacks. They also provide load-balancing to distribute traffic across servers, ensuring no single server is overloaded and rerouting requests if one becomes unavailable.

**Web Application Firewall (WAF)**

CDNs typically integrate WAFs in an effort to shield their customers' servers. They inspect incoming traffic and either allow, challenge, or block requests. WAFs work off of rules that integrate known attack indicators and threat intelligence. Modern WAF solutions are already very good at mitigating DoS and DDoS attacks because they know what to look out for. Custom rules can also be developed to assist in defending against targeted threats.