# PDF Q&A Agent (RAG)

A FastAPI-based application that implements a Retrieval-Augmented Generation (RAG) system to query PDF documents using LangChain, ChromaDB, and OpenAI.

## Features
- **PDF Ingestion:** Upload and parse PDF text.
- **Vector Store:** Chunk documents and store vector embeddings using ChromaDB.
- **Document Q&A:** Query contextually relevant information from uploaded documents with OpenAI GPT models.

## Project Structure
```text
pdf-rag/
├── app/
│   ├── api/
│   │   └── routes.py         # FastAPI endpoints (/upload, /ask)
│   ├── rag/
│   │   ├── pdf_reader.py     # Extracts text from uploaded PDFs
│   │   ├── vector_store.py   # Text chunking and vector storage
│   │   └── qa.py             # Prompting and LLM question answering
│   └── main.py               # FastAPI entry point
├── uploads/                  # Directory for uploaded documents
├── requirements.txt          # Python dependencies
└── .env.example              # Environment variables template
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create and activate a virtual environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1   # On Windows
# source venv/bin/activate    # On Linux/macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file based on `.env.example`:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the application
```powershell
python -m uvicorn app.main:app --port 8001 --reload
```

Open Swagger UI in your browser:
[http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
