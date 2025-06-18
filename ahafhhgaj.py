import os
import requests

BRANCH = "tds-2025-01"
REPO = "sanand0/tools-in-data-science-public"
API_URL = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"

OUTPUT_DIR = "course_md"
os.makedirs(OUTPUT_DIR, exist_ok=True)

response = requests.get(API_URL)
tree = response.json().get("tree", [])

for file in tree:
    path = file["path"]
    if path.endswith(".md"):
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{path}"
        print(f"Downloading: {path}")
        content = requests.get(raw_url).text
        filename = os.path.basename(path)
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)

print("✅ All .md files saved in 'output_md/'")
