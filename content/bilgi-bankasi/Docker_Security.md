+++
title = "Docker Güvenliği ve Hardening"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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