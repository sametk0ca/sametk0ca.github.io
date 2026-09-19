---
title: "Distributed Consensus and Paxos"
date: 2026-05-19
description: "Why distributed systems need consensus: the FLP theorem, Paxos, Raft and how BFT extends them to malicious nodes. / Dağıtık sistemlerin neden konsensüse ihtiyaç duyduğu: FLP teoremi, Paxos, Raft ve BFT'nin kötü niyetli düğümlere genişletilmesi."
draft: false
tags: ["Distributed Systems", "Consensus", "Paxos", "Raft", "CyBOK"]
categories: ["Knowledge Base"]
related:
  - "[[concepts/distributed-consensus-and-paxos|Distributed Consensus and Paxos]]"
  - "[[concepts/byzantine-fault-tolerance|Byzantine Fault Tolerance (BFT)]]"
  - "[[posts/byzantine-fault-tolerance|Byzantine Fault Tolerance]]"
  - "[[cap-theorem|CAP Theorem]]"
---

## 🇹🇷 Türkçe (TR)

Dağıtık sistemlerin temel problemi, ağ arızaları veya düğüm (node) çökmeleri durumunda bile tüm katılımcıların tek bir değer üzerinde hemfikir olmasını sağlamaktır. **Dağıtık Konsensüs (Distributed Consensus)**, modern bulut altyapılarının, veritabanlarının ve blokzincir sistemlerinin tutarlılığını (consistency) sağlayan temel mekanizmadır. Bu alandaki en önemli teorik çalışma olan **Paxos Algoritması**, güvenilir olmayan bir ağ üzerinde konsensüs sağlamanın matematiksel ispatını sunar.

### Teknik Zorluklar ve FLP Teoremi

Dağıtık sistemlerde konsensüs sağlamanın önündeki en büyük engel "FLP Impossibility" (Fischer, Lynch, Paterson) teoremidir. Bu teorem, tamamen asenkron bir ağda tek bir düğümün bile çökebildiği durumda, hiçbir deterministik algoritmanın konsensüsün her zaman sonlanacağını (termination) garanti edemeyeceğini ispatlar. Bu nedenle, gerçek dünya algoritmaları "zayıf eşzamanlılık" (weak synchrony) varsayımları üzerine inşa edilir.

### Konsensüs Algoritmaları ve Mekanizmalar

1. **Paxos:** Leslie Lamport tarafından geliştirilen bu algoritma, üç temel rol (Proposer, Acceptor, Learner) üzerinden çalışır. "Basic Paxos" tek bir değer üzerinde anlaşırken, "Multi-Paxos" bir değerler dizisi (log) üzerinde anlaşarak replike edilmiş durum makineleri (RSM) oluşturulmasını sağlar.
2. **Raft:** Paxos'un anlamsal karmaşıklığını gidermek amacıyla geliştirilen, daha anlaşılır ve uygulanabilir bir konsensüs algoritmasıdır. Lider seçimi (Leader Election) ve günlük replikasyonu (Log Replication) süreçlerini merkezi bir yapıda yönetir.
3. **Bizans Hata Toleransı (BFT):** Paxos ve Raft yalnızca çöken düğümlere (crash fault) dayanıklıdır. BFT ise kötü niyetli (malicious) veya hatalı veri gönderen düğümlere karşı da dirençli olmayı hedefler. PBFT (Practical Byzantine Fault Tolerance) algoritması, izinli (permissioned) blokzincir sistemlerinin birçoğuna temel oluşturmuştur.

### Güvenlik ve Tutarlılık İlişkisi

Konsensüs algoritmaları, siber güvenlikte "Kullanılabilirlik" (Availability) ve "Bütünlük" (Integrity) ilkeleri ile doğrudan ilişkilidir. Bir sistemin saldırı altında bile doğru karar verebilmesi (Safety) ve kararların nihayete ermesi (Liveness), bu algoritmaların doğru kurgulanmasına bağlıdır. CAP Teoremi (Consistency, Availability, Partition Tolerance), bu sistemlerin tasarımındaki temel ödünleşimleri (trade-offs) tanımlar.

---

## 🇬🇧 English (EN)

### Distributed Consensus and Paxos: Foundations of Reliable Systems

The fundamental problem of distributed systems is ensuring that all participants agree on a single value even in the event of network failures or node crashes. **Distributed Consensus** is the core mechanism that ensures consistency in modern cloud infrastructures, databases, and blockchain systems. The most significant theoretical work in this field, the **Paxos Algorithm**, provides the mathematical proof for achieving consensus over an unreliable network.

### Technical Challenges and the FLP Theorem

The primary obstacle to achieving consensus in distributed systems is the "FLP Impossibility" (Fischer, Lynch, Paterson) theorem. This theorem proves that in a fully asynchronous network where even a single node may crash, no deterministic algorithm can guarantee that consensus will always terminate. Therefore, real-world algorithms are built upon "weak synchrony" assumptions.

### Consensus Algorithms and Mechanisms

1. **Paxos:** Developed by Leslie Lamport, this algorithm operates through three primary roles: Proposer, Acceptor, and Learner. While "Basic Paxos" agrees on a single value, "Multi-Paxos" allows for agreement on a sequence of values (a log), enabling the creation of Replicated State Machines (RSM).
2. **Raft:** Developed to address the semantic complexity of Paxos, Raft is a more understandable and implementable consensus algorithm. It manages processes like Leader Election and Log Replication within a centralized structure.
3. **Byzantine Fault Tolerance (BFT):** Paxos and Raft only tolerate crash faults. BFT aims for resilience against nodes that are malicious or send erroneous data as well. The PBFT (Practical Byzantine Fault Tolerance) algorithm underlies many permissioned blockchain systems.

### Relationship Between Security and Consistency

Consensus algorithms are directly related to the "Availability" and "Integrity" principles of cybersecurity. The ability of a system to make correct decisions even under attack (Safety) and for those decisions to eventually terminate (Liveness) depends on the correct implementation of these algorithms. The CAP Theorem (Consistency, Availability, Partition Tolerance) defines the fundamental trade-offs in the design of such systems.
