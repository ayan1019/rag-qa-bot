# chatbot_app.py

from app.index_builder import get_index
from llama_index.core.query_engine import RetrieverQueryEngine
import streamlit as st

# Get the index
index = get_index()

# Build retriever and query engine
retriever = index.as_retriever()
query_engine = RetrieverQueryEngine(retriever=retriever)

# UI
st.title("📄 RAG QA Chatbot")

question = st.text_input("Ask a question:")
if st.button("Ask") and question:
    response = query_engine.query(question)
    st.markdown(f"**Answer:** {response}")
