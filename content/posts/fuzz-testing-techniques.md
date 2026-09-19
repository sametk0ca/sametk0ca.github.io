---
title: "Fuzz Testing"
date: 2026-05-19
description: "How fuzzing finds bugs with random and coverage-guided inputs: black-, white- and grey-box approaches and their challenges. / Fuzzing'in rastgele ve kapsama güdümlü girdilerle nasıl açık bulduğu: kara, beyaz ve gri kutu yaklaşımları ve zorlukları."
draft: false
tags: ["Software Security", "Bug Hunting", "Fuzzing", "CyBOK"]
categories: ["Security Testing"]
related:
  - "[[concepts/fuzz-testing-techniques|Fuzz Testing Techniques (Fuzzing)]]"
---

## 🇹🇷 Türkçe (TR)

Fuzzing veya Fuzz Testi, yazılım sistemlerindeki beklenmedik davranışları ve güvenlik açıklarını tespit etmek için kullanılan dinamik bir analiz tekniğidir. Bu yöntem, bir hedef programa büyük hacimli, rastgele veya yarı-yapılandırılmış veriler göndererek sistemin çökmesine (crash) veya anormal bir duruma geçmesine neden olan girdilerin belirlenmesine dayanır. Modern güvenlik ekosisteminde fuzzing, özellikle sıfırıncı gün (zero-day) açıklarının keşfinde kritik bir rol oynar.

### Teknik Taksonomi ve Metodolojiler

Fuzzing teknikleri, CyBOK "Software Security" alanı çerçevesinde yazılımın iç yapısına olan erişim seviyesine göre sınıflandırılır:

1. **Kara Kutu Fuzzing (Black-box Fuzzing):** Yazılımın kaynak kodu veya dahili yapısı hakkında bilgi sahibi olmadan gerçekleştirilir. Girdiler genellikle rastgele veya mutasyon tabanlıdır. Protokol fuzzing (Örn: HTTP, TLS) bu kategoride yaygındır.
2. **Beyaz Kutu Fuzzing (White-box Fuzzing):** Kaynak kod analizi ve sembolik yürütme (symbolic execution) tekniklerini kullanır. Kod kapsamını (code coverage) maksimize etmek için matematiksel modeller (SMT solver) aracılığıyla spesifik girdi yolları oluşturur.
3. **Gri Kutu Fuzzing (Grey-box Fuzzing):** En yaygın kullanılan yöntemdir. Programın yürütülmesi sırasında hafif bir geri bildirim (instrumentation) mekanizması kullanarak hangi girdilerin yeni kod dallarını tetiklediğini takip eder. AFL (American Fuzzy Lop) ve libFuzzer bu tekniğin öncü araçlarıdır.

### Standartlar ve Teknik Zorluklar

Microsoft SDL gibi güvenli yazılım geliştirme süreçleri fuzzing'i doğrulama aşamasının bir parçası olarak öngörür; Google'ın OSS-Fuzz projesi ise açık kaynak yazılımları sürekli olarak fuzz'lar. Ancak modern sistemlerin karmaşıklığı nedeniyle "Path Explosion" (yol patlaması, özellikle sembolik yürütmede) ve "Semantic Gap" (anlamsal boşluk: rastgele girdilerin çoğu yapısal doğrulamada elenir) gibi zorluklar mevcuttur. Bellek güvenliği (buffer overflow, use-after-free) açıklarını fark edilebilir hale getirmek için AddressSanitizer (ASan) gibi araçlarla birlikte kullanmak önemlidir.

---

## 🇬🇧 English (EN)

### Fuzz Testing: Automation in Software Security and Vulnerability Analysis

Fuzzing, or Fuzz Testing, is a dynamic analysis technique used to detect unexpected behaviors and security vulnerabilities in software systems. This method relies on providing a target program with a large volume of random or semi-structured data to identify inputs that cause the system to crash or enter an anomalous state. In the modern security ecosystem, fuzzing plays a critical role, particularly in the discovery of zero-day vulnerabilities.

### Technical Taxonomy and Methodologies

Fuzzing techniques are classified according to the level of access to the software's internal structure, within the framework of the CyBOK "Software Security" area:

1. **Black-box Fuzzing:** Performed without knowledge of the software's source code or internal structure. Inputs are typically random or mutation-based. Protocol fuzzing (e.g., HTTP, TLS) is common in this category.
2. **White-box Fuzzing:** Utilizes source code analysis and symbolic execution techniques. It generates specific input paths through mathematical models (SMT solvers) to maximize code coverage.
3. **Grey-box Fuzzing:** The most widely used method. It tracks which inputs trigger new code branches by using a lightweight feedback (instrumentation) mechanism during program execution. AFL (American Fuzzy Lop) and libFuzzer are pioneering tools for this technique.

### Standards and Technical Challenges

Secure development processes such as Microsoft SDL include fuzzing as part of the verification phase, and Google's OSS-Fuzz project continuously fuzzes open-source software. However, due to the complexity of modern systems, technical challenges such as "Path Explosion" (especially in symbolic execution) and the "Semantic Gap" (most random inputs are rejected by structural validation) persist. Using fuzzers together with tools like AddressSanitizer (ASan) is important for making memory safety bugs (buffer overflow, use-after-free) visible.
