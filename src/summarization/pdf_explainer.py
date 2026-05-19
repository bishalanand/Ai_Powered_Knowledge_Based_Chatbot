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
    Explain the following document in a structured way with multiple paragraphs.
    Provide the summary in the following sections, each as a separate paragraph:

    Short Summary:
    [Provide a brief overview of the document.]

    Key Points:
    [List the main points, each on a new line or in bullet points.]

    Important Ideas:
    [Highlight the core concepts or ideas.]

    Document:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content