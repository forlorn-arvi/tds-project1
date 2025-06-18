import os
import json
import html2text
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm
import re

def cooked_to_markdown(cooked_html):
    soup = BeautifulSoup(cooked_html, "html.parser")
    return html2text.html2text(str(soup))

def slugify(text):
    # Slugify title to use in file names
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s_]+', '-', text).strip('-')

def save_posts_as_markdown(posts, output_dir="output_md"):
    Path(output_dir).mkdir(exist_ok=True)
    topics = defaultdict(list)
    id_map = {}

    print(f"\n📦 Processing {len(posts)} posts...\n")
    for post in tqdm(posts, desc="Converting posts to markdown"):
        title = post['topic_title']
        body_md = cooked_to_markdown(post['cooked'])
        topics[title].append(f"### Post {post['post_number']} (ID: {post['id']})\n\n{body_md}")
        id_map[title] = post['id']

    print("\n📂 Saving markdown files by topic...\n")
    for title, contents in topics.items():
        slug = slugify(title)
        id = id_map[title]
        full_name = f"{slug}-{id}.md"
        with open(Path(output_dir) / full_name, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write("\n---\n\n".join(contents))
        print(f"✔️  Saved: {full_name} ({len(contents)} post(s))")

# Load JSON and run
with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

save_posts_as_markdown(posts)
