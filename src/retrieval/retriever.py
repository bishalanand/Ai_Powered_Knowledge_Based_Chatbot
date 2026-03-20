import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

index_name = os.getenv("PINECONE_INDEX_NAME")

# same embedding model used in ingestion
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings
)


def get_retriever(doc_id: str):
    """
    Create retriever filtered by document id
    """

    print(f"Creating retriever for document: {doc_id}")

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 5,
            "filter": {"doc_id": doc_id}
        }
    )

    return retriever