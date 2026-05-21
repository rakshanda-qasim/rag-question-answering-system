import os

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.ingestion.cleaner import clean_text

FILE_PATH = "data/raw/attention.pdf"

print(os.path.exists(FILE_PATH))
print(FILE_PATH)

documents = load_pdf(FILE_PATH)

for doc in documents:
    doc.page_content = clean_text(doc.page_content)

chunks = chunk_documents(documents)

print(f"Loaded Documents: {len(documents)}")
print(f"Generated Chunks: {len(chunks)}")

print("\nSample Chunk:\n")
print(chunks[0].page_content)