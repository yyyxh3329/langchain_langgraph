"""
    通过Sqlite实现长期记忆
"""
import sqlite3
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph



class MyState(TypedDict):
    k1: str
    k2: str
    k3: str


def node_one(state : MyState):
    print("node_one节点执行")
    return {"k1":"value1"}

def node_two(state : MyState):
    print("node_two节点执行")
    return {"k2":"value2"}

def node_three(state : MyState):
    print("node_three节点执行")
    return {"k3":"value3"}

# 获取连接Sqlite的连接对象
conn = sqlite3.connect(database='./test_sqlite', check_same_thread=False)

checkpointer = SqliteSaver(conn)

builder = StateGraph(MyState)

builder.add_node(node_one)
builder.add_node(node_two)
builder.add_node(node_three)

builder.add_edge(START, "node_one")
builder.add_edge("node_one", "node_two")
builder.add_edge("node_one", "node_three")
builder.add_edge("node_two", END)
builder.add_edge("node_three", END)

graph = builder.compile(checkpointer=checkpointer)

# 如果按以下执行，只有当执行图的完全结束后，才会将状态存入sqlite中，因为其中任意一个都会修改状态
# # 第一次模拟节点的异常
# result = graph.invoke({},config={"configurable":{"thread_id":"abc123"}})
# print(result)
# # 第二次模型节点的异常
# result = graph.invoke(None,config={"configurable":{"thread_id":"abc123"}})
# print(result)



# 第一次模拟节点的异常
# result = graph.invoke({},config={"configurable":{"thread_id":"abc123"}})
# print(result)
# 第二次模型节点的异常，此时必须传None，
result = graph.invoke(None,config={"configurable":{"thread_id":"abc123"}})
print(result)