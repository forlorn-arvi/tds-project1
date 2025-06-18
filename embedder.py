import os
import json
import requests
import sqlite3
import numpy as np
from pathlib import Path
from tqdm import tqdm

# Constants
AIPIPE_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFyYXZpbnRoMzAwN2tAZ21haWwuY29tIn0.l8--n57gwkqL3SAcWR8oQFjODfR_TUwHd8_cM8KkqDg"
EMBEDDING_URL = "https://aipipe.org/openai/v1/embeddings"
HEADERS = {
    "Authorization": f"Bearer {AIPIPE_API_KEY}",
    "Content-Type": "application/json"
}

DB_PATH = "tds_docs.db"
MD_DIR = "output_md"
MODEL = "text-embedding-3-small"

# Initialize SQLite DB with FTS5
def init_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS docs USING fts5(
            title, 
            chunk, 
            url, 
            embedding
        )
    """)
    return con

# Read and chunk markdown
def chunk_markdown(text, max_tokens=300):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = []

    token_estimate = lambda txt: len(txt.split())

    for para in paragraphs:
        if token_estimate(" ".join(current_chunk + [para])) <= max_tokens:
            current_chunk.append(para)
        else:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [para]
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks

# Embed text using AI Pipe
def embed_text(text):
    response = requests.post(
        EMBEDDING_URL,
        headers=HEADERS,
        json={"model": MODEL, "input": [text]}
    )
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]

# Main embedder
def embed_all_markdown():
    con = init_db()
    files = list(Path(MD_DIR).glob("*.md"))

    for file in tqdm(files, desc="Embedding Markdown Files"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
        title = file.name  # <--- Keep full filename including .md
        chunks = chunk_markdown(text)

        for idx, chunk in enumerate(tqdm(chunks, desc=f"{title}", leave=False)):
            try:
                embedding = embed_text(chunk)
                embedding_json = json.dumps(embedding)
                url = f"{title.replace(' ', '_')}#{idx}"
                con.execute("INSERT INTO docs (title, chunk, url, embedding) VALUES (?, ?, ?, ?)",
                            (title, chunk, url, embedding_json))
            except Exception as e:
                print(f"❌ Error embedding chunk {idx} of {title}: {e}")
    con.commit()
    con.close()

if __name__ == "__main__":
    embed_all_markdown()
