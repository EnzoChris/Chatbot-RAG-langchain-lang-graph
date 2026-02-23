from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS;
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from factory.llm_factory import get_embedding
import os
from dotenv import load_dotenv


load_dotenv()


nome_base_de_dados="data"
embeddings = get_embedding()

def carregar_documentos_para_vetorizar():
    loader = PyPDFDirectoryLoader(nome_base_de_dados, glob="*.pdf")
    documentos = loader.load()
    
    #separando os documentos

    separador = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=75,
        length_function=len,
        add_start_index=True
    )

    chunks = separador.split_documents(documentos)
    
    #salvando base_vetorizada
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("db_config_faiss")

    print("DEU TUDO CERTO")

carregar_documentos_para_vetorizar()


