from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from state.state import AgentState
from pathlib import Path
from main import retornar_resp


server = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@server.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


#@server.get("/state/pergunta/{pergunta}")
#def perguntar_api(pergunta: str):
#    resposta = retornar_resp(pergunta)
#    return {
#        "pergunta": pergunta,
#        "resposta": resposta
#    }

@server.post("/perguntar", response_class=HTMLResponse)
def perguntar_fast(request:Request, pergunta: str = Form(...)):
    resposta = retornar_resp(pergunta)

    return templates.TemplateResponse(
        "resposta.html",
        {
        "request":request,
        "pergunta":pergunta,
        "resposta":resposta
        }
    )
