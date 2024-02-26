from .embeddings_calculations import Embeddings
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

vectordb = Embeddings("Txt_vector_search").vectorstore

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectordb.as_retriever()
    )

def query_response(query):
    
    return qa.invoke(query)["result"]