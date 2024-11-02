from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from get_embedding_function import get_embedding_function
from langchain_chroma import Chroma

DATA_PATH = "data"
CHROMA_PATH = "chroma"

def load_documents(path):
    loader = PyPDFDirectoryLoader(path)
    return loader.load()

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        is_separator_regex=False,
    )
    return splitter.split_documents(documents)

def add_to_chroma(chunks):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )
    db.add_documents(chunks)

documents = load_documents(DATA_PATH)
chunks = split_documents(documents)
add_to_chroma(chunks)