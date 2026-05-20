+++
title = "XSS Önleme ve Sanitization"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

Cross-Site Scripting (XSS), saldırganın web sayfalarına istemci taraflı scriptler (genellikle JavaScript) enjekte etmesine olanak tanıyan bir zafiyettir.

### Özet
XSS'i önlemenin temel mantığı, kullanıcıdan gelen veriyi asla doğrudan HTML içeriği olarak "yorumlamamak" ve veriyi görüntülemeden önce uygun şekilde temizlemektir.

### Teknik Detaylar
- **Output Encoding:** HTML, JavaScript, CSS ve URL bağlamlarına göre veriyi kodlayın (örn: `<` -> `&lt;`).
- **Sanitization:** Tehlikeli HTML etiketlerini ve özelliklerini (örn: `<script>`, `onerror`) güvenli bir kütüphane kullanarak temizleyin.
- **CSP (Content Security Policy):** Tarayıcıya hangi kaynaklardan script yüklenebileceğini söyleyen bir güvenlik katmanıdır.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Context-Aware Encoding:** Verinin nereye yazılacağına göre (HTML gövdesi, öznitelik, script bloğu) farklı kodlama metodları kullanın.
- **Modern Frameworks:** React, Angular gibi frameworkler varsayılan olarak birçok XSS türüne karşı koruma sağlar.
- **HttpOnly Cookies:** Session ID gibi hassas çerezleri JavaScript erişimine kapatın.