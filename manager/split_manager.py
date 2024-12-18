from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_pdf_manager(docs):
    """
    Split the loaded documents into smaller chunks using RecursiveCharacterTextSplitter.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    final_documents = text_splitter.split_documents(docs)
    return final_documents
