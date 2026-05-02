from fastapi import APIRouter, UploadFile, File
from typing import List
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger


router = APIRouter()

@router.post("/upload_pdfs/")
async def upload_pdfs(files: List[UploadFile] = File(...)):

    try:
        logger.info("Received request to upload PDFs.")
        load_vectorstore(files)
        logger.info("Document added to vector store successfully.")
        return {"message": "Documents uploaded and processed successfully."}    
    
    except Exception as e:
        logger.exception("Error processing uploaded files")
        return JSONResponse(status_code=500, content={"error": str(e)})