# app/query_engine.py
from llama_index.core.query_engine import RetrieverQueryEngine

def create_query_engine(index):
    retriever = index.as_retriever()
    return RetrieverQueryEngine(retriever=retriever)
