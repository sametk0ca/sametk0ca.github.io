+++
title = "SQL Injection Önleme Teknikleri"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

SQL Injection (SQLi), web uygulamalarındaki veritabanı sorgularına kötü niyetli kodların enjekte edilmesiyle oluşan kritik bir zafiyettir.

### Özet
SQLi'yi önlemenin en etkili yolu, kullanıcıdan alınan girdilerin sorgu komutu olarak algılanmasını engellemektir. Bu, verinin ve kodun birbirinden net bir şekilde ayrılmasıyla sağlanır.

### Teknik Detaylar
- **Prepared Statements (Parametrizasyon):** Sorgu şablonu ve veri ayrı gönderilir. Veritabanı motoru veriyi asla kod olarak çalıştırmaz.
- **Stored Procedures:** Veritabanı tarafında tanımlanmış prosedürler kullanılır.
- **Allow-listing:** Girdilerin sadece beklenen karakterleri içermesine izin verilir.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Asla String Concatenation Yapmayın:** Sorguları `query = "SELECT * FROM users WHERE id = " + id` şeklinde birleştirmeyin.
- **ORM Kullanımı:** Django ORM, Entity Framework gibi modern araçlar varsayılan olarak SQLi koruması sağlar (dikkatli kullanıldığında).
- **Least Privilege:** Veritabanı kullanıcısına sadece gerekli yetkileri (örn: sadece SELECT) verin.