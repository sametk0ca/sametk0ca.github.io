+++
title = "Editörler (Vim, Nano, Emacs) | Editors (Vim, Nano, Emacs)"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

CLI (Command Line Interface) based text editors are essential tools for system administration and quick file editing.

### Summary
When you connect to a server via SSH or work in a restricted environment, it becomes necessary to use these tools that work via the terminal instead of editors with graphical interfaces (such as VS Code).

### Technical Details
- **Vim:** It offers very fast text editing with its "Modal" structure (Normal, Insert, Visual modes), but its learning curve is high.
- **Nano:** It has a user-friendly and simple interface; Ideal for basic arrangements.
- **Emacs:** It is not just an editor, it is a huge tool that contains its own ecosystem.

### Security Approach and Best Practices
- **Sudo Usage:** It is safer to use `sudoedit` instead of `sudo vim` when editing a file; because in this way, the editor works with user rights, not root rights, and only the file is updated.
- **Plugin Security:** Pay attention to the source of the plugins you install in your editors.
- **Swap Files:** Be sure to clear the temporary swap files created by editors such as Vim after editing files containing sensitive data.
