# RAG Question Generation System

## Description

A Retrieval-Augmented Generation (RAG) application that combines semantic search with Large Language Models to generate context-aware questions from uploaded documents. The system uses FAISS for efficient vector search, SentenceTransformers for embeddings, and Google Gemini for question generation.

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic Search using FAISS
* Text Embeddings with SentenceTransformers
* AI-Powered Question Generation using Gemini API
* FastAPI Backend
* PDF Document Processing

## Tech Stack

* Python
* FastAPI
* FAISS
* SentenceTransformers
* Google Gemini API
* NLP

## Installation

Clone the repository:

```bash
git clone https://github.com/radik-ha/first_RAG.git
cd first_RAG
```

## Create & Activate Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run Locally

Start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

Open:

```text
http://127.0.0.1:10000
```

## Demo Video

https://github.com/radik-ha/first_RAG/blob/main/demovideo.mp4

## Future Improvements

* Multi-document support
* Chat-based RAG interface
* Advanced reranking
* Support for additional LLMs
