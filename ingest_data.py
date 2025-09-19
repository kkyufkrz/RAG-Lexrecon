import logging
from langchain_community.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from config import Config
from src.utils import split_to_chunks, load_uu_file

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def ingest_data():
    config = Config()
    logger.info("Memulai proses indexing...")

    raw_text = load_uu_file(config.UU_FILE_PATH)
    chunks = split_to_chunks(raw_text)
    
    # Perbaikan: Konversi chunks (list of dicts) menjadi list of Documents
    documents_for_qdrant = [
        Document(page_content=c["content"], metadata=c["metadata"]) 
        for c in chunks
    ]

    embedding_model = GoogleGenerativeAIEmbeddings(
        model=config.EMBEDDING_MODEL_NAME, 
        google_api_key=config.GOOGLE_API_KEY
    )

    logger.info(f"Mengindeks {len(documents_for_qdrant)} chunks ke Qdrant...")
    Qdrant.from_documents(
        documents=documents_for_qdrant,
        embedding=embedding_model,
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME,
        force_recreate=True
    )
    logger.info("Proses indexing selesai!")

if __name__ == "__main__":
    ingest_data()
