from sentence_transformers import SentenceTransformer

from app.core.config import settings

model = SentenceTransformer(settings.EMBEDDING_MODEL)

def generate_embedding(texts):

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings