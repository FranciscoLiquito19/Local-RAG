LOCAL RAG

A fully local Retrieval-Augmented Generation (RAG) chatbot that runs 100% on your machine ; no cloud, no API keys, no data leaving your PC.

Built with a RTX 5070 (12GB VRAM) and Ryzen 5 9600X.

What it does

- Loads documents (PDF, TXT) from a local folder
- Converts them into vector embeddings using your GPU
- Lets you ask questions about the documents in natural language
- Answers using a local LLM (Gemma3 12B via Ollama)
- Clean web interface built with Streamlit

Stack

| Component | Tool |
|---|---|
| LLM | Gemma3 12B (via Ollama) |
| Embeddings | BAAI/bge-small-en-v1.5 (HuggingFace) |
| RAG framework | LlamaIndex |
| Interface | Streamlit |
| Runtime | WSL2 + CUDA |

Requirements

- NVIDIA GPU with 8GB+ VRAM
- WSL2 with CUDA drivers
- Python 3.12+
- [Ollama](https://ollama.com) installed

Setup

```bash
# 1. Clone the repo
git clone https://github.com/FranciscoLiquito19/Local-RAG.git
cd Local-RAG

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the model
ollama pull gemma3:12b

# 5. Add your documents
mkdir docs
# Place your PDF or TXT files inside /docs

# 6. Run
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

Notes

- First run downloads the embedding model (~133MB)
- Documents are re-indexed on every run (ChromaDB persistence coming soon)
- Tested with PDF and TXT files
