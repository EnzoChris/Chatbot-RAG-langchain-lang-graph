from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_model():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("CHAVE_API"), temperature=0)