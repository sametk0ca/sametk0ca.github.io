+++
title = "VLAN Hopping (VLAN Atlaması)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
+++

VLAN Hopping, bir saldırganın ağdaki bir sanal ağdan (VLAN) diğerine, normalde yetkisi olmadığı halde gizlice geçiş yapmasıdır.

### 1. Saldırı Mantığı
Normalde VLAN'lar birbirlerinden tamamen izoledir (ayrıdır). Ancak saldırgan, Switch'lerin (Ağ anahtarları) çalışma mantığındaki bazı açıkları kullanarak bu duvarları aşabilir.

### 2. İki Ana Yöntem
- **Switch Spoofing:** Saldırgan kendi bilgisayarını bir "Switch" gibi gösterir. Gerçek Switch ile kendi arasında bir "Trunk" (tüm VLAN trafiğini taşıyan hat) bağlantısı kurar. Böylece ağdaki tüm VLAN'ların trafiği saldırganın bilgisayarına akmaya başlar.
- **Double Tagging:** Saldırgan gönderdiği paketin içine iki adet VLAN etiketi yerleştirir. İlk Switch ilk etiketi çıkarır ve paketi ikinci etiketteki VLAN'a (asıl hedef) gönderir. Bu yöntemle saldırgan tek yönlü (sadece veri gönderme) bir sızma sağlar.

### 3. Bilmen Gereken Bazı Terimler
- **VLAN ID:** Bir sanal ağın numarası (Örn: VLAN 10).
- **Trunk Port:** Bir kablo üzerinden birden fazla VLAN trafiğini taşımaya yarayan özel port tipi.
- **Access Port:** Sadece tek bir VLAN'a hizmet veren standart kullanıcı portu.
- **Native VLAN:** Bir trunk hattında etiketlenmemiş (untagged) gelen paketlerin atandığı varsayılan VLAN.

### 4. Korunma Yolları
- **Kullanılmayan Portları Kapatın:** Ofisteki boş ağ prizlerini her zaman kapalı tutun.
- **Access Modu:** Tüm kullanıcı portlarını manuel olarak "Access" moduna alın ki saldırgan kendisini Switch gibi gösteremesin.
- **Native VLAN Değiştirin:** Varsayılan olarak gelen VLAN 1'i kullanmayın; Native VLAN'ı rastgele ve kimsenin kullanmadığı bir ID ile değiştirin.

### Gerçek Dünya Analojisi
VLAN Hopping, bir otelde sadece kendi odanızın kartına sahipken, asansörün kontrol sistemini hackleyip kartınızla genel müdürün katına veya gizli kasaların olduğu kata çıkmanız gibidir. Normalde asansör (Switch) sizi oraya götürmemeliydi ama siz sistemi kandırdınız.