# mini-rag

This is a minimal implementation of the RAG model for question answering.

## 📁 Project Structure

### Folder Organization

```
learning-mini-rag/
├── src/
│   ├── routes/              # API Endpoints Layer
│   ├── controllers/         # Business Logic Layer
│   ├── models/              # Database Layer
│   ├── stores/              # External Service Abstractions
│   │   ├── llm/            # LLM Provider Integration
│   │   └── vectordb/       # Vector Database Integration
│   ├── helpers/            # Utility Functions
│   └── assets/             # File & Database Storage
├── docker/                 # Docker Configuration
└── .vscode/                # Editor Settings
```

### Detailed Folder Breakdown

#### **1. 📡 `routes/` - API Endpoints Layer**
Defines all HTTP endpoints that users interact with.

- `base.py` - Basic endpoints (welcome/health check)
- `data.py` - File upload & processing endpoints
- `nlp.py` - NLP operations (indexing, search, RAG answers)
- `schemes/` - Request/response validation models

**Example:** `POST /api/v1/data/upload/{project_id}` → handled by `routes/data.py`

---

#### **2. 🎮 `controllers/` - Business Logic Layer**
Contains core business logic and orchestrates operations between API and database.

- `BaseController.py` - Shared utilities for all controllers
- `ProjectController.py` - Manages project folder creation
- `DataController.py` - File validation and path generation
- `ProcessController.py` - Document loading and chunking (uses LangChain)
- `NLPController.py` - **RAG orchestration** (embedding, indexing, search, answer generation)

**Example:** `NLPController` takes a question → retrieves relevant chunks → builds prompt → calls LLM

---

#### **3. 💾 `models/` - Database Layer**
Handles all database operations (CRUD) and schema definitions.

**Structure:**
```
models/
├── ProjectModel.py       # Project CRUD operations
├── AssetModel.py         # File asset CRUD operations  
├── ChunkModel.py         # Document chunks CRUD operations
├── db_schemes/           # Data schemas (structure definitions)
│   ├── project.py
│   ├── asset.py
│   └── data_chunk.py
└── enums/                # Enumerations (constants)
```

**Example:** `ChunkModel.insert_many_chunks()` saves text chunks to MongoDB in batches

---

#### **4. 🤖 `stores/llm/` - LLM Provider Abstraction**
Manages LLM integrations (OpenAI, Cohere) with a unified interface.

**Structure:**
```
stores/llm/
├── LLMInterface.py              # Abstract interface (contract)
├── LLMProviderFactory.py        # Creates provider instances
├── LLMEnums.py                  # Provider types, roles
├── providers/
│   ├── OpenAIProvider.py        # OpenAI implementation
│   └── CoHereProvider.py        # Cohere implementation
└── templates/                   # Prompt templates
    ├── template_parser.py       # Multi-language template loader
    └── locales/
        ├── en/rag.py           # English RAG prompts
        └── ar/rag.py           # Arabic RAG prompts
```

**Example:** Factory creates OpenAI client → generates embeddings → creates chat completion

---

#### **5. 🗄️ `stores/vectordb/` - Vector Database Abstraction**
Manages vector database operations (currently Qdrant).

**Structure:**
```
stores/vectordb/
├── VectorDBInterface.py         # Abstract interface
├── VectorDBProviderFactory.py   # Creates DB client
├── VectorDBEnums.py             # DB types, distance metrics
└── providers/
    └── QdrantDBProvider.py      # Qdrant implementation
```

**Example:** Stores chunk embeddings → Performs semantic search by cosine similarity

---

#### **6. ⚙️ `helpers/` - Utility Functions**
Provides shared helper functions used across the application.

- `config.py` - Loads `.env` settings into Pydantic model

**Example:** `get_settings()` returns all configuration (API keys, database URLs, model IDs)

---

#### **7. 📦 `assets/` - File Storage**
Stores uploaded files and database files.

**Structure:**
```
assets/
├── files/                  # Uploaded documents organized by project
│   └── {project_id}/      # Each project has its own folder
├── database/              # Vector database storage (Qdrant)
│   └── qdrant_db/
└── *.postman_collection.json  # API testing collections
```

**Example:** Uploaded file saved as `assets/files/1/abc123_resume.pdf`

---

### 🔄 RAG Pipeline Flow

```
1. Upload        → POST /data/upload/{project_id}
                   (User uploads PDF/TXT)
                   ↓
2. Process       → POST /data/process/{project_id}
                   (File chunked using LangChain)
                   ↓
3. Embed & Index → POST /nlp/index/push/{project_id}
                   (Chunks embedded and stored in Qdrant)
                   ↓
4. Query         → POST /nlp/index/answer/{project_id}
                   (User asks a question)
                   ↓
5. Retrieve      → Semantic search finds relevant chunks
                   ↓
6. Augment       → Retrieved chunks added to prompt template
                   ↓
7. Generate      → LLM generates answer with context
```

---

### 📊 How Components Work Together

```
User Request (API)
    ↓
[routes/]          ← Receives HTTP request
    ↓
[controllers/]     ← Processes business logic
    ↓
[models/]          ← Reads/writes to MongoDB
[stores/llm/]      ← Calls OpenAI/Cohere APIs
[stores/vectordb/] ← Searches Qdrant vector DB
    ↓
[helpers/]         ← Provides config & utilities
    ↓
Response sent back to user
```

---

### 🎯 Responsibility Summary

| Folder | Responsibility | Example |
|--------|---------------|---------|
| **routes/** | API endpoints (HTTP layer) | `POST /upload` |
| **controllers/** | Business logic (orchestration) | Validate file → chunk → embed |
| **models/** | Database operations (data layer) | Save 100 chunks to MongoDB |
| **stores/llm/** | AI provider integration | Call OpenAI to get embeddings |
| **stores/vectordb/** | Vector database operations | Search Qdrant for similar docs |
| **helpers/** | Configuration & utilities | Load `.env` settings |
| **assets/** | File & database storage | Store uploaded PDFs |

---

## Requirements

* Python 3.8 or later

#### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:

```bash
$ conda create -n mini-rag python=3.8
```

3. Activate the environment:

```bash
$ conda activate mini-rag
```

### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

* update `.env` with your credentials

```bash
$ cd docker
$ sudo docker compose up -d
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## API Endpoints

### Base Endpoints
- `GET /api/v1/` - Welcome endpoint

### Data Endpoints
- `POST /api/v1/data/upload/{project_id}` - Upload files (PDF/TXT)
- `POST /api/v1/data/process/{project_id}` - Process files into chunks

### NLP Endpoints
- `POST /api/v1/nlp/index/push/{project_id}` - Index chunks into vector DB
- `GET /api/v1/nlp/index/info/{project_id}` - Get collection info
- `POST /api/v1/nlp/index/search/{project_id}` - Semantic search
- `POST /api/v1/nlp/index/answer/{project_id}` - RAG question answering

## POSTMAN Collection

Download the POSTMAN collection from `/assets/mini-rag-app.postman_collection.json`

## About

Learning mini-rag course - A step-by-step educational project to build a production-ready RAG application.