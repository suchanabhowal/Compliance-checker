#TAKES THE OUPUT OF THE FILES INSIDE CONTROLLER FOLDER. 
#IN ORDER TO  RUN THIS TYPE :- uvicorn main:app --reload
#inside swagger,go to upload-pdf/ route. browse the pdf document, and hit execute button. the chunking, vector embedding wil be created. 
# once the faiss index is created succesfully it will show a success:true in response body. 
import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from controller.load_controller import load_pdf_controller
from controller.split_controller import split_pdf_controller
from controller.embed_controller import embed_documents_controller
from controller.faiss_controller import create_faiss_index_controller, load_faiss_index_controller

# Load environment variables
load_dotenv()

# FastAPI app instance
app = FastAPI()

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, extract its content, create embeddings, and save FAISS index.
    """
    try:
        # Save the uploaded PDF temporarily
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process the PDF
        docs = load_pdf_controller(file_path)
        final_documents = split_pdf_controller(docs)
        embeddings = embed_documents_controller()
        create_faiss_index_controller(embeddings, final_documents)

        # Print embeddings processing success
        print(f"Embeddings for '{file.filename}' have been created and stored.")

        # Cleanup: Remove the uploaded file
        os.remove(file_path)

        return JSONResponse(content={"success": True, "message": f"Embeddings created for {file.filename}"})

    except Exception as e:
        return JSONResponse(content={"success": False, "error": str(e)}, status_code=500)

@app.get("/status/")
def check_status():
    """
    Check if the FAISS index was successfully created.
    """
    try:
        load_faiss_index_controller()
        return {"success": True, "message": "FAISS index successfully created and stored locally."}
    except Exception:
        return {"success": False, "message": "FAISS index not found."}

@app.get("/")
def root():
    return {"message": "Welcome to the PDF Embedding API!"}
