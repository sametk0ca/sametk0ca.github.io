+++
title = "Bash Scripting"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Programming"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Bash (Bourne Again SHell), Linux ve Unix sistemlerde varsayılan komut satırı yorumlayıcısı ve güçlü bir otomasyon aracıdır.

### Özet
Sistem yönetimi, rutin işlerin otomasyonu ve siber güvenlikte "post-exploitation" (sızma sonrası) süreçlerinde temel yetkinliklerden biridir.

### Teknik Detaylar
- **Pipes (|):** Bir komutun çıktısını diğerine girdi olarak göndererek karmaşık işlemleri basitleştirir.
- **Variables & Loops:** Koşullu ifadeler ve döngülerle güçlü otomasyon senaryoları yazılabilir.
- **System Calls:** İşletim sistemi fonksiyonlarına doğrudan erişim sağlar.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Quoting:** Değişkenleri her zaman tırnak içine alın (`"$VAR"`), aksi takdirde boşluklu veriler beklenmedik sonuçlara yol açabilir.
- **Set Flags:** Betiğin başında `set -e` (hata anında dur) ve `set -u` (tanımsız değişken hatası ver) gibi bayraklar kullanın.
- **Güvenli Temp Dosyaları:** Geçici dosyalar oluştururken tahmin edilebilir isimler yerine `mktemp` kullanın.