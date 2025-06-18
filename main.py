from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import base64
import requests
import numpy as np
import json
from typing import List, Optional

app = FastAPI()

DB_PATH = r"C:\\Users\\aravi\\Downloads\\tds-project1\\tds_docs.db"
EMBEDDING_URL = "https://aipipe.org/openai/v1/embeddings"
COMPLETION_ENDPOINT = "https://aipipe.org/openai/v1/chat/completions"
MODEL = "text-embedding-3-small"
AIPIPE_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFyYXZpbnRoMzAwN2tAZ21haWwuY29tIn0.l8--n57gwkqL3SAcWR8oQFjODfR_TUwHd8_cM8KkqDg"  # Replace with your real key
HEADERS = {"Authorization": f"Bearer {AIPIPE_API_KEY}", "Content-Type": "application/json"}

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class QueryResponse(BaseModel):
    answer: str
    links: List[Link]

def embed_text(text: str) -> List[float]:
    response = requests.post(
        EMBEDDING_URL,
        headers=HEADERS,
        json={"model": MODEL, "input": [text]}
    )
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]

def get_image_description(image_b64: str) -> str:
    prompt = f"Describe the content of this image briefly in under 200 characters: {image_b64[:200]}..."
    response = requests.post(COMPLETION_ENDPOINT, json={
        "model": "gpt-3.5-turbo-0125",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates minimal image descriptions."},
            {"role": "user", "content": prompt}
        ]
    }, headers=HEADERS)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def cosine_similarity(a: List[float], b: List[float]) -> float:
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def search_similar_docs(query_embedding: List[float]) -> List[str]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT filename, embedding FROM docs")
    rows = cursor.fetchall()
    conn.close()

    scored_docs = []
    for filename, embedding_str in rows:
        try:
            doc_embedding = json.loads(embedding_str)
            score = cosine_similarity(query_embedding, doc_embedding)
            scored_docs.append((score, filename))
        except Exception as e:
            print(f"Skipping file {filename} due to error: {e}")

    scored_docs.sort(reverse=True, key=lambda x: x[0])
    top_filenames = [filename for _, filename in scored_docs[:3]]
    return top_filenames

def get_final_answer(question: str, context_filenames: List[str]) -> str:
    context_str = "\n".join(context_filenames)
    system_prompt = "You are an automated assistant for answering course-related questions. Only use provided filenames as reference."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context_str}\n\nQuestion: {question}"}
    ]
    response = requests.post(COMPLETION_ENDPOINT, json={
        "model": "gpt-3.5-turbo-0125",
        "messages": messages
    }, headers=HEADERS)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def build_links_from_filenames(filenames: List[str]) -> List[Link]:
    links = []
    for name in filenames:
        name = name.strip()

        # Handle course: files
        if name.startswith("course:"):
            # Remove "course:" prefix and ".md" suffix
            pure_name = name.replace("course:", "").replace(".md", "")
            url = f"http://tds.s-anand.net/#{pure_name}"
            links.append(Link(url=url, text=pure_name))

        # Handle Discourse markdown files
        elif name.endswith(".md") and "-" in name:
            parts = name.replace(".md", "").rsplit("-", 1)
            if len(parts) == 2 and parts[1].isdigit():
                slug, topic_id = parts
                url = f"https://discourse.onlinedegree.iitm.ac.in/t/{slug}/{topic_id}"
                links.append(Link(url=url, text=slug.replace("-", " ").title()))
            else:
                # fallback
                url = f"https://discourse.onlinedegree.iitm.ac.in/t/{name.replace('.md','')}"
                links.append(Link(url=url, text=name.replace(".md", "")))
        else:
            # fallback
            links.append(Link(url=name, text=name))
    return links[:3]

@app.post("/api/", response_model=QueryResponse)
def handle_query(req: QueryRequest):
    try:
        combined_text = req.question
        if req.image:
            image_desc = get_image_description(req.image)
            combined_text += "\n" + image_desc

        query_embedding = embed_text(combined_text)
        top_filenames = search_similar_docs(query_embedding)

        if not top_filenames:
            return QueryResponse(answer="No relevant information found in the course material.", links=[])

        answer = get_final_answer(req.question, top_filenames)
        links = build_links_from_filenames(top_filenames)

        return QueryResponse(answer=answer, links=links)
    except Exception as e:
        return QueryResponse(answer=f"Error processing the request. No output generated. {e}", links=[])
