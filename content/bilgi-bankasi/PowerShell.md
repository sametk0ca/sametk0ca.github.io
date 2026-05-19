+++
title = "PowerShell Scripting"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Programming"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

PowerShell, Microsoft tarafından geliştirilen, nesne yönelimli (object-oriented) ve hem Windows hem de Linux üzerinde çalışan güçlü bir kabuk ve betik dilidir.

### Özet
Windows ekosisteminde sistem yönetimi ve güvenlik operasyonları için vazgeçilmezdir. Hem mavi takım (savunma/izleme) hem de kırmızı takım (saldırı) ekipleri tarafından yoğun olarak kullanılır.

### Teknik Detaylar
- **Objects vs Text:** Bash'in aksine, PowerShell komutlar arasında metin değil, zengin nesneler taşır.
- **Cmdlets:** `Verb-Noun` formatındaki (örn: `Get-Process`) standart komut yapısı.
- **.NET Integration:** Alt yapısında .NET framework gücünü barındırır.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Execution Policy:** Betiklerin çalıştırılma politikasını (`Set-ExecutionPolicy`) doğru yapılandırın.
- **Logging:** PowerShell'in gelişmiş loglama (Script Block Logging) özelliklerini aktif ederek şüpheli aktiviteleri izleyin.
- **Remote Security:** PowerShell Remoting (WinRM) kullanırken sertifika tabanlı kimlik doğrulaması ve HTTPS tercih edin.