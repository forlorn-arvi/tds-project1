import os
import re
from pathlib import Path
from tqdm import tqdm

def clean_markdown_content(md_text):
    # Remove discourse mentions like [@user](/u/user)
    md_text = re.sub(r'\[@[^]]+\]\(/u/[^)]+\)', '', md_text)

    # Remove emoji markdown or embedded images with 'emoji' in URL
    md_text = re.sub(r'!\[.*?\]\((.*?emoji.*?)\)', '', md_text, flags=re.IGNORECASE)

    # Remove excessive empty lines
    md_text = re.sub(r'\n\s*\n', '\n\n', md_text)

    return md_text.strip()

def clean_all_markdown_files(folder="output_md"):
    md_files = list(Path(folder).glob("*.md"))
    for md_path in tqdm(md_files, desc="Cleaning markdown files"):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned = clean_markdown_content(content)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

# Execute cleaning
clean_all_markdown_files()
