from fastapi import FastAPI
from pydantic import BaseModel
from state.state import AgentState
from main import retornar_resp


server = FastAPI()


@server.get("/")
def home():
    return {"mensagem": "O chatbot chrisSeek está rodando! 🚀"}


@server.get("/state/pergunta/{pergunta}")
def perguntar_api(pergunta: str):
    resposta = retornar_resp(pergunta)

    return {
        "pergunta": pergunta,
        "resposta": resposta
    }
