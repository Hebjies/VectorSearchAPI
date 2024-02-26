from qdrant_client import QdrantClient
from qdrant_client.http import models

class VectorBase:

    def __init__(self,):
        
        self.client=QdrantClient(host="localhost", port=6333)

    def create_collection(self,):
        
        try:
            self.client.create_collection(
                collection_name='Txt_vector_search',
                vectors_config=models.VectorParams(
                    size=1536, # We will use text-embedding-ada-002 from open ai, so the embedding dimension is 1536.
                    distance=models.Distance.COSINE # We want to use vector cosine similarity.
                )
            )
        
            print("Text vector search collection has been created")
        except:
            print("Unable to create collection database")