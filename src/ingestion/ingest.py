import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=PINECONE_API_KEY)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def ingest_pdf(pdf_path: str):

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} does not exist")

    file_name = os.path.basename(pdf_path)
    doc_id = file_name.replace(".pdf", "")

    print(f"\nProcessing document: {file_name}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(documents)

    for chunk in chunks:
        chunk.metadata["doc_id"] = doc_id
        chunk.metadata["source"] = file_name

    index = pc.Index(INDEX_NAME)

    # remove old vectors of same document
    index.delete(filter={"doc_id": doc_id})

    PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        index_name=INDEX_NAME
    )

    print(f"Document '{file_name}' stored successfully.")
    print(f"Chunks created: {len(chunks)}")

    return {
        "doc_id": doc_id,
        "file_name": file_name,
        "chunks": len(chunks),
        "chunk":chunks
    }