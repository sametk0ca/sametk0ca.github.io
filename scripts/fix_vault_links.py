import os
import re
from pathlib import Path

vault_root = Path(r"c:\Users\PC\Desktop\me\SOC\SOC Analyst")

categories = [
    "Attacks", "CTFs", "Certifications", "Cloud", "Cryptography", "Defense",
    "DevSecOps", "Frameworks", "Hardware", "IncidentResponse", "Legal_Compliance",
    "Networking", "OS", "OS_Virtualization", "Principles", "Programming",
    "Tools", "Virtualization"
]

def clean_link_path(path_str):
    # Split header
    header = ""
    if "#" in path_str:
        path_str, header = path_str.split("#", 1)
        header = "#" + header
        
    # Strip .md
    if path_str.endswith(".md"):
        path_str = path_str[:-3]
        
    parts = path_str.replace("\\", "/").split("/")
    basename = parts[-1].strip()
    
    # Check if pointing to a deleted category index
    is_index = basename == "index"
    category_match = None
    for part in parts:
        if part in categories:
            category_match = part
            break
            
    if is_index and category_match:
        # Category index is deleted, return None to signal to convert to plain text or skip
        return None, category_match
        
    return basename + header, None

link_pattern = re.compile(r'\[\[(.*?)\]\]')

# Target directories only
target_dirs = [
    vault_root / "digital-samet" / "wiki",
    vault_root / "blog-source" / "content" / "bilgi-bankasi"
]

# We must absolutely exclude TryHackMe and img folders
exclude_dirs = [
    vault_root / "TryHackMe Security Engineer Path",
    vault_root / "TryHackMe SOC Path SAL",
    vault_root / "img"
]

def should_process(fpath):
    # Must be in one of the target dirs
    in_target = False
    for td in target_dirs:
        if td.resolve() in fpath.resolve().parents or td.resolve() == fpath.resolve():
            in_target = True
            break
    if not in_target:
        return False
        
    # Must not be in any excluded dir
    for ed in exclude_dirs:
        if ed.resolve() in fpath.resolve().parents:
            return False
            
    # Do not process index.md (we will edit wiki/index.md manually to make it extremely beautiful and customized!)
    if fpath.name == "index.md" and fpath.parent.name == "wiki":
        return False
        
    return fpath.name.endswith('.md')

# Find all markdown files to process
all_files = []
for dirpath, _, filenames in os.walk(vault_root):
    for f in filenames:
        fp = Path(dirpath) / f
        if should_process(fp):
            all_files.append(fp)

print(f"Found {len(all_files)} markdown files to clean links in.")

modified_count = 0
links_fixed_count = 0

for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        original_content = f.read()
        
    def replacer(match):
        global links_fixed_count
        link_content = match.group(1)
        
        # Skip if it is an asset (has image extension)
        if any(link_content.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.mp4']):
            return match.group(0)
        if link_content.startswith('!'):
            return match.group(0)
            
        alias = ""
        path_part = link_content
        if "|" in link_content:
            path_part, alias = link_content.split("|", 1)
            
        cleaned_path, cat_match = clean_link_path(path_part)
        
        if cleaned_path is None:
            # It was a category index link which is now deleted
            # Convert to plain text using alias, or category name
            links_fixed_count += 1
            if alias:
                return alias
            elif cat_match:
                return cat_match
            else:
                return "Category Index"
                
        links_fixed_count += 1
        if alias:
            return f"[[{cleaned_path}|{alias}]]"
        else:
            return f"[[{cleaned_path}]]"

    new_content = link_pattern.sub(replacer, original_content)
    
    if new_content != original_content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1

print(f"\nCompleted Link Cleanup!")
print(f"Total files modified: {modified_count}")
print(f"Total links updated/fixed: {links_fixed_count}")
