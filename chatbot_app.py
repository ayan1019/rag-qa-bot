import streamlit as st
from llama_index.core.query_engine import RetrieverQueryEngine
from rag_qa_bot import index  

# Initialize retriever and query engine
retriever = index.as_retriever()
query_engine = RetrieverQueryEngine(retriever=retriever)

# Streamlit UI
st.set_page_config(page_title="📘 Business FAQ Chatbot", layout="centered")
st.title("🤖 Business FAQ Chatbot")

query = st.text_input("Ask a question about the document:", "")

if st.button("Ask"):
    if query.strip():
        response = query_engine.query(query)
        st.success(f"**Answer:** {response}")
    else:
        st.warning("Please enter a valid question.")
