from langgraph.graph import StateGraph, END
from typing import TypedDict
from retriever import retrieve_docs
from hitl import human_escalation
from groq import Groq


client = Groq(api_key="ENTER_YOUR_KEY")

class State(TypedDict):
    query: str
    context: str
    answer: str
    escalate: bool

def process_node(state: State):
    print("\nSearching knowledge base...")
    context = retrieve_docs(state["query"])
    state["context"] = context
    if not context or len(context.strip()) < 20:
        state["escalate"] = True
    else:
        state["escalate"] = False
    return state

def answer_node(state: State):
    print("Generating answer...")
    prompt = f"""You are a customer support assistant.
Use the context below to answer the question.
If you are not sure, say you don't know.

Context:
{state["context"]}

Question: {state["query"]}

Answer:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    state["answer"] = response.choices[0].message.content
    return state

def escalate_node(state: State):
    state["answer"] = human_escalation(state["query"])
    return state

def route(state: State):
    if state["escalate"]:
        return "escalate"
    return "answer"

def build_graph():
    graph = StateGraph(State)
    graph.add_node("process", process_node)
    graph.add_node("answer", answer_node)
    graph.add_node("escalate", escalate_node)
    graph.set_entry_point("process")
    graph.add_conditional_edges("process", route, {
        "answer": "answer",
        "escalate": "escalate"
    })
    graph.add_edge("answer", END)
    graph.add_edge("escalate", END)
    return graph.compile()

