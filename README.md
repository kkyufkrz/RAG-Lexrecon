# 🇮🇩 LexRecon – Asisten Hukum UU ITE 2024

![LexRecon Logo](https://i.imgur.com/v7q5Nb8.png)

**LexRecon** (Legal Expert RAG) adalah sistem asisten hukum berbasis **FastAPI**, **LangChain**, dan **Gemini (Google Generative AI)** yang dirancang khusus untuk menjawab pertanyaan masyarakat mengenai **Undang-Undang Informasi dan Transaksi Elektronik (UU ITE) 2024** secara **akurat, sopan, dan edukatif**.

> 🚀 Ditenagai oleh teknologi Retrieval-Augmented Generation (RAG) dengan Google Gemini + CrossEncoder untuk kepercayaan jawaban yang tinggi.

---

## 🧠 Fitur Utama

- 🔎 Pencarian Cerdas Pasal dan Ayat UU ITE berdasarkan pertanyaan pengguna.
- 🤖 RAG + Gemini: Menggabungkan pencarian berbasis vektor dan model LLM generatif dari Google.
- 🧠 Prompt Korektif: Memperbaiki kesalahan penyebutan pasal/ayat pengguna.
- 📊 Confidence Score: Menggunakan CrossEncoder untuk evaluasi keakuratan jawaban.
- 🧱 Modular & Extendable: Struktur kode yang rapi dan mudah dikembangkan.

---

## ⚙️ Arsitektur Teknologi

- **FastAPI** – Backend API cepat & ringan.
- **LangChain** – Framework RAG.
- **Google Gemini API** – Model LLM dari Google.
- **Qdrant (in-memory)** – Vector store untuk pencarian cerdas.
- **CrossEncoder (HuggingFace)** – Evaluasi kecocokan jawaban.
- **Regex Parsing** – Untuk strukturisasi Pasal dan Ayat.

---

## 📦 Instalasi

```bash
# Clone repositori
git clone https://github.com/username/LexRecon.git
cd LexRecon

# Buat virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

--- 

## 👨‍💻 Tentang Pengembang

### 🔹 Muhammad Azhar  
- Machine Learning Engineer & Cloud Computing Engineer  
- Fokus pada pengembangan sistem RAG, pemrosesan bahasa alami (NLP), serta integrasi Gemini AI di Google Cloud Platform (GCP).
- 📍 Jakarta, Indonesia.
- 🧑‍🎓 Mahasiswa Teknik Informatika, ID.
- 💡 Penggagas utama LexRecon sebagai proyek tugas dan kontribusi sosial berbasis AI dalam bidang hukum.

### 🔹 Akbar Fauzan Warahidayat  
- Fullstack JavaScript Developer  
- Fokus pada pengembangan backend FastAPI, pengelolaan API, serta strukturisasi data hukum.
- 📍 Banten, Indonesia.
- 🧑‍🎓 Mahasiswa Teknik Informatika, ID.
- 💡 Berkontribusi dalam menangani arsitektur sistem dan integrasi teknologi pendukung.

---
## 💡Catatan Tambahan
- Model ini tidak menggantikan nasihat hukum profesional.
- Proyek ini bertujuan edukasi dan pemberdayaan hukum digital.
- Jika kamu tertarik mengembangkan LexRecon untuk bidang hukum lain (misal KUHP, UU Perlindungan Anak), silakan hubungi pengembang.

---

## 📜 Lisensi
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
