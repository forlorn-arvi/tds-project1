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

def save_posts_as_markdown(posts, output_dir="output_md"):
    Path(output_dir).mkdir(exist_ok=True)
    topics = defaultdict(list)

    print(f"\n📦 Processing {len(posts)} posts...\n")
    for post in tqdm(posts, desc="Converting posts to markdown"):
        title = post['topic_title']
        body_md = cooked_to_markdown(post['cooked'])
        topics[title].append(f"### Post {post['post_number']} (ID: {post['id']})\n\n{body_md}")

    print("\n📂 Saving markdown files by topic...\n")
    for title, contents in topics.items():
        safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
        filename = f"{safe_title}.md"
        with open(Path(output_dir) / filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write("\n---\n\n".join(contents))
        print(f"✔️  {title} — {len(contents)} post(s)")


# Load JSON and run
with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

save_posts_as_markdown(posts)
