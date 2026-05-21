from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.ingestion.cleaner import clean_text

from app.embeddings.embedder import generate_embedding

from app.vectorstore.qdrant_client import create_collection
from app.vectorstore.retriever import upload_embeddings

FILE_PATH = "data/raw/attention.pdf"

documents = load_pdf(FILE_PATH)

for doc in documents:
    doc.page_content = clean_text(doc.page_content)

chunks = chunk_documents(documents)

texts = [chunk.page_content for chunk in chunks]

embeddings = generate_embedding(texts)

create_collection()

upload_embeddings(chunks, embeddings)

print("Indexing complete.")