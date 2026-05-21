from qdrant_client.models import PointStruct

from app.vectorstore.qdrant_client import client
from app.core.config import settings

def upload_embeddings(chunks, embeddings):

    points = []

    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        points.append(
            PointStruct(
                id=idx,

                vector=embedding.tolist(),

                payload={
                    "text": chunk.page_content,
                    "metadata": chunk.metadata
                }
            )
        )

    client.upsert(
        collection_name=settings.COLLECTION_NAME,
        points=points
    )

    print("Embeddings uploaded.")