# 🤖 RAG Chatbot (Retrieval-Augmented Generation)

An AI-powered chatbot that answers questions based on uploaded documents using Retrieval-Augmented Generation (RAG). This project combines vector search (FAISS) with a language model to provide accurate, context-aware responses.

---

## 🚀 Features

* 📄 Upload documents (PDF / text)
* 🔍 Semantic search using embeddings
* ⚡ FastAPI backend for fast responses
* 🤖 AI-generated answers based on your data
* 💬 Interactive chatbot interface
* 📦 Scalable and efficient architecture

---

## 🛠️ Tech Stack

* Python
* FastAPI
* FAISS (Vector Database)
* NumPy
* Pydantic
* LLM API (Gemini / OpenAI)

---

## 📂 Project Structure

```
├── main.py              # FastAPI entry point (routes & server)
├── RAG_ChatBot.py      # Core RAG pipeline (embedding + retrieval + response)
├── requirements.txt    # Dependencies
├── .env                # API keys (ignored)
├── .gitignore          # Ignored files
├── data/               # Uploaded documents
├── embeddings/         # FAISS vector index storage
├── static/ (optional)  # Frontend files
├── templates/ (optional) # HTML UI files
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file and add your API key:

```
API_KEY=your_api_key_here
```

⚠️ Make sure `.env` is added to `.gitignore`

---

## ▶️ Run the Project

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📌 Usage

1. Start the FastAPI server
2. Upload a document via API or UI
3. The system converts text into embeddings and stores them in FAISS
4. Ask questions related to the uploaded content
5. The chatbot retrieves relevant chunks and generates answers using the LLM

---

## 👩‍💻 Author

Your Name
GitHub: [https://github.com/your-username](https://github.com/radik-ha)
