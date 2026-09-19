---
title: "Formal Methods"
date: 2026-05-19
description: "How formal methods prove a system meets its specification: model checking, theorem proving, symbolic execution and seL4. / Formal metotların bir sistemin spesifikasyona uygunluğunu nasıl kanıtladığı: model denetimi, teorem kanıtlama, sembolik yürütme ve seL4."
draft: false
tags: ["Formal Methods", "Verification", "Software Security", "CyBOK"]
categories: ["Advanced Security"]
related:
  - "[[concepts/formal-methods-foundations|Formal Methods Foundations]]"
  - "[[model-checking-basics|Model Checking Basics]]"
  - "[[ka-formal-methods|CyBOK KA: Formal Methods for Security]]"
---

## 🇹🇷 Türkçe (TR)

Yazılım ve donanım sistemlerinin karmaşıklığı arttıkça, geleneksel test yöntemleri tüm olası hata durumlarını kapsamakta yetersiz kalmaktadır. **Formal Metotlar (Formal Methods)**, bir sistemin spesifikasyonlarına (tasarım özelliklerine) uygunluğunu matematiksel olarak kanıtlama sürecidir. Bu disiplin, güvenlik açısından kritik sistemlerde (havacılık, tıp, nükleer) en güçlü güvenceyi sağlayan tekniklerden biridir. Ancak kanıt, yalnızca spesifikasyonun doğru yazıldığı varsayımı altında geçerlidir; spesifikasyon hatalıysa "kanıtlanmış" bir sistem de hatalı olabilir.

### Teknik Yaklaşımlar ve Araçlar

Formal metotlar, CyBOK "Formal Methods for Security" bilgi alanı çerçevesinde üç temel kategoride incelenir:

1. **Model Denetimi (Model Checking):** Sistemin sonlu bir durum makinesi (finite state machine) olarak modellenmesi ve LTL (Linear Temporal Logic) veya CTL (Computation Tree Logic) gibi mantıksal kurallar çerçevesinde tüm olası durumların taranmasıdır. SPIN ve NuSMV bu alandaki popüler araçlardır.
2. **Teorem Kanıtlama (Theorem Proving):** Sistemin ve istenen özelliklerin matematiksel aksiyomlar olarak ifade edilmesi ve tümevarım yoluyla doğruluğunun ispatlanmasıdır. Coq, Isabelle ve PVS bu teknik için kullanılan karmaşık "proof assistant" araçlarıdır.
3. **Statik Analiz ve Sembolik Yürütme:** Kodun davranışını, programı çalıştırmadan soyutlama (abstraction) ve sembolik girdiler kullanarak analiz eder. Z3 SMT çözücü (solver) gibi araçlar, bu süreçlerin matematiksel altyapısını oluşturur.

### Standartlar ve Endüstriyel Uygulamalar

Havacılık endüstrisinde DO-178C (formal metotlar için DO-333 eki ile) ve otomotiv sektöründe ISO 26262 standartları, kritik güvenlik seviyelerindeki sistemler için formal doğrulama tekniklerinin kullanılmasına yer verir. Örneğin, seL4 mikroçekirdeği (microkernel), işlevsel doğruluğu makine denetimli matematiksel kanıtla gösterilen ilk genel amaçlı işletim sistemi çekirdeklerinden biridir ve "isolation" (izolasyon) özellikleri de kanıtlanmıştır. Bu kanıtlar donanım ve derleyici gibi belirli varsayımlara dayanır. Formal metotlar, akıllı sözleşmelerin (smart contracts) ve kriptografik protokollerin tasarımında zafiyetleri önlemek için giderek yaygınlaşan bir araçtır.

---

## 🇬🇧 English (EN)

### Formal Methods: Mathematical Rigor in Software and Hardware Security

As the complexity of software and hardware systems increases, traditional testing methods fall short of covering all possible error states. **Formal Methods** is the process of mathematically proving that a system complies with its specifications (design properties). This discipline is among the techniques that provide the strongest assurance in safety-critical systems, such as aerospace, medical, and nuclear applications. However, a proof holds only if the specification itself is correct; if the specification is wrong, a "proven" system can still be wrong.

### Technical Approaches and Tools

Formal methods are examined in three primary categories within the framework of the CyBOK "Formal Methods for Security" knowledge area:

1. **Model Checking:** Modeling the system as a finite state machine and exhaustively searching all possible states within logical rules such as LTL (Linear Temporal Logic) or CTL (Computation Tree Logic). SPIN and NuSMV are popular tools in this field.
2. **Theorem Proving:** Expressing the system and its desired properties as mathematical axioms and proving their correctness through induction. Coq, Isabelle, and PVS are sophisticated "proof assistant" tools used for this technique.
3. **Static Analysis and Symbolic Execution:** Analyzing the behavior of code without running it, using abstraction and symbolic inputs. Tools like the Z3 SMT solver form the mathematical backbone of these processes.

### Standards and Industrial Applications

Standards such as DO-178C in the aerospace industry (with its DO-333 supplement on formal methods) and ISO 26262 in the automotive sector make room for formal verification techniques in systems at critical safety levels. For instance, the seL4 microkernel is one of the first general-purpose operating system kernels whose functional correctness was shown with a machine-checked mathematical proof, and its isolation properties have been proven as well. These proofs rest on certain assumptions, such as the hardware and the compiler. Formal methods are an increasingly common tool for preventing vulnerabilities in the design of smart contracts and cryptographic protocols.
