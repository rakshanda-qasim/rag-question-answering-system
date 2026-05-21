from app.vectorstore.qdrant_client import client
from app.core.config import settings

collections = client.get_collections()

print(collections)