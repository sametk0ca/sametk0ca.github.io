---
title: "Race Condition"
date: 2026-06-20
draft: false
tags: ["Race Condition", "Concurrency", "Web Security", "Cybersecurity", "Exploit"]
categories: ["Security"]
ShowToc: true
math: false
mermaid: true
cover:
    image: "https://images.unsplash.com/photo-1461896836934-ffe607ba8211"
    alt: "Athletes racing, symbolizing multiple processes competing for the same resource."
    relative: false
---

### Türkçe

## **1. Giriş: Zamanın ve Sıralamanın Önemi**

Modern yazılımlar, kullanıcılara hızlı yanıt verebilmek için aynı anda birden fazla işi (eşzamanlılık - concurrency) yürütür. Ancak bu hız ve paralel işlem gücü, beraberinde yönetilmesi zor senkronizasyon problemlerini getirir. Bu problemlerin en sinsilerinden biri de **Race Condition (Yarış Durumu)** zafiyetidir. 

Basit bir benzetme yapalım: Ortak bir banka hesabınız olduğunu ve bu hesapta sadece 100 TL bulunduğunu düşünün. İki farklı kişi, iki ayrı ATM'den tam olarak aynı milisaniyede 100 TL çekmeye çalışıyor. Sistem, her iki ATM'ye de aynı anda "Evet, hesapta 100 TL var" yanıtını verirse ne olur? Her iki ATM de parayı verir ve hesap -100 TL'ye düşer ya da banka havadan 100 TL kaybetmiş olur. İşte sistemlerin bu şekilde "kim önce bitirecek" yarışına girmesi ve beklenmeyen sonuçlar doğurması durumuna Race Condition denir.

---

## **2. Race Condition Nedir ve Nasıl Oluşur?**

Race Condition, iki veya daha fazla iş parçacığının (thread/process) aynı paylaşılan kaynağa (veri tabanı satırı, dosya, bellek adresi) aynı anda erişmeye çalışması ve bu kaynağın nihai durumunun, işlemlerin tamamlanma sırasına bağlı olarak değişmesiyle ortaya çıkar.

Siber güvenlik dünyasında bu zafiyet genellikle **TOCTOU (Time of Check to Time of Use - Kontrol Zamanı ile Kullanım Zamanı)** olarak adlandırılan bir zaman boşluğundan beslenir. Yazılım, bir işlemi yapmadan önce bir koşulu kontrol eder (Check) ve ardından işlemi gerçekleştirir (Use). Eşzamanlı sistemlerde, "kontrol" ile "kullanım" arasındaki o mikro saniyelik zaman diliminde araya başka bir işlem girerse, güvenlik kontrolleri tamamen bypass edilebilir.

---

## **3. Mermaid ile Race Condition Akışı**

Aşağıdaki diyagramda, bir saldırganın aynı anda başlattığı iki satın alma isteğiyle sistemi nasıl manipüle ettiği gösterilmektedir:

![Diyagram / Diagram](/img/mermaid-race-condition-1-d4331d33.svg)

---

## **4. Gerçek Hayattan Senaryolar ve Siber Güvenlik Etkileri**

Race Condition zafiyetleri genellikle aşağıdaki alanlarda yıkıcı sonuçlar doğurur:

1. **Finansal Mantık Hataları (Business Logic Flaws):** Para transferleri, hediye kartı/kupon kullanımları veya dijital cüzdan harcamaları. Bir kupon kodunu aynı anda yüzlerce kez göndererek tek kullanımlık kuponla binlerce liralık alışveriş yapmak klasik bir web race condition saldırısıdır.
2. **Yetki Yükseltme (Privilege Escalation):** Çoklu oturum açma (OAuth) veya geçici şifre (OTP) doğrulama süreçlerinde, doğrulama kodu kontrol edilirken eşzamanlı isteklerle sistemin doğrulanmış durumunu manipüle ederek başka kullanıcıların hesaplarına sızmak mümkündür.
3. **Dosya Sistemi Saldırıları:** Unix tabanlı sistemlerde, bir dosyanın varlığı kontrol edildikten hemen sonra ama yazılmadan hemen önce dosya yolunun sembolik bir bağ (symlink) ile sistemdeki kritik bir dosyaya (örn: `/etc/passwd`) yönlendirilmesi.

---

## **5. Race Condition Nasıl Önlenir?**

Bu zafiyeti önlemenin yolu, eşzamanlılığı tamamen kapatmak değil, paylaşılan kaynaklara erişimi güvenli hale getirmektir (Thread-Safety).

* **Veritabanı Kilitleme (Database Locking):** İlgili veritabanı satırı kontrol edilirken kilitlenmelidir. PostgreSQL veya MySQL'de `SELECT ... FOR UPDATE` ifadesi kullanılarak, işlem bitene kadar diğer isteklerin o satırı okuması veya yazması engellenir.
* **Mutex ve Kilitleme Mekanizmaları:** Kod düzeyinde, kritik bölümlere (critical sections) aynı anda sadece tek bir iş parçacığının girmesine izin veren kilitler (mutex, semaphore) kullanılmalıdır.
* **Atomik İşlemler (Atomic Operations):** Kontrol ve kullanım adımları tek bir bölünmez (atomic) işlem haline getirilmelidir. Örneğin, bakiyeyi kontrol edip sonra düşürmek yerine, veritabanında tek bir `UPDATE cüzdan SET bakiye = bakiye - 100 WHERE id = 1 AND bakiye >= 100` sorgusu çalıştırmak işlemi güvenli kılar.
* **İstek Hız Sınırlandırması (Rate Limiting):** Aynı kullanıcının milisaniyeler içinde yüzlerce istek göndermesini engelleyen WAF veya API Gateway kuralları uygulamak, kaba kuvvetle tetiklenen yarış durumlarının önüne geçer.

---

# Race Condition

### English

## **1. Introduction: The Importance of Time and Ordering**

To provide quick responses to users, modern software applications execute multiple tasks simultaneously (concurrency). However, this speed and parallel processing power bring along synchronization challenges that are difficult to manage. One of the most silent and dangerous among these is the **Race Condition** vulnerability.

Let's use a simple analogy: Imagine a shared bank account containing only $100. Two different people try to withdraw $100 from two separate ATMs at the exact same millisecond. What happens if the system responds to both ATMs at the same time saying "Yes, there is $100 in the account"? Both ATMs dispense the money, and either the account drops to -$100 or the bank loses $100 out of thin air. This situation, where processes compete in a "who will finish first" race and produce unexpected outcomes, is called a Race Condition.

---

## **2. What is a Race Condition and How Does it Occur?**

A Race Condition occurs when two or more threads or processes attempt to access the same shared resource (a database row, a file, a memory address) at the same time, and the final state of that resource depends on the order in which the operations complete.

In the cybersecurity world, this vulnerability usually feeds on a time window known as **TOCTOU (Time of Check to Time of Use)**. The software checks a condition (Check) before performing an action (Use). In concurrent systems, if another process slips in during that microsecond gap between the "check" and the "use," security controls can be bypassed entirely.

---

## **3. Visualizing Race Condition Flows**

The following diagram illustrates how an attacker can manipulate a system using two purchase requests triggered at the exact same time:

![Diyagram / Diagram](/img/mermaid-race-condition-2-2a009799.svg)

---

## **4. Real-World Scenarios and Cybersecurity Impact**

Race Condition vulnerabilities often lead to devastating outcomes in the following areas:

1. **Business Logic Flaws:** Financial transfers, gift card/coupon redemptions, or digital wallet spending. Sending a single-use coupon code hundreds of times simultaneously to buy thousands of dollars worth of goods is a classic web race condition exploit.
2. **Privilege Escalation:** In multi-factor authentication (MFA), single sign-on (OAuth), or one-time password (OTP) verification processes, attackers can compromise other users' accounts by sending concurrent requests to manipulate the authenticated state during verification checks.
3. **File System Attacks:** In Unix-based systems, immediately after checking a file's existence but before writing to it, an attacker can replace the file path with a symbolic link (symlink) pointing to a critical system file (e.g., `/etc/passwd`).

---

## **5. How to Prevent Race Conditions**

The solution to preventing this vulnerability is not to disable concurrency entirely, but to make access to shared resources secure (Thread-Safety).

* **Database Locking:** The relevant database row must be locked during verification. In PostgreSQL or MySQL, using `SELECT ... FOR UPDATE` prevents other requests from reading or writing to that row until the transaction finishes.
* **Mutexes and Locking Mechanisms:** At the code level, locks (mutexes, semaphores) should be used to allow only one thread to enter a critical section at a time.
* **Atomic Operations:** The verification (Check) and execution (Use) steps must be combined into a single, indivisible (atomic) operation. For example, instead of checking the balance and then deducting it, executing a single update query like `UPDATE wallet SET balance = balance - 100 WHERE id = 1 AND balance >= 100` makes the transaction secure.
* **Rate Limiting:** Applying Web Application Firewall (WAF) or API Gateway rules to prevent a user from sending hundreds of requests within milliseconds stops brute-force concurrency attacks before they can exploit a race condition.

---
*This post is linked to the Knowledge Base: [[Knowledge Base / Race-Condition-Vulnerability]]*
