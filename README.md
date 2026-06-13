# RAG Question Generation System

## Description
A Retrieval-Augmented Generation (RAG) system using FAISS, SentenceTransformers, and Google Gemini API.

## Features
- Semantic search using FAISS
- Text embeddings using SentenceTransformers
- AI-generated questions using Gemini

## Tech Stack
Python, FAISS, NLP, Gemini API

## Run Locally
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
