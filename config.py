import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Kelas untuk mengelola semua konfigurasi sistem dari file .env
    dan parameter lainnya.
    """
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

    if not all([GOOGLE_API_KEY, LANGCHAIN_API_KEY, QDRANT_API_KEY]):
        raise ValueError("Pastikan GOOGLE_API_KEY, LANGCHAIN_API_KEY, dan QDRANT_API_KEY ada di file .env")

    QDRANT_URL = ""
    QDRANT_COLLECTION_NAME = "uu_ite_chunks"
    UU_FILE_PATH = "data/UU_ITE_2024.txt"

    EMBEDDING_MODEL_NAME = "models/embedding-001"
    LLM_MODEL_NAME = "gemini-2.0-flash"
    CROSS_ENCODER_MODEL_NAME = 'cross-encoder/ms-marco-MiniLM-L-6-v2'

    N_TOP_RETRIEVED_DOCS = 10
    N_TOP_CONTEXT_DOCS = 10

    UVICORN_PORT = int(os.getenv("PORT", 8000))
    UVICORN_HOST = "0.0.0.0"

    PROMPT_TEMPLATE = """

    Identitas Sistem:   
    - Nama: LexRecon   
    - Dikembangkan oleh: Azhar   
    
    {context}
    
    Pertanyaan:   
    {question}   
    
    """
