from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
def create_faiss_index_manager(embeddings, final_documents):
    """
    Create a FAISS index from the document embeddings and store it locally.
    """
    vector_store = FAISS.from_documents(final_documents, embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def load_faiss_index_manager():
    """
    Load a FAISS index from a saved local file.
    """
    vector_store = FAISS.load_local("faiss_index", HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), allow_dangerous_deserialization=True)
    return vector_store
