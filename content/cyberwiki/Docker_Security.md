+++
title = "Docker Güvenliği ve Hardening | Docker Security and Hardening"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Docker güvenliği, konteynerize edilmiş uygulamaların izolasyonunu sağlamak ve ana makine (host) ile diğer konteynerleri korumak için alınan önlemler bütünüdür.

### Özet
Konteynerler, sanal makineler kadar güçlü bir izolasyon sunmazlar. Bu nedenle, Docker daemon yapılandırmasından imaj seçimine kadar her adımda güvenlik sıkılaştırması (hardening) yapılması kritiktir.

### Teknik Detaylar
- **Namespace & Cgroups:** Konteynerlerin kaynak erişimini ve görünürlüğünü kısıtlayan Linux kernel özellikleridir.
- **Rootless Mode:** Docker daemon'ın root yetkisi olmadan çalıştırılması.
- **Seccomp & AppArmor:** Konteynerin yapabileceği sistem çağrılarını (syscalls) kısıtlayan güvenlik profilleri.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **User Directive:** Konteyner içinde asla root kullanıcısını kullanmayın; `USER node` veya benzeri bir komutla yetkisiz kullanıcıya geçin.
- **Minimal Base Images:** Saldırı yüzeyini küçültmek için `alpine` veya `distroless` imajlarını tercih edin.
- **ReadOnly Filesystem:** Konteynerin dosya sistemini sadece okunur (`--read-only`) yaparak saldırganın dosya yazmasını engelleyin.

---

## English Version

Docker security is a set of measures taken to ensure the isolation of containerized applications and to protect the host and other containers.

### Summary
Containers do not offer as strong isolation as virtual machines. Therefore, it is critical to harden security at every step, from Docker daemon configuration to image selection.

### Technical Details
- **Namespace & Cgroups:** These are Linux kernel features that restrict resource access and visibility of containers.
- **Rootless Mode:** Running the Docker daemon without root privileges.
- **Seccomp & AppArmor:** Security profiles that restrict the system calls (syscalls) the container can make.

### Security Approach and Best Practices
- **User Directive:** Never use root user inside the container; Switch to unauthorized user with `USER node` or similar command.
- **Minimal Base Images:** Choose 'alpine' or 'distroless' images to reduce the attack surface.
- **ReadOnly Filesystem:** Make the container's file system read-only (`--read-only`), preventing the attacker from writing files.
