import logging
from typing import List
from google.api_core.exceptions import ResourceExhausted
from langchain_core.embeddings import Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

class EmbeddingService(Embeddings):
    def __init__(self, use_local_fallback=True):
        self.use_local_fallback = use_local_fallback

        # Model Google Gemini
        try:
            self.gemini = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            logger.info("✅ Google Gemini Embedding diinisialisasi.")
        except Exception as e:
            logger.error(f"❌ Gagal inisialisasi Gemini: {e}")
            self.gemini = None

        # Model lokal (HuggingFace)
        if use_local_fallback:
            try:
                self.local_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
                logger.info("✅ Local Embedding (MiniLM) diinisialisasi.")
            except Exception as e:
                logger.error(f"❌ Gagal load local model: {e}")
                self.local_model = None

    def embed_query(self, text: str) -> List[float]:
        """Embed untuk single query"""
        # coba pakai Gemini dulu
        if self.gemini:
            try:
                return self.gemini.embed_query(text)
            except ResourceExhausted:
                logger.warning("⚠️ Quota Gemini habis, fallback ke local embedding.")
            except Exception as e:
                logger.error(f"❌ Error Gemini embedding: {e}")

        # fallback ke lokal
        if self.use_local_fallback and self.local_model:
            return self.local_model.encode([text])[0].tolist()

        raise RuntimeError("Tidak ada embedding service yang tersedia.")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed untuk banyak dokumen"""
        if self.gemini:
            try:
                return self.gemini.embed_documents(texts)
            except ResourceExhausted:
                logger.warning("⚠️ Quota Gemini habis, fallback ke local embedding.")
            except Exception as e:
                logger.error(f"❌ Error Gemini embedding: {e}")

        if self.use_local_fallback and self.local_model:
            return [vec.tolist() for vec in self.local_model.encode(texts)]

        raise RuntimeError("Tidak ada embedding service yang tersedia.")
