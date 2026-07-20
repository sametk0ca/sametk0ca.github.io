+++
title = "Linux Kernel ve Dağıtımlar - Teknik Mimari | Linux Kernel and Distributions - Technical Architecture"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

The Linux system consists of two main areas: **User Space** and **Kernel Space**.

### 1. User Space vs. Kernel Space
- **User Space:** All applications you run, such as a browser, text editor or game, run here. This area does not have direct access to hardware (RAM, Disk).
- **Kernel Space:** The heart of the operating system is here. It has full access to the hardware. 
- **Security:** If an application wants to read a file or send a packet from the network, it sends a "request" (Syscall) to the kernel. Kernel checks this request and performs the operation if allowed.

### 2. Syscalls
It is the communication language between an application and the kernel. There are hundreds of calls such as `open()`, `read()`, `write()`, `execve()`.
- **Analysis:** By monitoring which system calls a program makes with a tool like `strace`, you can see what that program is doing in the background (Which file did it open? Where did it connect?).

### 3. Kernel Modules (LKM)
The Linux kernel is flexible. New hardware drivers or features can be added to the kernel as "modules" without shutting down the system.
- **Risk (Rootkit):** When an attacker gets root permission, he can install "LKM Rootkit" into the kernel. Since this rootkit operates at the kernel level, it can hide itself in the file list or process list. No antivirus in the system can see this because the antivirus also receives information from the kernel.

### 4. Security Approaches of Distributions
- **Kali Linux:** Designed for attack, not defense. Many security features (e.g. firewall) may be disabled by default.
- **RHEL / CentOS:** Enterprise focused. `SELinux` comes with clear and strict rules by default.
- **Tails:** Privacy oriented. It passes all traffic through Tor and clears everything including RAM when you shut down the computer (Anti-forensics).
