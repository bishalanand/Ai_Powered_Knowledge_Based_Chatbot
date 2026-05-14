# 🤖 AI-Powered Knowledge Base Chatbot

An intelligent **full-stack RAG (Retrieval-Augmented Generation) chatbot** that enables users to upload PDF documents, automatically generate summaries, and ask context-aware questions directly from the uploaded document.

The system uses **semantic search, vector embeddings, and LLM reasoning** to generate accurate answers grounded in document content instead of hallucinating generic responses.

Built using **React, FastAPI, LangChain, Pinecone, and Groq API (Llama3)**.

---

## 🚀 Project Demo

🔗 **GitHub Repository:**  
https://github.com/bishalanand/Ai_Powered_Knowledge_Based_Chatbot

🔗 **Project Demo Video:**  
https://drive.google.com/drive/folders/1hNtdEzN5NCtFfjKbM2trgMfWEa2fKxXq?usp=sharing)

---

## 📌 Features

✅ Upload PDF documents through a React frontend  
✅ Automatic PDF summarization after upload  
✅ Ask questions directly from uploaded PDFs  
✅ Retrieval-Augmented Generation (RAG) pipeline  
✅ Context-aware question answering  
✅ Semantic search using vector embeddings  
✅ Pinecone vector database integration  
✅ Metadata-based document filtering  
✅ FastAPI backend integration  
✅ Groq API integration for fast LLM inference  
✅ Responsive and clean frontend UI  
✅ Modular and scalable architecture

---

## 🏗️ System Architecture

```text
                ┌─────────────────┐
                │  React Frontend │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ FastAPI Backend │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
         PDF Upload          User Question
              │                     │
              ▼                     ▼
       Text Extraction        Retriever
              │                     │
              ▼                     ▼
         Text Chunking      Pinecone Search
              │                     │
              ▼                     ▼
     Embedding Generation    Relevant Chunks
              │                     │
              └──────────┬──────────┘
                         ▼
                Groq API (Llama3)
                         │
                         ▼
              Summary / Chat Response
```

---

## 🛠️ Tech Stack

### Frontend
- React.js
- CSS

### Backend
- FastAPI
- Python

### AI / RAG Pipeline
- LangChain
- Groq API
- Sentence Transformers

### Vector Database
- Pinecone

### Embedding Model
- `sentence-transformers/all-MiniLM-L6-v2`

### LLM
- `Llama3` via **Groq API**

---

## ✨ Core Functionalities

### 📄 1. PDF Upload

Users can upload PDF documents directly through the **React frontend**.

Once uploaded, the backend processes the document and prepares it for semantic retrieval and question answering.

---

### 📝 2. Automatic PDF Summary Generation

After uploading a document:

- Text is extracted from the PDF
- Important information is analyzed
- A concise summary is generated automatically

This enables users to quickly understand the document before interacting with the chatbot.

### Example

```text
Uploaded Document:
Transformer Architecture.pdf

Generated Summary:
This document explains transformer architecture,
attention mechanisms, encoder-decoder structure,
self-attention, and applications in NLP.
```

---

### 💬 3. Ask Questions From PDF

After upload and summarization, users can ask doubts/questions directly from the uploaded document.

The chatbot retrieves relevant document chunks and generates accurate responses based on PDF context.

### Example

```text
Question:
What is self-attention?

Answer:
Self-attention is a mechanism that allows
a model to focus on different words in
a sequence while processing information.
```

---

## 🔍 How It Works

### Step 1 — Upload PDF

User uploads a PDF document through the frontend.

↓

### Step 2 — Text Extraction

The document text is extracted.

↓

### Step 3 — Text Chunking

The document is divided into smaller chunks for efficient retrieval.

Configuration:

```text
Chunk Size: 800
Chunk Overlap: 150
```

↓

### Step 4 — Embedding Generation

Each chunk is converted into vector embeddings using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

↓

### Step 5 — Vector Storage

Embeddings are stored inside **Pinecone Vector Database**.

↓

### Step 6 — Summary Generation

A concise summary of the uploaded document is generated automatically using **Groq Llama3**.

↓

### Step 7 — User Questions

Users ask questions related to the uploaded document.

↓

### Step 8 — Semantic Retrieval

Top relevant chunks are retrieved from Pinecone.

Configuration:

```text
Top K Retrieval = 5
```

↓

### Step 9 — Response Generation

Retrieved chunks are passed to **Groq Llama3**, which generates a context-aware answer.

---

## 📸 Application Screenshots

### 🏠 Home Page

<img src="Ai chatbot picture/Home.png" width="100%" />

---

### 📤 PDF Upload Interface

<img src="Ai chatbot picture/upload.png" width="100%" />

---

### 📝 Generated Summary

<img src="Ai chatbot picture/summary.png" width="100%" />

---

### 💬 Chatbot Interface

<img src="Ai chatbot picture/chat.png" width="100%" />

---

## 📂 Project Structure

```text
Ai_Powered_Knowledge_Based_Chatbot
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── backend
│
│   ├── api
│   │   └── upload.py
│   │
│   ├── src
│   │   ├── ingestion
│   │   │   └── ingest.py
│   │   │
│   │   ├── retrieval
│   │   │   └── retriever.py
│   │   │
│   │   ├── llm
│   │   │   └── chatbot.py
│   │   │
│   │   ├── pipelines
│   │   │   └── rag_pipeline.py
│   │
│   ├── data
│   │   └── uploads
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/bishalanand/Ai_Powered_Knowledge_Based_Chatbot.git

cd Ai_Powered_Knowledge_Based_Chatbot
```

---

## Backend Setup

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---
### 4️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend will run on:

```text
http://localhost:8000
```

---

## Frontend Setup

### 5️⃣ Navigate to Frontend

```bash
cd frontend
```

---

### 6️⃣ Install Dependencies

```bash
npm install
```

---

### 7️⃣ Start React Application

```bash
npm run dev
```

or

```bash
npm start
```

Frontend will run on:

```text
http://localhost:5173
```

---

## 🔥 Key Highlights

- Built a **full-stack AI application**
- Implemented **Retrieval-Augmented Generation (RAG)**
- Integrated **React frontend with FastAPI backend**
- Added **automatic PDF summarization**
- Enabled **document-based conversational AI**
- Used **semantic search with Pinecone vector DB**
- Integrated **Groq API for ultra-fast inference**
- Built **context-aware PDF Q&A system**
- Designed **scalable modular architecture**

---

## ⚠️ Known Limitations

- Currently optimized for single-document chat
- Re-uploading the same document may create duplicate vectors
- Requires internet connection for Groq API access
- No authentication system yet

---

## 🛣️ Future Improvements

### 📚 Multi-Document Chat

Enable users to interact with multiple PDFs simultaneously.

Example:

```text
Chat with:
- faq.pdf
- research.pdf
- policy.pdf
```

### ⚡ Advanced RAG Improvements

- Hybrid Search
- Reranking
- Streaming Responses
- Embedding Cache
- Response Cache


## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

### Bishal Anand

🔗 **GitHub:**  
https://github.com/bishalanand



---

## ⭐ Support

If you found this project useful, consider giving it a **star ⭐** on GitHub.
