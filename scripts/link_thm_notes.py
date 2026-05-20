import os
import sys
from pathlib import Path

# Configure stdout for UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

vault_root = Path(r"c:\Users\PC\Desktop\me\SOC\SOC Analyst")

se_path = vault_root / "TryHackMe Security Engineer Path"
soc_path = vault_root / "TryHackMe SOC Path SAL"

se_footer = """

---
## 🔗 Bağlantılar
- [[TryHackMe Security Engineer Path/index|🎓 TryHackMe: Security Engineer Path]]
- [[index|🏠 Ana İndeks]]
"""

soc_footer = """

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
"""

def process_directory(dir_path, footer, path_identifier):
    if not dir_path.exists():
        print(f"Directory not found: {dir_path}")
        return
        
    modified_count = 0
    total_count = 0
    
    for dirpath, _, filenames in os.walk(dir_path):
        for f in filenames:
            if not f.endswith(".md") or f == "index.md":
                continue
                
            fpath = Path(dirpath) / f
            total_count += 1
            
            with open(fpath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                
            # Check if already has the backlink
            if path_identifier in content:
                # Already linked, skip
                continue
                
            # Strip trailing newlines and spaces to prevent extra padding
            content_cleaned = content.rstrip()
            
            # Append the footer
            new_content = content_cleaned + footer
            
            with open(fpath, "w", encoding="utf-8") as file:
                file.write(new_content)
                
            modified_count += 1
            print(f"Updated: {fpath.relative_to(vault_root)}")
            
    print(f"\nFinished processing {dir_path.name}:")
    print(f"  Processed {total_count} files.")
    print(f"  Added backlinks to {modified_count} files.")

if __name__ == "__main__":
    print("Starting linking for TryHackMe folders...\n")
    
    print("--- Processing Security Engineer Path ---")
    process_directory(se_path, se_footer, "TryHackMe Security Engineer Path/index")
    
    print("\n--- Processing SOC Path SAL ---")
    process_directory(soc_path, soc_footer, "TryHackMe SOC Path SAL/index")
    
    print("\nAll TryHackMe files are successfully processed!")
