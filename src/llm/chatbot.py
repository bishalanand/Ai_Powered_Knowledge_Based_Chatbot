import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

load_dotenv()

def create_chatbot(retriever):

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain