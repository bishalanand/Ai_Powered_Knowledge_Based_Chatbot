from fastapi import APIRouter,HTTPException

from api.models import ChatRequest,ChatResponse
from store import chunk_store,pipeline_cache
from src.retrieval.retriever import get_retriever
from src.pipelines.rag_pipeline import build_rag_pipeline

router=APIRouter()
@router.post('/chat',response_model=ChatResponse)
def chatting(request: ChatRequest):
    doc_id=request.document_id
    question=request.question
    if doc_id in pipeline_cache:
        qa_chain=pipeline_cache["doc_id"]
        
    else:
        retiever=get_retriever(doc_id)
        qa_chain=build_rag_pipeline(doc_id)
        pipeline_cache["doc_id"]=qa_chain
        
        
    result = qa_chain.invoke({"query": question})

    return ChatResponse(answer=result["result"])
    