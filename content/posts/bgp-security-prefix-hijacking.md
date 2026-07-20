---
title: "BGP Security & Prefix Hijacking | BGP Güvenliği ve Önek Ele Geçirme"
date: 2026-07-02
description: "How the Border Gateway Protocol (BGP) is exploited through prefix hijacking and how modern cryptographic frameworks like RPKI, BGPsec, and ASPA secure global routing. / Sınır Geçit Protokolü'nün (BGP) önek ele geçirme ile nasıl suistimal edildiği ve RPKI, BGPsec ile ASPA gibi modern kriptografik yapıların küresel yönlendirmeyi nasıl güvenceye aldığı."
tags: ["Network Security", "BGP", "Routing", "Cryptography", "Internet Infrastructure"]
categories: ["Security"]
ShowToc: true
math: false
mermaid: true
cover:
    image: "/img/cover-1544197150-b99a580bb7a8.jpg"
    alt: "Global network and routing infrastructure visualization"
    relative: false
---

## Türkçe (TR)

### 1. Giriş: İnternetin Yön Tabelaları ve Güven Problemi
İnternet, binlerce bağımsız ağın (Otonom Sistemler - AS) bir araya gelmesiyle oluşan devasa bir ağlar ağıdır. Bir e-postanın, videonun ya da web sitesi isteğinin dünyayı dolaşarak doğru hedefe ulaşmasını sağlayan protokol ise **BGP (Border Gateway Protocol - Sınır Geçit Protokolü)**'dir. BGP, internetin gizli yön tabelası ve haritacısı gibidir.

Ancak BGP, internetin henüz akademik ve sınırlı bir topluluk tarafından kullanıldığı 1989 yılında tasarlandı. Bu nedenle, doğası gereği güvenlik mekanizmalarına sahip değildir. Protokol, her otonom sistemin "doğru söylediğini" varsayar. Bir otonom sistem, "Şu IP blokları benim üzerimden geçiyor" dediğinde, diğer sistemler bu bilgiye sorgusuz sualsiz güvenir. Bu yapısal güven, küresel internet yönlendirme tablosunu manipülasyonlara ve saldırılara son derece açık hale getirmektedir.

---

### 2. BGP Prefix Hijacking (Önek Ele Geçirme) Nedir?
BGP Prefix Hijacking, kötü niyetli veya yanlış yapılandırılmış bir otonom sistemin (AS), aslında sahibi olmadığı bir IP adres bloğunu (prefix) tüm dünyaya anons etmesidir. 

Bunu, bir otoyoldaki yön tabelalarını değiştirip trafiği başka bir şehre yönlendiren bir saldırgana benzetebiliriz. İnternet trafiği, her zaman en spesifik (en uzun önek - longest prefix match) ve en kısa yola yönlendiği için, saldırgan bu kuralları kullanarak trafiği kendi üzerine çekebilir.

*   **Veri Dinleme (Eavesdropping):** Saldırgan trafiği kendi ağından geçirip analiz ettikten sonra orijinal hedefine iletebilir (Man-in-the-Middle).
*   **Hizmet Dışı Bırakma (DoS/Blackholing):** Trafiği kendi üzerine çekip tamamen çöpe atarak (blackhole) hedeflenen servisi erişilemez kılabilir.
*   **Route Leak (Rota Sızıntısı):** Bir operatörün, müşterisi veya akranı olan başka bir ağdan aldığı rota bilgilerini yanlışlıkla diğer sağlayıcılara anons etmesidir. Bu durum kasıtlı olmasa da büyük trafik darboğazlarına yol açar.

#### BGP Hijack Saldırı Akışı
Aşağıdaki diyagramda, meşru bir yönlendirme ile bir saldırganın (AS 666) yalan anons yaparak trafiği nasıl kendi üzerine çektiği gösterilmektedir:

![Diyagram / Diagram](/img/mermaid-bgp-security-prefix-hijacking-1-6d676905.svg)

---

### 3. RPKI (Resource Public Key Infrastructure): İlk Savunma Kalkanı
BGP zafiyetlerine karşı geliştirilen en yaygın ve etkili modern savunma yöntemi **RPKI (Resource Public Key Infrastructure)**'dir. RPKI, yönlendirme bilgilerinin orijinini doğrulamak için tasarlanmış bir açık anahtar altyapısıdır.

*   **ROA (Route Origin Authorization):** IP adres bloğunun gerçek sahibi, hangi otonom sistemin bu IP bloğunu anons etmeye yetkili olduğunu belirten kriptografik olarak imzalanmış bir ROA belgesi oluşturur.
*   **ROV (Route Origin Validation):** Yönlendiriciler (routers), aldıkları BGP anonslarını RPKI veri tabanıyla karşılaştırarak doğrular. Eğer anons edilen otonom sistem ROA belgesindekiyle eşleşmiyorsa, anons "Geçersiz" (Invalid) kabul edilir ve trafik filtrelenerek çöpe atılır. Bu sayede sahte orijin anonsları engellenmiş olur.

---

### 4. BGPsec ve ASPA: Yol Doğrulama Teknolojileri
RPKI, bir anonsun *başlangıç noktasını* (orijinini) doğrulamada harikadır ancak anonsun yönlendiriciler arasında gezinirken izlediği *yolu* (AS Path) koruyamaz. Saldırganlar, anonsu yapan son halkayı taklit ederek hala yolu manipüle edebilirler.

*   **BGPsec:** Rota bilgisinin geçtiği her otonom sistemin anonsu kendi özel anahtarıyla imzalamasını gerektiren bir provizyondur. Bu sayede tüm rota yolu kriptografik olarak doğrulanır. Ancak, yönlendiriciler üzerinde çok yüksek işlem gücü gerektirmesi ve küresel olarak tüm internet sağlayıcılarının aynı anda geçiş yapma zorunluluğu nedeniyle yaygınlaşamamıştır.
*   **ASPA (Autonomous System Provider Authorization):** Yol doğrulamadaki karmaşıklığı azaltmak için geliştirilen daha yeni bir standarttır. ASPA, her otonom sistemin kendi üst sağlayıcılarını (provider) kriptografik olarak beyan etmesini sağlar. Böylece "valley-free" yönlendirme kuralları denetlenerek, aradaki hileli otonom sistem geçişleri kolayca tespit edilebilir.

---

## English (EN)

### 1. Introduction: The Internet's Signposts and the Trust Deficit
The Internet is a massive network of networks, connecting thousands of independent networks known as Autonomous Systems (ASs). The Border Gateway Protocol (BGP) acts as the global post office and mapping system, ensuring that data packets traverse these networks to reach their correct destination.

However, BGP was designed in 1989 when the Internet was a collaborative, trusted environment. Consequently, it contains no built-in security or validation mechanisms. The protocol operates on implicit trust: when an AS announces that it can route traffic to a specific range of IP addresses, all other ASs believe it and update their routing tables accordingly. This lack of authentication makes the global routing pipeline highly vulnerable to disruption and exploitation.

---

### 2. What is BGP Prefix Hijacking?
BGP Prefix Hijacking occurs when an AS maliciously or accidentally advertises an IP prefix that it does not own. 

This is analogous to someone changing the physical highway signs to redirect traffic meant for a specific city toward an alternate destination. Because routers prefer the most specific route (longest prefix match) and the shortest path, attackers can exploit these rules to intercept and control data flows.

*   **Traffic Interception (PITM):** The hijacker routes the traffic through their own network to inspect, log, or manipulate it before forwarding it to the legitimate destination.
*   **Blackholing (DoS):** The attacker draws the traffic and drops it entirely, making the targeted service completely unreachable.
*   **Route Leaks:** Unlike malicious hijacking, a route leak is typically a misconfiguration where an AS propagates routing information beyond its intended boundaries, causing massive traffic congestion.

#### BGP Hijack Attack Flow
The diagram below illustrates how traffic is diverted when a malicious entity (AS 666) publishes a fake BGP announcement:

![Diyagram / Diagram](/img/mermaid-bgp-security-prefix-hijacking-2-edfb13e2.svg)

---

### 3. RPKI (Resource Public Key Infrastructure): Origin Validation
To secure BGP, the industry developed **RPKI (Resource Public Key Infrastructure)**. RPKI uses cryptographic signatures to enable **Origin Validation**, ensuring that only authorized networks can advertise specific IP blocks.

*   **ROA (Route Origin Authorization):** The owner of an IP block signs a digital certificate stating which AS is authorized to originate advertisements for their prefix.
*   **ROV (Route Origin Validation):** Network operators run local validators that pull ROA data. Routers match incoming BGP announcements against these records. If a route is marked as "Invalid" (meaning the announcing AS does not match the ROA), the route is discarded, stopping the hijack at the border.

---

### 4. BGPsec and ASPA: Securing the AS Path
While RPKI is excellent for validating where a route *starts*, it does not protect the transit path (AS Path). An attacker can still insert themselves into the middle of a path or pretend to be connected directly to the legitimate origin AS.

*   **BGPsec:** An extension to BGP that requires every hop in the routing chain to cryptographically sign the update. While it offers robust path validation, BGPsec demands substantial CPU power from routers and requires universal adoption to be effective, which has stalled its deployment.
*   **ASPA (Autonomous System Provider Authorization):** A newer, more pragmatic standard designed to secure path verification. ASPA enables ASs to publish a signed list of their authorized upstream providers. This allows routers to detect anomalies in customer-provider relationships and identify invalid paths without the performance overhead of full BGPsec signing.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / bgp-security-and-prefix-hijacking]]*
