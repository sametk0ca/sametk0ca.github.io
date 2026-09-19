---
title: "DNS Leak"
date: 2026-05-12
description: "What DNS leaks are, how they expose your browsing to your ISP despite a VPN, and how to prevent them. / DNS sızıntılarının ne olduğu, VPN'e rağmen tarama bilgilerinizi ISP'ye nasıl açtığı ve nasıl önlenebileceği."
draft: false
tags: ["Privacy", "CyberSecurity", "Networking", "VPN"]
categories: ["Blog"]
math: false
mermaid: false
related:
  - "[[dns-leak|DNS Leak]]"
---

## 🇹🇷 Türkçe (TR)

DNS (Alan Adı Sistemi) sızıntıları, DNS sorgularının güvenli bir VPN tünelinin dışından gönderilmesi ve böylece kullanıcının ziyaret ettiği alan adlarının internet servis sağlayıcısına (ISP) ifşa olması durumunda gerçekleşir. Bu, şifrelenmiş bağlantılar tarafından sağlanan güvenliği zayıflatabilecek yaygın bir gizlilik açığıdır.

### DNS Sızıntısına Ne Sebep Olur?

1. **İşletim Sistemi Varsayılanları:** Bazı işletim sistemi sürümleri, VPN tarafından sağlanan DNS sunucuları yerine ISP'nin DNS sunucularına öncelik verebilir.
2. **IPv6 Trafiği:** Eğer bir VPN yalnızca IPv4'ü destekliyorsa, IPv6 DNS sorguları yerel ISP üzerinden sızabilir.
3. **Şeffaf DNS Proxy'leri:** ISP'ler, DNS trafiğini yakalamak ve yönlendirmek için şeffaf proxy'ler kullanabilir.

### Nasıl Önlenir?

- **Sızıntı Korumalı bir VPN Kullanın:** VPN istemcinizin yerleşik bir "DNS Sızıntı Koruması" (DNS Leak Protection) özelliğine sahip olduğundan emin olun.
- **DNS Trafiğini Tünelden Geçirin:** Sistemin DNS sorgularının VPN'in kendi DNS sunucusuna gittiğinden emin olun. Cloudflare (1.1.1.1) veya Google (8.8.8.8) gibi bir sunucuyu elle yapılandırırsanız, sorgularınızın yine tünelin içinden gittiğini kontrol edin; aksi halde ISP bu sorguları görmeye devam eder. Şifreli DNS (DoH/DoT) kullanmak da ek koruma sağlar.
- **IPv6'yı Yönetin:** VPN'iniz IPv6'yı desteklemiyorsa IPv6'yı devre dışı bırakmak veya VPN'in IPv6 sızıntı korumasını açmak kazara oluşabilecek sızıntıları önler.
- **Test Edin:** dnsleaktest.com veya ipleak.net gibi araçlarla, VPN açıkken görünen DNS sunucularının ISP'nize ait olmadığını doğrulayın.

---

## 🇬🇧 English (EN)

DNS (Domain Name System) leaks occur when DNS queries are sent outside of a secure VPN tunnel, exposing the domains a user visits to their ISP. This is a common privacy gap that can undermine the security provided by encrypted connections.

### What causes a DNS Leak?

1. **Operating System Defaults:** Some OS versions might prioritize the ISP's DNS servers over the ones provided by the VPN.
2. **IPv6 Traffic:** If a VPN only supports IPv4, IPv6 DNS queries might leak through the local ISP.
3. **Transparent DNS Proxies:** ISPs can use transparent proxies to intercept and redirect DNS traffic.

### How to prevent it?

- **Use a VPN with Leak Protection:** Ensure your VPN client has a built-in "DNS Leak Protection" feature.
- **Route DNS Through the Tunnel:** Make sure your system's DNS queries go to the VPN's own DNS server. If you configure a server such as Cloudflare (1.1.1.1) or Google (8.8.8.8) manually, verify that the queries still travel inside the tunnel; otherwise your ISP can keep seeing them. Encrypted DNS (DoH/DoT) adds further protection.
- **Manage IPv6:** If your VPN does not support IPv6, disabling IPv6 or enabling the VPN's IPv6 leak protection prevents accidental leaks.
- **Test It:** Use tools like dnsleaktest.com or ipleak.net to confirm that, with the VPN on, the DNS servers shown do not belong to your ISP.
