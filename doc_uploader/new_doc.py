from langchain.text_splitter import CharacterTextSplitter
from .embeddings_calculations import Embeddings
from docx import Document

vectordb = Embeddings("Txt_vector_search")
    
def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def add_doc(file_path):   
    try:
        raw_text = read_docx(f'media/{file_path}')
        texts = get_chunks(raw_text)

        vectordb.add_new_doc(texts)
    except Exception as e:
        print(f"Unable to load doc: {e}")
    