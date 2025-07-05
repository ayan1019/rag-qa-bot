# app/loader.py
from llama_index.core import SimpleDirectoryReader

def load_documents(file_path: str):
    loader = SimpleDirectoryReader(input_files=[file_path])
    return loader.load_data()
