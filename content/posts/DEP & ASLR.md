---
title: "DEP & ASLR: What Are They?"
date: 2026-01-04
draft: false
tags: ["Exploit Mitigation", "Memory Safety", "Red Team"]
categories: ["Writeups"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:512/1*w6iEx4Wt25EiEc0nb1bZ1Q.png"
    alt: "DEP & ASLR"
    relative: false
---
![](https://miro.medium.com/v2/resize:fit:512/1*w6iEx4Wt25EiEc0nb1bZ1Q.png)

## DEP ve ASLR Nedir? Siber Güvenlikte Neden Önemlidir?

Bilgisayar güvenliği denildiğinde akla gelen en önemli kavramlardan biri bellek güvenliğidir. İşte tam da burada **DEP (Data Execution Prevention — Veri Yürütme Engelleme)** ve **ASLR (Address Space Layout Randomization — Adres Alanı Düzeni Rastgeleleştirme)** devreye girer. Peki, bu iki güvenlik mekanizması tam olarak ne işe yarar? Hacker’ların işini nasıl zorlaştırır? Hadi birlikte inceleyelim.



![](https://miro.medium.com/v2/resize:fit:700/1*NuvIvbJc7L8mx__38yuAew.jpeg)

## DEP: Kod Çalıştırmaya Karşı Koruma

DEP, sistemdeki belirli bellek bölgelerinin çalıştırılabilir (executable) olmasını engelleyen bir güvenlik önlemidir. Normalde kodlar, çalıştırılabilir bellek bölgelerinde tutulur, ancak kötü amaçlı yazılımlar genellikle bir programın **veri bölgesine kötü niyetli kod enjekte edip çalıştırmaya çalışır.**

DEP, **yığın (stack)** ve **yığın dışı bellek bölgelerinin (heap)** yürütülmesini engelleyerek bu tür saldırıları önler. Eğer bir saldırgan, bu bölgelerde kötü amaçlı kod çalıştırmaya kalkarsa, DEP devreye girer ve programı çökerterek saldırının başarılı olmasını engeller.

## Özetle DEP:

✅ Belleğin yalnızca izin verilen bölgelerde kod çalıştırmasına izin verir.  
✅ Veri olarak tanımlanmış bellek bölgelerinin yürütülmesini engeller.  
✅ Buffer Overflow gibi saldırılara karşı koruma sağlar.



![](https://miro.medium.com/v2/resize:fit:700/1*irRMt483WT83lb08WUYOcA.png)

## ASLR: Bellek Adreslerini Karıştırmak

ASLR, sistemde çalışan programların bellek adreslerini **rastgele hale getirerek** saldırganların kötü amaçlı kodlarını doğru bir şekilde yerleştirmesini zorlaştırır.

Örneğin, bir saldırganın bir programın hafızasında **hangi adrese saldırması gerektiğini bilmesi gerekir.** ASLR devrede olduğunda, her programın bellek yerleşimi her başlatıldığında değişir. Yani, saldırganın önce doğru bellek adreslerini bulması gerekir ki bu da saldırıyı **çok daha zor hale getirir.**

## Özetle ASLR:

✅ Programların hafızada her seferinde farklı adreslerde çalışmasını sağlar.  
✅ Saldırganların bellek adreslerini tahmin etmesini zorlaştırır.  
✅ ROP (Return Oriented Programming) gibi saldırıları önlemeye yardımcı olur.

## Peki, DEP ve ASLR Kırılabilir mi?

Evet, ne yazık ki bu iki güvenlik önlemi **kusursuz değil.** Saldırganlar **ROP (Return-Oriented Programming)** veya **ASLR bypass teknikleri** gibi yöntemlerle bu önlemleri aşmaya çalışabilir. Ancak DEP ve ASLR birlikte kullanıldığında, saldırganın işi **çok daha zor hale gelir.**


**Sonuç olarak:** Eğer bir yazılım geliştiriciyseniz veya güvenlik alanında çalışıyorsanız, **DEP ve ASLR’nin aktif olduğundan emin olun.** Günümüz saldırılarının büyük bir kısmı, bu önlemler devrede değilken başarılı olur.

![](https://miro.medium.com/v2/resize:fit:512/1*w6iEx4Wt25EiEc0nb1bZ1Q.png)

## What Are DEP and ASLR? Why Are They Important in Cybersecurity?

When we talk about computer security, one of the most important topics is **memory protection**. This is where **DEP (Data Execution Prevention)** and **ASLR (Address Space Layout Randomization)** come into play. But what exactly do these security mechanisms do? How do they make a hacker’s job harder? Let’s dive in.



![](https://miro.medium.com/v2/resize:fit:700/1*NuvIvbJc7L8mx__38yuAew.jpeg)

## DEP: Protection Against Malicious Code Execution

DEP is a security mechanism that prevents certain memory regions from being executable. Normally, executable code is stored in specific areas of memory. However, **malware often tries to inject and execute malicious code in non-executable data regions**.

DEP **blocks execution in the stack and heap memory regions**, preventing this type of attack. If an attacker tries to run malicious code in these regions, DEP **crashes the program, stopping the attack.**

## In Summary, DEP:

✅ Ensures that only designated memory regions can execute code.  
✅ Prevents execution in data-marked memory areas.  
✅ Protects against Buffer Overflow attacks.



![](https://miro.medium.com/v2/resize:fit:700/1*irRMt483WT83lb08WUYOcA.png)

## ASLR: Randomizing Memory Addresses

ASLR **randomizes memory locations** used by programs, making it difficult for attackers to predict where to place their malicious code.

For an attack to succeed, the hacker **must know the exact memory address to target**. With ASLR enabled, every time a program runs, **its memory layout is different**. This makes it much harder for attackers to exploit vulnerabilities.

## In Summary, ASLR:

✅ Ensures that programs run at different memory locations each time.  
✅ Makes it harder for attackers to guess memory addresses.  
✅ Helps mitigate Return-Oriented Programming (ROP) attacks.

## Can DEP and ASLR Be Bypassed?

Yes, unfortunately, these security measures **are not perfect**. Attackers use techniques like **ROP (Return-Oriented Programming)** and **ASLR bypass methods** to circumvent these protections. However, when DEP and ASLR are **used together, it makes attacks significantly more difficult.**

**Bottom line:** If you’re a developer or working in security, always ensure that **DEP and ASLR are enabled**. Many modern attacks succeed simply because these protections are turned off.