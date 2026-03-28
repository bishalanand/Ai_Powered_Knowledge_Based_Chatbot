from pydantic import BaseModel, Field
from typing import Optional, List


# ---------- Upload ----------

class UploadResponse(BaseModel):
    message: str = Field(..., example="PDF uploaded successfully")
    document_id: str = Field(..., example="doc_12345")


# ---------- Chat ----------

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3, example="What is curb space management?")
    document_id: str = Field(..., example="doc_12345")


class Source(BaseModel):
    page: Optional[int] = Field(None, example=3)
    content: Optional[str] = Field(None, example="Curb space is managed using...")


class ChatResponse(BaseModel):
    answer: str
    sources: Optional[List[Source]] = None


# ---------- Summary ----------

class SummaryRequest(BaseModel):
    document_id: str = Field(..., example="doc_12345")


class SummaryResponse(BaseModel):
    document_id: str
    summary: str