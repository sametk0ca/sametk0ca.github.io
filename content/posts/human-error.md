---
title: "Human Error"
date: 2026-06-14
description: "Siber güvenlikteki insan hatalarının arkasındaki psikolojik ve sistemsel nedenler, İsviçre Peyniri Modeli ve hızlı/yavaş düşünme teorisi. / The psychological and systemic factors behind human errors in cybersecurity, the Swiss Cheese Model, and fast/slow thinking theory."
tags: ["Human Factors", "Security Awareness", "Psychology", "Security Hygiene"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: true
cover:
    image: "https://images.unsplash.com/photo-1541746972996-4e0b0f43e02a?q=80&w=1200&auto=format&fit=crop"
    alt: "Workplace pressure, human decisions, and cybersecurity errors"
    relative: false
---

## Türkçe (TR)

### Giriş
Siber güvenlik dünyasında çok bilinen bir klişe vardır: *"Sistemlerin en zayıf halkası insandır."* Şirketler güvenlik ihlallerinden sonra genellikle faturayı bir çalışanın dikkatsizliğine keser, "Kullanıcı oltalama linkine tıklamış, ne yapabilirdik ki?" diyerek işin içinden çıkarlar. Ancak insan faktörleri (human factors) bilimi bize durumun hiç de bu kadar basit olmadığını gösteriyor. İnsanların yaptığı hatalar genellikle öngörülebilir, kaçınılmaz ve aslında sistem tasarımlarındaki daha derin kusurların birer sonucudur. Yani insan en zayıf halka değil, genellikle kötü tasarlanmış sistemlerin en son ve en savunmasız kurbanıdır.

### İsviçre Peyniri Modeli ve Hata Türleri
Bir siber güvenlik kazası, genellikle tek bir kişinin hatasından dolayı yaşanmaz. James Reason tarafından geliştirilen **İsviçre Peyniri Modeli**, savunma katmanlarındaki farklı zafiyet "delikleri" üst üste denk geldiğinde kazanın gerçekleştiğini savunur:
*   **Gizli Hatalar (Latent Failures)**: Organizasyonel veya sistemsel eksikliklerdir. Yetersiz eğitim, kısıtlayıcı bütçeler, aşırı iş yükü veya kullanılması zor güvenlik yazılımları gibi arka planda bekleyen durumlardır.
*   **Aktif Hatalar (Active Failures)**: Bir çalışanın o an yaptığı yanlış bir eylemdir. (Örn: Gelen sahte maile tıklamak veya yanlış sunucu ayarı yapmak).

Sistemde gizli hatalar (delikler) olmasa, tek bir aktif hata (bir çalışanın tıklaması) savunmanın diğer katmanları (e-posta filtresi, antivirüs vb.) tarafından engellenebilir. Kazalar, tüm bu delikler hizalandığında meydana gelir.

![Diyagram / Diagram](/img/mermaid-human-error-1-256face6.svg)

### Hızlı ve Yavaş Düşünme: Kahneman Teorisi
Daniel Kahneman'ın ünlü "Hızlı ve Yavaş Düşünme" teorisi, siber güvenlik davranışlarını anlamak için mükemmel bir araçtır:
*   **Sistem 1 (Hızlı Düşünme)**: Otomatik, hızlı, rutin ve çaba gerektirmeyen düşünme biçimidir. Günlük işlerimizin %90'ını bu modda yaparız. Sürekli e-posta yanıtlayan bir çalışan, Sistem 1 modundadır ve gelen her e-postadaki gönderici adresini veya kilit simgesini detaylıca denetlemez.
*   **Sistem 2 (Yavaş Düşünme)**: Bilinçli, odaklanmış ve çaba gerektiren mantıksal süreçlerdir.

Siber güvenlik ekipleri genellikle kullanıcılara sürekli *"Dur ve Düşün!"* uyarısı yapar. Ancak günde 100 e-posta alan bir çalışandan her tıklamada Sistem 2'yi devreye sokmasını istemek biyolojik ve psikolojik olarak imkansızdır. Eğer güvenlik önlemleri işin yapılmasını çok zorlaştırıyorsa, çalışanlar işi yetiştirmek için güvenlik kurallarını esneteceklerdir (**Kural Bükme - Rule-Bending**).

### Çözüm ve Öneriler: İnsancıl Siber Güvenlik
Kullanıcıları cezalandırmak yerine, güvenliği insana uygun hale getirmeliyiz:
1.  **Uygulanamayacak Politikalar Yazmayın**: Eğer bir şifre politikası 20 karakterli, her ay değişen ve içinde emoji barındıran şifreler istiyorsa, çalışanlar bu şifreyi post-it kağıdına yazıp monitöre yapıştıracaktır. Bu bir kullanıcı hatası değil, tasarım hatasıdır.
2.  **Teknik Koruma Ağını Güçlendirin**: Kullanıcıların hata yapabileceğini kabul edin. E-posta ağ geçitlerinde DMARC ve SPF doğrulamalarını sıkılaştırarak sahte e-postaların daha kullanıcıya ulaşmadan filtrelenmesini sağlayın.
3.  **Hatalara Öğrenme Fırsatı Olarak Bakın**: Bir çalışan oltalama testinde başarısız olduğunda onu cezalandırmak, gelecekte gerçek bir hacklenme durumunu yönetimden gizlemesine yol açar. Hataları ve "ramak kala" (near-miss) olayları sistemsel iyileştirme için analiz edin.

---

## English (EN)

### Introduction
There is a persistent cliché in the cybersecurity world: *"Human is the weakest link in the security chain."* Following a major security breach, organizations frequently blame the disaster on a single employee's oversight: "The user clicked a phishing link, what could we do?" However, the science of human factors reveals that human errors are rarely spontaneous or isolated. Instead, they are predictable, inevitable, and almost always the symptom of systemic flaws in system design. The human is not the weakest link; they are simply the last and most vulnerable victim of a poorly designed system.

### The Swiss Cheese Model and Error Types
A cybersecurity incident is rarely caused by a single person making a single mistake. James Reason's famous **Swiss Cheese Model** suggests that defensive systems are like slices of Swiss cheese, each containing various "holes" (vulnerabilities). An incident occurs only when the holes in these successive defensive layers align, allowing a threat to slip through:
*   **Latent Failures**: These are organizational or workplace conditions. Poor system design, high workload, inadequate training, or exhausting security policies are latent issues waiting to trigger a mistake.
*   **Active Failures**: This is the immediate mistake made by an individual, such as clicking a malicious link or misconfiguring a database port.

If the system has no latent failures, a single active failure (e.g., clicking a link) is stopped by other defensive layers (like email filters or endpoint protection). The breach only happens when all these holes align.

![Diyagram / Diagram](/img/mermaid-human-error-2-645b108e.svg)

### Thinking Fast and Slow: Kahneman's Theory
Daniel Kahneman's pioneering "Thinking, Fast and Slow" framework is a powerful tool for analyzing security behaviors:
*   **System 1 (Fast)**: Automatic, rapid, emotional, and efficient. We run 90% of our daily tasks on System 1. An employee managing a constant stream of emails relies on System 1, meaning they do not inspect sender domains or lock icons on every incoming message.
*   **System 2 (Slow)**: Conscious, step-by-step, analytical, and effortful.

Security teams often demand that users *"Stop and Think!"* before every action. However, demanding System 2 cognitive effort for every email click is unrealistic and fatigue-inducing. If security checks disrupt primary tasks, users will resort to **Rule-Bending**—finding workarounds like "Shadow IT" to keep up productivity.

### Recommendations for Human-Centric Security
Instead of punishing users, we must adapt security to fit human behavior:
1.  **Do Not Create Unenforceable Policies**: If a password policy requires a 20-character password changed monthly, users will write it on a sticky note and paste it to their monitors. This is a design failure, not a user failure.
2.  **Strengthen Technical Safety Nets**: Accept that humans will make mistakes. Harden email gateways using strict DMARC, DKIM, and SPF validation to filter out phishing messages before they ever reach the user's inbox.
3.  **Treat Mistakes as Data**: Punishing employees who fail phishing simulations teaches them to hide real incidents out of fear. Investigate near-misses as symptoms of latent system failures that need to be resolved, not as people who need to be disciplined.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / human-error]]*
