from fastapi import UploadFile,APIRouter,HTTPException,File
import os

from api.models import UploadResponse
import store
from src.ingestion.ingest import ingest_pdf

router=APIRouter()
upload_folder="data/uploads"

os.makedirs(upload_folder,exist_ok=True)

@router.post("/upload",response_model=UploadResponse)
async def upload_pdf(file : UploadFile=File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="Only pdf file allowed")
    
    file_path=os.path.join(upload_folder,file.filename)#inbuilt function of file 
    
    with open(file_path,"wb")as f:
        content=await file.read()
        f.write(content)
        
    result=ingest_pdf(file_path)
    
    doc_id=result["doc_id"]
    file_name=result["file_name"]
    docs=result["chunk"]
    store.chunk_store[doc_id]=docs
    print("Available docs:", store.chunk_store.keys())
    
    return UploadResponse(
        message="Documnet uploaded successfully and summary created succesfully{doc_id}",
        document_id=doc_id
    )
    

    
    
    