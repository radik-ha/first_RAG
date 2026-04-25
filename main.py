from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import pickle
import numpy as np
import faiss
from pathlib import Path
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# ---------------- Setup ----------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)
g_model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI(
    title="RAG Service",
    description="RAG powered by Gemini + FAISS",
    version="1.0.0"
)

# Mount static folder
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------------- Load Corpus ----------------
file_path = "corpus.txt"

if not os.path.exists(file_path):
    raise FileNotFoundError("corpus.txt not found!")

corpus = Path(file_path).read_text(encoding="utf-8").strip()

if not corpus:
    raise ValueError("corpus.txt is empty!")

# ---------------- Text Chunking ----------------
def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

# ---------------- Embedding Model ----------------
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return model.encode(text, convert_to_numpy=True).astype(np.float32)

# ---------------- FAISS Setup ----------------
faiss_file = "faiss_index.bin"
id_map_file = "id_to_chunk.pkl"

if os.path.exists(faiss_file) and os.path.exists(id_map_file):
    index = faiss.read_index(faiss_file)
    with open(id_map_file, "rb") as f:
        id_to_chunk = pickle.load(f)
else:
    chunks = chunk_text(corpus)

    if not chunks:
        raise ValueError("No chunks created from corpus!")

    chunk_embeddings = [get_embedding(chunk) for chunk in chunks]

    embedding_dim = chunk_embeddings[0].shape[0]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(np.array(chunk_embeddings))

    id_to_chunk = {i: chunk for i, chunk in enumerate(chunks)}

    faiss.write_index(index, faiss_file)
    with open(id_map_file, "wb") as f:
        pickle.dump(id_to_chunk, f)

# ---------------- Retrieval ----------------
def retrieve(query, top_k=1):
    if index.ntotal == 0:
        return ""

    query_emb = get_embedding(query)
    top_k = min(top_k, index.ntotal)

    D, I = index.search(np.array([query_emb]), top_k)

    results = [id_to_chunk[i] for i in I[0] if i != -1]

    return "\n\n".join(results)

# ---------------- RAG Query ----------------
def rag_query(query, top_k=1):
    context = retrieve(query, top_k)

    if not context:
        return "No relevant information found."

    prompt = f"""
Answer ONLY using the given context.
Do NOT add extra knowledge.
If answer is not in the context, say "Not found in document".

Context:
{context}

Question: {query}

Answer:
"""

    try:
        response = g_model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "No response generated."

    except Exception as e:
        return f"Error generating response: {str(e)}"

# ---------------- API Model ----------------
class QueryRequest(BaseModel):
    query: str
    top_k: int = 1

# ---------------- API Endpoint ----------------
@app.post("/rag")
def rag_endpoint(request: QueryRequest):
    answer = rag_query(request.query, request.top_k)
    return {
        "query": request.query,
        "answer": answer
    }

# ---------------- Home Page ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    index_file = "static/index.html"

    if os.path.exists(index_file):
        return FileResponse(index_file)
    else:
        return HTMLResponse("<h2>RAG API is running 🚀</h2>")