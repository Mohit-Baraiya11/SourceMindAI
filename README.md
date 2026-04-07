# SourceMind AI 🧠

A hybrid RAG chatbot that lets you chat with your documents. Built with child/parent chunking for smart retrieval, session-based memory, and a minimal chat UI.

---

## Tech Stack

- **Backend** — FastAPI + Python
- **LLM** — Groq (LLaMA 3)
- **Vector Store** — Pinecone
- **Database** — Supabase
- **RAG Framework** — LangChain

---

## Features

- Child/parent chunking for precise + context-rich retrieval
- Session-based chat memory persisted in Supabase
- PDF ingestion via API
- Clean single-file chat UI

---

## Setup
```bash
git clone https://github.com/yourusername/sourcemind-ai.git
cd sourcemind-ai

uv venv && source .venv/bin/activate
uv sync
```

Add your keys to a `.env` file:
```env
GROQ_API_KEY=
PINECONE_API_KEY=
PINECONE_INDEX_NAME=
SUPABASE_URL=
SUPABASE_KEY=
```
```bash
uvicorn main:app --reload
```

Then open `index.html` in your browser.

---

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/ingest` | Upload and index a PDF |
| POST | `/sessions` | Create a new chat session |
| POST | `/chat` | Send a message |
| GET | `/sessions/{id}/messages` | Get chat history |

---

## Author

**Mohit** — B.E. AI & Data Science | [LinkedIn](https://www.linkedin.com/in/mohit-baraiya-a929242a7/) 
