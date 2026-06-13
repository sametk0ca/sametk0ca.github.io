import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime
import os
import html
import sys

# Cybersecurity feeds to fetch (RSS and Atom formats supported)
FEEDS = {
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
    "Dark Reading": "https://www.darkreading.com/rss.xml",
    "r/netsec": "https://www.reddit.com/r/netsec/.rss"
}

def clean_html(raw_html):
    if not raw_html:
        return ""
    # Remove HTML tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    # Decode HTML entities
    cleantext = html.unescape(cleantext)
    # Remove extra spaces/newlines
    cleantext = re.sub(r'\s+', ' ', cleantext).strip()
    return cleantext

def parse_date(date_str):
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %y %H:%M:%S %z",
        "%a, %d %b %y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%SZ"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return datetime.now()

def fetch_feed(source_name, url):
    print(f"Fetching {source_name}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (weekly-news-bot:v1.0)'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            xml_data = response.read()
            return xml_data
    except Exception as e:
        print(f"Error fetching {source_name}: {e}")
        return None

def parse_feed(source_name, xml_data):
    articles = []
    if not xml_data:
        return articles
    try:
        # Register namespaces to find tags easily
        # ET.fromstring can parse with namespaces
        root = ET.fromstring(xml_data)
        
        # Try RSS format first
        channel = root.find('channel')
        if channel is not None:
            items = channel.findall('item')
            for item in items:
                title = item.findtext('title', '')
                link = item.findtext('link', '')
                pub_date_str = item.findtext('pubDate', '')
                desc = item.findtext('description', '') or item.findtext('{http://purl.org/rss/1.0/modules/content/}encoded', '')
                summary = clean_html(desc)
                
                parsed_date = parse_date(pub_date_str)
                
                articles.append({
                    "source": source_name,
                    "title": title,
                    "link": link,
                    "date": parsed_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "timestamp": parsed_date.timestamp(),
                    "summary": summary
                })
        else:
            # Atom format (like Reddit)
            # Find entries using namespace handling
            # Atom elements are usually prefixed with namespace '{http://www.w3.org/2005/Atom}'
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('atom:entry', ns)
            for entry in entries:
                title = entry.findtext('atom:title', '', ns)
                link_elem = entry.find('atom:link', ns)
                link = link_elem.attrib.get('href', '') if link_elem is not None else ''
                pub_date_str = entry.findtext('atom:updated', '', ns) or entry.findtext('atom:published', '', ns)
                content = entry.findtext('atom:content', '', ns) or entry.findtext('atom:summary', '', ns)
                summary = clean_html(content)
                
                # Truncate summary for reddit to avoid huge inputs
                if len(summary) > 1000:
                    summary = summary[:1000] + "..."
                
                parsed_date = parse_date(pub_date_str)
                
                articles.append({
                    "source": source_name,
                    "title": title,
                    "link": link,
                    "date": parsed_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "timestamp": parsed_date.timestamp(),
                    "summary": summary
                })
    except Exception as e:
        print(f"Error parsing {source_name}: {e}")
    return articles

def ask_gemini(prompt, api_key):
    print("Sending news to Gemini for filtering and summarization...")
    # Using v1beta endpoint to support responseMimeType with gemini-3.5-flash
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            text_response = res_data["candidates"][0]["content"]["parts"][0]["text"]
            
            # Clean markdown code blocks from Gemini response
            text_response = text_response.strip()
            if text_response.startswith("```"):
                lines = text_response.splitlines()
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines[-1].startswith("```"):
                    lines = lines[:-1]
                text_response = "\n".join(lines).strip()
                
            return json.loads(text_response)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e else ""
        print(f"HTTP Error calling Gemini API: {e.code} - {e.reason}")
        print(f"API Response: {error_body}")
        return None
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None

def build_prompt(news_items):
    formatted_news = ""
    for i, item in enumerate(news_items, 1):
        formatted_news += f"{i}. Source: {item['source']}\n"
        formatted_news += f"   Title: {item['title']}\n"
        formatted_news += f"   Link: {item['link']}\n"
        formatted_news += f"   Description: {item['summary'][:300]}\n\n"
        
    prompt = f"""
Aşağıda bu haftaya ait siber güvenlik haberlerinin listesi (başlık, kaynak ve özetler) yer almaktadır.
Lütfen bu haberler içinden siber güvenlik dünyasını bu hafta en çok etkileyen, teknik derinliği en yüksek ve en kritik 3 haberi seç (eğer listede 3'ten az kritik haber varsa sadece onları seç).

Haberler:
{formatted_news}

Seçtiğin her haber için aşağıdaki JSON yapısına uygun olarak bir liste üret.
Çıktı sadece şu şemaya uygun bir JSON objesi olmalıdır:
{{
  "news": [
    {{
      "source": "Kaynak Adı (örn: BleepingComputer)",
      "original_link": "Habere ait orijinal URL linki",
      "title_tr": "Haberin Türkçe Başlığı",
      "title_en": "Haberin İngilizce Başlığı",
      "summary_tr": "Haberin detaylarını ve neden önemli olduğunu açıklayan, siber güvenlik teknik terimlerine sadık kalınarak yazılmış 2-3 cümlelik özlü Türkçe teknik özet",
      "summary_en": "Haberin detaylarını ve neden önemli olduğunu açıklayan, siber güvenlik teknik terimlerine sadık kalınarak yazılmış 2-3 cümlelik özlü İngilizce teknik özet",
      "category": "Haber kategorisi (örn: Malware, Vulnerability, Data Breach, Zero-Day vb.)"
    }}
  ]
}}
"""
    return prompt

def generate_markdown(weekly_data, year, week):
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    content = f"""---
title: "Weekly Security Summary | Haftalık Siber Güvenlik Özeti - Week {year}/{week:02d}"
date: {date_str}
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

"""
    for i, item in enumerate(weekly_data["news"], 1):
        content += f"### {i}. [{item['title_tr']}]({item['original_link']})\n"
        content += f"**Kategori:** `{item['category']}` | **Kaynak:** `{item['source']}`\n\n"
        content += f"{item['summary_tr']}\n\n"
        
    content += """---

## English

The most critical cybersecurity developments and technical insights of the week:

"""
    for i, item in enumerate(weekly_data["news"], 1):
        content += f"### {i}. [{item['title_en']}]({item['original_link']})\n"
        content += f"**Category:** `{item['category']}` | **Source:** `{item['source']}`\n\n"
        content += f"{item['summary_en']}\n\n"
        
    return content

def main():
    all_articles = []
    for source, url in FEEDS.items():
        xml_data = fetch_feed(source, url)
        articles = parse_feed(source, xml_data)
        # Limit to top 3 articles per source (total around 10-12 articles) to keep it fast
        articles = articles[:3]
        print(f"Parsed {len(articles)} articles from {source}")
        all_articles.extend(articles)
        
    if not all_articles:
        print("No articles fetched. Exiting.")
        sys.exit(1)
        
    # Sort by timestamp descending to get latest news
    all_articles.sort(key=lambda x: x['timestamp'], reverse=True)
    
    # We send all candidate articles (which is now max 10-12 total) to Gemini
    candidate_articles = all_articles
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable not found! Cannot summarize news.")
        # Fallback: create mock data for local testing
        print("Generating mock weekly summary for demonstration/testing.")
        weekly_data = {
            "news": [
                {
                    "source": "BleepingComputer",
                    "original_link": "https://www.bleepingcomputer.com/news/security/example-1",
                    "title_tr": "Windows SmartScreen Atlatma Zafiyeti İstismar Ediliyor",
                    "title_en": "Windows SmartScreen Bypass Vulnerability Actively Exploited",
                    "summary_tr": "Saldırganlar, Windows SmartScreen güvenlik önlemini atlatmak için yeni bir zero-day zafiyetini aktif olarak kullanıyor. Zafiyet, kullanıcıların zararlı dosyaları güvenlik uyarıları almadan açmasına olanak tanıyor. Microsoft zafiyet için güvenlik güncellemesi yayınladı. Güvenlik ekiplerinin yamaları acilen uygulaması önerilmektedir.",
                    "summary_en": "Attackers are actively exploiting a new zero-day vulnerability to bypass Windows SmartScreen protections. The vulnerability allows users to open malicious files without triggering security warnings. Microsoft has released security updates for this flaw. Security teams are advised to apply patches immediately.",
                    "category": "Vulnerability"
                }
            ]
        }
    else:
        prompt = build_prompt(candidate_articles)
        weekly_data = ask_gemini(prompt, api_key)
        if not weekly_data or "news" not in weekly_data:
            print("Failed to get parsed weekly news from Gemini. Exiting.")
            sys.exit(1)

    # Generate markdown content
    today = datetime.now()
    year, week, _ = today.isocalendar()
    
    markdown_content = generate_markdown(weekly_data, year, week)
    
    # Ensure content directory exists
    os.makedirs('content/weekly-news', exist_ok=True)
    
    filepath = f"content/weekly-news/weekly-security-summary-{year}-w{week:02d}.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"Weekly security summary successfully saved to: {filepath}")

if __name__ == "__main__":
    main()
