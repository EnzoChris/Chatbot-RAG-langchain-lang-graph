from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from state.state import AgentState
from database.db import carregar_documentos_para_vetorizar
from pathlib import Path
import shutil
import os
from main import retornar_resp


server = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")




@server.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


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


Upload_dir = "database/data"

@server.post("/carregar-pdf", response_class=HTMLResponse)
def carregar_pdf(request:Request, arquivo: UploadFile = File(...)):

    if arquivo.content_type != "application/pdf":
        return {"erro": "Este arquivo não é .pdf"}
    
    file_path = os.path.join(Upload_dir, arquivo.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)

    carregar_documentos_para_vetorizar("database\data")
    
    return templates.TemplateResponse(
        "index21.html",
        {
        "request":request
        }
    )
