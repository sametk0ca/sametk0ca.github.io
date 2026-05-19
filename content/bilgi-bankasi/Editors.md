+++
title = "Editörler (Vim, Nano, Emacs)"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "bilgi-bankasi"
+++

CLI (Komut Satırı Arayüzü) tabanlı metin editörleri, sistem yönetimi ve hızlı dosya düzenleme işlemleri için temel araçlardır.

### Özet
Bir sunucuya SSH ile bağlandığınızda veya kısıtlı bir ortamda çalıştığınızda, grafik arayüzlü editörler (VS Code gibi) yerine terminal üzerinden çalışan bu araçları kullanmak zorunluluk haline gelir.

### Teknik Detaylar
- **Vim:** "Modal" yapısı ile (Normal, Insert, Visual modları) çok hızlı metin düzenleme imkanı sunar, ancak öğrenme eğrisi yüksektir.
- **Nano:** Kullanıcı dostu ve basit bir arayüze sahiptir; temel düzenlemeler için idealdir.
- **Emacs:** Sadece bir editör değil, içinde kendi ekosistemini barındıran devasa bir araçtır.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Sudo Kullanımı:** Bir dosyayı düzenlerken `sudo vim` yerine `sudoedit` kullanmak daha güvenlidir; çünkü bu sayede editör root haklarıyla değil, kullanıcı haklarıyla çalışır ve sadece dosya güncellenir.
- **Plugin Güvenliği:** Editörlerinize kurduğunuz eklentilerin kaynağına dikkat edin.
- **Swap Dosyaları:** Vim gibi editörlerin oluşturduğu geçici swap dosyalarını hassas veri içeren dosyalarda düzenleme yaptıktan sonra temizlediğinizden emin olun.