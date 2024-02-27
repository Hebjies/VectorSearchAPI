from .embeddings_calculations import Embeddings
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

# Vector database collection connection is created

vectordb = Embeddings("Txt_vector_search").vectorstore

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectordb.as_retriever()
    )

def query_response(query):
    
    # Vector database is queried and and response with context.
    
    return qa.invoke(query)["result"]