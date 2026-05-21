+++
title = "SQL Injection Önleme Teknikleri | SQL Injection Prevention Techniques"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

SQL Injection (SQLi) is a critical vulnerability that occurs by injecting malicious code into database queries in web applications.

### Summary
The most effective way to prevent SQLi is to prevent user input from being detected as query commands. This is achieved by clearly separating data and code.

### Technical Details
- **Prepared Statements (Parametrization):** Query template and data are sent separately. The database engine never executes data as code.
- **Stored Procedures:** Procedures defined on the database side are used.
- **Allow-listing:** Entries are allowed to contain only expected characters.

### Security Approach and Best Practices
- **Never Do String Concatenation:** Do not concatenate queries as `query = "SELECT * FROM users WHERE id = " + id`.
- **ORM Usage:** Modern tools like Django ORM, Entity Framework provide SQLi protection by default (when used carefully).
- **Least Privilege:** Give only necessary privileges (eg: SELECT only) to the database user.
