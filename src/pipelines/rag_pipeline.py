from src.retrieval.retriever import get_retriever
from src.llm.chatbot import create_chatbot


def build_rag_pipeline(doc_id: str):

    print(f"Building RAG pipeline for document: {doc_id}")

    retriever = get_retriever(doc_id)

    qa_chain = create_chatbot(retriever)

    return qa_chain