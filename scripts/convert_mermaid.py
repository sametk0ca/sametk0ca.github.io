import os
import re
import base64
import urllib.request
import hashlib
import time

posts_dir = "/Users/smtkc/obsidian-vault/obsidian-vault/blog-source/content/posts"
static_img_dir = "/Users/smtkc/obsidian-vault/obsidian-vault/blog-source/static/img"

os.makedirs(static_img_dir, exist_ok=True)

# Regex to find mermaid blocks
mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:8]

def clean_for_api(text):
    # Map Turkish characters to ASCII equivalents to prevent encoding errors on mermaid.ink
    mapping = {
        'ç': 'c', 'Ç': 'C',
        'ğ': 'g', 'Ğ': 'G',
        'ı': 'i', 'I': 'I', 'İ': 'I',
        'ö': 'o', 'Ö': 'O',
        'ş': 's', 'Ş': 'S',
        'ü': 'u', 'Ü': 'U'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    # Remove any other non-ascii character
    text = text.encode('ascii', 'ignore').decode('ascii')
    return text

def download_svg(mermaid_code, filename):
    cleaned_code = clean_for_api(mermaid_code)
    code_bytes = cleaned_code.encode('utf-8')
    base64_bytes = base64.b64encode(code_bytes)
    base64_string = base64_bytes.decode('utf-8')
    
    url = f"https://mermaid.ink/svg/{base64_string}"
    dest_path = os.path.join(static_img_dir, filename)
    
    max_retries = 3
    for attempt in range(max_retries):
        print(f"Downloading SVG (Attempt {attempt+1}/{max_retries}): {filename}")
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                content = response.read()
                if b"<svg" in content:
                    with open(dest_path, "wb") as f:
                        f.write(content)
                    print(f"Successfully saved to {dest_path}")
                    return True
                else:
                    print(f"Error: Content downloaded for {filename} is not valid SVG.")
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(3.0) # Wait before retry
                
    return False

# Scan files
files = [f for f in os.listdir(posts_dir) if f.endswith(".md")]

for file in files:
    file_path = os.path.join(posts_dir, file)
    file_slug = file[:-3].replace(" ", "-").lower()
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    matches = list(mermaid_pattern.finditer(content))
    if not matches:
        continue
        
    print(f"\nProcessing {file} ({len(matches)} diagrams found)...")
    
    # Process in reverse to maintain correct string indices while replacing
    new_content = content
    for idx, match in reversed(list(enumerate(matches))):
        mermaid_code = match.group(1).strip()
        code_hash = get_hash(mermaid_code)
        svg_filename = f"mermaid-{file_slug}-{idx+1}-{code_hash}.svg"
        
        svg_path = os.path.join(static_img_dir, svg_filename)
        
        # Check if file exists, if not download it
        success = True
        if not os.path.exists(svg_path):
            success = download_svg(mermaid_code, svg_filename)
            time.sleep(1.5) # Sleep between calls to avoid rate limits / 503s
            
        if success and os.path.exists(svg_path):
            md_replacement = f"![Diyagram / Diagram](/img/{svg_filename})"
            new_content = new_content[:match.start()] + md_replacement + new_content[match.end():]
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated {file}")

print("\nDone converting Mermaid blocks!")
