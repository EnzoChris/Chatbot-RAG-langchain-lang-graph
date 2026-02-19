from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

def get_model():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("CHAVE_API"), temperature=0)

def get_embedding():
    return GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", api_key=os.getenv("CHAVE_API"))