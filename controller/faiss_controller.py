from manager.faiss_manager import create_faiss_index_manager, load_faiss_index_manager

def create_faiss_index_controller(embeddings, final_documents):
    """
    Controller for creating and saving FAISS index.
    """
    return create_faiss_index_manager(embeddings, final_documents)

def load_faiss_index_controller():
    """
    Controller for loading FAISS index.
    """
    return load_faiss_index_manager()
