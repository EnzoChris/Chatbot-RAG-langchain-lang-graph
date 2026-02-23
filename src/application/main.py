from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from state.state import AgentState
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


Upload_dir = "database/data"
os.makedirs(Upload_dir, exist_ok=True)


@server.post("/perguntar", response_class=HTMLResponse)
def perguntar_fast(request:Request, pergunta: str = Form(...), arquivo: UploadFile = File(...)):

    if arquivo.content_type != "application/pdf":
        return {"erro": "Este arquivo não é .pdf"}
    
    file_path = os.path.join(Upload_dir, arquivo.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)


    resposta = retornar_resp(pergunta)

    return templates.TemplateResponse(
        "resposta.html",
        {
        "request":request,
        "pergunta":pergunta,
        "resposta":resposta
        }
    )
