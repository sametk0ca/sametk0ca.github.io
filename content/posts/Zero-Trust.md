---
title: "Zero Trust"
date: 2026-01-04
draft: false
tags: ["Security Architecture", "Network Security"]
categories: ["Writeups"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:700/0*nb18LJob45T401tt.jpeg"
    alt: "Zero Trust"
    relative: false
---
![](https://miro.medium.com/v2/resize:fit:700/0*nb18LJob45T401tt.jpeg)

“Zero Trust” (Sıfır Güven) modeli, günümüzde güvenlik alanında öne çıkan, güvenlik önlemlerini yalnızca ağın sınırında almak yerine tüm sistemde sıkı bir şekilde uygulayan bir yaklaşımdır. Bu modelde, hem kurum içinden hem de dışından gelen tüm erişim talepleri için sürekli kimlik doğrulaması yapılır. Zero Trust’ın temel prensibi, **“Asla güvenme, daima doğrula”** anlayışına dayanır. Yani, kimseye — içeriden veya dışarıdan — otomatik olarak güven duyulmaz; herkesin erişim talebi önce doğrulama sürecinden geçer.


![](https://miro.medium.com/v2/resize:fit:700/0*YXSoQ-LddcoO739X.jpg)

**Zero Trust’ın Temel Bileşenleri**  
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


![](https://miro.medium.com/v2/resize:fit:700/1*kwIcOhUXQDi6uRZ3Psfm0g.png)

**Zero Trust Modelinin Faydaları**  
Zero Trust modelinin uygulanması, birçok saldırı türünü engeller ve hassas verilere erişimi ciddi anlamda koruma altına alır.

- **Fidye Yazılımı (Ransomware) Saldırılarının Engellenmesi**: Bir kullanıcı zararlı bir bağlantıya tıklayıp fidye yazılımı indirse bile, saldırı tüm ağa yayılamaz. Ağın segmentasyonu sayesinde saldırı, sadece kullanıcının segmentinde kısıtlanır.
- **İçeriden Gelen Tehditlerin Kontrolü**: Zero Trust ile içeriden gelen tehditler de sürekli doğrulamaya tabi tutulduğu için, içeride bir kötü niyetli çalışan veya güvenlik açığı yaratan bir davranış tespit edilmesi daha kolaydır. Örneğin, sistem verilerine sürekli olarak yetkisiz erişim taleplerinin gelmesi durumunda sistem alarmlarını aktive eder.

Bu model özellikle bulut sistemlerinde güvenliği artırmak ve veri ihlallerini önlemek için kritik öneme sahiptir.


The “Zero Trust” model is a prominent security approach today that enforces strict security controls throughout the entire system, rather than only at the network perimeter. In this model, all access requests, whether from inside or outside the organization, are continuously authenticated. The core principle of Zero Trust is **”Never trust, always verify.”** In other words, no one — whether internal or external — is automatically trusted, and everyone’s access request must go through verification.


![](https://miro.medium.com/v2/resize:fit:700/0*YXSoQ-LddcoO739X.jpg)

**Key Components of Zero Trust**  
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


![](https://miro.medium.com/v2/resize:fit:700/1*kwIcOhUXQDi6uRZ3Psfm0g.png)

**Benefits of the Zero Trust Model and Examples**  
Implementing Zero Trust helps prevent many types of attacks and provides substantial protection for sensitive data.

- **Blocking Ransomware Attacks**: If a user clicks a malicious link and downloads ransomware, the attack cannot spread throughout the entire network. Thanks to network segmentation, the attack is contained within the user’s segment.
- **Controlling Insider Threats**: With Zero Trust, insider threats are continuously verified, making it easier to detect malicious employees or behaviors that create security risks. For example, if unauthorized access attempts are consistently made to system data, the system raises alarms.

This model is especially critical for enhancing security in cloud environments and preventing data breaches.