from manager.split_manager import split_pdf_manager

def split_pdf_controller(docs):
    """
    Controller for splitting a PDF into smaller chunks.
    """
    return split_pdf_manager(docs)
