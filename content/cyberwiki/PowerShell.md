+++
title = "PowerShell Scripting"
date = "2026-05-19"
draft = false
categories = ["Programming"]
type = "cyberwiki"
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

---

## English Version

PowerShell is a powerful object-oriented shell and scripting language developed by Microsoft that runs on both Windows and Linux.

### Summary
It is indispensable for system administration and security operations in the Windows ecosystem. Used heavily by both blue team (defense/tracking) and red team (offensive) teams.

### Technical Details
- **Objects vs Text:** Unlike Bash, PowerShell carries rich objects, not text, between commands.
- **Cmdlets:** Standard command structure in `Verb-Noun` format (eg: `Get-Process`).
- **.NET Integration:** It contains the power of .NET framework in its infrastructure.

### Security Approach and Best Practices
- **Execution Policy:** Configure the scripts execution policy (`Set-ExecutionPolicy`) correctly.
- **Logging:** Monitor suspicious activities by activating PowerShell's advanced logging (Script Block Logging) features.
- **Remote Security:** Prefer certificate-based authentication and HTTPS when using PowerShell Remoting (WinRM).
