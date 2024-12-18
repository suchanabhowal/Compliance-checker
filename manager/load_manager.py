from langchain_community.document_loaders import PyPDFLoader

def load_pdf_manager(file_path):
    """
    Load a PDF document using PyPDFLoader.
    """
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
