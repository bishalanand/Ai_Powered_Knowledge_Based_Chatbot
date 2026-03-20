import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def generate_pdf_summary(documents):

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )

    text = ""

    for doc in documents[:10]:
        text += doc.page_content + "\n"

    prompt = f"""
    Explain the following document in a short and clear way.
    Provide:
    1. Short summary
    2. Key points
    3. Important ideas

    Document:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content