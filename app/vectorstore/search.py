from app.embeddings.embedder import generate_embedding
from app.vectorstore.qdrant_client import client
from app.core.config import settings

def search(query: str):

    query_embedding = generate_embedding([query])[0]

    results = client.query_points(
        collection_name=settings.COLLECTION_NAME,

        query=query_embedding.tolist(),

        limit=settings.TOP_K
    )

    return results.points