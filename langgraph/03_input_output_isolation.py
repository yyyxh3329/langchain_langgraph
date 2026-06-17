"""
    测试：langgraph的入门案例
    LangGraph中的三个组成：1、状态  2、节点（函数） 3、边

    LangGraph的使用流程：
    1、创建状态，本质就是一个模型类，其中设置了LangGraph中需要共享和传递的数据
    2、创建节点
    3、通过状态创建builder实例，并添加节点和边
    4、添加节点和边
    5、对builder进行编译，获取图对象
    6、执行图对象
"""
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph


# 创建状态，本质就是一个模型类，其中设置了LangGraph中需要共享和传递的数据
class MyState(TypedDict):
    query: str
    rag_search_result: str
    web_search_result: str
    final_result: str

class InputSchema(TypedDict):
    query: str


class OutputSchema(TypedDict):
    final_result: str

# 2、节点 就是函数
# 创建节点，节点的形参列表中至少要包含状态参数
# 节点的返回值是一个字典，字典中的键要和状态中的属性保持一致
# 当执行了这个节点，节点所返回的数据就会保存在状态中所对应的属性中
def rag_search_node(state: MyState):
    print("rag_search_node",state)
    # 获取 query
    query = state["query"]
    return {"rag_search_result":f"{query}的RAG检索结果"}


def web_search_node(state: MyState):
    print("web_search_node", state)
    # 获取 query
    query = state["query"]
    return {"web_search_result": f"{query}WEB检索结果"}


def final_node(state: MyState):
    print("final_node", state)
    # 获取 rag_search_result web_search_result
    rag_search_result = state["rag_search_result"]
    web_search_result = state["web_search_result"]
    return {"final_result":f"对{rag_search_result}和{web_search_result}的总结"}

# 通过状态创建builder实例
builder = StateGraph(state_schema=MyState, input_schema=InputSchema, output_schema=OutputSchema)

# 添加节点
builder.add_node(rag_search_node)
builder.add_node(web_search_node)
builder.add_node(final_node)

# 添加边
builder.add_edge(START,"rag_search_node")
builder.add_edge(START,"web_search_node")
builder.add_edge("rag_search_node","final_node")
builder.add_edge("web_search_node","final_node")
builder.add_edge("final_node",END)

# 对builder进行编译,获取图对象
graph = builder.compile()

# 执行图对象
result = graph.invoke({"query":"什么是graph"})
print(result)