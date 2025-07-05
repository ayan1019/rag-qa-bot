# 🤖 RAG QA Bot with OpenAI, Pinecone & LlamaIndex

This is a modular **Retrieval-Augmented Generation (RAG)** chatbot that allows users to query information from custom **PDF documents** via a simple **Streamlit interface**. It uses:

- **OpenAI** (for embedding & answering)
- **LlamaIndex** (for document indexing & querying)
- **Pinecone** (for storing vector embeddings)
- **Streamlit** (for the frontend chatbot interface)

---

## 🗂️ Project Structure

rag-qa-bot/
│
├── app/
│ ├── loader.py # Loads PDF from disk
│ ├── Config.py # config setup (OpenAI / HuggingFace)
│ ├── index_builder.py # Builds or loads the vector index
│ ├── query_engine.py # Prepares the query engine
│ ├── chatbot_ui.py # Streamlit chatbot interface
│
├── business_faq.pdf # 📄 Sample PDF document
├── chatbot_app.py # 🔁 Streamlit UI
├── main.py # 🔁 Streamlit entry point
├── .env # 🔑 API credentials (not shared)
├── .gitignore # Git ignored files
└── README.md # This file



---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-qa-bot.git
cd rag-qa-bot
```

### 2. Set up a virtual environment 

```bash
python -m venv env310
source env310/bin/activate  # macOS/Linux
env310\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

```bash

OPENAI_API_KEY=your-openai-key
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENV=your-pinecone-region
PINECONE_INDEX_NAME=your-index-name

```

### 5. Run the app

```bash
streamlit run main.py
```


## Project Link : 