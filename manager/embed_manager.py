from langchain_huggingface import HuggingFaceEmbeddings

def embed_documents_manager():
    """
    Generate embeddings for the split documents using HuggingFaceEmbeddings.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
