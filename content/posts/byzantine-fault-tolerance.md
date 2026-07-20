---
title: "Byzantine Fault Tolerance"
date: 2026-06-14
description: "Dağıtık sistemlerin ve blokzincir ağlarının, kötü niyetli veya hatalı düğümlere rağmen nasıl konsensüse varabildiği ve Bizans Generalleri Problemi. / How distributed systems and blockchain networks reach consensus despite malicious or faulty nodes, and the Byzantine Generals Problem."
tags: ["Distributed Systems", "Consensus", "BFT", "Blockchain"]
categories: ["Blog"]
ShowToc: true
math: true
mermaid: true
cover:
    image: "/img/cover-1599707367072-cd6ada2bc375.jpg"
    alt: "Byzantine castle fortification representing network consensus"
    relative: false
---

## Türkçe (TR)

### Giriş
Bir bilgisayar çöktüğünde veya ağ bağlantısı koptuğunda, sisteme ne olduğunu anlamak kolaydır: Düğüm (node) artık yanıt vermiyordur. Ancak, bir düğüm çalışmaya devam edip **kasıtlı olarak yalan söylerse** ne olur? Ağa sahte veriler gönderen, farklı düğümlere çelişkili talimatlar ileten veya saldırıya uğramış olan bu düğümler, dağıtık sistemler teorisinde en zorlu hata türünü oluşturur. Bu tür rastgele ve kötü niyetli davranışları tolere ederek ağın güvenli bir şekilde ortak bir karara varmasını sağlayan sistemsel özelliğe **Bizans Hata Toleransı (Byzantine Fault Tolerance - BFT)** denir.

### Bizans Generalleri Problemi
BFT kavramı, 1982 yılında Leslie Lamport, Robert Shostak ve Marshall Pease tarafından ortaya atılan "Bizans Generalleri Problemi"ne dayanır. Problem şu şekildedir:
*   Bir düşman kalesini kuşatan birkaç Bizans generali vardır. Generaller sadece ulaklar (mesajlar) aracılığıyla haberleşebilir.
*   Kuşatmanın başarılı olması için generallerin ortak bir karar alması gerekir: **Hep birlikte saldırmak** ya da **hep birlikte geri çekilmek**.
*   Ancak generallerden bazıları haindir ve amaçları ortak bir karara varılmasını engelleyerek orduyu bozguna uğratmaktır.
*   Örneğin, hain bir general, saldırmak isteyen bir generale "Saldırıyorum", geri çekilmek isteyen bir diğerine ise "Geri çekiliyorum" mesajı göndererek koordinasyonu bozabilir.

### Problem Senaryosu
Aşağıdaki diyagramda, iki dürüst general ile ağa çelişkili mesajlar göndererek konsensüsü bozmaya çalışan hain bir lider generalin yarattığı Bizans çıkmazı gösterilmiştir:

![Diyagram / Diagram](/img/mermaid-byzantine-fault-tolerance-1-ba9d19c3.svg)

### BFT Matematiksel Gereksinimleri
Matematiksel olarak kanıtlanmıştır ki, dürüst generallerin (düğümlerin) hainlerin (kötü niyetli düğümlerin) varlığına rağmen doğru bir kararda uzlaşabilmesi için dürüst düğüm sayısının hain düğüm sayısının en az üç katından fazla olması gerekir.
*   **Düğüm Sayısı Formülü**: Tolere edilmek istenen hain/hatalı düğüm sayısı $f$ ise, sistemdeki toplam düğüm sayısı en az $3f + 1$ olmalıdır. Örneğin, 1 hain düğümü tolere etmek için en az 4 düğüme ihtiyaç vardır.
*   **Karar Çoğunluğu (Quorum)**: Kararların onaylanması için en az $2f + 1$ dürüst düğümün ortak bir fikirde birleşmesi gerekir.

### PBFT (Practical Byzantine Fault Tolerance)
BFT algoritmaları uzun yıllar boyunca aşırı mesaj trafiği ($O(n^2)$ işlem karmaşıklığı) nedeniyle pratik sistemlerde kullanılamadı. 1999 yılında geliştirilen **PBFT (Pratik Bizans Hata Toleransı)** algoritması, üç aşamalı bir oylama (Pre-prepare, Prepare, Commit) ve lider değişimi (View Change) mekanizmasıyla bu sorunu çözdü ve yüksek performanslı ağlarda BFT'nin kullanılabilmesinin önünü açtı.

### Siber Güvenlikteki Önemi
Bizans Hata Toleransı, günümüzde şu kritik alanlarda güvenlik sağlar:
*   **Blokzincir ve Kripto Paralar**: Bitcoin (Proof of Work) ve Ethereum (Proof of Stake) gibi sistemler, merkeziyetsiz ve güvenilmeyen bir ortamda (trustless) çift harcamayı önlemek ve işlemlerde uzlaşmak için BFT mantığına dayanan konsensüs algoritmaları kullanır.
*   **Kritik Altyapılar**: Havacılık kontrol sistemleri (uçak otopilotları), nükleer santral kontrol mekanizmaları ve SCADA sistemleri, sensörlerden gelebilecek hatalı veya kasıtlı olarak tahrif edilmiş verilerden etkilenmemek için BFT mimarileriyle tasarlanır.

---

## English (EN)

### Introduction
When a computer crashes or a network connection drops, it is easy to diagnose: the node simply stops responding. But what happens if a node continues to operate and **deliberately sends false information**? Nodes that inject fake data, broadcast conflicting messages to different peers, or act under adversary control represent the most difficult class of failures in distributed computing. The systemic property that allows a network to survive arbitrary, malicious behaviors and still reach a unified, correct agreement is called **Byzantine Fault Tolerance (BFT)**.

### The Byzantine Generals Problem
The concept of BFT originated from a logical puzzle proposed in 1982 by Leslie Lamport, Robert Shostak, and Marshall Pease, known as the "Byzantine Generals Problem":
*   Several divisions of the Byzantine army are camping outside an enemy city, each commanded by its own general. The generals can communicate only by messengers.
*   To succeed, the generals must agree on a common plan of action: either **attack together** or **retreat together**.
*   However, some of the generals might be traitors, aiming to prevent consensus and guide the army into a coordinated disaster.
*   For example, a traitorous general can send "Attack" to one honest general and "Retreat" to another, causing them to execute conflicting moves.

### Problem Scenario
The diagram below illustrates the Byzantine deadlock created when a malicious leader general sends contradictory instructions to two honest generals:

![Diyagram / Diagram](/img/mermaid-byzantine-fault-tolerance-2-08d9de94.svg)

### Mathematical Requirements of BFT
It is mathematically proven that for honest nodes to reach consensus in the presence of traitors, the honest nodes must outnumber the malicious ones by a factor of three:
*   **Node Count Formula**: To tolerate $f$ Byzantine (malicious) failures, a system must consist of at least $3f + 1$ total nodes. For example, to tolerate 1 traitorous node, a minimum of 4 nodes is required.
*   **Quorums**: Agreements require a quorum of at least $2f + 1$ nodes to verify state changes, ensuring that honest nodes always dominate the decision process.

### PBFT (Practical Byzantine Fault Tolerance)
For decades, early BFT algorithms were too slow for real-world deployments due to high message complexity ($O(n^2)$). In 1999, Miguel Castro and Barbara Liskov introduced **PBFT (Practical Byzantine Fault Tolerance)**. By using a three-phase state machine replication protocol (Pre-prepare, Prepare, and Commit) and a leader-reelection mechanism (View Change), PBFT made BFT viable for low-latency, high-performance distributed networks.

### Cybersecurity Significance
Today, Byzantine Fault Tolerance is a foundational concept across modern security engineering:
*   **Blockchain Networks**: Decentralized cryptocurrencies like Bitcoin (via Proof of Work) and Ethereum (via Proof of Stake) rely on BFT-derived consensus to prevent double-spending and record transactions in a trustless environment where participants are unknown.
*   **Critical Infrastructure**: Aerospace control systems, autonomous train signaling, and SCADA control rooms leverage BFT systems. This prevents a single failed sensor or a spoofed controller command from crashing the vehicle or disrupting public utility grids.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / byzantine-fault-tolerance]]*
