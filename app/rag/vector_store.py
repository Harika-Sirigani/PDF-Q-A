from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

DB_PATH = "chroma_db"


def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()

    Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )


def load_vector_store():

    embeddings = OpenAIEmbeddings()

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )