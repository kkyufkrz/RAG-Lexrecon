import os
import uvicorn
import logging
import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import Config
from src.rag_system import RAGSystem

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Init FastAPI
app = FastAPI(title="Asisten Hukum UU ITE")

# CORS (sesuaikan dengan frontend lo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model request body
class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, description="Pertanyaan yang ingin diajukan")

# Inisialisasi RAGSystem secara global
rag_system = None

@app.on_event("startup")
async def startup_event():
    global rag_system
    try:
        rag_system = RAGSystem(Config())
        logger.info("✅ Sistem RAG berhasil diinisialisasi.")
    except FileNotFoundError as e:
        logger.error(f"❌ File tidak ditemukan: {e}")
        exit(1)
    except ValueError as e:
        logger.error(f"❌ Konfigurasi error: {e}")
        exit(1)
    except Exception as e:
        logger.error(f"❌ Error saat inisialisasi RAGSystem: {e}\n{traceback.format_exc()}")
        exit(1)

# --- Endpoint ---

@app.post("/query")
async def query_uuite(request: QueryRequest):
    """
    Endpoint utama untuk menjawab pertanyaan hukum terkait UU ITE.
    """
    try:
        response = rag_system.query(request.question)
        return {"answer": response["answer"]}
    except Exception as e:
        logger.error(f"❌ Error di /query: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/chunks_metadata")
async def get_chunks_metadata():
    """
    Endpoint untuk melihat semua chunks UU ITE yang sudah diindeks ke Qdrant.
    """
    try:
        chunks = rag_system.get_all_chunks()
        return [
            {"metadata": c.metadata, "content": c.page_content}
            for c in chunks
        ]
    except Exception as e:
        logger.error(f"❌ Error di /chunks_metadata: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/health")
async def health_check():
    """
    Endpoint health check untuk monitoring service.
    """
    return {"status": "ok", "message": "Asisten Hukum UU ITE siap digunakan"}

# Serve frontend (public/)
app.mount("/", StaticFiles(directory="public", html=True), name="public")

# Run
if __name__ == "__main__":
    logger.info("🚀 Menjalankan server FastAPI...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Railway otomatis set PORT
        reload=True
)
