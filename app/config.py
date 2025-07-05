# app/config.py
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Choose HuggingFace or OpenAI embeddings
EMBED_MODEL_NAME = "BAAI/bge-small-en"

# app/config.py

class Settings:
    PDF_FILE_PATH = "business_faq.pdf"  # or wherever your PDF is located
