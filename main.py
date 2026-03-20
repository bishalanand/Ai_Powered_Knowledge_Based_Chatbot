import os

from src.ingestion.ingest import ingest_pdf
from src.pipelines.rag_pipeline import build_rag_pipeline


upload_folder = "data/uploads"

pdf_name = input("Enter uploaded PDF name: ")

pdf_path = os.path.join(upload_folder, pdf_name)

if not os.path.exists(pdf_path):
    print("PDF not found!")
    exit()

print("Ingesting document...")

# run ingestion
result = ingest_pdf(pdf_path)

doc_id = result["doc_id"]
docs=result["chunk"]
from src.summarization.pdf_explainer import generate_pdf_summary

print("\nGenerating PDF explanation...")

summary = generate_pdf_summary(docs)

print("\nPDF Explanation:")
print(summary)

# build rag pipeline
qa_chain = build_rag_pipeline(doc_id)

print("\nChatbot ready!")

while True:

    query = input("\nAsk question (type exit to stop): ")

    if query.lower() == "exit":
        break

    result = qa_chain.invoke({"query": query})

    print("\nAnswer:")
    print(result["result"])