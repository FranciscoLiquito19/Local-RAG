import torch
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

st.set_page_config(page_title="Local RAG", page_icon="🧠")
st.title("🧠 Local RAG")
st.caption("Running 100% on your PC with RTX 5070")

@st.cache_resource(show_spinner="A carregar documentos e modelo...")
def load_engine():
    Settings.llm = Ollama(model="gemma3:12b", base_url="http://ollama:11434", request_timeout=120.0)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5",
        device=device
    )
    docs = SimpleDirectoryReader("docs").load_data()
    index = VectorStoreIndex.from_documents(docs)
    return index.as_query_engine(similarity_top_k=5)

engine = load_engine()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask a question about the document..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("A pensar..."):
            response = str(engine.query(prompt))
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
