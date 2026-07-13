---
title: "Bypassing Path Traversal Filters | Dizin Aşımı Filtrelerini Atlatmak"
date: 2026-07-13
description: "How simple string replacements fail to prevent Path Traversal and how to bypass them. / Basit karakter değiştirme filtrelerinin Dizin Aşımı zafiyetlerini önlemedeki başarısızlığı ve filtre atlatma yöntemleri."
tags: ["Cybersecurity", "Web Application Security", "LFI", "Bypass"]
categories: ["Blog", "CTF"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/xiaohei-path-traversal-filter-bypass-1.png"
    alt: "Path Traversal Bypass Illustration"
    relative: false
---

## Dizin Aşımı (Path Traversal) ve Filtre Atlama

Web uygulamalarında sıkça karşılaşılan dosya okuma ve dahil etme (LFI) özellikleri, doğru yapılandırılmadığında ciddi siber güvenlik riskleri barındırır. Geliştiriciler genellikle bu tür zafiyetleri önlemek için basit karakter filtreleme (sanitization) yöntemlerine başvururlar. Ancak, bu yöntemler çoğunlukla saldırganlar tarafından kolaylıkla atlatılabilir.

Bu yazıda, basit bir `../` filtrelemesinin neden yetersiz olduğunu ve bu filtrenin iç içe geçmiş (nested) karakter dizileriyle nasıl atlatılabileceğini inceleyeceğiz.

### Zafiyet Senaryosu ve Zayıf Filtreleme

Geliştiricilerin dizin aşımı saldırılarını önlemek için en sık başvurduğu hatalı yöntemlerden biri, gelen girdideki `../` ifadesini boş bir karakter dizisiyle (`""`) değiştirmektir. Örneğin Python dilinde yazılmış şu fonksiyonu inceleyelim:

```python
def safe_file_read(user_input):
    # Saldırganlar üst dizine çıkamasın diye "../" ifadesini siliyoruz
    clean_input = user_input.replace("../", "")
    
    # Dosya belirtilen güvenli dizinden okunuyor
    return read_file("/var/www/html/pages/" + clean_input)
```

İlk bakışta bu kod oldukça mantıklı görünebilir. Kullanıcı `../../etc/passwd` girmeye çalışırsa, `../` ifadeleri silinecek ve geriye sadece `etc/passwd` kalacaktır. Ancak bu filtreleme mantığı **tek seferliktir** ve ardışık silme işlemlerini hesaba katmaz.

### Filtre Atlama (Bypass) Mekanizması

Eğer uygulama girdiyi temizlemek için sadece tek bir kez `replace()` işlemi uyguluyorsa, filtreyi atlatmak için **iç içe geçmiş (nested)** karakter dizileri kullanabiliriz.

Örnek olarak, hedefimiz `/var/www/secret/flag.txt` dosyasına ulaşmak olsun. Normal şartlarda `/var/www/html/pages/` dizininden iki seviye yukarı çıkıp (`../../`) ardından `secret/flag.txt` hedefine gitmeliyiz.

Eğer girdimizi şu şekilde tasarlarsak:
`....//`

Filtrenin (`replace("../", "")`) bu girdi üzerindeki davranışını adım adım inceleyelim:
1. Girdi: `.` `.` `.` `.` `/` `/`
2. Filtre, bu girdi içindeki ilk `../` ifadesini (ortadaki iki nokta ve bir eğik çizgiyi) bulur ve siler: `.. [ ../ ] /`
3. Silme işleminden sonra geriye kalan sol taraftaki `..` ile sağ taraftaki `/` birleşir ve yeni bir `../` oluşturur!

Bu durumda, iki seviye yukarı çıkabilmek için bu yapıyı iki kez tekrarlamamız yeterlidir:
`....//....//secret/flag.txt`

Filtre her iki `....//` öbeğindeki `../` kısımlarını sildiğinde, sunucunun elinde doğrudan `../../secret/flag.txt` kalacak ve filtre başarıyla atlatılmış olacaktır.

![İllüstrasyon / Illustration](/img/xiaohei-path-traversal-filter-bypass-1.png)

### Güvenli Kodlama Çözümleri

Bu tür filtre atlatma zafiyetlerini önlemek için asla basit metin değiştirme yöntemlerine güvenilmemelidir. Bunun yerine şu önlemler alınmalıdır:

1. **Mutlak Yol Doğrulaması (Absolute Path Resolution):** Girdiyi aldıktan sonra sistemin mutlak yolunu (canonical path) çözüp, bu yolun izin verilen kök dizinin dışına çıkıp çıkmadığı kontrol edilmelidir.
   Python örneği:
   ```python
   import os

   def secure_file_read(user_input):
       base_dir = os.path.abspath("/var/www/html/pages/")
       target_path = os.path.abspath(os.path.join(base_dir, user_input))
       
       # Hedef yolun izin verilen kök dizinle başlayıp başlamadığını kontrol et
       if not target_path.startswith(base_dir):
           raise PermissionError("Erişim Reddedildi!")
           
       return read_file(target_path)
   ```
2. **Beyaz Liste (Whitelist):** Sadece belirli dosya isimlerinin veya uzantılarının okunmasına izin verilmelidir.

---

## Bypassing Path Traversal Filters

File reading and Local File Inclusion (LFI) features are common in web applications, but if they are not configured correctly, they present security risks. Developers often resort to simple string sanitization to prevent these vulnerabilities. However, these methods are usually easy to bypass.

In this post, we will look at why a simple `../` filter is insufficient and how it can be bypassed using nested string structures.

### The Vulnerability Scenario and Weak Sanitization

One of the most common mistakes developers make to prevent path traversal attacks is replacing the `../` string in the input with an empty string (`""`). Let's examine a weak sanitization function implemented in Python:

```python
def safe_file_read(user_input):
    # Remove "../" to prevent users from traversing upwards
    clean_input = user_input.replace("../", "")
    
    # Read the file from the designated safe directory
    return read_file("/var/www/html/pages/" + clean_input)
```

At first glance, this code might seem reasonable. If a user tries to enter `../../etc/passwd`, the `../` portions are stripped, leaving only `etc/passwd`. However, this filtering logic is **non-recursive** (it runs only once) and does not account for nested string modifications.

### The Bypass Mechanism

If the application applies the `replace()` function only once, we can use **nested** string inputs to bypass the filter.

Suppose our target is to read the file `/var/www/secret/flag.txt`. Under normal circumstances, starting from `/var/www/html/pages/`, we need to go up two directories (`../../`) and then access `secret/flag.txt`.

If we structure our input like this:
`....//`

Let's examine step-by-step how the filter (`replace("../", "")`) processes this input:
1. Input: `.` `.` `.` `.` `/` `/`
2. The filter searches for the first occurrence of `../` (the middle two dots and a slash) and deletes it: `.. [ ../ ] /`
3. After the deletion, the leftover `..` from the left and `/` from the right merge to form a brand new `../`!

To go up two levels, we just repeat this pattern twice:
`....//....//secret/flag.txt`

When the filter runs, it strips the internal `../` from both `....//` sequences, leaving the server with `../../secret/flag.txt`. The bypass is successful!

### Secure Coding Remediation

To prevent path traversal bypass vulnerabilities, you should never rely on simple string replacement. Instead, apply the following defenses:

1. **Absolute Path Verification:** Resolve the canonical absolute path of the requested file and verify that it remains within the allowed base directory.
   Python Example:
   ```python
   import os

   def secure_file_read(user_input):
       base_dir = os.path.abspath("/var/www/html/pages/")
       target_path = os.path.abspath(os.path.join(base_dir, user_input))
       
       # Ensure the target path starts with the allowed base directory
       if not target_path.startswith(base_dir):
           raise PermissionError("Access Denied!")
           
       return read_file(target_path)
   ```
2. **Whitelisting:** Restrict user inputs to a strict list of allowed filenames or specific extensions.

*This post is linked to the Knowledge Base: [[Knowledge Base / Path Traversal Bypass]]*
