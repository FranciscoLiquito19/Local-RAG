from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Ollama(model="gemma3:12b", request_timeout=120.0)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
    device="cuda"
)

documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

print("RAG ready. Ask your questions (type 'exit' to quit)\n")
while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    response = query_engine.query(question)
    print(f"\nAI: {response}\n")
