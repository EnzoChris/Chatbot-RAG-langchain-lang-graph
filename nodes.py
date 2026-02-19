#pip install python-dotenv langchain langchain_google_genai langchain_community 
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
#from db import carregar_base_conhecimento
from state import AgentState
from llm_factory import get_model
from dotenv import load_dotenv
import os
load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", api_key=os.getenv("CHAVE_API"))



def carregar_dados_base(state:AgentState):
    vector_store = FAISS.load_local(
        "db_config_faiss",
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    documentos_relevantes = vector_store.similarity_search_with_relevance_scores(state['question'], k=3)

    documentos_juntos = []
    for doc in documentos_relevantes:
        text = doc[0].page_content
        documentos_juntos.append(text)

    documentos_juntos_para_base = "-----".join(documentos_juntos)

    return {"base_dados": documentos_juntos_para_base}




def triagem_informacao(state: AgentState):
    #vai pegar a pergunta, lançar ela ao modelo e relacionar os documentos, seu objetivo é classificar se dá pra responder, pedir informação ou pedir fallback

    prompt = f"A pergunta é: {state['question']}, e a base de dados é: {state['base_dados']}. Responda com 'sim' ou 'não' se há informação suficiente "
    llm = get_model()
    resp = llm.invoke(prompt)


    #de acordo com os documentos relevantes, eu classifico se vai responder, pedir infromação ou parar
    return {"status":"responder"} if "sim" in resp.content.lower() else {"status":"não"}
    




def gerar_resposta(state:AgentState):
    prompt = f"Responda a pergunta: {state['question']} com essa base de dados {state['base_dados']}"
    llm = get_model()
    resp = llm.invoke(prompt)

    return {"generate": resp.content}




def fallback(state:AgentState):
    return {"generate": f"Desculpe, mas não consegui responder a sua pergunta '{state['question']}'"}


