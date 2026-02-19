from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import  carregar_dados_base, triagem_informacao, gerar_resposta, fallback

def criar_grafo():
    workflow = StateGraph(AgentState)

    workflow.add_node("carregar_dados_base", carregar_dados_base)
    workflow.add_node("triagem_informacao", triagem_informacao)
    workflow.add_node("gerar_resposta", gerar_resposta)
    workflow.add_node("fallback", fallback)

    workflow.set_entry_point("carregar_dados_base")
    workflow.add_edge("carregar_dados_base", "triagem_informacao")

    workflow.add_conditional_edges(
        "triagem_informacao",
        lambda x: x['status'],
        {
            "responder":"gerar_resposta",
            "não":"fallback"
        }
    )

    workflow.add_edge("gerar_resposta",END)
    workflow.add_edge("fallback",END)

    return workflow.compile()

app = criar_grafo()


