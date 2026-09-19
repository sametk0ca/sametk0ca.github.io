---
title: "DEP & ASLR"
date: 2026-01-04
description: "What DEP and ASLR do, how they make memory-corruption exploits harder, and how attackers bypass them. / DEP ve ASLR'nin ne yaptığı, bellek istismarlarını nasıl zorlaştırdığı ve nasıl aşıldıkları."
draft: false
tags: ["Exploit Mitigation", "Memory Safety", "Red Team"]
categories: ["Writeups"]
related:
  - "[[software-security-mitigation-techniques|Software Security Mitigation Techniques]]"
  - "[[Buffer_Overflow|Buffer Overflow (Tampon Bellek Taşması)]]"
  - "[[os-hardening-techniques|OS Hardening Techniques]]"
---

## 🇹🇷 Türkçe (TR)

### DEP ve ASLR Nedir? Siber Güvenlikte Neden Önemlidir?

Bilgisayar güvenliği denildiğinde akla gelen en önemli kavramlardan biri bellek güvenliğidir. İşte tam da burada **DEP (Data Execution Prevention — Veri Yürütme Engelleme)** ve **ASLR (Address Space Layout Randomization — Adres Alanı Düzeni Rastgeleleştirme)** devreye girer. Peki, bu iki güvenlik mekanizması tam olarak ne işe yarar? Hacker’ların işini nasıl zorlaştırır? Hadi birlikte inceleyelim.

### DEP: Kod Çalıştırmaya Karşı Koruma

DEP, sistemdeki belirli bellek bölgelerinin çalıştırılabilir (executable) olmasını engelleyen bir güvenlik önlemidir. Normalde kodlar, çalıştırılabilir bellek bölgelerinde tutulur, ancak kötü amaçlı yazılımlar genellikle bir programın **veri bölgesine kötü niyetli kod enjekte edip çalıştırmaya çalışır.**

DEP, **yığın (stack)** ve **öbek (heap)** gibi veri bölgelerinde kod çalıştırılmasını engelleyerek bu tür saldırıları önler. Eğer bir saldırgan, bu bölgelerde kötü amaçlı kod çalıştırmaya kalkarsa, DEP devreye girer ve programı çökerterek saldırının başarılı olmasını engeller.

### Özetle DEP:

✅ Kodun yalnızca çalıştırılabilir olarak işaretlenmiş bellek bölgelerinde yürütülmesine izin verir.  
✅ Veri olarak tanımlanmış bellek bölgelerinin yürütülmesini engeller.  
✅ Buffer overflow ile enjekte edilen kodun çalışmasını engeller.

### ASLR: Bellek Adreslerini Karıştırmak

ASLR, sistemde çalışan programların bellek adreslerini **rastgele hale getirerek** saldırganların kötü amaçlı kodlarını doğru bir şekilde yerleştirmesini zorlaştırır.

Örneğin, bir saldırganın bir programın hafızasında **hangi adrese saldırması gerektiğini bilmesi gerekir.** ASLR devrede olduğunda, programın bellek yerleşimi her başlatmada (veya sistem açılışında) değişir. Yani, saldırganın önce doğru bellek adreslerini bulması gerekir ki bu da saldırıyı **çok daha zor hale getirir.**

### Özetle ASLR:

✅ Programların hafızada her seferinde farklı adreslerde çalışmasını sağlar.  
✅ Saldırganların bellek adreslerini tahmin etmesini zorlaştırır.  
✅ ROP (Return-Oriented Programming) gibi saldırıları zorlaştırır; çünkü saldırganın kullanacağı kod parçalarının adresleri önceden bilinmez.

### Peki, DEP ve ASLR Kırılabilir mi?

Evet, ne yazık ki bu iki güvenlik önlemi **kusursuz değil.** Saldırganlar DEP'i genellikle **ROP (Return-Oriented Programming)** ile, yani yeni kod enjekte etmek yerine bellekteki mevcut kod parçalarını zincirleyerek aşar. ASLR'yi ise çoğunlukla **bellek adresi sızıntıları (information leak)** ile atlatır. Ancak DEP ve ASLR birlikte kullanıldığında, saldırganın işi **çok daha zor hale gelir.**

**Sonuç olarak:** Eğer bir yazılım geliştiriciyseniz veya güvenlik alanında çalışıyorsanız, **DEP ve ASLR’nin aktif olduğundan emin olun.** Bu önlemlerin kapalı olduğu sistemlerde bellek bozulması açıklarını istismar etmek çok daha kolaydır.

---

## 🇬🇧 English (EN)

### What Are DEP and ASLR? Why Are They Important in Cybersecurity?

When we talk about computer security, one of the most important topics is **memory protection**. This is where **DEP (Data Execution Prevention)** and **ASLR (Address Space Layout Randomization)** come into play. But what exactly do these security mechanisms do? How do they make a hacker’s job harder? Let’s dive in.

### DEP: Protection Against Malicious Code Execution

DEP is a security mechanism that prevents certain memory regions from being executable. Normally, executable code is stored in specific areas of memory. However, **malware often tries to inject and execute malicious code in non-executable data regions**.

DEP **blocks execution in the stack and heap memory regions**, preventing this type of attack. If an attacker tries to run malicious code in these regions, DEP **crashes the program, stopping the attack.**

### In Summary, DEP:

✅ Ensures that only designated memory regions can execute code.  
✅ Prevents execution in data-marked memory areas.  
✅ Stops code injected through buffer overflows from running.

### ASLR: Randomizing Memory Addresses

ASLR **randomizes memory locations** used by programs, making it difficult for attackers to predict where to place their malicious code.

For an attack to succeed, the hacker **must know the exact memory address to target**. With ASLR enabled, each time a program starts (or the system boots), **its memory layout is different**. This makes it much harder for attackers to exploit vulnerabilities.

### In Summary, ASLR:

✅ Ensures that programs run at different memory locations each time.  
✅ Makes it harder for attackers to guess memory addresses.  
✅ Makes Return-Oriented Programming (ROP) attacks harder, since the addresses of the code snippets they rely on are unknown.

### Can DEP and ASLR Be Bypassed?

Yes, unfortunately, these security measures **are not perfect**. Attackers typically bypass DEP with **ROP (Return-Oriented Programming)**, chaining existing code snippets in memory instead of injecting new code, and bypass ASLR mostly through **memory address leaks (information leaks)**. However, when DEP and ASLR are **used together, attacks become significantly more difficult.**

**Bottom line:** If you’re a developer or working in security, always ensure that **DEP and ASLR are enabled**. On systems where these protections are turned off, exploiting memory-corruption bugs is far easier.
