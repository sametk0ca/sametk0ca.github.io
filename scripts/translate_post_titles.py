import os
import sys
from pathlib import Path

# Configure stdout for UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

posts_dir = Path(r"c:\Users\PC\Desktop\me\SOC\SOC Analyst\blog-source\content\posts")

replacements = {
    "distributed-consensus-and-paxos.md": {
        "from": 'title: "Dağıtık Konsensüs ve Paxos"',
        "to": 'title: "Distributed Consensus and Paxos"'
    },
    "formal-methods-foundations.md": {
        "from": 'title: "Formal Metotlar"',
        "to": 'title: "Formal Methods"'
    },
    "main-memory-forensics.md": {
        "from": 'title: "Bellek Adli Bilişimi"',
        "to": 'title: "Main Memory Forensics"'
    },
    "post-quantum-cryptography.md": {
        "from": 'title: "Post-Kuantum Kriptografi"',
        "to": 'title: "Post-Quantum Cryptography"'
    },
    "side-channel-attacks-and-masking.md": {
        "from": 'title: "Yan Kanal Saldırıları ve Maskeleme"',
        "to": 'title: "Side-Channel Attacks and Masking"'
    }
}

def translate_titles():
    modified_count = 0
    for filename, mapping in replacements.items():
        filepath = posts_dir / filename
        if not filepath.exists():
            print(f"File not found: {filename}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Perform replacement
        if mapping["from"] in content:
            new_content = content.replace(mapping["from"], mapping["to"])
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Successfully translated title in {filename}:")
            print(f"  Old: {mapping['from']}")
            print(f"  New: {mapping['to']}")
            modified_count += 1
        else:
            # Check if there is variation in quotes/spacing
            # Try a looser replacement just in case
            import re
            pattern = re.compile(r'^title:\s*["\']?(.*?)["\']?$', re.MULTILINE)
            match = pattern.search(content)
            if match:
                current_title = match.group(0)
                # Let's replace title line directly
                # We extract the clean title string
                clean_title = match.group(1)
                # Check if it matches our expected Turkish title without quotes
                expected_clean = mapping["from"].split(':', 1)[1].strip().strip('"')
                if clean_title == expected_clean:
                    new_title_line = f'title: "{mapping["to"].split(":", 1)[1].strip().strip(chr(34))}"'
                    new_content = content.replace(current_title, new_title_line)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Successfully translated title in {filename} (using regex matching):")
                    print(f"  Old: {current_title}")
                    print(f"  New: {new_title_line}")
                    modified_count += 1
                else:
                    print(f"Title mismatch in {filename}: Found '{clean_title}', expected '{expected_clean}'")
            else:
                print(f"Could not find title front matter in {filename}")
                
    print(f"\nDone! Translated {modified_count} post titles to English.")

if __name__ == "__main__":
    translate_titles()
