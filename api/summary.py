from fastapi import APIRouter,HTTPException

from api.models import SummaryRequest,SummaryResponse
import store
from src.summarization.pdf_explainer import generate_pdf_summary

router=APIRouter()
@router.post('/summary',response_model=SummaryResponse)
async def sumary_generator(request: SummaryRequest):
    doc_id=request.document_id
    
    if doc_id not in store.chunk_store:
        print("Available docs:", store.chunk_store.keys())
        print("Requested doc:", doc_id)
        raise HTTPException(status_code=404,detail="document did not find")
    
    docs=store.chunk_store[doc_id]
    summary=generate_pdf_summary(docs)
    
    return SummaryResponse(
        document_id=doc_id,
        summary=summary
    )