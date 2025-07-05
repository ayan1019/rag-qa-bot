# app/index_builder.py
from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.llms.mock import MockLLM  # You can replace with OpenAI LLM
from app.config import EMBED_MODEL_NAME
from app.loader import load_documents

def build_index(file_path: str):
    Settings.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)
    Settings.llm = MockLLM()
    documents = load_documents(file_path)
    return VectorStoreIndex.from_documents(documents)
