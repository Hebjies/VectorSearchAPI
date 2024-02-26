from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings

from .qdrant_collection import VectorBase

import requests

class Embeddings:
    
    def __init__(self, collection_name,):
        
        self.collection_name = collection_name
        q_collection = VectorBase()
        
        self.qclient = q_collection.client

        if requests.get('http://localhost:6333/collections').json()['result']['collections'] == []:
            q_collection.create_collection()
            
        self.vectorstore = Qdrant(
                client=self.qclient,
                collection_name=self.collection_name,
                embeddings=OpenAIEmbeddings()
            )


    def add_new_doc(self, text_chunks):
        try:
            self.vectorstore.add_texts(text_chunks)
            print(f"New embeddings stored in {self.collection_name}")
        except:
            print(f"Failed to load to {self.collection_name}")
