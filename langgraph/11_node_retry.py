"""
    测试：节点的重试
    LangGraph不会重试的异常类型：
    ValueError, TypeError, ArithmeticError, ImportError
    LookupError, NameError, SyntaxError, RuntimeError
     ReferenceError, StopIteration, StopAsyncIteration, OSError
"""
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import CachePolicy, RetryPolicy


class MyState(TypedDict):
    result: str


counter = 0


def node_retry(state: MyState):
    global counter
    counter += 1
    if counter <= 5:
        print(f"当前第{counter}次重试，抛出异常")
        raise Exception("测试节点重试")
    else:
        return {"result": f"当前第{counter}次重试，执行成功"}


builder = StateGraph(MyState)

builder.add_node(node_retry, retry_policy=RetryPolicy(max_attempts=3))

builder.add_edge(START, "node_retry")
builder.add_edge("node_retry", END)

graph = builder.compile()

result = graph.invoke({})
print(result)
