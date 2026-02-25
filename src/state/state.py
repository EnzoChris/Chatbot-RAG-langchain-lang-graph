from typing import TypedDict

class AgentState(TypedDict):
    question:str
    base_dados:str
    status:str
    generate:str
    base_vetorizada:bool
