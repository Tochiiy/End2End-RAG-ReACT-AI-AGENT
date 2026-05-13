
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vectorstore(file_path: str):
    from rag.loader import load_documents
    chunks = load_documents(file_path)
    return FAISS.from_documents(chunks, embeddings)