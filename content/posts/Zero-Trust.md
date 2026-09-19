---
title: "Zero Trust"
date: 2026-01-04
description: "The Zero Trust model: never trust, always verify, built on identity, device security and micro-segmentation. / Zero Trust modeli: asla güvenme, daima doğrula; kimlik, cihaz güvenliği ve mikro-segmentasyon üzerine kurulu."
draft: false
tags: ["Security Architecture", "Network Security"]
categories: ["Writeups"]
related:
  - "[[Zero_Trust|Zero Trust Architecture (Sıfır Güven Mimarisi)]]"
---

## 🇹🇷 Türkçe (TR)

“Zero Trust” (Sıfır Güven) modeli, günümüzde güvenlik alanında öne çıkan, güvenlik önlemlerini yalnızca ağın sınırında almak yerine tüm sistemde sıkı bir şekilde uygulayan bir yaklaşımdır. Bu modelde, hem kurum içinden hem de dışından gelen her erişim talebi doğrulanır ve yetkilendirilir. Zero Trust’ın temel prensibi, **“Asla güvenme, daima doğrula”** anlayışına dayanır. Yani, kimseye — içeriden veya dışarıdan — otomatik olarak güven duyulmaz; herkesin erişim talebi önce doğrulama sürecinden geçer. Modelin diğer iki dayanağı **en az yetki** (yalnızca gereken erişimi ver) ve **ihlal varsayımıdır** (saldırganın zaten içeride olabileceğini kabul ederek tasarım yap). Yaklaşımın ayrıntılı bir tanımı NIST SP 800-207 belgesinde yer alır.

### Zero Trust’ın Temel Bileşenleri

Zero Trust’ın çalışma prensiplerini daha iyi anlamak için üç ana bileşene odaklanalım:

1. **Kimlik ve Erişim Yönetimi (IAM)**:  
— Tüm kullanıcılar (çalışanlar, yükleniciler, ziyaretçiler) kimlik doğrulama sürecinden geçer. Bu süreçte çok faktörlü kimlik doğrulama (MFA) gibi yöntemler kullanılır.  
— Örnek: Bir çalışan ofisteki ağda olmasına rağmen, kritik veriye erişmeden önce kimliğini doğrulaması için ek bir şifre doğrulama ekranıyla karşılaşır.

2. **Cihaz Güvenliği**:  
— Sisteme bağlanan her cihazın güvenilir olup olmadığını kontrol eder. Güvenlik durumuna göre cihazlar sınırlı erişim seviyeleri ile ağa dahil edilebilir.  
— Örnek: Bir çalışanın kişisel cihazı, şirketteki verilere sadece kısıtlı erişimle bağlanabilir veya yalnızca internete erişebilir.

3. **Ağ Segmentasyonu ve Mikro-Segmentasyon**:  
— Ağ, belirli gruplara veya departmanlara göre bölümlere ayrılır. Böylece her bir bölümdeki veriler, sadece o bölüme yetkili olanlar tarafından erişilebilir.  
— Örnek: Şirketin finans departmanındaki dosyalar, yalnızca finans ekibindeki çalışanların erişimine açıktır. Başka bir departmandan veya dışarıdan bir erişim talebi geldiğinde, güvenlik doğrulamasından geçilmeden bu verilere ulaşılamaz.

### Zero Trust Modelinin Faydaları

Zero Trust modelinin uygulanması, saldırıların etkisini sınırlar ve hassas verilere erişimi ciddi anlamda koruma altına alır.

- **Fidye Yazılımı (Ransomware) Yayılımının Sınırlanması**: Bir kullanıcı zararlı bir bağlantıya tıklayıp fidye yazılımı indirse bile, ağın segmentasyonu sayesinde saldırının tüm ağa yayılması zorlaşır ve etki büyük ölçüde kullanıcının segmentiyle sınırlı kalır.
- **İçeriden Gelen Tehditlerin Kontrolü**: İçeriden gelen erişimler de sürekli doğrulamaya tabi tutulduğu için, kötü niyetli bir çalışanın veya riskli bir davranışın fark edilmesi daha kolaydır. Örneğin, yetkisiz erişim denemeleri tekrar tekrar geldiğinde sistem alarm üretir.

Bu model özellikle bulut sistemlerinde güvenliği artırmak ve veri ihlallerini önlemek için kritik öneme sahiptir.

---

## 🇬🇧 English (EN)

The “Zero Trust” model is a prominent security approach today that enforces strict security controls throughout the entire system, rather than only at the network perimeter. In this model, every access request, whether from inside or outside the organization, is verified and authorized. The core principle of Zero Trust is **“Never trust, always verify.”** In other words, no one — whether internal or external — is automatically trusted, and everyone’s access request must go through verification. Two further pillars are **least privilege** (grant only the access that is needed) and **assume breach** (design as if the attacker may already be inside). NIST SP 800-207 defines the approach in detail.

### Key Components of Zero Trust

To better understand how Zero Trust operates, let’s focus on three main components:

1. **Identity and Access Management (IAM)**:  
— All users (employees, contractors, visitors) must go through an authentication process. Multi-factor authentication (MFA) is one such method.  
— Example: Even though an employee is connected to the office network, they are prompted to verify their identity with an additional authentication step before accessing critical data.

2. **Device Security**:  
— Every device connecting to the system is checked for reliability. Depending on its security status, the device may be granted limited access to the network.  
— Example: An employee’s personal device may only be allowed limited access to the company network or internet access only.

3. **Network Segmentation and Micro-Segmentation**:  
— The network is divided into segments based on specific groups or departments, so that data within each segment is accessible only to those authorized for that segment.  
— Example: Files in the company’s finance department are accessible only to employees in the finance team. If another department or external party tries to access this data, they must pass security verification.

### Benefits of the Zero Trust Model

Implementing Zero Trust limits the impact of attacks and provides substantial protection for sensitive data.

- **Limiting Ransomware Spread**: If a user clicks a malicious link and downloads ransomware, network segmentation makes it much harder for the attack to spread, so the damage stays largely within the user’s segment.
- **Controlling Insider Threats**: Because internal access is continuously verified, it is easier to notice malicious employees or risky behavior. For example, if unauthorized access attempts keep coming in, the system raises alarms.

This model is especially critical for enhancing security in cloud environments and preventing data breaches.
