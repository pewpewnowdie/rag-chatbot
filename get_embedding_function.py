from langchain_ollama import OllamaEmbeddings

EMBEDDING_MODEL = "nomic-embed-text"

def get_embedding_function():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    return embeddings