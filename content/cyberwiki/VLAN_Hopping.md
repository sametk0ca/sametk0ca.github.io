+++
title = "VLAN Hopping (VLAN Atlaması) | VLAN Hopping"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

VLAN Hopping is when an attacker secretly moves from one virtual network (VLAN) in the network to another, even though he or she would not normally be authorized to do so.

### 1. Attack Logic
Normally VLANs are completely isolated (separate) from each other. However, the attacker can overcome these walls by using some vulnerabilities in the operating logic of Switches (Network switches).

### 2. Two Main Methods
- **Switch Spoofing:** The attacker disguises his own computer as a "Switch". It establishes a "Trunk" (the line that carries all VLAN traffic) connection between the real Switch and itself. Thus, traffic from all VLANs on the network begins to flow to the attacker's computer.
- **Double Tagging:** The attacker places two VLAN tags in the packet he sends. The first Switch strips the first tag and sends the packet to the VLAN (original destination) in the second tag. With this method, the attacker provides a one-way (only sending data) infiltration.

### 3. Some Terms You Should Know
- **VLAN ID:** The number of a virtual network (Ex: VLAN 10).
- **Trunk Port:** A special port type used to carry more than one VLAN traffic over a cable.
- **Access Port:** Standard user port serving only a single VLAN.
- **Native VLAN:** ​​The default VLAN to which untagged incoming packets are assigned on a trunk line.

### 4. Ways of Protection
- **Turn Off Unused Ports:** Always keep vacant network outlets in the office turned off.
- **Access Mode:** Manually put all user ports in "Access" mode so that the attacker cannot pose as a Switch.
- **Change Native VLAN:** ​​Do not use the default VLAN 1; Change the Native VLAN to a random ID that no one uses.

### Real World Analogy
VLAN Hopping is like hacking the elevator control system and going to the general manager's floor or the floor where the secret safes are with your card, when you only have the card for your own room in a hotel. Normally the elevator (Switch) shouldn't have taken you there, but you tricked the system.
