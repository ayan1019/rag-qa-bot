# app/index_builder.py

import os
from app.config import Settings
from app.loader import load_documents
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

INDEX_DIR = "storage"

def build_index():
    file_path = Settings.PDF_FILE_PATH  # or manually set: "data/your_doc.pdf"
    documents = load_documents(file_path)
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=INDEX_DIR)
    return index

def get_index():
    if os.path.exists(INDEX_DIR):
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage_context)
    else:
        return build_index()
