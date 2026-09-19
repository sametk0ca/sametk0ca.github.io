---
title: "Byzantine Fault Tolerance"
date: 2026-06-14
description: "Dağıtık sistemlerin ve blokzincir ağlarının, kötü niyetli veya hatalı düğümlere rağmen nasıl konsensüse varabildiği ve Bizans Generalleri Problemi. / How distributed systems and blockchain networks reach consensus despite malicious or faulty nodes, and the Byzantine Generals Problem."
draft: false
tags: ["Distributed Systems", "Consensus", "BFT", "Blockchain"]
categories: ["Blog"]
ShowToc: true
math: true
mermaid: false
cover:
    image: "/img/cover-1599707367072-cd6ada2bc375.jpg"
    alt: "Byzantine castle fortification representing network consensus"
    relative: false
related:
  - "[[concepts/byzantine-fault-tolerance|Byzantine Fault Tolerance (BFT)]]"
  - "[[posts/distributed-consensus-and-paxos|Distributed Consensus and Paxos]]"
---

## 🇹🇷 Türkçe (TR)

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

![Diyagram](/img/mermaid-byzantine-fault-tolerance-1-ba9d19c3.svg)

### BFT Matematiksel Gereksinimleri

Matematiksel olarak kanıtlanmıştır ki, dürüst düğümlerin hainlerin varlığına rağmen doğru bir kararda uzlaşabilmesi için düğümlerin en fazla üçte birinden azının hain olması gerekir.
*   **Düğüm Sayısı Formülü**: Tolere edilmek istenen hain/hatalı düğüm sayısı $f$ ise, sistemdeki toplam düğüm sayısı en az $3f + 1$ olmalıdır. Örneğin, 1 hain düğümü tolere etmek için en az 4 düğüme ihtiyaç vardır.
*   **Karar Çoğunluğu (Quorum)**: Kararların onaylanması için en az $2f + 1$ düğümün aynı görüşte olması gerekir. Bunların en fazla $f$ tanesi hain olabileceğinden en az $f + 1$ tanesi dürüsttür ve doğru karar öne çıkar.

### PBFT (Practical Byzantine Fault Tolerance)

İlk BFT çözümleri uzun yıllar boyunca fazlasıyla yavaş olduğu için pratik sistemlerde kullanılamadı. 1999 yılında Miguel Castro ve Barbara Liskov tarafından geliştirilen **PBFT (Pratik Bizans Hata Toleransı)** algoritması, üç aşamalı bir oylama (Pre-prepare, Prepare, Commit) ve lider değişimi (View Change) mekanizmasıyla BFT'yi gerçek sistemlerde kullanılabilir hale getirdi. Ancak $O(n^2)$ mesaj karmaşıklığı nedeniyle çok sayıda düğüme ölçeklenmesi hâlâ sınırlıdır.

### Siber Güvenlikteki Önemi

Bizans Hata Toleransı, günümüzde şu kritik alanlarda güvenlik sağlar:
*   **Blokzincir ve Kripto Paralar**: Blokzincirler, tanımadıkları katılımcıların olduğu güvensiz bir ortamda çift harcamayı önlemek ve işlemlerde uzlaşmak zorundadır. Bitcoin (Proof of Work), Bizans davranışlarına olasılıksal olarak dayanıklı Nakamoto konsensüsünü kullanır. Ethereum (Proof of Stake) BFT tarzı bir kesinleştirme mekanizması içerir. Tendermint tabanlı ağlar (örneğin Cosmos) ise klasik BFT algoritmalarına dayanır.
*   **Güvenlik-Kritik Sistemler**: Uçak kontrol sistemleri gibi güvenlik-kritik alanlarda, hatalı veya tahrif edilmiş sensör verilerinden etkilenmemek için çoklu yedeklilik ve oylama gibi Bizans hatalarına dayanıklı tasarımlar kullanılır.

---

## 🇬🇧 English (EN)

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

![Diagram](/img/mermaid-byzantine-fault-tolerance-2-08d9de94.svg)

### Mathematical Requirements of BFT

It is mathematically proven that for honest nodes to reach consensus in the presence of traitors, fewer than one third of all nodes may be malicious:
*   **Node Count Formula**: To tolerate $f$ Byzantine (malicious) failures, a system must consist of at least $3f + 1$ total nodes. For example, to tolerate 1 traitorous node, a minimum of 4 nodes is required.
*   **Quorums**: Agreements require a quorum of at least $2f + 1$ matching nodes. At most $f$ of them can be traitors, so at least $f + 1$ are honest and the correct decision prevails.

### PBFT (Practical Byzantine Fault Tolerance)

For years, early BFT solutions were too slow for real-world deployments. In 1999, Miguel Castro and Barbara Liskov introduced **PBFT (Practical Byzantine Fault Tolerance)**. By using a three-phase state machine replication protocol (Pre-prepare, Prepare, and Commit) and a leader-reelection mechanism (View Change), PBFT made BFT usable in real systems. Its $O(n^2)$ message complexity still limits how well it scales to large numbers of nodes.

### Cybersecurity Significance

Today, Byzantine Fault Tolerance is a foundational concept across modern security engineering:
*   **Blockchain Networks**: Blockchains must prevent double-spending and agree on transactions in a trustless environment where participants are unknown. Bitcoin (Proof of Work) uses Nakamoto consensus, which tolerates Byzantine behavior probabilistically. Ethereum (Proof of Stake) includes a BFT-style finality mechanism. Tendermint-based networks (for example, Cosmos) rely on classical BFT algorithms.
*   **Safety-Critical Systems**: In domains such as flight control, Byzantine-tolerant designs (redundancy plus voting) keep a single failed sensor or a spoofed command from bringing down the whole system.
