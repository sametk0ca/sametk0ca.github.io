+++
title = "Linux Kernel ve Dağıtımlar - Teknik Mimari"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "OS"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Linux sistemi iki ana bölgeden oluşur: **User Space** (Kullanıcı Alanı) ve **Kernel Space** (Çekirdek Alanı).

### 1. User Space vs. Kernel Space
- **User Space:** Tarayıcı, metin düzenleyici veya oyun gibi sizin çalıştırdığınız tüm uygulamalar burada çalışır. Bu alanın donanıma (RAM, Disk) doğrudan erişimi yoktur.
- **Kernel Space:** İşletim sisteminin kalbi buradadır. Donanıma tam erişimi vardır. 
- **Security:** Eğer bir uygulama bir dosyayı okumak veya ağdan paket göndermek isterse, kernel'e bir "rica" (Sistem Çağrısı - Syscall) gönderir. Kernel bu isteği kontrol eder ve izin verirse işlemi yapar.

### 2. Syscalls (Sistem Çağrıları)
Bir uygulama ile kernel arasındaki iletişim dilidir. `open()`, `read()`, `write()`, `execve()` gibi yüzlerce çağrı vardır.
- **Analiz:** `strace` gibi bir araçla bir programın hangi sistem çağrılarını yaptığını izleyerek, o programın arka planda ne yaptığını (Hangi dosyayı açtı? Nereye bağlandı?) görebilirsiniz.

### 3. Kernel Modülleri (LKM)
Linux çekirdeği esnektir. Yeni donanım sürücüleri veya özellikler sistemi kapatmadan kernel'e "modül" olarak eklenebilir.
- **Risk (Rootkit):** Bir saldırgan root yetkisi aldığında, kernel'e "LKM Rootkit" yükleyebilir. Bu rootkit, kernel seviyesinde çalıştığı için kendini dosya listesinde veya süreç listesinde gizleyebilir. Sistemdeki hiçbir antivirüs bunu göremez çünkü antivirüs de kernel'den bilgi alır.

### 4. Dağıtımların Güvenlik Yaklaşımları
- **Kali Linux:** Savunma için değil, saldırı için tasarlanmıştır. Varsayılan olarak pek çok güvenlik özelliği (örneğin firewall) kapalı gelebilir.
- **RHEL / CentOS:** Kurumsal odaklıdır. `SELinux` varsayılan olarak açık ve katı kurallarla gelir.
- **Tails:** Gizlilik odaklıdır. Tüm trafiği Tor üzerinden geçirir ve bilgisayarı kapattığınızda RAM dahil her şeyi temizler (Anti-forensics).