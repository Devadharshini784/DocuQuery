# knowdex 📚

> Turn your documents into a searchable knowledge base. Ask questions and get answers with exact source citations.

knowdex is an AI-powered document question-answering system that allows users to upload PDFs, DOCX, TXT, and Markdown files, automatically index their content, and ask questions in natural language. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant passages and generate answers backed by document-level citations.

---

## Features

- 📂 **Multi-format document upload** — Supports PDF, DOCX, TXT, and Markdown files up to 50MB
- ⚡ **Automatic document indexing** — Parses, cleans, chunks, embeds, and stores uploaded documents
- 💬 **Natural language queries** — Ask questions about your documents without writing complex search queries
- 📎 **Source-backed answers** — Every answer includes citations with the filename, page number, and relevant passage
- 🔀 **Three chat modes** — Document-only (`knowdex`), general knowledge (`LLM`), and combined (`Hybrid`)
- 🧮 **Vector similarity search** — Uses PostgreSQL and pgvector with HNSW indexing and cosine similarity
- 🔴 **Real-time response streaming** — Streams LLM responses token by token using Server-Sent Events (SSE)
- 🔌 **Multiple LLM providers** — Supports Groq, OpenAI, Anthropic, Gemini, and local Ollama models
- 🔐 **Authentication system** — HTTP-only session cookies, PBKDF2-SHA256 password hashing, and protected routes
- 🛡️ **Security features** — Per-IP rate limiting and security headers
- 🎙️ **Voice input** — Ask questions using the Web Speech API
- ⌨️ **Keyboard accessibility** — Keyboard navigation and `Ctrl+K` shortcut for creating new chats

---

## Tech Stack

**Frontend**
- Next.js 16.2 (App Router)
- React 19.2
- TypeScript 5
- Tailwind CSS v4
- Radix UI
- Framer Motion
- Zustand 5
- TanStack Query v5
- react-markdown + remark-gfm

**Backend**
- Python 3.13
- FastAPI 0.115
- SQLAlchemy 2 (Async)
- Alembic
- PyMuPDF
- python-docx
- slowapi

**Database & AI**
- PostgreSQL 16
- pgvector
- ONNX Runtime
- BAAI/bge-small-en-v1.5 (INT8 embeddings)
- Groq, OpenAI, Anthropic, Gemini, Ollama

**Deployment**
- Frontend → Vercel
- Backend → Railway
- Database → PostgreSQL + pgvector

---

## How It Works

1. **Upload documents** — Upload PDF, DOCX, TXT, or Markdown files through the interface.
2. **Process and index** — Documents are parsed, cleaned, split into chunks, converted into 384-dimensional embeddings, and stored in PostgreSQL using pgvector.
3. **Ask questions** — Enter questions in natural language and choose your preferred chat mode.
4. **Retrieve relevant context** — The system performs vector similarity search to identify the most relevant document passages.
5. **Generate cited answers** — The selected LLM generates a response using the retrieved context and streams the answer with source citations.

---

## Chat Modes

| Mode | Description |
|------|-------------|
| `knowdex` | Answers questions using indexed documents only, with document citations |
| `llm` | Uses general LLM knowledge without retrieving document content |
| `hybrid` | Combines document retrieval, LLM reasoning, and optional live web search through Tavily |

---

## Getting Started Locally

### Prerequisites

- Node.js 20+
- Python 3.13+
- Docker Desktop
- Groq API key ([Get one here](https://console.groq.com/))

### Clone the Repository

```bash
git clone https://github.com/Devadharshini784/knowdex.git
cd knowdex
```

### Setup Backend

```bash
cd backend
cp .env.example .env
```

Configure your environment variables in `backend/.env`:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/knowdex

LLM_PROVIDER=groq
LLM_MODEL=qwen/qwen3.8-27b
LLM_API_KEY=your_groq_api_key

# Optional: Live web search for Hybrid mode
TAVILY_API_KEY=your_tavily_api_key
```

Start the backend using Docker:

```bash
docker compose up --build
```

Run database migrations:

```bash
docker compose exec api python -m alembic upgrade head
```

Backend runs at `http://localhost:8000`.

### Setup Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000`.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check API and database connectivity |
| POST | `/upload` | Upload a document and start indexing |
| GET | `/documents` | Retrieve all uploaded documents |
| GET | `/documents/{id}` | Get document details |
| GET | `/documents/{id}/chunks` | Inspect indexed document chunks |
| DELETE | `/documents/{id}` | Delete a document and its chunks |
| POST | `/retrieve` | Perform vector similarity search |
| POST | `/chat` | Generate and stream answers with citations |
| POST | `/auth/signup` | Create a new account |
| POST | `/auth/login` | Authenticate and create a session |
| GET | `/auth/me` | Get authenticated user details |
| POST | `/auth/logout` | End the current session |

Interactive API documentation is available at `http://localhost:8000/docs` when `DEBUG=true`.

---

## Document Processing Pipeline

```text
Document Upload
      |
      v
File Validation
      |
      v
Document Parsing
(PyMuPDF / python-docx / Plain Text)
      |
      v
Text Cleaning & Chunking
(800 tokens / 120 overlap)
      |
      v
Embedding Generation
(BAAI/bge-small-en-v1.5)
      |
      v
Vector Storage
(PostgreSQL + pgvector)
      |
      v
Document Ready for Search
```

---

## Roadmap

- [x] Multi-format document ingestion
- [x] Automated text chunking and embedding generation
- [x] Vector similarity search using pgvector
- [x] Multi-provider LLM integration
- [x] Real-time response streaming with SSE
- [x] Source citations with document and page references
- [x] Authentication and protected routes
- [x] Rate limiting and security headers
- [ ] Hybrid retrieval with BM25 and Reciprocal Rank Fusion
- [ ] Cross-encoder reranking
- [ ] Role-based access control
- [ ] Agentic RAG with multi-agent orchestration
- [ ] Multimodal RAG for images, OCR, and tables

---

## Running Tests

**Backend**

```bash
cd backend
pytest -q
```

**Frontend**

```bash
cd frontend
npx tsc --noEmit
npm run lint
npm run build
```

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes using Conventional Commits.
4. Run the tests and ensure everything works.
5. Open a pull request against `main`.


---

**Built with Next.js, FastAPI, PostgreSQL, pgvector, and Groq.**

⭐ If you find knowdex useful, consider giving the repository a star!