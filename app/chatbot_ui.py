# app/chatbot_ui.py
import streamlit as st
from app.index_builder import build_index
from app.query_engine import create_query_engine

def run_chatbot():
    st.set_page_config(page_title="📘 RAG QA Chatbot", layout="centered")
    st.title("🤖 Business FAQ Chatbot")

    query = st.text_input("Ask a question:", "")

    if "query_engine" not in st.session_state:
        index = build_index("business_faq.pdf")
        st.session_state.query_engine = create_query_engine(index)

    if st.button("Ask"):
        if query.strip():
            response = st.session_state.query_engine.query(query)
            st.success(f"**Answer:** {response}")
        else:
            st.warning("Please enter a valid question.")
