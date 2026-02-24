from state.state import AgentState
from graph.graph import app


def retornar_resp(pergunta):
    input = {'question':pergunta}

    result = app.invoke(input)

    return {result['generate']}
