from typing import TypedDict, Annotated

from langgraph.constants import START, END
from langgraph.graph import StateGraph, add_messages


def add_message(old : list[str], new: list[str]):
    return old + new


class MyState(TypedDict):
    # result: Annotated[list[str], add_message]  # 自定义函数
    # result: Annotated[list[str], add_messages]   # 系统函数，会封装成HumanMessage等等
    result: Annotated[list[str], lambda old,new : old + new]



def node_one(state : MyState):
    return {"result": ["hello"]}


def node_two(state : MyState):
    return {"result": ["world"]}

builder = StateGraph(MyState)
builder.add_node(node_one)
builder.add_node(node_two)

builder.add_edge(START, "node_one")
builder.add_edge("node_one", "node_two")
builder.add_edge("node_two", END)

graph = builder.compile()

result = graph.invoke({"result": ["你好"]})

print(result)