from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    QDRANT_HOST = os.getenv("QDRANT_HOST")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT"))

    COLLECTION_NAME = os.getenv("COLLECTION_NAME")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

    TOP_K = int(os.getenv("TOP_K"))

settings = Settings()