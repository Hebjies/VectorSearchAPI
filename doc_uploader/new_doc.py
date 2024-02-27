from langchain.text_splitter import CharacterTextSplitter
from .embeddings_calculations import Embeddings
from docx import Document

vectordb = Embeddings("Txt_vector_search") # Vector database connections is stablished.
    
def get_chunks(text):
    
    # Doc file is divided in chinks of 1000
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def read_docx(file_path):
    
    # Docx file is open and then the text is returned as a str.
    
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def add_doc(file_path):
    
    # Docx is converted to chunks and then stored in the vector database.
       
    try:
        raw_text = read_docx(f'media/{file_path}')
        texts = get_chunks(raw_text)

        vectordb.add_new_doc(texts)
    except Exception as e:
        print(f"Unable to load doc: {e}")
    