---
title: "WebAudio Fingerprinting: AliExpress Case | WebAudio ile Cihaz Takibi"
date: 2026-08-23
description: "How e-commerce platforms secretly fingerprint devices via WebAudio API at zero volume. / E-ticaret platformlarının WebAudio API ile sıfır ses düzeyinde gizlice cihaz parmak izi çıkarma mekanizması."
draft: false
tags: ["WebAudio API", "Browser Fingerprinting", "Privacy", "Covert Channels", "Web Security"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/webaudio-fingerprinting.png"
    alt: "WebAudio Fingerprinting Cover"
    relative: false
related:
  - "[[webaudio-fingerprinting-aliexpress|Sessizliğin Parmak İzi: AliExpress ve WebAudio ile Cihaz Takibi…]]"
---

## 🇹🇷 Türkçe (TR)

### Giriş: Sessiz Ses Dalgalarıyla Cihaz Takibi

Geçtiğimiz günlerde bir yazılımcının kablosuz Bluetooth kulaklığının bilgisayardan telefona geçiş yapmamasıyla fark edilen bir olay, modern web dünyasında kullanıcı mahremiyetinin hangi sınırlara kadar zorlandığını bir kez daha kanıtladı. 

Kullanıcı, AliExpress web sitesinde gezinirken bilgisayarda hiçbir medya veya ses çalmamasına rağmen kulaklığının ses boru hattının (audio pipeline) kilitli kaldığını fark etti. Tarayıcının geliştirici araçları (DevTools) ve JavaScript çağrıları incelendiğinde; arka planda çalışan komut dosyalarının tarayıcının **WebAudio API** arayüzünü kullanarak kullanıcıya hissettirmeden **sıfır ses düzeyinde (zero-volume)** gizli sinyaller yürüttüğü ve donanımsal yanıtı ölçerek benzersiz bir **Ses Parmak İzi (Audio Fingerprint)** ürettiği ortaya çıktı.

### WebAudio Fingerprinting Nasıl Çalışır?

Geleneksel çerezler (cookies) ve yerel depolama (`localStorage`), modern gizlilik eklentileri veya gizli sekme (Incognito) ile kolayca engellenebilmektedir. Buna karşılık veri toplayıcılar, doğrudan cihazın fiziksel donanım özelliklerini hedef alan parmak izi tekniklerine yönelmektedir.

```
+---------------------------------------------------------------------------------------+
|                       SES PARMAK İZİ (AUDIO FINGERPRINTING) AKIŞI                     |
+---------------------------------------------------------------------------------------+
| [ Web Sayfası ] ---> [ WebAudio API: Sessiz Osilatör Sinyali (Zero-Volume Buffer) ]  |
|                             |                                                         |
|                             v                                                         |
|                      [ Donanım Katmanı ]                                              |
|            (Ses Kartı, DAC Çipi, Floating Point İşlemci, Sürücüler)                   |
|                             |                                                         |
|                             v                                                         |
|             [ Mikroskobik Matematiksel Sapmalar (D/A Noise) ]                         |
|                             |                                                         |
|                             v                                                         |
| [ Benzersiz Hash / Cihaz Parmak İzi ] ===> Çerezsiz, VPN'siz Kalıcı Kullanıcı Takibi! |
+---------------------------------------------------------------------------------------+
```

1. **Sinyal Üretimi:** Web sayfası, Web Audio API üzerinden bir osilatör (`OscillatorNode`) veya dinamik sıkıştırıcı (`DynamicsCompressorNode`) oluşturur.
2. **Çevrimdışı İşleme (OfflineAudioContext):** Bu işlem hoparlörden fiziksel bir ses çıkarmadan doğrudan bellekte milisaniyeler içinde işlenir. (Kulaklığın ses hattının kilitli kalması, bu vakada sayfanın ayrıca gerçek zamanlı bir `AudioContext` açık tuttuğuna işaret eder; yalnızca `OfflineAudioContext` ses çıkış donanımını kullanmaz.)
3. **Yazılım ve Donanım Sapmaları:** Her cihazın CPU mimarisi, tarayıcının ses motoru, işletim sistemi kütüphaneleri ve kayan nokta (floating-point) aritmetik hesaplama ayrıntıları birbirinden mikroskobik düzeyde farklıdır. Bu farklar üretilen dalga biçiminde küçük sapmalara yol açar.
4. **Frekans Analizi ve Hashleme:** Üretilen ses sinyali Hızlı Fourier Dönüşümü (FFT) ile analiz edilir ve çıkan spektrum dizisi bir hash fonksiyonundan (`MurmurHash` veya `SHA-256`) geçirilerek o cihaza özel tekil bir kimlik numarası (UUID) üretilir.

### Neden Kritik Bir Güvenlik ve Mahremiyet Tehdidi?

* **Kalıcı ve Kolay Engellenemez:** Çerezleri temizlemek veya VPN kullanmak bu takibi durdurmaz; çünkü takip edilen şey bir çerez değil, cihazınızın donanım ve yazılım özellikleridir. Ses parmak izi tek başına benzersiz olmayabilir; genellikle canvas, yazı tipleri ve ekran çözünürlüğü gibi diğer sinyallerle birleştirilerek kullanılır.
* **Kullanıcı İzni Gerektirmez:** Mikrofon veya kamera gibi çevre birimlerine erişilirken tarayıcı kullanıcıdan izin ister; ancak WebAudio API standart bir ses işleme arayüzü olduğu için hiçbir onay kutusu göstermez.
* **Gizli Kanal İstismarı:** Bu vakada olduğu gibi, arka planda açık tutulan ses kanalı Bluetooth yığınını meşgul eder, donanım kaynaklarını tüketir ve pil ömrünü olumsuz etkiler.

### Korunma ve Savunma Yolları

* **Brave Tarayıcısı ve Farbling Teknolojisi:** Brave, `Farbling` mekanizması ile WebAudio ve Canvas API çıktılarının içine rastgele çok küçük matematiksel gürültüler (pseudo-random noise) ekleyerek parmak izinin her seferinde farklı çıkmasını sağlar.
* **Firefox Resist Fingerprinting:** `about:config` üzerinden `privacy.resistFingerprinting` ayarı `true` yapılarak tarayıcının tüm donanım API'lerini jenerik standart değerlere zorlaması sağlanabilir.

---

## 🇬🇧 English (EN)

### Introduction: Silent Audio Fingerprinting on the Modern Web

A recent finding by a software developer revealed a stealthy tracking vector embedded within e-commerce platforms. While browsing AliExpress with Bluetooth headphones connected, the developer noticed his wireless headset failed to automatically switch audio to his mobile device, indicating an active audio stream despite no media playing on the page.

Inspecting the underlying JavaScript and browser execution trace revealed that background scripts were exploiting the **WebAudio API** to generate inaudible, zero-volume audio buffers. By measuring hardware-specific signal rendering differences, the script generated a unique, persistent **Audio Device Fingerprint**.

### Technical Mechanics of WebAudio Fingerprinting

As traditional tracking mechanisms (third-party cookies, `localStorage`, IP tracking) face severe restrictions from privacy regulations and ad-blockers, tracking vendors increasingly rely on hardware-level device fingerprinting.

1. **Audio Synthesis:** The webpage instantiates an `AudioContext` or `OfflineAudioContext`, configuring an `OscillatorNode` combined with a `DynamicsCompressorNode`.
2. **Buffer Processing:** The audio graph processes the synthetic signal silently within memory without outputting audible sound to the speaker.
3. **Software and Hardware Discrepancies:** Differences in CPU architecture, the browser's audio engine, OS libraries, and floating-point arithmetic details introduce microscopic mathematical deviations in the rendered waveform. (An `OfflineAudioContext` renders in software, so the sound card itself is not involved. The headset staying locked in this case suggests the page also kept a real-time `AudioContext` open.)
4. **Spectral Hashing:** The processed buffer is analyzed via Fast Fourier Transform (FFT). The resulting frequency spectrum values are hashed (e.g., using `MurmurHash3`) to generate a deterministic hardware identifier.

### Threat Vectors and Privacy Implications

* **Stateless Tracking:** The generated identifier persists across private browsing sessions, cookie purges, and VPN toggles, as it is derived from the device's hardware and software characteristics rather than stored data. On its own an audio fingerprint may not be unique; trackers usually combine it with other signals such as canvas, fonts, and screen resolution.
* **Zero Permission Prompts:** While microphone and webcam access require explicit user consent, the WebAudio synthesis pipeline operates silently without triggering browser permission dialogs.
* **Covert Channel Resource Exhaustion:** Keeping the audio pipeline permanently engaged locks wireless audio routing (Bluetooth A2DP/HFP profiles) and causes unnecessary power consumption.

### Mitigation Strategies

* **Brave Browser (Farbling):** Brave actively counters WebAudio fingerprinting by injecting balanced pseudo-random noise into audio buffers, making fingerprint matching much harder.
* **Firefox Fingerprinting Resistance:** Enabling `privacy.resistFingerprinting` forces audio and graphics APIs to return standardized generic outputs.
