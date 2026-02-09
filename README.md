# 🤖 Mini-RAG: Production-Ready RAG Chatbot System

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-success)

*A modular, production-ready Retrieval-Augmented Generation (RAG) system for intelligent question answering over document collections.*

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Architecture](#-architecture) • [API Reference](#-api-reference)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [RAG Pipeline](#-rag-pipeline)
- [Development](#-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

**Mini-RAG** is a minimalist yet powerful implementation of a Retrieval-Augmented Generation (RAG) system designed for building intelligent chatbots that answer questions based on your document collections. The system combines semantic search with large language models to provide accurate, context-aware responses.

### What is RAG?

Retrieval-Augmented Generation enhances LLM responses by:
1. **Retrieving** relevant context from a knowledge base
2. **Augmenting** the user query with retrieved information
3. **Generating** accurate answers using the enriched context

### Use Cases

- 📚 **Document Q&A**: Query large document collections (PDFs, text files)
- 🏢 **Enterprise Knowledge Base**: Build internal chatbots over company documentation
- 📖 **Research Assistant**: Quickly find and summarize information from research papers
- 🎓 **Educational Tools**: Create tutoring systems based on course materials
- 💼 **Customer Support**: Automate responses using product documentation

---

## ✨ Features

### Core Capabilities

- 🔍 **Semantic Search**: Vector-based similarity search using state-of-the-art embeddings
- 🤖 **Multi-LLM Support**: Compatible with OpenAI GPT and Cohere models
- 📄 **Document Processing**: Automatic chunking and processing of PDF and TXT files
- 🗄️ **Vector Database**: Efficient storage and retrieval using Qdrant
- 🌍 **Multilingual**: Built-in support for English and Arabic prompts
- 🎯 **Project Management**: Organize documents into separate projects
- ⚡ **Batch Processing**: Efficient batch embedding and indexing
- 🔌 **REST API**: Clean, well-documented FastAPI endpoints

### Technical Highlights

- **Modular Architecture**: Clean separation of concerns (routes, controllers, models, stores)
- **Provider Abstraction**: Easily swap LLM and vector DB providers via factory pattern
- **Production Ready**: MongoDB integration, Docker support, environment-based configuration
- **Template System**: Customizable prompt templates with locale support
- **Comprehensive Error Handling**: Robust validation and error responses
- **Scalable Design**: Supports concurrent requests and batch operations

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────────┐
│                         Client Layer                             │
│                   (REST API Endpoints)                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│                    Business Logic Layer                          │
│              (Controllers - Orchestration)                       │
└─────┬──────────────────┬──────────────────┬─────────────────────┘
      │                  │                  │
┌─────▼─────┐   ┌────────▼────────┐   ┌────▼──────────────────────┐
│   Data    │   │   Persistence   │   │   External Services       │
│   Layer   │   │     Layer       │   │                           │
│           │   │                 │   │  ┌─────────────────────┐  │
│  Models   │   │    MongoDB      │   │  │   LLM Providers     │  │
│  (CRUD)   │   │  (Documents)    │   │  │  - OpenAI           │  │
│           │   │                 │   │  │  - Cohere           │  │
└───────────┘   └─────────────────┘   │  └─────────────────────┘  │
                                      │                           │
                                      │  ┌─────────────────────┐  │
                                      │  │  Vector Database    │  │
                                      │  │  - Qdrant           │  │
                                      │  └─────────────────────┘  │
                                      └───────────────────────────┘
```

### Component Overview

| Component | Responsibility | Technology |
|-----------|---------------|------------|
| **API Layer** | HTTP request handling, validation | FastAPI, Pydantic |
| **Controllers** | Business logic orchestration | Python |
| **Models** | Database CRUD operations | PyMongo |
| **LLM Store** | AI provider integration | OpenAI SDK, Cohere SDK |
| **Vector Store** | Semantic search operations | Qdrant Client |
| **Helpers** | Configuration, utilities | Pydantic Settings |

---

## 📋 Prerequisites

### System Requirements

- **Python**: 3.8 or later
- **Docker**: 20.10+ (for database services)
- **Docker Compose**: 1.29+
- **Memory**: Minimum 4GB RAM recommended
- **Storage**: 2GB free space

### API Keys Required

- **OpenAI API Key** (for GPT models and embeddings)
  - Or **Cohere API Key** (alternative LLM provider)

---

## 🚀 Installation

### Option 1: Using Conda (Recommended)

```bash
# Download and install Miniconda
# Visit: https://docs.anaconda.com/free/miniconda/#quick-command-line-install

# Create virtual environment
conda create -n mini-rag python=3.8

# Activate environment
conda activate mini-rag

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using venv

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Install Docker Services

```bash
# Navigate to docker directory
cd docker

# Copy environment template
cp .env.example .env

# Update .env with your credentials
# Edit MongoDB and Qdrant settings

# Start services
sudo docker compose up -d

# Verify services are running
sudo docker compose ps
```

---

## ⚙️ Configuration

### Environment Setup

```bash
# Copy environment template (in project root)
cp .env.example .env
```

### Configure `.env` File

```bash
# ============================================
# LLM Provider Settings
# ============================================
OPENAI_API_KEY=sk-your-openai-api-key-here
COHERE_API_KEY=your-cohere-api-key-here  # Optional

# Select active LLM provider
LLM_PROVIDER=openai  # Options: openai, cohere

# Model Configuration
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_CHAT_MODEL=gpt-4-turbo-preview
COHERE_EMBEDDING_MODEL=embed-english-v3.0
COHERE_CHAT_MODEL=command-r-plus

# ============================================
# Vector Database Settings
# ============================================
VECTOR_DB_PROVIDER=qdrant  # Currently only Qdrant supported
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_GRPC_PORT=6334

# Vector Search Parameters
VECTOR_SIZE=1536  # Must match embedding model output
DISTANCE_METRIC=cosine  # Options: cosine, euclidean, dot

# ============================================
# MongoDB Settings
# ============================================
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_DATABASE=mini_rag_db
MONGODB_USER=admin
MONGODB_PASSWORD=your-secure-password

# ============================================
# Application Settings
# ============================================
CHUNKING_SIZE=500  # Characters per chunk
CHUNKING_OVERLAP=50  # Overlap between chunks
TOP_K_RESULTS=5  # Number of chunks to retrieve

# Language for prompts
DEFAULT_LOCALE=en  # Options: en, ar
```

### Docker Environment (docker/.env)

```bash
# MongoDB Configuration
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=your-secure-password
MONGO_INITDB_DATABASE=mini_rag_db

# Qdrant Configuration
QDRANT_API_KEY=your-qdrant-api-key  # Optional for local deployment
```

---

## 📚 Usage

### Start the Application

```bash
# Ensure Docker services are running
cd docker && sudo docker compose up -d

# Return to project root
cd ..

# Start FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

Server will be available at: `http://localhost:5000`

### Interactive API Documentation

Visit: `http://localhost:5000/docs` for Swagger UI

### Basic Workflow

#### 1. Upload Documents

```bash
curl -X POST "http://localhost:5000/api/v1/data/upload/my-project" \
  -F "files=@document.pdf" \
  -F "files=@report.txt"
```

#### 2. Process Documents (Chunking)

```bash
curl -X POST "http://localhost:5000/api/v1/data/process/my-project"
```

#### 3. Index Documents (Create Embeddings)

```bash
curl -X POST "http://localhost:5000/api/v1/nlp/index/push/my-project"
```

#### 4. Ask Questions

```bash
curl -X POST "http://localhost:5000/api/v1/nlp/index/answer/my-project" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the key findings in the document?",
    "locale": "en"
  }'
```

---

## 📡 API Reference

### Base Endpoints

#### Health Check
```http
GET /api/v1/
```

**Response:**
```json
{
  "message": "Welcome to Mini-RAG API",
  "version": "1.0.0"
}
```

---

### Data Management Endpoints

#### Upload Files
```http
POST /api/v1/data/upload/{project_id}
```

**Parameters:**
- `project_id` (path): Unique project identifier

**Request Body:**
- `files`: List of files (multipart/form-data)

**Supported Formats:** `.pdf`, `.txt`

**Response:**
```json
{
  "success": true,
  "project_id": "my-project",
  "uploaded_files": [
    {
      "filename": "document.pdf",
      "asset_id": "507f1f77bcf86cd799439011",
      "file_path": "assets/files/my-project/abc123_document.pdf"
    }
  ]
}
```

#### Process Documents
```http
POST /api/v1/data/process/{project_id}
```

**Description:** Loads documents and splits them into chunks using LangChain

**Response:**
```json
{
  "success": true,
  "project_id": "my-project",
  "chunks_created": 150,
  "processing_time": "2.3s"
}
```

---

### NLP & RAG Endpoints

#### Index Documents
```http
POST /api/v1/nlp/index/push/{project_id}
```

**Description:** Generates embeddings and stores them in vector database

**Response:**
```json
{
  "success": true,
  "project_id": "my-project",
  "vectors_indexed": 150,
  "collection_name": "my-project"
}
```

#### Get Collection Info
```http
GET /api/v1/nlp/index/info/{project_id}
```

**Response:**
```json
{
  "collection_name": "my-project",
  "vectors_count": 150,
  "config": {
    "vector_size": 1536,
    "distance": "Cosine"
  }
}
```

#### Semantic Search
```http
POST /api/v1/nlp/index/search/{project_id}
```

**Request Body:**
```json
{
  "query": "machine learning applications",
  "top_k": 5
}
```

**Response:**
```json
{
  "results": [
    {
      "chunk_id": "507f1f77bcf86cd799439011",
      "text": "Machine learning has various applications...",
      "score": 0.89,
      "metadata": {
        "source": "document.pdf",
        "page": 5
      }
    }
  ]
}
```

#### RAG Question Answering
```http
POST /api/v1/nlp/index/answer/{project_id}
```

**Request Body:**
```json
{
  "question": "What are the main benefits of RAG systems?",
  "locale": "en",
  "temperature": 0.7,
  "max_tokens": 500
}
```

**Response:**
```json
{
  "answer": "RAG systems provide several key benefits: 1) Access to up-to-date information...",
  "sources": [
    {
      "chunk_id": "507f1f77bcf86cd799439011",
      "text": "Retrieved context...",
      "relevance_score": 0.89
    }
  ],
  "metadata": {
    "model": "gpt-4-turbo-preview",
    "tokens_used": 450,
    "processing_time": "1.2s"
  }
}
```

---

## 📂 Project Structure

```
mini-rag/
├── src/
│   ├── routes/                    # 📡 API Endpoints Layer
│   │   ├── base.py               # Welcome & health check
│   │   ├── data.py               # File upload & processing
│   │   ├── nlp.py                # Indexing, search, Q&A
│   │   └── schemes/              # Request/response schemas
│   │
│   ├── controllers/               # 🎮 Business Logic Layer
│   │   ├── BaseController.py     # Shared utilities
│   │   ├── ProjectController.py  # Project management
│   │   ├── DataController.py     # File validation
│   │   ├── ProcessController.py  # Document chunking
│   │   └── NLPController.py      # RAG orchestration
│   │
│   ├── models/                    # 💾 Database Layer
│   │   ├── ProjectModel.py       # Project CRUD
│   │   ├── AssetModel.py         # File asset CRUD
│   │   ├── ChunkModel.py         # Chunk CRUD
│   │   ├── db_schemes/           # Data schemas
│   │   │   ├── project.py
│   │   │   ├── asset.py
│   │   │   └── data_chunk.py
│   │   └── enums/                # Constants
│   │
│   ├── stores/                    # 🔌 External Service Abstractions
│   │   ├── llm/                  # LLM Provider Integration
│   │   │   ├── LLMInterface.py
│   │   │   ├── LLMProviderFactory.py
│   │   │   ├── LLMEnums.py
│   │   │   ├── providers/
│   │   │   │   ├── OpenAIProvider.py
│   │   │   │   └── CoHereProvider.py
│   │   │   └── templates/        # Prompt templates
│   │   │       ├── template_parser.py
│   │   │       └── locales/
│   │   │           ├── en/rag.py
│   │   │           └── ar/rag.py
│   │   │
│   │   └── vectordb/             # Vector Database Integration
│   │       ├── VectorDBInterface.py
│   │       ├── VectorDBProviderFactory.py
│   │       ├── VectorDBEnums.py
│   │       └── providers/
│   │           └── QdrantDBProvider.py
│   │
│   ├── helpers/                   # ⚙️ Utility Functions
│   │   └── config.py             # Environment config loader
│   │
│   └── assets/                    # 📦 File & Database Storage
│       ├── files/                # Uploaded documents
│       │   └── {project_id}/
│       ├── database/             # Vector DB storage
│       │   └── qdrant_db/
│       └── *.postman_collection.json
│
├── docker/                        # 🐳 Docker Configuration
│   ├── docker-compose.yml
│   ├── .env.example
│   └── .env
│
├── .vscode/                       # 💻 Editor Settings
├── main.py                        # 🚀 Application entry point
├── requirements.txt               # 📦 Python dependencies
├── .env.example                   # ⚙️ Environment template
└── README.md                      # 📖 Documentation
```

### Component Responsibilities

| Layer | Components | Purpose |
|-------|-----------|---------|
| **API** | `routes/` | HTTP request handling, input validation |
| **Business Logic** | `controllers/` | Orchestration, workflow management |
| **Data Access** | `models/` | MongoDB CRUD operations |
| **External Services** | `stores/llm/`, `stores/vectordb/` | LLM and vector DB integrations |
| **Configuration** | `helpers/` | Settings management |
| **Storage** | `assets/` | File and database persistence |

---

## 🔄 RAG Pipeline

### Complete Workflow

```
┌─────────────┐
│  1. UPLOAD  │  User uploads PDF/TXT files
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 2. PROCESS  │  Documents split into chunks (LangChain)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  3. EMBED   │  Chunks converted to vectors (OpenAI/Cohere)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  4. INDEX   │  Vectors stored in Qdrant
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  5. QUERY   │  User asks a question
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 6. RETRIEVE │  Semantic search finds relevant chunks
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 7. AUGMENT  │  Question + Context → Prompt template
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 8. GENERATE │  LLM generates contextual answer
└─────────────┘
```

### Detailed Process Flow

#### Step 1-2: Upload & Processing
```python
# User uploads files
POST /api/v1/data/upload/project-123

# System processes documents
POST /api/v1/data/process/project-123
↓
LangChain TextLoader → CharacterTextSplitter
↓
Chunks saved to MongoDB
```

#### Step 3-4: Embedding & Indexing
```python
# Generate embeddings
POST /api/v1/nlp/index/push/project-123
↓
Batch processing: chunks → OpenAI/Cohere → embeddings
↓
Qdrant collection created/updated
↓
Vectors indexed with metadata
```

#### Step 5-8: Query & Generation
```python
# User query
POST /api/v1/nlp/index/answer/project-123
{
  "question": "What is RAG?",
  "locale": "en"
}
↓
Query → Embedding → Vector Search (Qdrant)
↓
Top-K relevant chunks retrieved
↓
Template populated:
  - System prompt
  - Retrieved context
  - User question
↓
LLM generates answer
↓
Response returned with sources
```

---

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/mini-rag.git
cd mini-rag

# Create development environment
conda create -n mini-rag-dev python=3.8
conda activate mini-rag-dev

# Install dependencies with development tools
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Setup pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

### Code Style Guidelines

- **Formatting**: Use `black` for code formatting
- **Linting**: Follow `flake8` rules
- **Type Hints**: Add type annotations for all functions
- **Docstrings**: Use Google-style docstrings

```python
def process_document(file_path: str, chunk_size: int = 500) -> List[str]:
    """
    Process a document into chunks.

    Args:
        file_path: Path to the document file
        chunk_size: Maximum characters per chunk

    Returns:
        List of text chunks

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_nlp_controller.py
```

### Adding a New LLM Provider

1. Create provider class in `src/stores/llm/providers/`
2. Implement `LLMInterface` abstract methods
3. Register in `LLMProviderFactory`
4. Update `.env.example` with new configuration

Example:
```python
# src/stores/llm/providers/CustomProvider.py
from ..LLMInterface import LLMInterface

class CustomProvider(LLMInterface):
    def create_embedding(self, text: str) -> List[float]:
        # Implementation
        pass
    
    def generate_chat_completion(self, messages: List[dict]) -> str:
        # Implementation
        pass
```

### Adding a New Vector Database

1. Create provider in `src/stores/vectordb/providers/`
2. Implement `VectorDBInterface`
3. Update factory and enums
4. Add Docker service if needed

---

## 🐛 Troubleshooting

### Common Issues

#### Docker Services Not Starting

```bash
# Check service status
sudo docker compose ps

# View logs
sudo docker compose logs mongodb
sudo docker compose logs qdrant

# Restart services
sudo docker compose down
sudo docker compose up -d
```

#### MongoDB Connection Errors

```bash
# Verify MongoDB is running
sudo docker compose ps mongodb

# Test connection
mongosh --host localhost --port 27017 -u admin -p your-password

# Check .env configuration
cat docker/.env | grep MONGO
```

#### Qdrant Vector Size Mismatch

**Error:** `Vector dimension mismatch`

**Solution:** Ensure `VECTOR_SIZE` in `.env` matches your embedding model:
- `text-embedding-3-small`: 1536
- `text-embedding-3-large`: 3072
- `embed-english-v3.0` (Cohere): 1024

#### API Key Not Found

**Error:** `OpenAI API key not found`

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify key is set
cat .env | grep OPENAI_API_KEY

# Restart server after updating
```

#### File Upload Fails

**Error:** `Unsupported file type`

**Solution:** Ensure file has `.pdf` or `.txt` extension

**Error:** `File too large`

**Solution:** Check file size limits in FastAPI configuration

### Performance Optimization

#### Slow Embedding Generation

```python
# Enable batch processing in config
BATCH_SIZE=50  # Process 50 chunks at once
```

#### Vector Search Too Slow

```python
# Reduce top_k results
TOP_K_RESULTS=3  # Instead of 10

# Use faster distance metric
DISTANCE_METRIC=dot  # Faster than cosine
```

#### Out of Memory

```python
# Reduce chunk size
CHUNKING_SIZE=300  # Instead of 500

# Process files one at a time
# Or increase Docker memory limits
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/mini-rag.git
   cd mini-rag
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow code style guidelines
   - Add tests for new features
   - Update documentation

3. **Test Your Changes**
   ```bash
   pytest
   black src/
   flake8 src/
   ```

4. **Submit Pull Request**
   - Write clear commit messages
   - Reference any related issues
   - Provide description of changes

### Contribution Areas

- 🐛 **Bug Fixes**: Report and fix bugs
- ✨ **Features**: Add new capabilities
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Tests**: Increase test coverage
- 🎨 **UI/UX**: Enhance API design
- 🌍 **Localization**: Add new language support

### Code Review Process

1. Automated checks must pass
2. At least one maintainer approval required
3. No merge conflicts
4. Documentation updated if needed

### Reporting Issues

Use GitHub Issues and include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Error messages and logs

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 Mini-RAG Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Technologies

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern web framework
- **[LangChain](https://python.langchain.com/)** - Document processing and chunking
- **[OpenAI](https://openai.com/)** - GPT models and embeddings
- **[Cohere](https://cohere.com/)** - Alternative LLM provider
- **[Qdrant](https://qdrant.tech/)** - Vector database
- **[MongoDB](https://www.mongodb.com/)** - Document database
- **[Docker](https://www.docker.com/)** - Containerization

### Inspiration

This project was built as an educational resource for learning RAG systems in production environments.

### Community

Special thanks to all contributors who have helped improve this project through code, documentation, and feedback.

---

## 📞 Support

- **Documentation**: Check this README and inline code comments
- **Issues**: [GitHub Issues](https://github.com/yourusername/mini-rag/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/mini-rag/discussions)
- **Email**: support@mini-rag.dev

---

## 🗺️ Roadmap

### Upcoming Features

- [ ] Support for additional document formats (DOCX, HTML, Markdown)
- [ ] Advanced chunking strategies (semantic chunking)
- [ ] Query refinement and expansion
- [ ] Multi-query retrieval
- [ ] Re-ranking mechanisms
- [ ] Streaming responses
- [ ] Web UI dashboard
- [ ] API rate limiting
- [ ] User authentication
- [ ] Multi-tenancy support

### Version History

- **v1.0.0** (Current) - Initial release with core RAG functionality
- **v0.9.0** - Beta release with OpenAI and Qdrant support
- **v0.5.0** - Alpha release with basic document processing

---

<div align="center">

**[⬆ Back to Top](#-mini-rag-production-ready-rag-chatbot-system)**

Made with ❤️ by the Mini-RAG Team

</div>
