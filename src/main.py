from state.state import AgentState
from graph.graph import app

if __name__ == "__main__":

    pergunta = input("Qual a sua pergunta? ")

    input = {'question':pergunta}

    result = app.invoke(input)

    print("***"*30)
    print(f"RESULTADO: {result['generate']}")
    print("***"*30)


def retornar_resp(pergunta):
    input = {'question':pergunta}

    result = app.invoke(input)

    #print("***"*30)
    #print(f"RESULTADO: {result['generate']}")
    #print("***"*30)
    return {result['generate']}
