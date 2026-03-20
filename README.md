# Faq_Chatbot

RAG FAQ Chatbot — Project Documentation
1. Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents.

Instead of relying only on an LLM’s internal knowledge, the system:

Extracts text from PDFs

Converts the text into vector embeddings

Stores them in a vector database (Pinecone)

Retrieves relevant chunks when a user asks a question

Sends those chunks to an LLM (Ollama Llama3)

Generates an answer based on the retrieved context

2. System Architecture

The pipeline follows this structure:

User Question
      ↓
Retriever (Pinecone)
      ↓
Relevant Text Chunks
      ↓
LLM (Ollama - Llama3)
      ↓
Final Answer

Full system flow:

PDF Upload
   ↓
Ingestion Pipeline
   ↓
Text Chunking
   ↓
Embedding Generation
   ↓
Vector Storage (Pinecone)
   ↓
Retriever
   ↓
LLM (Llama3)
   ↓
Chatbot Response
3. Project Folder Structure
faq-rag-chatbot
│
├── data
│   └── uploads
│        └── faq.pdf
│
├── src
│
│   ├── ingestion
│   │      ingest.py
│
│   ├── retrieval
│   │      retriever.py
│
│   ├── llm
│   │      chatbot.py
│
│   ├── pipelines
│   │      rag_pipeline.py
│
├── main.py
├── .env
4. Module Descriptions
4.1 Ingestion Module

File:

src/ingestion/ingest.py

Purpose:

Convert PDF documents into vector embeddings and store them in Pinecone.

Pipeline:

PDF
 ↓
Load document
 ↓
Split text into chunks
 ↓
Create embeddings
 ↓
Store vectors in Pinecone

Key operations:

PDF Loading
PyPDFLoader

Extracts text from the document.

Text Chunking
RecursiveCharacterTextSplitter

Parameters:

chunk_size = 800
chunk_overlap = 150

Purpose:

Split large text into smaller pieces so the retriever can search efficiently.

Example:

Document
   ↓
Chunk1
Chunk2
Chunk3
Embedding Generation

Model used:

sentence-transformers/all-MiniLM-L6-v2

This converts text into numerical vectors.

Example:

"What is refund policy?"
↓
[0.34, -0.18, 0.92, ...]
Vector Storage

Vector database:

Pinecone

Stored information:

vector
metadata

Example metadata:

{
 doc_id: "faq",
 source: "faq.pdf"
}
4.2 Retriever Module

File:

src/retrieval/retriever.py

Purpose:

Retrieve relevant document chunks from Pinecone.

Pipeline:

User Question
      ↓
Convert to embedding
      ↓
Similarity Search
      ↓
Top K Results

Configuration:

k = 5

Meaning:

Retrieve top 5 most relevant chunks

Filtering:

filter={"doc_id": doc_id}

This ensures the retriever searches only inside the selected document.

4.3 LLM Module

File:

src/llm/chatbot.py

Purpose:

Generate answers using the retrieved context.

Model used:

Ollama Llama3

Pipeline:

Retrieved Chunks
      ↓
Prompt Creation
      ↓
LLM
      ↓
Answer

Chain used:

RetrievalQA

This combines:

Retriever + LLM
4.4 RAG Pipeline Module

File:

src/pipelines/rag_pipeline.py

Purpose:

Connect the retriever and chatbot together.

Pipeline:

doc_id
   ↓
get_retriever()
   ↓
create_chatbot()
   ↓
QA Chain

This module acts as the system orchestrator.

4.5 Main Application

File:

main.py

Purpose:

Run the chatbot system.

Responsibilities:

Accept PDF name from user

Run ingestion

Build RAG pipeline

Start chatbot loop

Execution flow:

User enters PDF name
      ↓
Check if file exists
      ↓
Run ingestion
      ↓
Create retriever
      ↓
Initialize chatbot
      ↓
Start Q&A loop
5. Environment Configuration

File:

.env

Required variables:

PINECONE_API_KEY=your_api_key
PINECONE_INDEX_NAME=faq-chatbot
6. How to Run the Project

Step 1 — Install dependencies

pip install -r requirements.txt

Step 2 — Start Ollama

ollama serve

Step 3 — Pull Llama3 model

ollama pull llama3

Step 4 — Run the project

python main.py

Step 5 — Provide PDF name

Example:

Enter uploaded PDF name: faq.pdf

Step 6 — Start asking questions

Ask question: What is refund policy?
7. Current Features Implemented

✔ Modular architecture
✔ PDF ingestion pipeline
✔ Vector database integration
✔ Document metadata filtering
✔ RAG pipeline implementation
✔ Local LLM (Ollama) support

8. Known Limitations

Current system limitations:

Single-document chat

Only one document is used per session.

No Web Interface

Interaction happens through terminal.

Duplicate ingestion risk

Re-uploading the same document may create duplicate vectors.

Slow first response

LLM loading may take 30–60 seconds.

9. Future Improvements (Roadmap)
Phase 2 — Multi-document Chat

Allow querying across multiple documents.

Example:

Chat with:
- faq.pdf
- policy.pdf
Phase 3 — Web Application

Add frontend using:

React + FastAPI

User will be able to:

Upload PDFs
Chat in browser
Phase 4 — Advanced RAG Improvements

Possible improvements:

Hybrid Search

Combine:

vector search + keyword search
Reranking

Use models to reorder retrieved chunks.

Streaming Responses

Generate answers in real time.

Caching

Cache embeddings and responses.

10. Final Summary

This project implements a modular RAG chatbot system with the following pipeline:

PDF
 ↓
Ingestion
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
LLM
 ↓
Answer

The system is designed so each component can be independently improved or replaced, which makes it scalable for production systems.

If you want, I can also create a much better professional document for this project, including:

system diagrams

pipeline diagrams

RAG mathematics

vector similarity explanation

embedding theory
